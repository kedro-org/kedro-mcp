"""DataCatalog utility functions for Kedro MCP."""

import logging
from pathlib import Path
from typing import Any

from kedro.config import OmegaConfigLoader
from pydantic import ValidationError

from kedro_mcp.schemas.catalog import DATASET_SCHEMAS
from kedro_mcp.schemas.catalog.base_schemas import (
    CatalogFindingsSchema,
    DatasetErrorSchema,
    DatasetSuccessSchema,
)
from kedro_mcp.utils.shared_utils import get_kedro_project_path

logger = logging.getLogger(__name__)


def _load_merged_catalog(project_path: Path) -> dict[str, Any]:
    """Load merged catalog configuration using Kedro's OmegaConfigLoader."""
    conf_path = project_path / "conf"
    if not conf_path.exists():
        raise FileNotFoundError(
            f"No 'conf' folder found in Kedro project at '{project_path}'"
        )

    loader = OmegaConfigLoader(conf_path)
    merged_catalog = loader["catalog"]
    return merged_catalog or {}


def _validate_catalog_entries(catalog_entries: dict) -> CatalogFindingsSchema:
    """Validate catalog entries using static Pydantic schemas."""
    findings = CatalogFindingsSchema()

    for name, entry in catalog_entries.items():
        dataset_type = entry.get("type")
        if not dataset_type:
            findings.errors.append(
                DatasetErrorSchema(
                    dataset_name=name, message="Missing mandatory 'type' field"
                )
            )
            continue

        if dataset_type not in DATASET_SCHEMAS:
            # [TODO: MVP focusses on pandas]
            continue

        schema_cls = DATASET_SCHEMAS[dataset_type]
        try:
            validated = schema_cls(**entry)
            findings.success.append(
                DatasetSuccessSchema(
                    dataset_name=name,
                    dataset_type=dataset_type,
                    validated_fields=validated.dict(),
                )
            )
        except ValidationError as e:
            findings.errors.append(
                DatasetErrorSchema(dataset_name=name, message=str(e))
            )

    return findings


def validate_project_catalog() -> CatalogFindingsSchema:
    """Main entrypoint: load and validate the entire Kedro project catalog."""
    project_path = get_kedro_project_path()
    catalog_entries = _load_merged_catalog(project_path)
    validated = _validate_catalog_entries(catalog_entries)
    return validated


if __name__ == "__main__":
    findings = validate_project_catalog()

    logger.info("\nSuccess:")
    for s in findings.success:
        logger.info(f"  - {s.dataset_name} ({s.dataset_type})")

    logger.info("\nErrors:")
    for e in findings.errors:
        logger.info(f"  - {e.dataset_name}: {e.message}")

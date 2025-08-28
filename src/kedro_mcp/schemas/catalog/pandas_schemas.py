from typing import Any

from kedro_mcp.schemas.catalog.base_schemas import BaseDatasetSchema


class CSVDatasetSchema(BaseDatasetSchema):
    filepath: str
    save_args: dict[str, Any] | None = None
    version: str | None = None
    fs_args: dict[str, Any] | None = None
    metadata: dict[str, Any] | None = None


class DeltaTableDatasetSchema(BaseDatasetSchema):
    filepath: str | None = None
    catalog_type: str | None = None
    catalog_name: str | None = None
    database: str | None = None
    table: str | None = None
    save_args: dict[str, Any] | None = None
    fs_args: dict[str, Any] | None = None


class ExcelDatasetSchema(BaseDatasetSchema):
    filepath: str
    engine: str | None = "openpyxl"
    save_args: dict[str, Any] | None = None
    version: str | None = None
    fs_args: dict[str, Any] | None = None
    metadata: dict[str, Any] | None = None


class FeatherDatasetSchema(BaseDatasetSchema):
    filepath: str
    save_args: dict[str, Any] | None = None
    version: str | None = None
    fs_args: dict[str, Any] | None = None
    metadata: dict[str, Any] | None = None


class GBQTableDatasetSchema(BaseDatasetSchema):
    dataset: str
    table_name: str
    project: str | None = None
    save_args: dict[str, Any] | None = None
    metadata: dict[str, Any] | None = None


class GBQQueryDatasetSchema(BaseDatasetSchema):
    sql: str | None = None
    project: str | None = None
    fs_args: dict[str, Any] | None = None
    filepath: str | None = None
    metadata: dict[str, Any] | None = None


class GenericDatasetSchema(BaseDatasetSchema):
    filepath: str
    file_format: str
    save_args: dict[str, Any] | None = None
    version: str | None = None
    fs_args: dict[str, Any] | None = None
    metadata: dict[str, Any] | None = None


class HDFDatasetSchema(BaseDatasetSchema):
    filepath: str
    key: str
    save_args: dict[str, Any] | None = None
    version: str | None = None
    fs_args: dict[str, Any] | None = None
    metadata: dict[str, Any] | None = None


class JSONDatasetSchema(BaseDatasetSchema):
    filepath: str
    save_args: dict[str, Any] | None = None
    version: str | None = None
    fs_args: dict[str, Any] | None = None
    metadata: dict[str, Any] | None = None


class ParquetDatasetSchema(BaseDatasetSchema):
    filepath: str
    save_args: dict[str, Any] | None = None
    version: str | None = None
    fs_args: dict[str, Any] | None = None
    metadata: dict[str, Any] | None = None


class SQLTableDatasetSchema(BaseDatasetSchema):
    table_name: str
    save_args: dict[str, Any] | None = None
    metadata: dict[str, Any] | None = None


class SQLQueryDatasetSchema(BaseDatasetSchema):
    sql: str | None = None
    fs_args: dict[str, Any] | None = None
    filepath: str | None = None
    execution_options: dict[str, Any] | None = None
    metadata: dict[str, Any] | None = None


class XMLDatasetSchema(BaseDatasetSchema):
    filepath: str
    save_args: dict[str, Any] | None = None
    version: str | None = None
    fs_args: dict[str, Any] | None = None
    metadata: dict[str, Any] | None = None

from typing import Any

from pydantic import BaseModel


class BaseDatasetSchema(BaseModel):
    type: str
    credentials: dict[str, Any] | None = None
    load_args: dict[str, Any] | None = None


class DatasetErrorSchema(BaseModel):
    dataset_name: str
    message: str


class DatasetSuccessSchema(BaseModel):
    dataset_name: str
    dataset_type: str
    validated_fields: dict[str, Any]


class CatalogFindingsSchema(BaseModel):
    success: list[DatasetSuccessSchema] = []
    errors: list[DatasetErrorSchema] = []

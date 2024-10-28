"""
Generated by qenerate plugin=pydantic_v1. DO NOT MODIFY MANUALLY!
"""
from collections.abc import Callable  # noqa: F401 # pylint: disable=W0611
from datetime import datetime  # noqa: F401 # pylint: disable=W0611
from enum import Enum  # noqa: F401 # pylint: disable=W0611
from typing import (  # noqa: F401 # pylint: disable=W0611
    Any,
    Optional,
    Union,
)

from pydantic import (  # noqa: F401 # pylint: disable=W0611
    BaseModel,
    Extra,
    Field,
    Json,
)


DEFINITION = """
query ExternalResourcesModules {
    modules: external_resources_modules_v1 {
        provision_provider
        provider
        module_type
        image
        version
        reconcile_drift_interval_minutes
        reconcile_timeout_minutes
        outputs_secret_sync
        outputs_secret_image
        outputs_secret_version
    }
}
"""


class ConfiguredBaseModel(BaseModel):
    class Config:
        smart_union=True
        extra=Extra.forbid


class ExternalResourcesModuleV1(ConfiguredBaseModel):
    provision_provider: str = Field(..., alias="provision_provider")
    provider: str = Field(..., alias="provider")
    module_type: str = Field(..., alias="module_type")
    image: str = Field(..., alias="image")
    version: str = Field(..., alias="version")
    reconcile_drift_interval_minutes: int = Field(..., alias="reconcile_drift_interval_minutes")
    reconcile_timeout_minutes: int = Field(..., alias="reconcile_timeout_minutes")
    outputs_secret_sync: bool = Field(..., alias="outputs_secret_sync")
    outputs_secret_image: Optional[str] = Field(..., alias="outputs_secret_image")
    outputs_secret_version: Optional[str] = Field(..., alias="outputs_secret_version")


class ExternalResourcesModulesQueryData(ConfiguredBaseModel):
    modules: Optional[list[ExternalResourcesModuleV1]] = Field(..., alias="modules")


def query(query_func: Callable, **kwargs: Any) -> ExternalResourcesModulesQueryData:
    """
    This is a convenience function which queries and parses the data into
    concrete types. It should be compatible with most GQL clients.
    You do not have to use it to consume the generated data classes.
    Alternatively, you can also mime and alternate the behavior
    of this function in the caller.

    Parameters:
        query_func (Callable): Function which queries your GQL Server
        kwargs: optional arguments that will be passed to the query function

    Returns:
        ExternalResourcesModulesQueryData: queried data parsed into generated classes
    """
    raw_data: dict[Any, Any] = query_func(DEFINITION, **kwargs)
    return ExternalResourcesModulesQueryData(**raw_data)

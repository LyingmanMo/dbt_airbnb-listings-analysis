from dagster import AssetExecutionContext
from dagster_dbt import DbtCliResource, dbt_assets

from .project import dbt_airbnb_listing_project


@dbt_assets(manifest=dbt_airbnb_listing_project.manifest_path)
def dbt_airbnb_listing_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()
    
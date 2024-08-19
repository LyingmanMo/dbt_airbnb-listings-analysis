from pathlib import Path

from dagster_dbt import DbtProject

dbt_airbnb_listing_project = DbtProject(
    project_dir=Path(__file__).joinpath("..", "..", "..", "dbt_airbnb_listing").resolve(),
    packaged_project_dir=Path(__file__).joinpath("..", "..", "dbt-project").resolve(),
)
dbt_airbnb_listing_project.prepare_if_dev()
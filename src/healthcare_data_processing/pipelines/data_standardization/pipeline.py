"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.19.6
"""

import subprocess

from kedro.pipeline import Pipeline, node


def run_dbt() -> str:
    """
    Executes the dbt run command to execute dbt models in the specified directory.

    This function runs the dbt CLI command to build the dbt models located in the `./dbt/lupus_staging_tuva_model` directory.
    If the command fails, it raises an exception with the error details.

    Returns:
        str: A success message indicating the dbt run was successful.

    Raises:
        Exception: If the dbt run command fails, an exception is raised with the stdout and stderr output.
    """
    result = subprocess.run(
        ["dbt", "run"],
        cwd="./dbt/lupus_staging_tuva_model",
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise Exception(f"dbt run failed: {result.stdout}\n{result.stderr}")
    print("DBT run successful")
    return "DBT run successful"


def create_pipeline(**kwargs):
    return Pipeline([node(func=run_dbt, inputs=None, outputs="dbt_output")])

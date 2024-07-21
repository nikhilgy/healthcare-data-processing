"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.19.6
"""

import subprocess
from kedro.pipeline import Pipeline, node

def run_dbt():
    result = subprocess.run(['dbt', 'run'], cwd='./dbt/lupus_staging_tuva_model', capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"dbt run failed: {result.stdout}\n{result.stderr}")
    print("DBT run successful")
    return "DBT run successful"

def create_pipeline(**kwargs):
    return Pipeline([
        node(
            func=run_dbt,
            inputs=None,
            outputs="dbt_output"
        )
    ])

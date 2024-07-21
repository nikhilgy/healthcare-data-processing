"""
This is a boilerplate pipeline 'data_analysis'
generated using Kedro 0.19.6
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import merge_all_datasets


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=merge_all_datasets,
                inputs=[
                    "staging_table_patients",
                    "staging_table_conditions",
                    "staging_table_medications",
                    "staging_table_observations",
                    "staging_table_encounters",
                ],
                outputs="patient_master_dataset",
            )
        ]
    )

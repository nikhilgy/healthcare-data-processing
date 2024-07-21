"""
This is a boilerplate pipeline 'data_cleaning'
generated using Kedro 0.19.6
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import (clean_conditions, clean_encounters, clean_medications,
                    clean_patients, clean_symptoms)


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=clean_patients,
                inputs=["patients", "patient_gender"],
                outputs="table_patients",
            ),
            node(
                func=clean_conditions,
                inputs="conditions",
                outputs="table_conditions",
            ),
            node(
                func=clean_medications,
                inputs="medications",
                outputs="table_medications",
            ),
            node(
                func=clean_encounters,
                inputs="encounters",
                outputs="table_encounters",
            ),
            node(
                func=clean_symptoms,
                inputs=["symptoms", "patient_gender"],
                outputs="table_symptoms",
            ),
        ]
    )

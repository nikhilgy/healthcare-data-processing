"""
This is a boilerplate pipeline 'data_cleaning'
generated using Kedro 0.19.6
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import clean_patients, clean_conditions, clean_medications, clean_encounters, clean_symptoms


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=clean_patients,
                inputs=["patients", "patient_gender"],
                outputs="cleaned_patients",
            ),
            
            node(
                func=clean_conditions,
                inputs="conditions",
                outputs="cleaned_conditions",
            ),
            
            node(
                func=clean_medications,
                inputs="medications",
                outputs="cleaned_medications",
            ),
            
            node(
                func=clean_encounters,
                inputs="encounters",
                outputs="cleaned_encounters",
            ),
            
            node(
                func=clean_symptoms,
                inputs=["symptoms", "patient_gender"],
                outputs="cleaned_symptoms",
            )
        ]
    )

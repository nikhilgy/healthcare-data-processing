"""Project pipelines."""

from typing import Dict

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline
from healthcare_data_processing.pipelines.data_merge import create_pipeline as data_merge
from healthcare_data_processing.pipelines.data_cleaning import create_pipeline as data_cleaning
from healthcare_data_processing.pipelines.data_standardization import create_pipeline as data_standardization

def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    
    combined_pipeline = ( data_cleaning() + data_standardization() + data_merge())
    
    return {
        '__default__' : combined_pipeline,
        "data_cleaning" : data_cleaning(),
        "data_standardization" : data_standardization(),
        "data_merge" : data_merge()
    }

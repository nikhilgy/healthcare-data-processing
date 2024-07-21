"""Project pipelines."""

from typing import Dict

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline
from healthcare_data_processing.pipelines.data_analysis import create_pipeline as data_analysis
from healthcare_data_processing.pipelines.data_cleaning import create_pipeline as data_cleaning
from healthcare_data_processing.pipelines.data_processing import create_pipeline as data_processing

def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    
    combined_pipeline = ( data_cleaning() + data_processing() + data_analysis())
    
    return {
        '__default__' : combined_pipeline,
        "data_cleaning" : data_cleaning(),
        "data_processing" : data_processing(),
        "data_analysis" : data_analysis(),
        "combined": combined_pipeline
    }

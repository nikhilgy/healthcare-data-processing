"""
This is a boilerplate pipeline 'data_analysis'
generated using Kedro 0.19.6
"""
import pandas as pd

def merge_datasets(df1, df2, on_key, how='inner'):
    """
    Merges two datasets on a specified key.

    Parameters:
    df1 (pd.DataFrame): The first dataset.
    df2 (pd.DataFrame): The second dataset.
    on_key (str): The column name on which to merge the datasets.
    how (str): The type of merge to perform (e.g., 'inner', 'left', 'right', 'outer').

    Returns:
    pd.DataFrame: The merged dataset.
    """
    return pd.merge(df1, df2, on=on_key, how=how)


def merge_all_datasets(patients_df: pd.DataFrame, conditions_df: pd.DataFrame, medications_df: pd.DataFrame, observations_df : pd.DataFrame, encounters_df: pd.DataFrame) -> pd.DataFrame:
    
    df_master = merge_datasets(patients_df, conditions_df, on_key='patient_id', how='left')
    df_master = merge_datasets(df_master, medications_df, on_key='patient_id', how='left')
    df_master = merge_datasets(df_master, observations_df, on_key='patient_id', how='left')
    df_master = merge_datasets(df_master, encounters_df, on_key='patient_id', how='left')
    
    return df_master
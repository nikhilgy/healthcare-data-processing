"""
This is a boilerplate pipeline 'data_cleaning'
generated using Kedro 0.19.6
"""

import numpy as np
import pandas as pd

from ..utils import (convert_column_names_to_lowercase,
                     convert_column_values_to_lowercase, drop_columns,
                     remove_trailing_digits, rename_columns, replace_in_column)


def clean_patients(
    patients_df: pd.DataFrame, patient_gender_df: pd.DataFrame
) -> pd.DataFrame:
    """
    Cleans and preprocesses patient data by merging with gender information and standardizing columns.

    Args:
        patients_df (pd.DataFrame): DataFrame containing patient information with columns including 'PATIENT_ID', 'FIRST', 'LAST', 'MAIDEN', 'BIRTHDATE', etc.
        patient_gender_df (pd.DataFrame): DataFrame containing patient gender information with columns including 'Id' and 'GENDER'.

    Returns:
        pd.DataFrame: A cleaned DataFrame with standardized columns, including:
            - Merged patient and gender data
            - Renamed columns ('FIRST' to 'FIRST_NAME', 'LAST' to 'LAST_NAME')
            - Removal of unnecessary columns
            - Replacement of invalid birthdates ('9999-99-99') with NaN
            - Lowercased column names
    """

    result = pd.merge(
        patients_df, patient_gender_df, left_on="PATIENT_ID", right_on="Id", how="inner"
    )
    result = drop_columns(result, ["GENDER_x", "Id"])
    result = rename_columns(result, {"GENDER_y": "GENDER"})
    result = remove_trailing_digits(result, ["FIRST", "LAST", "MAIDEN"])
    result = rename_columns(result, {"FIRST": "FIRST_NAME", "LAST": "LAST_NAME"})
    result.loc[result["BIRTHDATE"] == "9999-99-99", "BIRTHDATE"] = np.nan
    result = convert_column_names_to_lowercase(result)

    return result


def clean_conditions(conditions_df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans and preprocesses condition data by standardizing column names and patient identifiers.

    Args:
        conditions_df (pd.DataFrame): DataFrame containing condition information with columns including 'PATIENT', etc.

    Returns:
        pd.DataFrame: A cleaned DataFrame with standardized patient identifiers and column names.
    """

    conditions_df = convert_column_values_to_lowercase(conditions_df, "PATIENT")
    conditions_df = convert_column_names_to_lowercase(conditions_df)
    return conditions_df


def clean_medications(medications_df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans and preprocesses medication data by removing duplicates, standardizing column values, and column names.

    Args:
        medications_df (pd.DataFrame): DataFrame containing medication information with columns including 'START', 'CODE', 'ENCOUNTER', 'REASONCODE', etc.

    Returns:
        pd.DataFrame: A cleaned DataFrame with standardized column values and column names.
    """

    medications_df = medications_df.drop_duplicates(subset=["START", "CODE"])
    medications_df = convert_column_values_to_lowercase(medications_df, "ENCOUNTER")
    medications_df = replace_in_column(medications_df, "REASONCODE", ".0", "")
    medications_df = convert_column_names_to_lowercase(medications_df)
    return medications_df


def clean_encounters(encounters_df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans and preprocesses encounter data by standardizing column values and column names.

    Args:
        encounters_df (pd.DataFrame): DataFrame containing encounter information with columns including 'PATIENT', 'REASONCODE', etc.

    Returns:
        pd.DataFrame: A cleaned DataFrame with standardized column values and column names.
    """

    encounters_df = convert_column_values_to_lowercase(encounters_df, "ENCOUNTER")
    encounters_df = replace_in_column(encounters_df, "REASONCODE", ".0", "")
    encounters_df = replace_in_column(encounters_df, "REASONCODE", "nan", "")
    encounters_df = convert_column_names_to_lowercase(encounters_df)
    return encounters_df


def clean_symptoms(
    symptoms_df: pd.DataFrame, patient_gender_df: pd.DataFrame
) -> pd.DataFrame:
    """
    Cleans and preprocesses symptoms data by merging with patient gender information and standardizing columns.

    Args:
        symptoms_df (pd.DataFrame): DataFrame containing symptom information with columns including 'PATIENT', etc.
        patient_gender_df (pd.DataFrame): DataFrame containing patient gender information with columns including 'Id' and 'GENDER'.

    Returns:
        pd.DataFrame: A cleaned DataFrame with standardized columns.
    """

    result = pd.merge(
        symptoms_df, patient_gender_df, left_on="PATIENT", right_on="Id", how="inner"
    )

    result = drop_columns(result, ["GENDER_x", "Id"])
    result = rename_columns(result, {"GENDER_y": "GENDER"})
    result = convert_column_names_to_lowercase(result)
    return result

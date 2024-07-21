"""
This is a boilerplate pipeline 'data_cleaning'
generated using Kedro 0.19.6
"""

import pandas as pd
import numpy as np

def clean_patients(
    patients_df: pd.DataFrame, patient_gender_df: pd.DataFrame
) -> pd.DataFrame:

    # TODO add docstrings

    result = pd.merge(
        patients_df, patient_gender_df, left_on="PATIENT_ID", right_on="Id", how="inner"
    )

    # TODO add rename and drop utility functions
    result.drop(columns=["GENDER_x"], inplace=True)
    result.drop(columns=["Id"], inplace=True)
    result.rename(columns={"GENDER_y": "GENDER"}, inplace=True)

    result["FIRST"] = result["FIRST"].str.replace(r"\d+$", "", regex=True)
    result["LAST"] = result["LAST"].str.replace(r"\d+$", "", regex=True)
    result["MAIDEN"] = result["MAIDEN"].str.replace(r"\d+$", "", regex=True)

    result.rename(columns={"FIRST": "FIRST_NAME"}, inplace=True)
    result.rename(columns={"LAST": "LAST_NAME"}, inplace=True)

    result.loc[result["BIRTHDATE"] == '9999-99-99', 'BIRTHDATE'] = np.nan

    result.columns = map(str.lower, result.columns)
    return result


def clean_conditions(conditions_df : pd.DataFrame) -> pd.DataFrame:
    
    # TODO add docstrings
    
    # TODO add lowercase utility functions
    conditions_df['PATIENT'] = conditions_df['PATIENT'].str.lower()
    conditions_df.columns = map(str.lower, conditions_df.columns)
    return conditions_df

def clean_medications(medications_df : pd.DataFrame) -> pd.DataFrame:
    
    # TODO add docstrings
    
    # TODO add lowercase & replace utility functions
    medications_df['ENCOUNTER'] = medications_df['ENCOUNTER'].str.lower()
    medications_df['REASONCODE'] = medications_df['REASONCODE'].astype(str).str.replace('.0', '', regex=False)
    medications_df.columns = map(str.lower, medications_df.columns)
    return medications_df

def clean_encounters(encounters_df: pd.DataFrame) -> pd.DataFrame:
    # TODO add docstrings
    
    # TODO add lowercase & replace utility functions
    
    encounters_df['PATIENT'] = encounters_df['PATIENT'].str.lower()
    encounters_df['REASONCODE'] = encounters_df['REASONCODE'].astype(str).str.replace('.0', '', regex=False).str.replace('nan', '', regex=False)
    encounters_df.columns = map(str.lower, encounters_df.columns)
    return encounters_df


def clean_symptoms(symptoms_df: pd.DataFrame, patient_gender_df: pd.DataFrame) -> pd.DataFrame:
    result = pd.merge(
        symptoms_df, patient_gender_df, left_on="PATIENT", right_on="Id", how="inner"
    )

    # TODO add rename and drop utility functions
    result.drop(columns=["GENDER_x"], inplace=True)
    result.drop(columns=["Id"], inplace=True)
    result.rename(columns={"GENDER_y": "GENDER"}, inplace=True)
    result.columns = map(str.lower, result.columns)
    return result
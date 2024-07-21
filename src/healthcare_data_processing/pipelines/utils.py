import pandas as pd


def remove_trailing_digits(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """
    Removes trailing digits from specified columns in the DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame containing the columns to be cleaned.
        columns (list): List of column names to remove trailing digits from.

    Returns:
        pd.DataFrame: The DataFrame with specified columns cleaned.
    """
    for column in columns:
        if column in df.columns:
            df[column] = df[column].str.replace(r"\d+$", "", regex=True)
    return df


def rename_columns(df: pd.DataFrame, column_map: dict) -> pd.DataFrame:
    """
    Renames columns in the DataFrame based on the provided mapping.

    Args:
        df (pd.DataFrame): The DataFrame whose columns will be renamed.
        column_map (dict): A dictionary where keys are current column names and values are new column names.

    Returns:
        pd.DataFrame: The DataFrame with renamed columns.
    """
    return df.rename(columns=column_map)


def drop_columns(df: pd.DataFrame, columns_to_drop: list) -> pd.DataFrame:
    """
    Drops specified columns from the DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame from which columns will be dropped.
        columns_to_drop (list): List of column names to be dropped.

    Returns:
        pd.DataFrame: The DataFrame with specified columns removed.
    """
    return df.drop(columns=columns_to_drop)


def convert_column_names_to_lowercase(df: pd.DataFrame) -> pd.DataFrame:
    """
    Converts all column names in the DataFrame to lowercase.

    Args:
        df (pd.DataFrame): The DataFrame whose column names will be converted to lowercase.

    Returns:
        pd.DataFrame: The DataFrame with column names converted to lowercase.
    """
    df.columns = map(str.lower, df.columns)
    return df


def convert_column_values_to_lowercase(
    df: pd.DataFrame, column_name: str
) -> pd.DataFrame:
    """
    Converts all values in a specified column of the DataFrame to lowercase.

    Args:
        df (pd.DataFrame): The DataFrame containing the column to be converted.
        column_name (str): The name of the column whose values will be converted to lowercase.

    Returns:
        pd.DataFrame: The DataFrame with specified column values converted to lowercase.
    """
    if column_name in df.columns:
        df[column_name] = df[column_name].str.lower()
    return df


def replace_in_column(
    df: pd.DataFrame, column_name: str, to_replace: str, replacement: str
) -> pd.DataFrame:
    """
    Replaces occurrences of a substring in a specified column of the DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame containing the column to be modified.
        column_name (str): The name of the column where replacements will occur.
        to_replace (str): The substring to be replaced.
        replacement (str): The string to replace the substring with.

    Returns:
        pd.DataFrame: The DataFrame with updated column values.
    """
    if column_name in df.columns:
        df[column_name] = (
            df[column_name]
            .astype(str)
            .str.replace(to_replace, replacement, regex=False)
        )
    return df

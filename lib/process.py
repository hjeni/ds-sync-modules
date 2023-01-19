"""
This module contains functions that can be used to process text data
"""


import pandas as pd


_STOPWORDS_DFLT = ["a", "i", "s", "v", "u"]


def _tokenize(df: pd.DataFrame, input_col: str, output_col: str) -> pd.DataFrame:
    """splits string into tokens"""
    df[output_col] =  df[input_col].apply(lambda x: x.split())
    return df


def _remove_stopwords(df: pd.DataFrame, input_col: str, output_col: str) -> pd.DataFrame:
    """splits string into tokens"""
    df[output_col] = (
        df
        .loc[:, input_col]
        .apply(lambda tokens: [x for x in tokens if x not in _STOPWORDS_DFLT])
    )
    
    return df


def tokenize_text_data(df: pd.DataFrame, input_col: str, output_col: str = "tokens") -> pd.DataFrame:
    """Processes text column, appending the tokenized column to the original DF"""
    tmp_col = "_tmp_"
    df_processed = (df
                    .transform(_tokenize, input_col=input_col, output_col=tmp_col)
                    .transform(_remove_stopwords, input_col=tmp_col, output_col=output_col)
                   )
    return df_processed.drop(tmp_col, axis=1)
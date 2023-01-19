"""
Text processing tests
"""

# example of adding module to PYTHONPATH dynamically
import sys
sys.path.append("./")


import pytest
import pandas as pd

from lib import process


@pytest.fixture()
def input_df() -> pd.DataFrame:
    return pd.DataFrame(
        data=["some text example"], columns=["text"]
    )


def test_split(input_df) -> None:
    df_tokenized = process._tokenize(input_df, input_col="text", output_col="tokens")
    tokens = df_tokenized.tokens.iloc[0]
    
    assert len(tokens) == 3

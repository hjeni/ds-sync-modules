# Databricks notebook source
# MAGIC %md
# MAGIC 
# MAGIC # Demo - funcitons
# MAGIC 
# MAGIC This notebook wrapes the code into functions

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ## Imports

# COMMAND ----------

import os
import pandas as pd

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ## Read

# COMMAND ----------

_DIR_DATA = "../../data/"
PATH_NPS = os.path.join(_DIR_DATA, "nps_example_1.csv")

# COMMAND ----------

df_raw = pd.read_csv(PATH_NPS)
df_raw.display()

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ## Process
# MAGIC 
# MAGIC **NOTE:** Column names are hardcoded for simplicity (which is a bad practice)

# COMMAND ----------

_STOPWORDS_DFLT = ["a", "i", "s", "v", "u"]


def tokenize(df: pd.DataFrame) -> pd.DataFrame:
    """splits string into tokens"""
    df["text_split"] =  df["text_nps"].apply(lambda x: x.split())
    return df


def remove_stopwords(df: pd.DataFrame, stopwords: list = None) -> pd.DataFrame:
    """splits string into tokens"""
    if stopwords is None:
        stopwords = _STOPWORDS_DFLT
    df["text_stopword_removed"] = (
        df
        .loc[:, "text_split"]
        .apply(lambda tokens: [x for x in tokens if x not in stopwords])
    )
    
    return df

# COMMAND ----------

df_processed = (df_raw
                .transform(tokenize)
                .transform(remove_stopwords)
               )

df_processed.display()

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ---

# COMMAND ----------



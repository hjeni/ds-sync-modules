# Databricks notebook source
# MAGIC %md
# MAGIC 
# MAGIC # Demo - linear code
# MAGIC 
# MAGIC This notebook contains simple linear code.

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

df = pd.read_csv(PATH_NPS)
df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ## Process

# COMMAND ----------

df["text_split"] = df["text_nps"].apply(lambda x: x.split())
df.display()

# COMMAND ----------

STOPWORDS = ["a", "i", "s", "v", "u"]

df["text_stopword_removed"] = df["text_split"].apply(lambda tokens: [x for x in tokens if x not in STOPWORDS])

df_exploded = df.explode("text_stopword_removed")
df_exploded.display()

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ## Frequency

# COMMAND ----------

# TODO: count number of occurences, etc.

# COMMAND ----------



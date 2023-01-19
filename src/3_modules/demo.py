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

from lib import process 

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

df_processed = process.tokenize_text_data(df_raw, input_col="text_nps")
df_processed.display()

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ---

# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



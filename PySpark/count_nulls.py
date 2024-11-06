# Write a PySpark Function to Count Nulls in Each Column
from pyspark.sql.functions import col, sum

def count_nulls(df):
    return df.select([sum(col(c).isNull().cast("int")).alias(c) for c in df.columns])
# This counts nulls per column by summing where each column value is null.
# Create a New Column in a DataFrame Based on Conditions Applied to Existing Columns
from pyspark.sql.functions import when

df = df.withColumn("new_column", when(df["existing_column"] > 10, "High").otherwise("Low"))
# Uses when() for conditional column creation.
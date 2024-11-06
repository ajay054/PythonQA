# Flatten a Nested JSON Structure Into a DataFrame

from pyspark.sql.functions import col

def flatten(df):
    flat_cols = [col(field.name) for field in df.schema.fields if isinstance(field.dataType, StructType)]
    nested_cols = [col(field.name + ".*") for field in df.schema.fields if isinstance(field.dataType, StructType)]
    return df.select(*flat_cols, *nested_cols)

# Write a PySpark UDF (User Defined Function) for Custom Transformations
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

def my_custom_function(value):
    return value.upper()

my_udf = udf(my_custom_function, StringType())
df = df.withColumn("new_column", my_udf("existing_column"))
# Defines a function and registers it as a UDF for transformations.
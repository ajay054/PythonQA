from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize Spark session
spark = SparkSession.builder.appName("FindDuplicates").getOrCreate()

# Sample data
data = [
    (1, 'Alice', 50000),
    (2, 'Bob', 60000),
    (3, 'Charlie', 70000),
    (4, 'David', 80000),
    (1, 'Alice', 50000),
    (3, 'Charlie', 70000)
]

# Define the schema for the DataFrame
columns = ['Employee ID', 'Employee Name', 'Salary']

# Create a DataFrame
df = spark.createDataFrame(data, columns)

# Identify duplicate rows based on 'Employee ID', 'Employee Name', and 'Salary'
duplicates = (
    df.groupBy('Employee ID', 'Employee Name', 'Salary')
    .count()
    .filter(col('count') > 1)
    .select('Employee ID', 'Employee Name', 'Salary')
)

# Join with original DataFrame to show all instances of duplicates
duplicate_rows = df.join(duplicates, on=['Employee ID', 'Employee Name', 'Salary'], how='inner')

# Show the duplicate rows
print("Duplicate Rows:")
duplicate_rows.show()

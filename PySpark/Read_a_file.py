# Read a CSV File Into a DataFrame and Show Basic Statistics
from pyspark.sql import SparkSession

# Initialize SparkSession
spark = SparkSession.builder.appName("ReadCSV").getOrCreate()

# Read the CSV file
df = spark.read.csv("file.csv", header=True, inferSchema=True)

# Display summary statistics
df.describe().show()

# Stop the SparkSession (optional but recommended)
spark.stop()

# Reads a CSV file into a DataFrame and displays basic stats using describe().

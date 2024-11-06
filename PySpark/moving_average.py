# Implement a Window Function to Find the Moving Average of a Column

from pyspark.sql.window import Window
from pyspark.sql.functions import avg

def moving_average(df, column, window_size):
    window_spec = Window.orderBy("id").rowsBetween(-window_size + 1, 0)
    return df.withColumn("moving_average", avg(column).over(window_spec))

#  This creates a moving average using a specified window size.

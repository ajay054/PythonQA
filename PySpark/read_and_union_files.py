# Write a PySpark Job to Read From Multiple Files and Union Them Into a Single DataFrame

def read_and_union_files(spark, file_paths):
    dfs = [spark.read.csv(file, header=True) for file in file_paths]
    return reduce(lambda df1, df2: df1.union(df2), dfs)
#  Reads multiple files into DataFrames and unions them into one.
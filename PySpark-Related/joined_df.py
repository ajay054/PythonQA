# Join Two DataFrames and Remove Duplicate Columns
joined_df = df1.join(df2, "common_column").drop(df2["common_column"])

# Joins on a common column and removes duplicates.
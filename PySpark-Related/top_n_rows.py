# Find the Top N Rows Based on a Column Value in a DataFrame
def top_n_rows(df, column, n):
    return df.orderBy(col(column).desc()).limit(n)


# Orders the DataFrame in descending order of a column and retrieves the top n rows.

# Explain How Spark's Lazy Evaluation Works With Examples

#  In Spark, transformations like map, filter, and select are lazy, meaning they’re not executed until an action (e.g., show(), count(), collect()) is called. This allows Spark to optimize execution plans.
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit

# Создаем Spark сессию
spark = SparkSession.builder.appName("Продукты и категории").getOrCreate()

# Пример данных
products_data = [(1, 'Продукт A'), (2, 'Продукт B'), (3, 'Продукт C'), (4, 'Продукт D')]
categories_data = [(1, 'Категория X'), (2, 'Категория Y')]
product_category_data = [(1, 1), (2, 1), (3, 2)]

# Создаем DataFrame
products_df = spark.createDataFrame(products_data, ['product_id', 'product_name'])
categories_df = spark.createDataFrame(categories_data, ['category_id', 'category_name'])
product_category_df = spark.createDataFrame(product_category_data, ['product_id', 'category_id'])

# Выполняем join для получения пар «Имя продукта – Имя категории»
product_category_joined = product_category_df.join(products_df, "product_id").join(categories_df, "category_id")

# Выбираем необходимые колонки
product_category_pairs = product_category_joined.select("product_name", "category_name")

# Выбираем продукты без категорий
products_with_categories = product_category_df.select("product_id").distinct()
products_without_categories = products_df.join(products_with_categories, "product_id", "left_anti").select("product_name")

# Показать результаты
print("Пары «Имя продукта – Имя категории»:")
product_category_pairs.show()

print("Продукты без категорий:")
products_without_categories.show()

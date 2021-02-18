from pyspark.sql.functions import mean
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SimpleApp").getOrCreate()

df = spark.read.format("csv")\
          .option("header", "true")\
          .option("inferSchema", "true").load("bar.txt")

df.show()

res = df.select([mean('foo')])
res.show()

res = df.groupBy("id").mean("foo","bar")
res.show()
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SimpleApp").getOrCreate()
sc = spark.sparkContext

rdd0 = sc.textFile("foo.txt")

rdd1 = rdd0.flatMap( lambda line : line.split(" ") )
rdd2 = rdd1.map( lambda word : (word,1) )
rdd3 = rdd2.reduceByKey( lambda a,b : (a + b) )

print(rdd3.collect())
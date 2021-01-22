from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import DataStructs
import numpy as np
from sklearn.datasets import dump_svmlight_file

from pyspark.ml import Pipeline
from pyspark.ml.regression import RandomForestRegressor
from pyspark.ml.feature import VectorIndexer
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.sql import SparkSession

from pyspark.ml.linalg import Vectors

spark = SparkSession.builder.appName("SimpleApp").getOrCreate()
df = spark.read.option("header","true")\
               .option("delimiter", '\t').csv("acd_logd_100.smiles")

print(df.select("canonical_smiles", "acd_logd").rdd)

data = df.select("canonical_smiles", "acd_logd").rdd.map( lambda row: (row.canonical_smiles, float(row.acd_logd)) )\
         .map( lambda x: (Chem.MolFromSmiles(x[0]), x[1]) )\
         .map( lambda x: (AllChem.GetMorganFingerprintAsBitVect(x[0], 2, nBits=1024), x[1]) )\
         .map( lambda x: (np.array(x[0]),x[1]) )\
         .map( lambda x: (Vectors.dense(x[0].tolist()),x[1]) )\
         .map( lambda x: (x[0],x[1]))\
         .toDF(["features", "label"] )

# Automatically identify categorical features, and index them.
# Set maxCategories so features with > 4 distinct values are treated as continuous.
featureIndexer =\
    VectorIndexer(inputCol="features", outputCol="indexedFeatures", maxCategories=4).fit(data)

# Split the data into training and test sets (30% held out for testing)
(trainingData, testData) = data.randomSplit([0.7, 0.3])

# Train a RandomForest model.
rf = RandomForestRegressor(featuresCol="indexedFeatures")

# Chain indexer and forest in a Pipeline
pipeline = Pipeline(stages=[featureIndexer, rf])

# Train model.  This also runs the indexer.
model = pipeline.fit(trainingData)

# Make predictions.
predictions = model.transform(testData)

# Select example rows to display.
predictions.select("prediction", "label", "features").show(5)

# Select (prediction, true label) and compute test error
evaluator = RegressionEvaluator(
    labelCol="label", predictionCol="prediction", metricName="rmse")
rmse = evaluator.evaluate(predictions)
print("Root Mean Squared Error (RMSE) on test data = %g" % rmse)

rfModel = model.stages[1]
print(rfModel)  # summary only

spark.stop()
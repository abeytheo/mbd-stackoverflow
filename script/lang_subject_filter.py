from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
import sys

sc = SparkContext()
sc.setLogLevel("Error")
spark = SparkSession.builder.getOrCreate()

if __name__ == "__main__":
	data_path = "file:///home/s1745646/Project/sample2"

	if len(sys.argv) > 1:
		data_path = sys.argv[1]

	sample = spark.read.json(data_path)
	df = sample.where(sample['_Tags'].isNotNull())
	df.withColumn("_Tags", lower(col("_Tags")))


	langs = spark.read.csv("file:///home/s1745646/Project/languages.csv", header=True)
	subjects = spark.read.csv("file:///home/s1745646/Project/subjects.csv", header=True)

	subset_terms = langs.crossJoin(subjects).rdd.map(lambda x : (x.Languages.lower(), x.Subjects.lower())).collect()

	for term in subset_terms:
		lang = term[0]
		subject = term[1]

		subset = df.filter(df['_Tags'].contains(lang)).filter(df['_Tags'].contains(subject))
		print(subset.count())
		## Measure popularity

#print(subset_terms)
#sample.printSchema()

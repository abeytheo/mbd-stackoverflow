from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

import subset_filter
import popularity_measure
import sys

sc = SparkContext()
sc.setLogLevel("Error")
spark = SparkSession.builder.getOrCreate()

## Set module variable
subset_filter.spark = spark

def subset_func(subset, csv_path, lang, subject):
	print(subset.count())
	#result = subset.select('_Tags').rdd.map(lambda x: x.replace('>','').replace('<',' ')).flatMap(lambda x: x.split(' ')).map(lambda x: (x,1).reduceByKey(lambda a,b: a+b))
	#res = result.sortBy(lambda x: x[1], ascending=False)
	#print(res.collect())

        # For Year aggregation
        # Note: passing tuple to group_column_list variable
        calculate_popularity_save_csv(subset, csv_path, lang, subject, ('year', ), 'year')

        # For year and month aggregation
        calculate_popularity_save_csv(subset, csv_path, lang, subject, ('year', 'month'), 'year_month')

if __name__ == "__main__":
	data_path = "file:///home/s2118947/sample3"
	csv_path = 'file:///home/s2118947/'

	if len(sys.argv) > 1:
		data_path = sys.argv[1]

    subset_filter.subset_filter(data_path, func=popularity_measure.popularity_measure)
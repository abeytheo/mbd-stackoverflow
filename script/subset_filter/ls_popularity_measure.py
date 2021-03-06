from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

import subset_filter
import popularity_measure
import topNTags
import sys

sc = SparkContext()
sc.setLogLevel("Error")
spark = SparkSession.builder.getOrCreate()

## Set module variables
subset_filter.spark = spark
topNTags.sc = sc

if __name__ == "__main__":
        #data_path = "file:///home/s2118947/sample3"
        data_path = "hdfs:///user/s2125048/stackoverflow/post3/"
	csv_path = 'file:///home/s2118947/new/'

        if len(sys.argv) > 1:
                data_path = sys.argv[1]
	# popularity measure
        subset_filter.subset_filter(data_path, csv_path=csv_path, func=popularity_measure.popularity_measure)
	
	# compute topNTags
	#subset_filter.subset_filter(data_path, func=topNTags.topNTags)

Import pyspark 
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType

spark = SparkSession.builder.master("local").appName("read_for_model").getOrCreate()

def catalog = '{"table":{"namespace":"default","name":"ABT"},
	"rowkey":"key",
	"columns":{
	"col0":{"cf":"rowkey","col":"id","type":"str"},
	"col1":{"cf":"rowkey","col":"date","type":"date"},
	"col2":{"cf":"rowkey","col":"open","type":"floata"},
	"col3":{"cf":"rowkey","col":"close","type":"float"},
	"col4":{"cf":"rowkey","col":"high","type":"float"},
	"col5":{"cf":"rowkey","col":"low","type":"float"},
	"col6":{"cf":"rowkey","col":"volume","type":int"}
}
}'


#load 
df = spark.read.format("org.apache.spark.sql.execution.datasources.hbase").option(catalog=catalog).load()



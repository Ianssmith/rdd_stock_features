Import pyspark 
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType

spark = SparkSession.builder.master("local").appName("put_in_hbase").getOrCreate()

stock_schema = StructType().add("id", "integer")
	.add("date", "date")
	.add("open", "float")
	.add("high", "float")
	.add("low", "float")
	.add("close", "float")
	.add("volume", "integer")

df = spark.read.json("hdfs://localhost:9000/UKUSMarHDFS/ian/proj/data/ABT.json", schema=stock_schema)

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

df.write.options(catalog=catalog).format("org.apache.spark.sql.execution.datasources.hbase").save()

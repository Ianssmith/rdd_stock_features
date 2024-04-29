import pyspark 
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType

spark = SparkSession.builder.master("local").appName("put_in_hbase").enableHiveSupport().getOrCreate()

# Load JSON data from HDFS into DataFrame
df = spark.read.json('hdfs://ip-172-31-3-80.eu-west-2.compute.internal:8020/user/ec2-user/UKUSMarHDFS/ian/proj/data/ACN.json')

df.write.saveAsTable('ian_hive_external_alphav')

df.createOrReplaceTempView("temp_json_table")

# Define Hive table schema (optional: infer schema from DataFrame)
hive_table_schema = "date STRING, open FLOAT, high FLOAT, low FLOAT, close FLOAT, volume INT"  # Modify according to your JSON schema

# Create external Hive table from temporary table
spark.sql(f"CREATE EXTERNAL TABLE IF NOT EXISTS ian_hive_external_alphav \
           ({hive_table_schema}) \
           ROW FORMAT SERDE 'org.apache.hive.hcatalog.data.JsonSerDe'\
           LOCATION 'hdfs://ip-172-31-3-80.eu-west-2.compute.internal:8020/user/ec2-user/UKUSMarHDFS/ian/proj/data/ACN.json'")

'''
stock_schema = StructType().add("date", "date")\
	.add("open", "float")\
	.add("high", "float")\
	.add("low", "float")\
	.add("close", "float")\
	.add("volume", "integer")

#df_spark.write.save(f'hdfs://ip-172-31-3-80.eu-west-2.compute.internal:8020/user/ec2-user/UKUSMarHDFS/ian/proj/data/{i[1]}.json', format='json', mode='append')
df = spark.read.json('hdfs://ip-172-31-3-80.eu-west-2.compute.internal:8020/user/ec2-user/UKUSMarHDFS/ian/proj/data/ACN.json', schema=stock_schema)
#df = spark.read.json("hdfs://localhost:9000/UKUSMarHDFS/ian/proj/data/ABT.json", schema=stock_schema)


catalog = '{"table":{"namespace":"default","name":"ACN"},\
	"rowkey":"key",\
	"columns":{\
	"col1":{"cf":"rowkey","col":"date","type":"date"},\
	"col2":{"cf":"rowkey","col":"open","type":"float"},\
	"col3":{"cf":"rowkey","col":"high","type":"float"},\
	"col4":{"cf":"rowkey","col":"low","type":"float"},\
	"col5":{"cf":"rowkey","col":"close","type":"float"},\
	"col6":{"cf":"rowkey","col":"volume","type":int"}\
}\
}'

df.write.options(catalog=catalog).format("org.apache.spark.sql.execution.datasources.hbase").save()

notes

'''
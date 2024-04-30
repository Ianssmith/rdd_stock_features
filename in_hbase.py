import pyspark 
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType

spark = SparkSession.builder.master("local").appName("put_in_hbase").enableHiveSupport().getOrCreate()


# Define Hive table schema (optional: infer schema from DataFrame)
hive_table_schema = "date date, open double, high double, low double, close double, volume double"  # Modify according to your JSON schema

# Create external Hive table from temporary table
spark.sql(f"CREATE EXTERNAL TABLE IF NOT EXISTS ian_hive_external_alphav \
           ({hive_table_schema}) \
			row format delimited\
            fields terminated by ','\
            stored as TEXTFILE\
           lOCATION 'hdfs://ip-172-31-3-80.eu-west-2.compute.internal:8020/user/ec2-user/UKUSMarHDFS/ian/proj/data/'\
           tblproperties(\"skip.header.line.count\"=\"1\")")

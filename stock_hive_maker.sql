create external table if not exists alphav(
    `date` date,
    `open` double,
    `high` double,
    `low` double,
    `close` double,
    `volume` double
)
row format delimited
fields terminated by ','
stored as TEXTFILE
LOCATION 'hdfs://ip-172-31-3-80.eu-west-2.compute.doubleernal:8020/user/ec2-user/UKUSMarHDFS/ian/proj/data/'
tblproperties("skip.header.line.count"="1");

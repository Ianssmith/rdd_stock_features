# S&P500 and Forex models

## data sources
Open exchange rates api
    1000 free requests per month
alphavantage api
    25 requests per day
google patents public data
## Flow 
### apis -> hdfs -> hive/hbase -> models

![alt text](CloudArchitecture.png "pipeline")
## beginning db model wip
![alt text](db_model.png "dbmodel")

## api to hdfs ingestion
![alt text](ingest_av_api_hdfs.png "hdfs_ingestion")

## external hive table from hdfs 
![alt text](hive_table.png "external hive table")

## jenkins build triggers
### one to periodically query data from the api
![alt text](cron_trigger.png "cron build trigger")
### one following the api query build trigger
![alt text](model_trigger.png "model build trigger")

### Some basic feature enhancement and visualization
![alt text](basic_feature_nplot.png "year column/pricechart")

## Simple regression model results to predict 2023 prices
![alt text](regression.png "prediction results")

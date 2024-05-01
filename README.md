# S&P500 and Forex models

## data sources
Open exchange rates api
    1000 free requests per month
alphavantage api
    25 requests per day
google patents public data
## Flow 
### apis -> hdfs -> hive/hbase -> models

[<img src="CloudArchitecture.png">](https://link-to-your-URL/)
## beginning db model wip
[<img src="./imgs/db_model.png">](https://link-to-your-URL/)

## api to hdfs ingestion
[<img src="./imgs/ingest_av_api_hdfs.png">](https://github.com/Ianssmith/rdd_stock_features/blob/master/alphav.py)

## external hive table from hdfs 
[<img src="./imgs/hive_table.png">](https://github.com/Ianssmith/rdd_stock_features/blob/master/in_hbase.py)

## jenkins build triggers
### one to periodically query data from the api
[<img src="./imgs/cron_trigger.png">](https://link-to-your-URL/)
### one following the api query build trigger
[<img src="./imgs/model_trigger.png">](https://link-to-your-URL/)

### Some basic feature enhancement and visualization
[<img src="./imgs/basic_feature_nplot.png">](https://github.com/Ianssmith/rdd_stock_features/blob/master/model.py)

## Simple regression model results to predict 2023 prices
[<img src="./imgs/regression.png">](https://github.com/Ianssmith/rdd_stock_features/blob/master/model.py)
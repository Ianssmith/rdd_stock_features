import json
import pandas as pd
import requests
import time
from pyspark.sql import SparkSession

spdf = pd.read_csv("./data/sp.csv")

#import env vars
file = open(".env", "r")
content = file.read()
file.close()
envdata = content.split("\n")
env = {}
for i in envdata:
    d = i.split("=")
    env[d[0]] = d[1]


#alpha vantage ticker symbol search
#search = requests.get(f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=apple&apikey={env["alphav"]}')
#data = search.json()
#pp.pprint(data)

#alphavantage api data 25 calls per day
#csv
#alvc = requests.get(f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IBM&apikey={env["alphav"]}&datatype=csv')
#json
dailyd = []
for i in spdf['symbol'][2:3]:
    print(f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={i}&outputsize=full&apikey={env["alphav"]}')
    alv_response = requests.get(f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={i}&outputsize=full&apikey={env["alphav"]}',verify=False)
    #index 0 will be data index 1 is data symbol
    dailyd.append([alv_response,i])
    time.sleep(42)
dfs = []
for i in dailyd:
    json_data = i[0].json()
    print(json_data)
    json_nometa = json_data['Time Series (Daily)']
    df = pd.DataFrame.from_dict(json_nometa, orient='index')
    ndf = df.reset_index()
    fdf = ndf.rename(columns={"index":"date","1. open": "open", "2. high": "high","3. low":"low","4. close":"close","5. volume":"volume","delta":"delta"})
    #again index 0 is data index 1 is data symbol
    dfs.append([fdf,i[1]])
    #write api calls to json file incase sparksession hdfs write does not work
    with open(f'./data/{i[1]}.json', 'w') as outfile:
        outfile.write(str(i[0].json()))

# Create SparkSession 
spark = SparkSession.builder \
      .master("local[1]") \
      .appName("alphav_data") \
      .getOrCreate() 

for i in dfs:
    df_spark = spark.createDataFrame(i[0])
    df_spark.write.save(f'/user/ec2-user/UKUSMarHDFS/ian/{i[1]}.parquet', format='parquet', mode='append')
    #df_spark.write.save(f'/user/ec2-user/UKUSMarHDFS/ian/{i[1]}.parquet', format='parquet', mode='append')

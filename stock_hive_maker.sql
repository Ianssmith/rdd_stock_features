create external table if not exists alphav(
    'date' date,
    'open' float,
    'high' float,
    'low' float,
    'close' float,
    'volume' float
)
row format delimited
fields terminated by ','
stored as json
location 'UKUSMarHDFS/ian/proj/data/ACN.json'
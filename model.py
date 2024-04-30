#data import
#import pyspark 
#from pyhive import hive
#from pyspark.sql import SparkSession
#from pyspark.sql.types import StructType
#data wrangling/plots
import pandas as pd
import scipy
import matplotlib.pyplot as plt
import datetime
#machine learning
#from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split

#host = "jdbc:hive2://ip-172-31-1-36.eu-west-2.compute.internal"
#port = 2181
#conn = hive.Connection(host=host,port=port)

#spark = SparkSession.builder.master("local").appName("read_for_model").getOrCreate()
#df.spark.read.table("alphav")

#df = pd.read_sql("select * from alphav", conn)
df = pd.read_csv('./data/ADBE.csv')
#print(df) 

df['date'] = pd.to_datetime(df['date'])
df['year'] = df['date'].dt.year

#df['year'] = df['date'].dt.year
print(df)


plt.plot(df['date'], df['close'])
plt.title('closing price vs date for Adobe stock')
plt.xlabel('date')
plt.ylabel('price')
plt.show()

print(df['close'].min())
print(df['close'].max())
yin = [x for x in range(int(df['close'].min()),int(df['close'].max()),20)]
print(yin)
Xin = scipy.sparse.csr_matrix(df.values)

X,y  =  (Xin,yin)
#clf = Perceptron(tol=1e-3, random_state=42)
clf = SGDClassifier(loss="perceptron", eta0=1, learning_rate="constant", penalty=None)
clf.fit(X,y)
clf.score(X,y)


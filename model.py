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
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
#from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier

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


traindf = df[df['year'] != 2023]
traindf.head()

testdf_wclose = df[df['year'] == 2023]
testdf = testdf_wclose[['open','high','low','volume']]
testdf.head()

# Split the 'close' column into features and target
X = traindf[['open', 'high', 'low', 'volume']]  # Features
y = traindf['close']  # Target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Linear Regression model
reg = LinearRegression()
reg.fit(X_train, y_train)

# Predict on the test set
y_pred = reg.predict(X_test)

# Evaluate the model using Mean Squared Error
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Predict further values
predicted_close = reg.predict(testdf)
print("Predicted close values for 2023 :", predicted_close[1:10])
print(len(predicted_close))
print(len(testdf_wclose))
matcher = []
for i,el in enumerate(predicted_close):
    print('prediction off by',el - testdf_wclose['close'].iloc[i])
    #print('prediction off by',el - testdf_wclose['close'].iloc[i],' for ',testdf_wclose['date'].iloc[i])


'''
## trying bin classification wip
print(traindf['close'].min())
print(traindf['close'].max())
ytrain = [x for x in range(int(traindf['close'].min()),int(traindf['close'].max()),40)]
print(ytrain)
Xin = scipy.sparse.csr_matrix(df['close'])

# Train the SGDClassifier
clf = SGDClassifier()
clf.fit(X_train, ytrain)

# Predict on the test set
y_pred = clf.predict(X_test)

# Evaluate the accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Predict 2023 categories

# Predict the 'close' values for 2023 data
predicted_close = clf.predict(testdf)
print("Predicted close values for further data:", predicted_close)


X,y  =  (Xin,yin)
#clf = Perceptron(tol=1e-3, random_state=42)
clf = SGDClassifier(loss="perceptron", eta0=1, learning_rate="constant", penalty=None)
clf.fit(X,y)
clf.score(X,y)

'''
import pandas as pd
import numpy as np
import math

#reading csv from pandas
data = pd.read_csv('train.csv')

#retrieving all the column names 
headers = data.columns.tolist()

#removing the Id field
headers.remove('Id')

#removing the SalePrice field which is not included in feature set matrix
headers.remove('SalePrice')

temp = []
temp.append(np.ones(len(data['SalePrice'].values))) #x0 values are populated
no_of_features = 1


#retrieving only the numerical value features[discarding all the categorical features]
for ele in headers:
	try:
		int((data[ele].values)[0])
		temp.append(data[ele].values)
		no_of_features+=1
	except:ValueError

Y = data['SalePrice'].values
X = np.array(temp).T

#all the nan values are replaced by zero
for i in range(len(X)):
	for j in range(len(X[i])):
		if math.isnan(X[i][j]):
			X[i][j] = 0

#initialising the theta values to 1
theta = np.array(np.ones(no_of_features))
#Y = data['SalePrice'].values



# print X
# print Y
# print theta
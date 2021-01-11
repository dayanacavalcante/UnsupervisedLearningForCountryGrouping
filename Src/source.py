# Imports

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

# Data Loading

data = pd.read_csv('C:\\Users\\RenanSardinha\\Documents\\Data Science\\Unsupervised Learing for country grouping\\Data\\Country-data.csv')
print(data)

# Data Preparation

print(data.isnull().sum())

print(data.dtypes)

data.child_mort = data.child_mort.astype("int")
data.exports = data.exports.astype("int")
data.health = data.health.astype("int")
data.imports = data.imports.astype("int")
data.inflation = data.inflation.astype("int")
data.life_expec = data.life_expec.astype("int")
data.total_fer = data.total_fer.astype("int")

print(data)

print(data.iloc[:,1:10])

data2 = data.iloc[:,1:10]

# Elbow Method

clf = KMeans()
ssd = []
K = range(1,10)
for k in K:
    km = KMeans(n_clusters=k)
    km = km.fit(data2)
    ssd.append(km.inertia_)

plt.figure()
plt.plot(K, ssd, '-bx')
plt.xlabel('Clusters')
plt.ylabel('Distance')
plt.title('Elbow Method For Optimization')
plt.show()

# Model Training

kmean = KMeans(n_clusters=4)
kmean.fit(data2)

pred = kmean.labels_
print(pred)

sns.scatterplot(data=data, x='gdpp', y='income', hue=kmean.labels_)

data['Cluster'] = pred
print(data.head())

boolArray = data['Cluster'] == 0
print(data[boolArray])

# Print the results

print(data['country'][data['income']<1000])
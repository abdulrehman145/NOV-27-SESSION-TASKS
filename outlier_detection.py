import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

np.random.seed(42)
n_values=np.random.normal(0,3,100)
outliers=np.random.normal(0,5,100)
data=np.concatenate([n_values,outliers])
df=pd.DataFrame(data,columns=['values'])

print("The values are given below:\n",df)
df['zscore']=np.abs(stats.zscore(df['values']))
print("The zscore of the values is below:\n",df)

plt.figure(figsize=(10,5))
sns.boxplot(df['values'])
plt.title("Boxplot Visualization Of Data")
plt.show()

Q1=df['values'].quantile(0.25)
Q3=df['values'].quantile(0.75)
IQR=Q3-Q1

lower_bound=(Q1-1.5)*IQR
upper_bound=(Q3+1.5)*IQR

outliers_detected_iqr=df[(df['values']>lower_bound) | (df['values']<upper_bound)]
print("outliers detected by IQR Method:\n")
print(outliers_detected_iqr)

plt.figure(figsize=(10,5))
sns.boxplot(x=df['values'],color='lightblue')
plt.scatter(outliers_detected_iqr['values'],np.ones(len(outliers_detected_iqr)),color="red",label="IQR detected outliers")
plt.title("Box plot representing IQR outliers")
plt.xlabel("Values")
plt.legend()
plt.show()

scaler = StandardScaler()
df["scaled_values"] = scaler.fit_transform(df[['values']])


db = DBSCAN(eps=0.5, min_samples=5).fit(df[['scaled_values']])
df['dbscan_labels'] = db.labels_


outliers_dbscan = df[df['dbscan_labels'] == -1]
print("Outliers detected by DBSCAN:")
print(outliers_dbscan)


plt.figure(figsize=(10, 5))


plt.scatter(df[df['dbscan_labels'] != -1]['scaled_values'],
            np.zeros(len(df[df['dbscan_labels'] != -1])),
            color="blue", label="Clustered Points")


plt.scatter(outliers_dbscan['scaled_values'],
            np.zeros(len(outliers_dbscan)),
            color="red", label="Outliers")

plt.title("Outliers detected by using DBSCAN")
plt.xlabel("Values")
plt.legend()
plt.show()
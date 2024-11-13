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

outliers_detected_iqr=df((df['values']>lower_bound) | (df['values']<upper_bound))
print("outliers detected by IQR Method:\n")
print(outliers_detected_iqr)

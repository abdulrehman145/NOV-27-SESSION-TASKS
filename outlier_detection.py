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
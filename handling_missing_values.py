import numpy as np
import pandas as pd

employee_data={
    'Name':["Abd","Zubair","Talha",np.nan,"Kashmir","Trip"],
    'Salary':[350000,49000,np.nan,700,8000,3000]
}

df=pd.DataFrame(employee_data)
print("Original Data:\n")
print(df)

df["forward filled Salary"]=df["Salary"].ffill()

df["backward filled Salary"]=df["Salary"].bfill()

df["mean filled salary"]=df["Salary"].fillna(df["Salary"].mean())

df["median filled salary"]=df["Salary"].fillna(df["Salary"].median())
print("Handled Data:\n")
print(df)
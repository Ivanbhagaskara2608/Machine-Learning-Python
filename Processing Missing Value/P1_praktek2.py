#Libraries
from sklearn.preprocessing import LabelEncoder
from pandas import DataFrame
import pandas as pd
import numpy as np

# Baca file dataset
df = pd.read_csv("Apartemen_ok.csv")

# melihat semua isi data
print(df)
le = LabelEncoder()

for col in df.columns.values:
    # Encoding pada variabel kategorial
    if df[col].dtypes=='object':
        data = df[col].append(df[col])
        le.fit(data.values)
        df[col]=le.transform(df[col])
df.head(10)

# Simpan data 
df.to_csv('Apartemen_numerik.csv', header=True, index=False)
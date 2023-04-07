from operator import le
from click import style
from pandas import DataFrame
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt

# baca file 
df  = pd.read_csv("Apartemen_ok2.csv")
print(df)
df.info()

# membuat list yanga akan ditambahkan menjadi kolom
label_kelas = ['Murah', 'Murah', 'Mahal', 'Murah', 'Mahal', 'Mahal', 'Mahal', 'Murah', 'Murah']

# memberi nama kolom tambahan 'label'
df['Label'] = label_kelas
print(df)

# menampilkan statistik deskriptif, hanya dengan numerik
print(df.describe())

# mengeksplore lebih dalam atribut wilayah (tipe kategori)
df.Wilayah.unique()
valueCount = df.Wilayah.value_counts()
print(valueCount)

# visualisasi dalam diagram batang kolom wilayah
sns.set(style="darkgrid")
ax = sns.countplot(x="Wilayah", data=df)

# bentuk lain plot kolom wilayah (ada text jumlah)
plt.figure(figsize=(5,5))

# total = float(len(df['Label']))
ax = sns.countplot(x="Wilayah", data=df)
for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x()+p.get_width()/2.,height,'{:1.0f}'.format((height)), ha="center")
plt.show()

# menampilkan histogram untuk semua atribut numerik
numerik_df = df.select_dtypes(include=['float64'])
numerik_index = numerik_df.columns
print(numerik_index)
df.hist(column=numerik_index, figsize=(10,20), layout=(5,1))
plt.show()

# menampilkan histogram untuk atribut numerik tertentu
numerik_df = ['Jum_kamar']
numerik_index = numerik_df
print(numerik_index)
df.hist(column=numerik_index, figsize=(10,20), layout=(5,1))
plt.show()

numerik_df = ['KodeApt']
numerik_index = numerik_df
print(numerik_index)
df.hist(column=numerik_index, figsize=(10,20), layout=(5,1))
plt.show()

# boxplot with mathplotlib, melihat outlier yg dapat terjadi misalnya karena kesalahan ketik
plt.boxplot(df.KodeApt)
plt.plot()
plt.show()
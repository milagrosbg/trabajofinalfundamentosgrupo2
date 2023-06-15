import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly_express as px

df=pd.read_csv('maquillajes.csv')

columns_to_exclude = ['codigo']
df_describe = df.drop(columns=columns_to_exclude)
description = df_describe.describe()
print(description)

valores = df[["nombre","precio"]]
print(valores)

ax = valores.plot.bar(x="nombre", y="precio", rot=0)
plt.show()


marca_stock = df.groupby('marca')['stock'].sum()
plt.pie(marca_stock, labels=marca_stock.index, autopct='%1.1f%%')
plt.axis('equal')
plt.title("Marca-Stock")
plt.show()


marca_precio_prom = df.groupby('marca')['precio'].mean()
plt.bar(marca_precio_prom.index, marca_precio_prom)
plt.xlabel('Marca')
plt.ylabel('Precio Promedio')
plt.title('Precio Promedio por Marca')
plt.show()

df['precioporstock'] = df['precio'] * df['stock']
plt.bar(df['nombre'], df['precioporstock'])
plt.xlabel('Nombre')
plt.ylabel('Precio segun stock')
plt.title('Precio del Stock segun producto')
plt.show()


marca_counts = df['marca'].value_counts()
plt.bar(marca_counts.index, marca_counts)
plt.xlabel('Marca')
plt.ylabel('Numero de Productos')
plt.title('Numero de Productos por Marca')
plt.xticks(rotation=90)
plt.show()
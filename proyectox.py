# -*- coding: utf-8 -*-
"""ProyectoX.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13_SjrPbZWilidkqCgoNLBxzoafZfqEka
"""

# Commented out IPython magic to ensure Python compatibility.
##LIBRERIAS Y IMPORTACION DE BASE DE DATOS

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as sp
import statsmodels as sm
import gspread
import math as mat
import os
# %matplotlib inline

import warnings
warnings.filterwarnings("ignore")
pd.set_option("display.max_columns", None)


ruta = "/content/Base_Datos.xlsx"

Base = pd.read_excel("Base_Datos.xlsx")
Base.head()

Base.info()

### LIMPIEZA DE DATOS

#QUITAR VALORES NA
Base.info()

"""Base = df.replace(0, pd.NA)"""

Base.replace(0, pd.NA)
Base.info()

## Definir las columnas

Base_columnas = ["VIN #","Condado","Ciudad","Estado","Codigo Postal","Modelo Año","Marca","Modelo","Tipo de vehiculo electrico","Elegibilidad para vehículos de combustible alternativo limpio (CAFV)","Rango Electrico","Precio Base Sugerido","Distrito Legislativo","ID","Ubicación del vehiculo","Utilidad Electrica","2020 Census Tract"]

Base_subniveles = ["Condado","Ciudad","Estado","Marca","Modelo","Tipo de vehiculo electrico","Elegibilidad para vehículos de combustible alternativo limpio (CAFV)","Rango Electrico","Precio Base Sugerido","Distrito Legislativo","Ubicación del vehiculo","Utilidad Electrica","2020 Census Tract"]

for col in Base_subniveles:
  print(f'Columna {col}: {Base[col].nunique()} datos diferentes')

Base.describe() ## MOSTRAR LAS COLUMNAS QUE TIENEN NUMEROS VALORICOS

Columnas_nro = ['Modelo Año','Rango Electrico', 'Precio Base Sugerido']


resumen_nro= Base[Columnas_nro].describe()


print(resumen_nro)

print(f'Tamaño de filas antes de eleminar las filas repetidas: {Base.shape}') ###ELEMINAR LAS FILAS REPETIDAS
Base.drop_duplicates(inplace=True)
print(f'despues{Base.shape}')

import pandas as pd


Base_columnas_1 = ["Estado","Modelo Año","Marca","Tipo de vehiculo electrico","Elegibilidad para vehículos de combustible alternativo limpio (CAFV)","Rango Electrico","Precio Base Sugerido"]

fig, ax = plt.subplots(nrows=len(Base_columnas_1), ncols=1, figsize=(25,150))
fig.subplots_adjust(hspace=0.5)


for i, col in enumerate(Base_columnas_1):
  sns.countplot(x=col, data=Base, ax=ax[i])
  ax[i].set_title(col)
  ax[i].set_xticklabels(ax[i].get_xticklabels(),rotation=90)

Modelo_barras = ["Modelo"]

fig, ax = plt.subplots(nrows=len(Modelo_barras), ncols=1, figsize=(50,40))
fig.subplots_adjust(hspace=0.5)


for i, col in enumerate(Modelo_barras):
  sns.countplot(x=col, data=Base, ax=ax)
  ax.set_title(col)
  ax.set_xticklabels(ax.get_xticklabels(),rotation=90)

Base_num = ["Rango Electrico"]

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(30,20))
fig.subplots_adjust(hspace=0.5)

for i, col in enumerate(Base_num):
  if col == 'Rango Electrico':
    nbins = 10
  else:
    nbins = 50
  sns.histplot(x=col, data=Base, ax=ax, bins=nbins, kde = True)
  ax.set_title(col)

Base_num = ["Utilidad Electrica"]

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(30,20))
fig.subplots_adjust(hspace=0.5)

for i, col in enumerate(Base_num):
  if col == 'Utilidad Electrica':
    nbins = 10
  else:
    nbins = 50
  sns.histplot(x=col, data=Base, ax=ax, bins=nbins, kde = True)
  ax.set_title(col)
  ax.set_xticklabels(ax.get_xticklabels(),rotation=90)

Utilidad_gra = ["Utilidad Electrica"]



Valores_Utilidad_gra = Base[Utilidad_gra].value_counts()

num_valores_ut = 10
Valores_Utilidad_lst = Valores_Utilidad_gra.head(num_valores_ut)
print("Valores mas comunes en la columna '{}':".format(Utilidad_gra))
print(Valores_Utilidad_gra)


print("Valores más recurrentes:")
print(Valores_Utilidad_gra)

plt.fill_between(Base['Marca'], Base['Rango Electrico'], Base['Rango Electrico'], color='skyblue', alpha=0.4)
plt.plot(Base['Marca'], Base['Rango Electrico'], color='Red', alpha=0.6, linewidth=2)
plt.xlabel('Marca')
plt.ylabel('Rango Electrico')
plt.title('Gráfico de Área Base de Datos')
ax.set_title(col)
ax.set_xticklabels(ax.get_xticklabels(),rotation=90)
plt.show()

# Obtener las ciudades y sus poblaciones
ciudades = Base['Ciudad']
marca = Base['Marca']

# Crear la gráfica de barras
plt.figure(figsize=(10,6))
plt.bar(ciudades, marca, color='skyblue')
plt.xlabel('Ciudad')
plt.ylabel('Marca')
plt.title('Población por Ciudad de carros')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

Base_subniveles = Base.sort_values(by='Marca', ascending=False)

# Tomar las 20 ciudades más pobladas
top_20_ciudades = Base_subniveles.head(20)

# Obtener las ciudades y sus poblaciones
ciudades = top_20_ciudades['Ciudad']
poblaciones = top_20_ciudades['Marca']

# Crear la gráfica de barras
plt.figure(figsize=(10,8))
plt.barh(ciudades, poblaciones, color='skyblue')
plt.xlabel('Marca')
plt.ylabel('Ciudad')
plt.title('Top 20 Ciudades Más Pobladas')
plt.gca().invert_yaxis()  # Invertir el eje y para mostrar la ciudad más poblada en la parte superior
plt.tight_layout()
plt.show()

Base_subniveles = ["Ciudad"]
Ciudad_re = Base_subniveles[:20]
Base_num = ["Ciudad"]

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(30,20))
fig.subplots_adjust(hspace=0.5)

for i, col in enumerate(Base_num):
  if col == 'Ciudad_re':
    nbins = 10
  else:
    nbins = 5
  sns.histplot(x=col, data=Base, ax=ax, bins=nbins, kde = True)
  ax.set_title(col)
  ax.set_xticklabels(ax.get_xticklabels(),rotation=90)

import pandas as pd
import matplotlib.pyplot as plt

# Load the data into a Pandas DataFrame
Base = pd.read_excel("Base_Datos.xlsx")
Base["Marca"] = pd.to_numeric(Base["Marca"], errors="coerce")

# Group the data by city and count the number of cars registered
city = Base.groupby("Ciudad")["Marca"].sum().sort_values(ascending=False)

# Extract the top 10 cities with the most cars registered
top10 = city.head(10)

# Create a bar chart
plt.figure(figsize=(10, 6))
top10.plot(kind="bar")

# Add labels and title
plt.xlabel("City")
plt.ylabel("Number of Cars Registered")
plt.title("Top 10 Cities with the Most Cars Registered")
print(city.shape)
print(top10.shape)


# Rotate x-axis labels for readability
plt.xticks(rotation=45)

# Show the plot
plt.show()

print(city.shape)
print(top10.shape)


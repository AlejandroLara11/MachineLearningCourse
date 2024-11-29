import pandas as pd
import numpy as np

df = pd.read_csv("dataset_1.csv", index_col=0)

# print(df)
# print(df.describe())
# print(df.info())

set_gen = set(df["Género"].tolist())
set_edu = set(df["Nivel_Educación"].tolist())
set_ciu = set(df["Ciudad"].tolist())

# print(set_gen)
# print(set_edu)
# print(set_ciu)

#Tratamiento de valores negativos (principiante)
df["Edad"] = df["Edad"].apply(lambda x : df["Edad"].mean() if x<0 else x)
df["Ingresos"] = df["Ingresos"].apply(lambda x : df["Ingresos"].mean()if x < 0 else x)
df["Altura"] = df["Altura"].apply(lambda x : df["Altura"].mean() if x < 1 else x)
df["Hijos"] = df["Hijos"].apply(lambda x : df["Hijos"].mean() if x < 0 else x)

print(df.describe())

#Imputar valores faltantes
for column in ["Edad", "Ingresos", "Hijos"]:
    median_value = df[column].median()
    df[column].fillna(median_value, inplace=True)
    
for column in ["Género", "Ciudad"]:
    mode_value = df[column].mode()[0]
    df[column].fillna(mode_value, inplace=True)

#Mapeo de datos
education_map = {
    "Bachelors" : "Bachelor",
    "mastre" : "Master",
    "pHd" : "PhD",
    "no education" : "None" 
}

df["Nivel_Educación"].replace(education_map, inplace= True)
df["Nivel_Educación"].fillna(df["Nivel_Educación"].mode(), inplace=True)

#Casteo de tipos
df["Edad"] = df["Edad"].astype(int)
df["Hijos"] = df["Hijos"].astype(int)
df["Ingresos"] = df["Ingresos"].astype(float)
df["Altura"] = df["Altura"].astype(float)

print(df)
print(df.describe())
print(df.info())
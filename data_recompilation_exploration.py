import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Titanic
df = pd.read_csv("train.csv")
#print(df)

#0 = Die,  1 = Live
print(df["Survived"].value_counts())
#Age is relevant to survive?
print(df.groupby("Survived")["Age"].mean())
#Sex is relevant?
print(df.groupby("Sex")["Survived"].mean())
#Class is relevant?
print(df.groupby("Pclass")["Survived"].mean())
#Port of Embarked is relevant?
print(df["Embarked"].value_counts())
#Survivors for Embarked
print(df.groupby("Embarked")["Survived"])
#Fare is relevant?
print(df.groupby("Survived")["Fare"].mean()) 
#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter


# ## Análise preliminar do dataset

# In[2]:


df = pd.read_csv("../Dados/covid_airport_clean.csv")
df.head(5)


# In[3]:


df.info()


# In[4]:


df.describe()


# In[40]:


sns.set(rc={'figure.figsize':(10,5)}) # aumentando os eixos
sns.lineplot(x="Date", y='PercentOfBaseline', data = df.loc[df.Country.isin(["Canada"])])


# ## Nas análises visuais, a série temporal contida no dataset não obedece nenhuma tendência clara, logo Regressão Linear não parece tão indicado como abordagem. Todavia, vamos ver se isso se concretiza na prática.

# ### Conjunto para análise

# In[38]:


pais = "Canada"
X = df.loc[df.Country == pais]
X.drop(X.columns[0],axis=1,inplace=True)
#X = X.select_dtypes(include=np.number)
X['Country'] = pd.get_dummies(X.Country)
X['AirportName'] = pd.get_dummies(X.AirportName)
X['ISO_3166_2'] = pd.get_dummies(X.ISO_3166_2)
X['State'] = pd.get_dummies(X.State)
X['City'] = pd.get_dummies(X.City)

X["Date"] = df[["Date"]]


# In[39]:


X = X.reset_index(drop=True)
X


# ## Percebe-se que não há variáveis numéricas linearmente independentes suficientes para a construção de um modelo. E as variáveis categóricas não podem ser usadas para o ajuste do modelo, logo não é possível fazer previsões a respeito do dataset utilizando regressões logísticas ou lineares simples.

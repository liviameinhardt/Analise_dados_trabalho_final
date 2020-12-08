#!/usr/bin/env python
# coding: utf-8

# In[72]:


# Bibliotecas de análise e visualização dos dados
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

# Bibliotecas para o modelo
from sklearn import linear_model
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix, precision_score, r2_score, mean_absolute_error, mean_squared_error


# ## Importando os dados para análise

# In[142]:


df1 = pd.read_csv("../Dados/fifa_players_clean.csv")
pd.set_option('display.max_columns', None)
# A coluna "ID" não interessa para a análise
df1.drop(df1.columns[0],axis=1,inplace=True)
# Transformando "Rigth" e "Left" em dummies
df1['Preferred_Foot'] = pd.get_dummies(df1.Preferred_Foot)
# Para o ajuste do modelo interessa apenas as features numéricas
df1 = df1.select_dtypes(include=np.number)
# Preenchendo os campos vazios com zeros
df1 = df1.fillna(0)
df1.head(5)


# In[143]:


df1.info()


# ### Análise preliminar dos dados tratados

# In[144]:


df1.describe()


# ## Vizualizando algumas relações lineares

# In[145]:


sns.lmplot(x='Overall', y= 'Wage', data = df1, hue ='Preferred_Foot', 
           palette='coolwarm', height=5)
plt.title('Relação Overall x Salário', size=18);

sns.lmplot(x='Value', y= 'Wage', data = df1, hue ='Preferred_Foot', 
           palette='coolwarm', height=5)
plt.title('Relação Valor x Salário', size=18);

sns.lmplot(x='Overall', y= 'Potential', data = df1, hue ='Preferred_Foot', 
           palette='coolwarm', height=5)
plt.title('Relação Overall x Potencial', size=18);

sns.lmplot(x='Overall', y= 'Wage', data = df1, hue ='International_Reputation', 
           palette='coolwarm', height=5)
plt.title('Relação Overall x Salário', size=18);


# # Regressão Linear
# 
# Utilizamos `Regressão Linear multivariada` pois queremos fazer previsões baseadas em várias features. Isso porque a `Regressão Logística` não é um modelo que atende de maneira precisa o suficiente o pretendido, dado que o conjunto de dados é contínuo e o objetivo não é classifica-los, mas sim prever um valor.

# ## Variável OVERALL

# ### Ajustando o modelo para análise preliminar

# In[146]:


reg = linear_model.LinearRegression()
feature = "Overall"
X = df1.drop(feature, axis = 1)
y = df1[f"{feature}"]
reg.fit(X, y);


# ### Analisando a importância das features

# In[148]:


plt.figure(figsize=(20,16))
sns.barplot(y=X.columns, x=reg.coef_);


# ## Modelo definitivo

# Baseado nisso montaremos outro modelo selecionando apenas as features mais relevantes para prever o Overall.

# ### Selecionando as features para o novo modelo

# In[149]:


X_imp = df1[["Age", "Potential", "Special", "Preferred_Foot", "International_Reputation", "Skill_Moves", "Reactions"]]
y = df1.Overall


# ## Separando em dados de treino e teste

# In[150]:


X_train, X_test, y_train, y_test = train_test_split(X_imp,y, test_size=0.4, random_state = 123)


# ## Ajustando o modelo

# In[151]:


reg_imp = linear_model.LinearRegression()
reg_imp.fit(X_train, y_train);


# ## Fazendo as previsões

# In[152]:


# Criando o conjunto de dados previstos
pred = reg_imp.predict(X_test)


# Utilizando uma entrada do próprio dataframe para mostrar uma previsão
entrada = 5245
print("Predito: ", round(reg_imp.predict([X_test.iloc[entrada]])[0], 0), "\nReal: ", df1.Overall[entrada])


# ## Analisando as métricas da regressão

# In[153]:


# Nota-se que os dados seguem uma clara correlação positiva entre os dados
plt.scatter(y_test, pred)
range = [y_test.min(), pred.max()]
plt.plot(range, range, 'red')
plt.xlabel('Overall real')
plt.ylabel('Overall predito')
plt.show()


# ## Sobre as métricas
# 
# - Coeficientes: São os pesos das features do modelo.
# - Intercept: O termo independente da regressão.
# - R_2: Quanto mais próximo de 0, menos o modelo é preciso sobre a variabilidade dos dados, e quanto mais próximo de 1 melhor explica a variação entre as variáveis.
# - Erro Médio Absoluto: É a soma das distâncias dos pontos à reta(erros) dividido pela quantidade de pontos.
# - Erro Quadrático Médio: É o quadrado da soma das distâncias dos pontos à reta(erros) dividido pela quantidade de pontos.

# In[154]:


print("Métricas\n",
"\n#####################"
"\nCoeficientes: ", reg_imp.coef_,
"\n\nIntercept: ", reg_imp.intercept_,
"\n\nR Quadrado: ", r2_score(y_test, pred),
"\n\nErro médio absoluto: ", mean_absolute_error(y_test, pred),
"\n\nErro quadrático médio: ", mean_squared_error(y_test, pred),
"\n#####################")


# ## Relação das habilidades com o OVERALL

# ### O processo é o mesmo de ajuste, criação do conjunto de teste e treino, previsão dos resultados e validação.

# In[155]:


X_hab = df1.iloc[:, 40:73]
y = df1.Overall


# In[156]:


X_hab_train, X_hab_test, y_hab_train, y_hab_test = train_test_split(X_hab,y, test_size=0.4, random_state = 123)


# In[157]:


reg_hab = linear_model.LinearRegression()
reg_hab.fit(X_hab_train, y_hab_train);


# In[158]:


# Criando o conjunto de dados previstos
pred_hab = reg_hab.predict(X_hab_test)


# Utilizando uma entrada do próprio dataframe para mostrar uma previsão
entrada = 5245
print("Predito: ", round(reg_hab.predict([X_hab.iloc[entrada]])[0], 0), "\nReal: ", df1.Overall[entrada])


# In[159]:


print("Métricas\n",
"\n#####################"
"\nCoeficientes: ", reg_hab.coef_,
"\n\nIntercept: ", reg_hab.intercept_,
"\n\nR Quadrado: ", r2_score(y_hab_test, pred_hab),
"\n\nErro médio absoluto: ", mean_absolute_error(y_hab_test, pred_hab),
"\n\nErro quadrático médio: ", mean_squared_error(y_hab_test, pred_hab),
"\n#####################")


# Concluimos que o modelo não se alterou para se obter a previsão do OVERALL, ainda que tenhamos pego partes separadas do dataset para fazer os conjuntos de teste e treino. E que as métricas apresentadas indicam que o modelo é preciso para o que se propõe, ou seja, a previsão do OVERALL dado um conjunto reduzido dos dados retorna valores coerentes e precisos.

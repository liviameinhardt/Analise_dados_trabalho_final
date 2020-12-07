import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("../Dados/fifa_players.csv")

#analise incial
# print(df.head())
# print(df.info())

# analise estatística 
# print(df.describe())

geral = list(df.columns)[2:21] +  list(df.columns)[-1:]
posicao = list(df.columns)[21:47]
habilidades = list(df.columns)[48:-1]

#mapa de calor da correlação (tudo)
# plt.rcParams['figure.figsize'] = (30, 20)
# sns.heatmap(df.corr(), annot = True)
# plt.show()

# #mapa de calor da correlação (características gerais)
# plt.rcParams['figure.figsize'] = (30, 20)
# sns.heatmap(df[geral].corr(), annot = True)
# #  wage - value / special - overall
# plt.show()

# #mapa de calor da correlação (posição)
# plt.rcParams['figure.figsize'] = (30, 20)
# sns.heatmap(df[posicao].corr(), annot = True)
# # LS:RM / LWB:RB 
# plt.show()

# #mapa de calor da correlação (habilidades)
# plt.rcParams['figure.figsize'] = (30, 20)
# sns.heatmap(df[habilidades].corr(), annot = True)
# # habilidades
# plt.show()

# ANALISE: SALÁRIO 
# df.groupby('Wage')[habilidades].mean()

#correlação com habilidades
# colunas_selecionadas = ['Value', 'Wage'] + habilidades
# plt.rcParams['figure.figsize'] = (30, 20)
# sns.heatmap(df[colunas_selecionadas].corr(), annot = True)
# plt.show()

# relação com potencial
# colunas_selecionadas = ["Potential","Overall"] 
# df.groupby('Wage')[colunas_selecionadas].mean().plot()

# POTENCIAL / HABILIDADES
# df.groupby('Potential')[habilidades].mean().plot()

#POTENCIAL/CAMISA
# plt.rcParams['figure.figsize'] = (10, 7)
# df2 = df[['Potential','Overall','Jersey_Number']].copy()
# df2.groupby("Potential").mean().plot(legend=True)

# POTENCIAL/OUTROS
# plt.rcParams['figure.figsize'] = (10, 7)

# IDADE
# df2 = df[['Potential','Age']].copy()
# df2.groupby("Potential").mean().plot(legend=True)

# REPUTAÇÃO/ SKILL
# df2 = df[['Potential','International_Reputation',"Skill_Moves"]].copy()
# df2.groupby("Potential").mean().plot(legend=True)


# OVERALL / HABILIDADES
# df.groupby('Overall')[habilidades].mean().plot()

# NACIONALIDADES
# nacao_habilidade = df.groupby("Nationality")[habilidades].mean()
# nacao_posicao = df.groupby("Nationality")[posicao].mean()
# nacao_descicao = df["Nationality"].value_counts().describe()
# nacao_distribuicao = df['Nationality'].value_counts().head(50).plot.bar()

# BODY TYPE
# df.groupby("Body_Type")[habilidades].mean()
# df.groupby("Body_Type")[posicao].mean()
# sns.barplot(data=df,y="International_Reputation",x="Body_Type")
# sns.barplot(data=df,y="Skill_Moves",x="Body_Type")


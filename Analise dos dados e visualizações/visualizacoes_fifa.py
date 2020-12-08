"""
Modulo para construção de visualizações do dataset FIFA 

Perguntas:
Qual é a reputação das maiores nações?
Como é a distribuição das habilidades por posição? 
Qual o número mais usado pelos os melhores jogadores de cada clube?
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("../Dados/fifa_players_clean.csv")



#Qual é a reputação das maiores nações?
sns.set(rc={'figure.figsize':(15,8)})
sns.set_theme(style="whitegrid")

# top 10 nações com maior potencial acumulado 
maiores_potenciais_por_nacao = df.groupby("Nationality")["Potential"].sum().sort_values(ascending=False)[:10]
nacoes_maior_potencial = list(maiores_potenciais_por_nacao.index)
maiores_potenciais_por_nacao = df.loc[df["Nationality"].isin(nacoes_maior_potencial)]

plot = sns.violinplot(x = 'Nationality', y = 'International_Reputation', data = maiores_potenciais_por_nacao,color="lightblue",
                      order=nacoes_maior_potencial)
plot.set_title("Reputação internacional dos países com maior potencial acumulado", fontsize = 20)

plot.set(xlabel='(Nações ordenadas por potencial acumulado)', ylabel='Reputação Internacional')

plt.show()
# figure = plot.get_figure()   
# figure.savefig("Visualizações/fifa/reputacao_paises.png")


#Qual é a reputação das maiores clubes? 
#(já que as nações não parecem ter relação)

sns.set(rc={'figure.figsize':(20,7)})
sns.set_theme(style="whitegrid")

# top 10 clubes com maior potencial acumulado 
maiores_potenciais_por_clube = df.groupby("Club")["Potential"].sum().sort_values(ascending=False)[:10]
clube_potenciais = list(maiores_potenciais_por_clube.index)
maiores_potenciais_por_clube = df.loc[df["Club"].isin(clube_potenciais)]

plot = sns.violinplot(x = 'Club', y = 'International_Reputation', data = maiores_potenciais_por_clube,color="lightblue",
                      order=clube_potenciais)
plot.set_title("Reputação internacional dos clubes com maior potencial acumulado", fontsize = 20)
plot.set(xlabel='(Clubes ordenados por potencial acumulado)', ylabel='Reputação Internacional')

plt.show()
# figure = plot.get_figure()   
# figure.savefig("Visualizações/fifa/reputacao_clubes.png")



#Como é a distribuição das habilidades por posição?
 
habilidades = list(df.columns)[48:-1]

# analise do melhor/ pior de posição
# Posições agrupadas: ataque, meio-campo e defesa
ataque = ["LS","ST","RS","LW","LF","CF","RF","RW"]
meio_campo = ["LAM","CAM","RAM","LM","LCM","CM","RCM","RM"]
defesa = ["LWB","LDM","CDM","RDM","RWB","LB","LCB","CB","RCB","RB"]

ataque = df.loc[df["Position"].isin(ataque)]
meio_campo = df.loc[df["Position"].isin(meio_campo)]
defesa = df.loc[df["Position"].isin(defesa)]

# Encontrar melhores/piores jogadores em cada categoria 
melhores_atacantes = ataque[ataque.Overall==ataque.Overall.max()].mean()
piores_atacantes = ataque[ataque.Overall==ataque.Overall.min()].mean()

melhores_meio_campo = meio_campo[meio_campo.Overall==meio_campo.Overall.max()].mean()
piores_meio_campo = meio_campo[meio_campo.Overall==meio_campo.Overall.min()].mean()

melhores_defesa = defesa[defesa.Overall==defesa.Overall.max()].mean()
piores_defesa = defesa[defesa.Overall==defesa.Overall.min()].mean()

# unir em um dataframe
melhor_pior = pd.concat([melhores_atacantes, piores_atacantes,melhores_meio_campo,piores_meio_campo,melhores_defesa,piores_defesa], axis=1)
melhor_pior.columns = ["melhores_atacantes", "piores_atacantes","melhores_meio_campo","piores_meio_campo","melhores_defesa","piores_defesa"]

# filtrar e salvar
melhor_pior = melhor_pior[melhor_pior.index.isin(habilidades)]
#melhor_pior.to_excel("Dados Tableau/melhor_pior.xlsx") 


# Qual o número mais usado pelos os melhores jogadores de cada clube?
clubes = []
melhores_camisas = []

for clube in df["Club"].unique():
    clubes.append(clube)
    clube = df.loc[df["Club"]==clube]
    numero = clube.loc[clube["Overall"].idxmax()]["Jersey_Number"]
    melhores_camisas.append(int(numero))

camisas_clube = {"clubes":clubes,"camisa":melhores_camisas}
camisas_clube = pd.DataFrame(data=camisas_clube)
# camisas_clube.to_excel("Dados Tableau/camisas_clube.xlsx")  
  
numero_camisa = list(camisas_clube["camisa"].value_counts().index)
contagem = list(camisas_clube["camisa"].value_counts())

camisa_contagem = {"camisa":numero_camisa,"contagem":contagem}
camisa_contagem = pd.DataFrame(data=camisa_contagem)
# camisa_contagem.to_excel("Dados Tableau/camisa_contagem.xlsx")  # gráfico no tableau
    








# Visualizações iniciais: entender os dados
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter

df = pd.read_csv("../Dados/covid_airport.csv")

# analise inicial   
# print(df.head())
# print(df.info())

#analise estatística dos dados 
# print(df.describe())

df["Date"] = pd.to_datetime(df["Date"]) # transformar coluna para tipo data
day = df["Date"].dt.day
month = df["Date"].dt.month
df['Day'] = day
df['Month'] = month

# data_pais_media = df.groupby(["Date","Country"]).mean() 

# data_estado_media = df.groupby(["Date","State"]).mean()

# pais_aeroporto_media = df.groupby(["Country","AirportName"]).mean()

# data_aeroporto_media = df.groupby(["Date","AirportName"]).mean()
# data_aeroporto_max = df.groupby(["Date","AirportName"]).max()
# data_aeroporto_min = df.groupby(["Date","AirportName"]).min()


# df.loc[df["Country"]=="Australia"]["AirportName"].unique() #apenas um
# df.loc[df["Country"]=="Chile"]["AirportName"].unique() #apenas um
# df.loc[df["Country"]=="United States"]["AirportName"].unique()
# df.loc[df["Country"]=="Canada"]["AirportName"].unique()



# VISUALIZANDO OS DADOS:
    
# PLOT INICIAL: AUSTRALIA 
# sns.set(rc={'figure.figsize':(10,5)}) # aumentando os eixos
# australia_plot = sns.lineplot(x="Date", y='PercentOfBaseline', data = df.loc[df.Country.isin(["Australia"])])

# COMPORTAMENTO DE CADA PAÍS
# sns.set(rc={'figure.figsize':(100,100)})
# sns.set_style("whitegrid")
# plot = sns.FacetGrid(data=df, col='Country', hue='Country', col_wrap=2, margin_titles=True, height=4, aspect=1)
# plot.map(sns.lineplot, "Date", 'PercentOfBaseline', ci=None)
# plot.set(xlabel='Meses',ylabel='Percentual da linha de base')
# xformatter = mdates.DateFormatter("%m")
# plot.axes[0].xaxis.set_major_formatter(xformatter)
# axes = plot.axes.flatten()
# axes[0].set_title("USA")
# axes[1].set_title("Canada")
# axes[2].set_title("Australia")
# axes[3].set_title("Chile")

# COMPORTAMENTO DE CADA PAÍS: MÉDIA POR MÊS
# sns.set(rc={'figure.figsize':(15,7)})
# sns.set_style("whitegrid")
# plt.title('Média do percentual da linha de base - por mês',size=20)
# grafico = sns.lineplot(x=month, y='PercentOfBaseline', hue = 'Country', data = df, ci=None,estimator="mean")
# grafico.set(xlabel='Meses',ylabel='Percentual da linha de base')
# figure = grafico.get_figure()   


# COMPORTAMENTO DE CADA PAÍS: MÉDIA POR DIA
# sns.lineplot(x=day, y='PercentOfBaseline', hue = 'Country', data = df, ci=None,estimator="mean")

# DISTRIBUIÇÃO DIÁRIA 
# sns.scatterplot(x="Date", y='PercentOfBaseline', hue = 'Country', data = df)

# DISTRIBUIÇÃO DIÁRIA: SEPARADO POR PAÍS
# sns.set(rc={'figure.figsize':(7,5)})
# plot = sns.FacetGrid(data=df, col='Country', hue='Country', col_wrap=2, height=4, aspect=1.5)
# plot.map(sns.scatterplot, 'Day', 'PercentOfBaseline')
# plt.show()

# AUSTRÁLIA X CHILE
# sns.barplot(palette = "crest", x=month, y='PercentOfBaseline', hue="Country", data= df.loc[df.Country.isin(["Chile","Australia"])])
# plt.show()

# USA x CANADA
# sns.barplot(palette = "crest", x=month, y='PercentOfBaseline', hue="Country", data= df.loc[df.Country.isin(["Canada","United States"])])

# AEROPORTOS CANDA
# sns.set(rc={'figure.figsize':(15,10)})
# sns.lineplot(x=month, y='PercentOfBaseline',hue="AirportName", data= df.loc[df.Country.isin(["Canada"])],ci=None)

# AEROPORTOS USA
# sns.lineplot(x=month, y='PercentOfBaseline',hue="AirportName", data= df.loc[df.Country.isin(["United States"])],ci=None)
# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# CONFERIR RELACAO AEROPORTO/DATA
# sns.set(rc={'figure.figsize':(15,10)})
# sns.scatterplot(y="AirportName", x='PercentOfBaseline',data= df.loc[df.Country.isin(["Canada"])])
# sns.scatterplot(y="AirportName", x='PercentOfBaseline',data= df.loc[df.Country.isin(["United States"])])

# COMPORTAMENTO POR AEROPORTO: SCATTERPLOT
# usa_canada =  df.loc[df.Country.isin(["United States","Canada"])]
# plot = sns.FacetGrid(data=usa_canada, col='AirportName', hue='Country', col_wrap=2, height=4, aspect=1.5)
# plot.map(sns.scatterplot, 'Day', 'PercentOfBaseline')
# plt.show()

# COMPORTAMENTO POR AEROPORTO: LINEPLOT
# usa_canada =  df.loc[df.Country.isin(["United States","Canada"])]
# plot = sns.FacetGrid(data=usa_canada, col='AirportName', hue='Country', col_wrap=2, height=4, aspect=1.5)
# plot.map(sns.lineplot, 'Day', 'PercentOfBaseline')
# plt.show()

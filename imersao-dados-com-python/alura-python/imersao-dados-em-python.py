#aula 1 - analises de dados com pandas
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com'
                 '/guilhermeonrails/data-jobs/refs/'
                 'heads/main/salaries.csv')
df.head()
df.info()
df.describe()
df.columns
df.shape()
linha, colunas = df.shape[0], df.shape[1]
print("Linhas: ",linha)
print("Colunas: ",colunas)
df.columns
display(df.columns)
df.columns= [
    'ano_de_trabalho','nivel_de_experiencia','tipo_de_emprego','cargo',
    'salario','moeada_salario','salario_em_usd',
    'residencia_do_funcionario','indice_remoto','localizacao_da_empresa',
    'tamanho_da_empresa'
]
display(df.columns)

RenomearColunas = {
    'ano_de_trabalho' : 'ano',
    'nivel_de_experiencia' : 'senioridade',
    'tipo_de_emprego' : 'contrato',
    'cargo' : 'cargo',
    'salario' : 'moeada',
    'moeada_salario' : 'salario',
    'salario_em_usd' : 'usd',
    'residencia_do_funcionario' : 'residencia',
    'indice_remoto' : 'remoto',
    'localizacao_da_empresa' : 'empresa',
    'tamanho_da_empresa' : 'tamanho_da_empresa'
}
df.rename(colums=RenomearColunas, inplace=True)
df.columns

# renomarColunas = {
#     'ano_de_trabalho': 'ano',
#     'nivel_de_experiencia': 'senioridade',
#     'tipo_emprego': 'contrato',
#     'cargo': 'cargo',
#     'salario': 'salario',
#     'moeda_salario': 'salario',
#     'salario_em_usd': 'usd',
#     'residencia_do_funcionario': 'residencia',
#     'indice_remoto': 'remoto',
#     'localizacao_da_empresa': 'empresa',
#     'tamanho_da_empresa': 'tamanho_da_empresa'
# }
# df.rename(columns=renomarColunas, inplace=True)
# df.columns

df['ano'].value_counts()
df['senioridade'].value_counts()
df['contrato'].value_counts()
df['cargo'].value_counts()
df['remoto'].value_counts()
df['tamanho_da_empresa'].value_counts()
df['empresa'].value_counts()
df['empresa'].value_counts()

traducao_senioridade = {
    'SE' : 'Senior',
    'MI' : 'Pleno',
    'EN' : 'Junior' ,
    'EX' : 'Executivo'
}
df['senioridade'] = df['senioridade'].replace(traducao_senioridade)
display(df['senioridade'].value_counts())

traducao_contrato = {
    'FT' : 'Tempo Integral',
    'CT' : 'Contrato',
    'PT': 'Tempo Parcial',
    'FL' : 'Freelancer'
}
df['contrato'] = df['contrato'].replace(traducao_contrato)
display(df['contrato'].value_counts())

traducao_tamanho_da_empresa = {
    'M' : 'Médio',
    'L' : 'Grande',
    'S' : 'Pequeno'
}
df['tamanho_da_empresa'] = df['tamanho_da_empresa'].replace(traducao_empresa)
display(df['tamanho_da_empresa'].value_counts())

traducao_remoto = {
    0 : 'Presencial' ,
    50 : 'Híbrido' ,
    100 : 'Remoto'
}
df['remoto'] = df['remoto'].replace()
display(df['remoto'].value_counts())

df.head()

df.describe(include='object')

##aula 2: preparacao e limpeza dos dados
df.insull()
df.head()
df.insull().sum()
df['ano'].unique()
df[df.isnull().any(axis=1)].head()

# import numpy as np
# df_salarios = pdf.DataFrame({
#     'nome' : ['Ana', 'bruno', 'Carlos', 'Daniele', 'Val'],
#     'moeda' : [4000, np.nan, 5000, nap.nan, 10000]
# })
# '''Calcula mediana e substitui os nulos pela mediana'''
# df_salarios['salario_media'] = df_salarios['moeda'].fillna(df_salarios['moeda'].media(2))
# display(df_salarios)

import numpy as np
df_salarios = pd.DataFrame({
    'nome' : ['Ana','Bruno','Carlos','Daniele','Val'],
    'moeda' : [4000, np.nan, 5000, np.nan , 10000]
})
#Calcular a media salarial e substitui os nulos pela media a arrendonda os valores
df_salarios['salario_media'] = df_salarios['moeda'].fillna(df_salarios['moeda'].mean().reound(2))
display(df_salarios)

df_temperatura = pd.DataFrame({
    "Dia" : ['Segunda','Terça','Quarta','Quinta','Sexta'],
    "Temperatura" : [30, np.nan, np.nan, 28, 27]
})
df_temperatura['Preenchido_ffill'] = df_temperatura['Temperatura'].fillna()
display(df_temperatura)

df_cidade = pd.DataFrame({
    'nome' : ["Ana","Bruno","Carlos","Daniele","Val"],
    'cidade' : ["São paulo", np.nan, "Curitiba", np.nan, "Belém"]
})
df_cidade['Cidade-preenchida'] = df_cidade["cidade"].fillna("Não informada")
display(df_cidade)
df_limpo = df.dropna()
df_limpo.isnull().sum()
df_limpo.head()
df_limpo.info()
df_limpo = df_limpo.assign(ano = df_limpo['ano'].astype('int64'))
##Aula 3 Grafico
df_limpo.head()
#Distribuição de senioridade
df_limpo['senioridade'].value_counts().plot(kind='bar', title='Distribuição de senioridade')

import seaborn as sn
sn.barplot(data=df_limpo, x='senioridade' , y='usd')

#Salario medio por senioridade
import matplotlib.pyplot as plt
plt.figure(figsize=(8,5))
sn.barplot(data=df_limpo, x='senioridade', y='usd')
plt.title("Salario medio por senioridade")
plt.xlabel("Senioridade")
plt.ylabel("Salario media anual (usd)")
plt.show()

ordem = df_limpo.groupby('senioridade')['usd'].mean().sort_values(ascending=True).index
print(ordem)

plt.figure(figsize=(8,5))
sn.barplot(data=df_limpo, x='senioridade', y='usd',order=ordem)
plt.title("Salario medio por senioridade")
plt.xlabel("Senioridade")
plt.ylabel("Salario media anual(USD)")
plt.show()

#Distribuição dos salario anual
plt.figure(figsize=(10,5))
sn.histplot(df_limpo['usd'], bins=50, kde=True)
plt.title("Distribuição dos salario anual")
plt.xlabel("Salario em (USD)")
plt.ylabel("Frequencia")
plt.show()

#Boxplot dos salarios
plt.figure(figsize=(8,5))
plt.title("boxplot dos salarios")
plt.xlabel("Salario em (USD)")
plt.show()

ordem_senioridade = ['Junior','Pleno','Senior','Executivo']

#Boxplot dos salarios  por senioridade
plt.figure(figsize=(8,5))
sn.boxplot(x='senioridade', y='usd',data=df_limpo, order=ordem_senioridade)
plt.title("Boxplot dos salarios por senioridade")
plt.xlabel("Senioridade")
plt.show()

#outro figura com o mesmo nome
ordem_senioridade = ['Junior','Pleno','Senior','Executivo']

plt.figure(figsize=(8,5))
sn.boxplot(x='senioridade', y='usd', order=ordem_senioridade, palette='Set2',heu='senioridade')
plt.title("Boxplot dos salarios por senioridade")
plt.xlabel("Senioridade")
plt.show()

import plotly.express as px
#prompt: crie um grafico de media por senioridade em barras usando o plotly
senioridade_media_salarial = df_limpo.groupby("senioridade")['usd'].mean().sort_values(ascending=False).reset_index()

fig = px.pie(senioridade_media_salarial,
             x = 'senioridade',
             y='usd',
             title='Média Salarial por senioridade',
             labels={'senioridade': 'Nível de senioridade', 'usd': 'Média Salarial anual'})
fig.show()

#figura de pizza
remoto_contagem = df_limpo['remoto'].value_counts().reset_index()
remoto_contagem.columns = ['tipo_trabalho','quantidade']

fig = px.pie(remoto_contagem,
             names='tipo_trabalha',
             values='quantidade',
             title='Proporção dos tipos de trabalho')
fig.show()

#figura de rosca
remoto_contagem = df_limpo['remoto'].value_counts().reset_index()
remoto_contagem.columns = ['tipo_emprego','quantidade']

fig = px.pie(remoto_contagem,
             names='tipo_emprego',
             values='quantidade',
             title='Proporção dos tipos de trabalho',
             hole=0.5)
fig.update_traces(textposition='inside', textinfo='percent+label')
fig.show()

df_limpo.head()

# %%capture
# !pip install pycontry
import pycontry as pc
def iso2_to_iso3(code):
    try:
        return pc.countries.get(alpha_2=code).alpha_3
    except:
        return None

df_limpo['residencia_iso3'] = df_limpo['residencia'].apply(iso2_to_iso3)

df_ds = df_limpo[df_limpo['cargo'] == 'Data Scientist']
media_ds_pais = df_ds.groupby('residencia_iso3')['usd'].mean().reset_index()

fig = px.chorpleth(media_ds_pais,
                   locations='residencia_iso3',
                   color='usd',
                   color_countinuos_scale='rdylgn',
                   title='Residencia médio de Cientista de Dados por país',
                   labels={'usd':'Salário médio(USD)', 'residencia_iso3':'País'})
fig.show()

#aula 4 contruindo um dashboard com streamlit pyscharm
# aprender a usar a biblioteca streamlit para a criação de um dashboard
# interativo simples, que permite visualizar dados filtrados e gerar gráficos de forma gráfica
# https://dashboard-salarios-dados.streamlit.app/
# 1 - criar o ambiente virtual:
# python3 -m venv.venv
# 2 - ativar o ambiante virtual:
# .venv\Scripts\Activate
# 3 - Ativar o ambiente virtual em MAC/LINUX:
# source .venv/bin/activate
# 4 - Criar arquivo chamado requeriments.txt e adicionar os pacotes necessários
# pandas==2.2.3
# streamlit==1.44.1
# plotly==5.24.1
# 5 - instalar as bibliotecas necessários
# %pip install -r requeriments.txt
# 6 - Criar a interface do Dashboard com streamlit
# 7 - Realizar o deploy do dashboard no streamlit cloud:https://streamlit.io/cloud
# %%capture
# !pip install streamlit
import streamlit as st
import pandas as pd
import plotly.expresso as px

st.set_page_config(
    page_title='Dashboard de Salarios na Area de Dados',
    pages_icon='📊',
    layout='wide'
)

df = pd.read_csv("https://raw.githubusercontent.com/"
                 "vqrca/dashboard_salarios_dados/refs/"
                 "heads/main/dados-imersao-final.csv")

st.sidebar.header('Filtro')
#Filtros do Anos
anos_disponiveis = sorted(df['ano'].unique())
anos_disponiveis = st.sidebar.multiselect("Ano", anos_disponiveis, default=anos_disponiveis)

#filtro de senioridade
senioridade_disponiveis = sorted(df['senioridade'].unique())
senioridade_disponiveis = st.sidebar.multiselect("Senioridade", senioridade_disponiveis,
                                                 default=senioridade_disponiveis)

#filtro por tipo de contrato
contrato_disponiveis = sorted(df['contrato'].unique())
contrato_disponiveis = st.sidebar.multiselect("contrato", contrato_disponiveis
                                              ,default=contrato_disponiveis)

#filtros por tamanho da empresa
tamanho_disponiveis = sorted(df['tamanho_da_empresa'].unique())
tamanho_disponiveis = st.sidebar.multiselect("Tamanho da Empresa", tamanho_disponiveis
                                             ,default=tamanho_disponiveis)

#---Filtragem do DataFrame ---
#O Dataframe principal é filtrado com base nas seleções feitas na barra lateral/
df_filtrado = df[
    (df['ano'].isin(anos_disponiveis)) &
    (df['senioridade'].isin(senioridade_disponiveis)) &
    (df['contrato'].isin(contrato_disponiveis)) &
    (df['tamanho_da_empresa'].isin(tamanho_disponiveis))
]

#--- Conteúdo Principal ---
st.title("🎲Dashboard de Análise de Salários na Área de Dados")
st.markdown("Explore os dados salariais na área de dados nos últimos anos."
            "Utilize os filtros á esquerda para refinar sua ánalise")

#--- Métrica Principais (KPIs) ---
st.subheader("Métricas gerais(Salários anual USD)")

if not df_filtrado.empty:
    salario_medio = df_filtrado['usd'].mean()
    salario_maximo = df_filtrado['usd'].max()
    total_registros = df_filtrado.shape[0]
else:
    salario_media,
    salario_mediano,
    salario_maximo,
    total_registros,
    cargo_mais_frequente = 0,0,0,""

col1 ,col2 ,col3 ,col4 = st.columns(4)
col1.metric("Salário Medio ", f"${salario_medio:,.0f}")
col2.metric("Salario Maximo ", f"{salario_maximo:,.0f}")
col3.metric("Total de registros ", total_registros)
col4.metric("Cargo mais frequente ", cargo_mais_frequente)

st.markdown("---")

#--- Análise Visuais com Plotly ---
st.subheader("Gráficos")

col_graf1, col_graf2 = st.columns()

with col_graf1:
    if not df_filtrado.empty:
        top_cargos = df_filtrado.groupby('cargo')['usd'].mean(
        ).nlargest(10).sort_values(ascending=True).reset_index()
        grafico_cargos = px.bar(
            top_cargos,
            x='usd',
            y='cargo',
            orientation='h',
            title='Top 10 Cargos por salario medio',
            labels={'usd' : 'Media salarial anula(USD)', 'Cargo' : ''}
        )
        grafico_cargos.update_layout(title=0.1, yaxis={'categoryoder':'total ascending'})
        st.plotly_chart(grafico_cargos, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico de cargos.")

with col_graf2:
    if not df_filtrado.empty:
        grafico_historia = px.histogram(
            df_filtrado,
            x = 'usd',
            nbins = 30,
            title = 'Distribuição de salarios anuais',
            labels = {'usd' : 'Faixa salarial', 'Cargo' : ''}
        )
        grafico_historia.update_layout(title_x=0.1)
        st.protly_chart(grafico_historia, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico de dsitribuição.")

col_graf3, col_graf4 = st.columns(2)

with col_graf3:
    if not df_filtrado.empty:
        remoto_contagem = df_filtrado['remoto'].value_counts().reset_index()
        remoto_contagem.columns = ['tipo_de_emprego','quantidade']
        grafico_remoto = px.pie(
            remoto_contagem,
            names='tipo_de_emprego',
            values='quantidade',
            title='Proporção dos tipos de trabalho',
            hole=0.5
        )
        grafico_remoto.update_traces(textinfo="percent + label")
        grafico_remoto.update_layout(title_x=0.1)
        st.plotly_chart(grafico_remoto, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico dos tipos de tarabalho")

with col_graf4:
    if not df_filtrado.empty:
        df_ds = df_filtrado[df_filtrado['cargo'] == 'Data Scientist']
        media_ds_pais = df_ds.groupby('residencia_iso3')['usd'].mean().reset_index()
        grafico_paises = px.choropleth(
            media_ds_pais,
            locations = 'residencia_iso3',
            color = 'usd',
            color_continous_scale = 'rdylgn',
            title = 'Salario médio de Cientista de Dados por pais',
            labels = {'usd' : 'Salario medio(USD)', 'residencia_iso3' : 'País'}
        )
        grafico_paises.update_layout(title_x = 0.1) 
        st.plotly_chart(grafico_paises, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico de países")

st.subheader("Dados Detalhados")
st.dataframe(df_filtrado)

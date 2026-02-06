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
import numpy as np

df_salarios = pdf.DataFrame({
    'nome' : ['Ana', 'bruno', 'Carlos', 'Daniele', 'Val'],
    'moeda' : [4000, np.nan, 5000, nap.nan, 10000]
})
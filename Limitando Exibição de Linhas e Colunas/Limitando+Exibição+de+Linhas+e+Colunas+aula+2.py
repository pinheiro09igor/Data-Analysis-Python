import pandas as pd

#Abrindo o arquivo do Excel
arquivo = pd.read_excel("Vendas_Jan.xlsx")
print(arquivo)
print("\n")


print("\nIndex exibe apenas informações sobre as linhas do DataFrame\n")
print(arquivo.index)
print("\n")

print("\ncolumns exibe o nome de todas as colunas do DataFrame\n")
print(arquivo.columns)
print("\n")

print("\nhead exibe apenas as 5 primeiras linhas por padrão\n")
print(arquivo.head())
print("\n")

print("\nhead exibe apenas as 10 primeiras linhas\n")
print(arquivo.head(10))
print("\n")

print("\ntail exibe apenas as últimas linhas\n")
print(arquivo.tail(3))
print("\n")

print("\nImprimindo somente a coluna de vendedor\n")
print(arquivo["Vendedor"])
print("\n")

print("\nImprimindo mais de uma coluna\n")
print(arquivo[["Vendedor", "Total Vendas"]])
print("\n")

print("\nImprimindo somente linhas de 1 ao 5\n")
print(arquivo.loc[1:5])
print("\n")

#loc = localizar
#Filtro vendas Leonardo Almeida
vendas_LeonardoAlmeida_DF = arquivo.loc[arquivo["Vendedor"] == "Leonardo Almeida"]

print("\nImprimindo somente vendas do Leonardo Almeida\n")
print(vendas_LeonardoAlmeida_DF)
print("\n")


#Filtrando vendas e colunas
vendas_Leonardo_A = arquivo.loc[arquivo["Vendedor"] == "Leonardo Almeida", ["Vendedor", "Total Vendas"]]

print("\nImprimindo somente vendas e duas colunas do Leonardo Almeida\n")
print(vendas_Leonardo_A)
print("\n")

print("\nVendedor do Indice 5\n")
print(arquivo.loc[5, "Vendedor"])
print("\n")

print("\nMétodo Shape mostra quantas linhas e colunas tem o DataFrame\n")
print(arquivo.shape)
print("\n")

#T = Transforma linhas em colunas e colunas em linhas
transformarLinhasEmColunas = arquivo.T

print("\nT = Transforma linhas em colunas e colunas em linhas\n")
print(transformarLinhasEmColunas)
print("\n")





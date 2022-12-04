import pandas as pd

#Abrimos o arquivo
vendasDF = pd.read_excel("Vendas_Merge.xlsx")
print("\n DataFrame Vendas \n")
print(vendasDF)
print("\n")

#Abrimos o arquivo
vendedoresDF = pd.read_excel("Vendedores_Merge.xlsx")
print("\n DataFrame Vendedores \n")
print(vendedoresDF)
print("\n")

#Abrimos o arquivo
produtosDF = pd.read_excel("Produtos_Merge.xlsx")
print("\n DataFrame Produtos \n")
print(produtosDF)
print("\n")

#---------------------------------------------

#merge - trás informações de outros DF para nosso DF através de um indentificador
vendasDF = vendasDF.merge(vendedoresDF)


print("\n merge Vendas x Vendedores \n")
print(vendasDF)
print("\n")

#---------------------------------------------

#merge - trás informações de outros DF para nosso DF através de um indentificador
vendasDF = vendasDF.merge(produtosDF)


print("\n merge Vendas x Produtos \n")
print(vendasDF)
print("\n")

#---------------------------------------------

print(vendasDF.columns)
print("\n")

#---------------------------------------------

resumoDataFrame = vendasDF[["Vendedor", "Produto", "Total Vendas"]]

print("\n Resumo DataFrame Merge \n")
print(resumoDataFrame)
print("\n")

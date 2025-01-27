import pandas as pd

data = {
    'nome': ['joao', 'maria', 'Pedro'],
    'idade': [25, 30, 28],
    'email': ['joao@gmail.com','maria@hotmail.com', 'pedro@yahoo.com'] 
}

df = pd.DataFrame(data)
print("DataFrame cirado: \n", df)

#ler dados de um arquivo csv
df_csv = pd.read_csv('clientes.csv')
print("\nDataFrame lido do CSV:\n", df_csv.head())

#Selecionar a coluna cidade
cidade = df['cidade']
print("\nColuna cidade:\n", cidade)

#Fltrar clientes com idade maior que 30
clientes_maiores_30 = df[df['idade'] > 30]
print("\nClientes maiores de 30:\n", clientes_maiores_30)
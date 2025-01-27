import matplotlib.pyplot as plt

# Dados para os gráficos
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun']
vendas = [1500, 2300, 1800, 2700, 3000, 2000]

# Gráfico de Linha
plt.figure(figsize=(10, 5))
plt.plot(meses, vendas, marker='o', linestyle='-', color='b', linewidth=2, label='Vendas')
plt.title('Vendas Mensais')
plt.xlabel('Meses')
plt.ylabel('Vendas (R$)')
plt.grid(True)
plt.legend()
plt.show()

# Gráfico de Barras
plt.figure(figsize=(10, 5))
plt.bar(meses, vendas, color='skyblue')
plt.title('Vendas Mensais')
plt.xlabel('Meses')
plt.ylabel('Vendas (R$)')
plt.grid(axis='y')
plt.show()

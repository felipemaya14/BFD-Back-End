#1. Dicionário de estoque:
estoque_loja = {
    "monitor": 15,
    "teclado": 25,
    "mouse": 30
}
#2. Dicionário de preços:

precos = {
    "monitor": 850.50,
    "teclado": 120.00,
    "mouse": 85.00
}

#3. Entrada de produto e quantidade:

produto = input("Digite o produto que deseja comprar: ").lower() # Entrada do protudo que o cliente deseja comprar já em minusculo.

if produto in estoque_loja:
    print(f"Quantidade disponível: {estoque_loja[produto]}") # Verifica se o produto existe no estoque.
else:
    print("Produto indisponível.") # Caso o produto nao exista no estoque.
quantidade = int(input("Quantidade desejada: ")) # Entrada da quantidade que o cliente deseja comprar.

if quantidade <= estoque_loja[produto]:
    estoque_loja[produto] -= quantidade # Atualiza o estoque subtraindo a quantidade vendida.
    preco = precos[produto] * quantidade # Calcula o valor total da venda.
    print(f"Compra realizada: {quantidade} unidades de {produto}. Total: R${preco:.2f}")
else:
    print("Quantidade indisponível.") # Caso a quantidade solicitada seja maior que a quantidade em estoque.
    
#4. Calculo do imposto:
def calcular_imposto(preco):
    imposto = preco * 0.15 # Calcula o imposto de 15% sobre o preco.
    return imposto

preco = precos[produto] * quantidade # Calcula o preco total da venda.
imposto = calcular_imposto(preco)
print(f"Valor do imposto: RS: {imposto:.2f}")

#5. Calculo do lucro:

for produto, quantidade in estoque_loja.items(): # Exibe o nome e o estoque de cada produto.
    print(f"Estoque atual de {produto.upper()}: {quantidade} unidades.")

lucro_total = preco - imposto # Calcula o lucro total.
print(f"Lucro total: R${lucro_total:.2f}")
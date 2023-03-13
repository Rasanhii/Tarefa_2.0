capital_inicial = float(input("Digite o valor inicial da poupança: "))

# Define a taxa de juros aplicada
taxa_juros = 0.005

# Define o número de períodos (meses) em que o dinheiro ficará investido
num_periodos = 12

# Calcula e imprime o montante mês a mês durante um período de 12 meses
for mes in range(1, num_periodos+1):
    montante = capital_inicial * (1 + taxa_juros)**mes
    print(f"Montante no mês {mes}: R${montante:.2f}")

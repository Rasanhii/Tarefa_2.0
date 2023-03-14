capi_ini = float(input("Digite o valor inicial da poupança: "))

juros = 0.005

num_periodos = 12

for mes in range(1, num_periodos+1):
    montante = capi_ini * (1 + juros)**mes
    print(f"Montante no mês {mes}: R${montante:.2f}")

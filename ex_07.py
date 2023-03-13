num = int(input("Digite um número inteiro positivo: "))

# Inicializa o fatorial com 1
fatorial = 1

# Calcula o fatorial do número
for i in range(1, num+1):
    fatorial *= i

# Exibe o resultado do fatorial
print(f"O fatorial de {num} é {fatorial}")
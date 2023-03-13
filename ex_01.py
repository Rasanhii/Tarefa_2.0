va = int(input('Digite um valor entre 1 a 10: '))
while True:
    if va < 1 or va > 10 :
        print('Digite um valor entre 1 a 10.')

    i = 1
    for i in range(1, 11):
        resp = va * i
        print(f'{va} x {i} = {resp}')
    
    sn = input('Deseja fazer outra consulta? (s/n) \n Resp: ')
    if sn.lower() == 'n':
        break

print('Obrigado por usar o programa.')
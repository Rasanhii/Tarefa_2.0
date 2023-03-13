#numero secreto uhum.
import random
shiu = random.randint(1, 100)

#se caso errar.
kkkk = False

while not kkkk:
    chute = int(input('Digite um número entre 1 e 100: '))
    if chute == shiu:
        print('Parabéns, você acertou! (sortudo :D)')
        kkkk = True
    elif chute < shiu:
        print('ERROU. O número secreto é maior. Não desista.')
    else:
        print('O número secreto é menor. Tente novamente.')
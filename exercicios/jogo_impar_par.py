print('impar ou par')
time = str(input('escolha entre impar ou par: '))
num = int(input('escolha um numero para jogar: '))
import random 
num2 = random.randint(1, 10)
print("a maquina escolheu {}".format(num2))
soma = num + num2

if soma % 2 == 0 and time == 'par':
    print('par ganhou')
else:
    print('impar ')

if soma % 2 == 1 and time == 'impar':
    print('impar ganhou')


print('verificador de triangulo retangulo')
caa = int(input('digite o cateto adjacente: '))
cao = int(input('digite cateto oposto: '))
hipo = int(input('digite o valor da hipotenusa: '))

caa2 = caa * caa 
cao2 = cao * cao 
hipo2 = hipo * hipo

scate = cao2 + caa2

if hipo < cao and hipo < caa:
    print('voce digitou valores invalidos')

elif hipo2 != scate:
    print('o triangulo não é retangul')

else:
    print('é um triangulo retangulo {} = {} + {}'.format(hipo2, cao2, caa2))

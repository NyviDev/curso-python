age = 26 #Idade aleatória
if age < 2:
    print('Você é um bebê.')
elif age >= 2 and age < 4:
    print('Você é uma criança.')
elif age >= 4 and age < 13:
    print('Você é um(a) garoto(a).')
elif age >= 13 and age < 20:
    print('Você é um(a) adolescente.')
elif age >= 20 and age < 65:
    print('Você é um adulto.')
else:
    print('Você é um idoso.')
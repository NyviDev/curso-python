responses = {}
active = True

while active:
    name = input('\nQual é o seu nome? ')
    response = input('Qual comida você mais gosta em festa junina? ')
    responses [name] = response
    repeat = input('Você gostaria de deixar outra pessoa responder? (sim/nao) ')
    if repeat == 'nao':
        active = False

print('\n --- Resultado da enquete ---')
for name, response in responses.items():
    print(f'{name} gosta de comer {response} em festa junina.')
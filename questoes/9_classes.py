from random import randint

class Dado():
    def __init__(self):
        self.lados = 0
        self.y = 0
        self.vezes = 0
    
    def rolar_dado(self):
        while self.y <= self.vezes:
            x = randint(1, self.lados)
            print(x)
            self.y += 1

    def reset_y(self):
        self.y = 0
    
    def mudar_dado(self):
        self.lados = int(input('Digite quantos lados o dado terá: '))
        self.vezes = int(input('Digite quantas vezes o dado rolará: '))
        self.vezes -= 1

dice = Dado()
active = True
print("Digite 0 caso queira fechar o programa!!")
while active: 
    dice.mudar_dado()
    if dice.lados < 1 or dice.vezes < 1:
        break
    dice.rolar_dado()
    dice.reset_y()
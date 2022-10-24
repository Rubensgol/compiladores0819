from pickle import TRUE
from lexico import Lexico
from actionslr import action
from goto import dic

class AnalisaDor:
    pilha = [0,'$']
    lexico = Lexico
    def __init__(self, lexico):
        self.lexico = lexico

    def analisa(self):
        acaba = False
        token = self.lexico.nextToken()[0]

        while (not acaba):
            if action[self.pilha[0]][token][0] == 'shift':
                self.pilha.insert(0, action[self.pilha[0]][token][1])
                token = self.lexico.nextToken()[0] 
            elif action[self.pilha[0]][token][0] == 'reduce':
                reduceComp = action[self.pilha[0]][token][2]
                reduce = action[self.pilha[0]][token][1]
                for i in range(0,reduce):
                    self.pilha.pop(0)
                estado = dic[self.pilha[0]][reduceComp]
                self.pilha.insert(0, estado)
            elif action[self.pilha[0]][token][0] == 'STOP':
                print("linguagem valida")
                acaba = True

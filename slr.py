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
        token = self.lexico.nextToken()[0]  # type: ignore

        while (not acaba):
            if action[self.pilha[0]][token][0] == 'shift':
                self.pilha.insert(0, action[self.pilha[0]][token][1])
                token = self.lexico.nextToken()[0]  # type: ignore
            elif action[self.pilha[0]][token][0] == 'reduce':
                reduce = sorted(dic[self.pilha[0]], reverse=True)
                estado = action[self.pilha[0]][token][1]
                for i in reduce:
                    if i == self.pilha.pop(0):
                        continue
                    else:
                        break
                self.pilha.insert(0, estado)
            elif action[self.pilha[0]][token][0] == 'STOP':
                print("linguagem valida")
                acaba = True

from asyncio.windows_events import NULL
from cmath import pi
from lexico import Lexico
from tabelaTransicaoAnalisador import tabelaTransicaoDic

class AnalisaDor:
    pilha = ['<FUNCAO>','$']
    lexico = Lexico
    def __init__(self, lexico):
        self.lexico = lexico


    def analisa(self):
        acaba = False
        token = self.lexico.nextToken()[0]
        while not acaba:
            try:
                if token == '&' and self.pilha[0] == '$':
                    acaba = True
                    print("aceitou")
                else:
                    if self.pilha[0] == token  and not token == '&':
                        self.pilha.pop(0)
                        token = self.lexico.nextToken()[0]
                    else:
                        if not token == self.pilha[0] and self.pilha[0].startswith('<'):
                            regra = tabelaTransicaoDic[self.pilha[0]][token]
                            self.pilha.pop(0)
                            self.pilha = regra + self.pilha
                        else:
                            raise KeyError
            except KeyError:
                print("erro sintatico")
                return False
        if (self.pilha):
            return False
        else:
            return True
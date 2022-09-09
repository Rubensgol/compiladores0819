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
            if token == '&' and self.pilha[0] == '$':
                acaba = True
                print("aceitou")
            else:
                if self.pilha[0] == token  and not token == '&':
                    self.pilha.pop(0)
                    token = self.lexico.nextToken()[0]
                else:
                    if not token == self.pilha[0] and self.pilha[0].startswith('<'):
                        try:
                            regra = tabelaTransicaoDic[self.pilha[0]][token]
                        except KeyError:
                            regra = tabelaTransicaoDic[self.pilha[0]]['']
                        self.pilha.pop(0)
                        self.pilha = regra + self.pilha
                    else:
                        print('terminal não esperado')
                        acaba = True
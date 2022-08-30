class AnalisaDor:
    listaToken = []
    anterior = 0
    cont = 0
    def __init__(self, listaT):
        self.listaToken = listaT

    def term(self, token):
        ret = self.listaToken[self.cont][0] == token
        self.cont = self.cont + 1
        return ret

    def FUNCAO(self):
        return self.term('funcao') and self.term('variavel') and self.term('AP') and self.PARAN() and self.term('FP') and self.term('AC') and self.ESCOPO() and self.term('FC')

    def PARAN(self):
        return self.TIPO() and self.term('variavel') and self.PARANS()

    def PARANS(self):
        return self.term('VIRGULA') and self.PARAN()

    def ESCOPO1(self):
        return self.IF
    
    def ESCOPO2(self):
        return self.PRINT

    def ESCOPO3(self):
        return self.ATRIB

    def IF(self):
        return self.term('if') and self.term('AP') and self.COND and self.term('FP') and self.term('AC') and self.ESCOPO() and self.term('FC')

    def COND(self):
        return self.VAR and self.SCOND and self.VAR

    def ATRIB(self):
        return self.VAR and self.term('igual') and self.VAR and self.term('PV')

    def SCOND(self):
        anterior = cont
        if self.SCOND1():
            return True
        else:
            cont = anterior
            return self.SCOND2()

    def SCOND1(self):
        self.term('maior')
    
    def SCOND2(self):
        self.term('menor')

    def PRINT(self):
        return self.term('print') and self.term('AP') and self.VAR and self.term('FP') and self.term('PV')

    def VAR(self):
        anterior = cont
        if self.VAR1():
            return True
        else:
            cont = anterior
            return self.VAR2()

    def VAR1(self):
        self.term('variavel')

    def VAR2(self):
        self.term('cont')
    
    def TIPO(self):
        self.term('int')

    def ESCOPO(self):
        anterior = cont
        if self.ESCOPO1():
            return True
        else:
            cont = anterior
            if self.ESCOPO2():
                return True
            else:
                cont = anterior
                return self.ESCOPO3()
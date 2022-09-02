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
        print("#<BLOCO> ::= FUNCAO VARIAVEL AP FP AC <ESCOPO> FC")
        return self.term('funcao') and self.term('variavel') and self.term('AP') and self.PARAN() and self.term('FP') and self.term('AC') and self.LISTESCOPO() and self.term('FC')

    def PARAN(self):
        print("#<BLOCO> ::= <TIPO> <VAR> <PARANS>")
        self.anterior = self.cont
        if self.TIPO() and self.term('variavel') and self.PARANS():
            return True

    def PARANS(self):
        print("#<BLOCO> ::= VIRGUILA <PARAN> ;; î")
        self.anterior = self.cont
        if self.term('VIRGULA') and self.PARAN():
            return True
        else:
            self.cont = self.anterior
            return self.VAZIO()

    def ESCOPO1(self):
        print("#<BLOCO> ::= <IF>")
        return self.IF()
    
    def ESCOPO2(self):
        print("#<BLOCO> ::= <PRINT>")
        return self.PRINT()

    def ESCOPO3(self):
        print("#<BLOCO> ::= <ATRIBUICAO>")
        return self.ATRIB()

    def IF(self):
        print("#<BLOCO> ::= if ap <COND> fp ac <ESCOPO> fc")
        return self.term('if') and self.term('AP') and self.COND() and self.term('FP') and self.term('AC') and self.LISTESCOPO() and self.term('FC')

    def COND(self):
        print("#<BLOCO> ::= <VAR> <SCOND> <VAR>")
        return self.VAR() and self.SCOND() and self.VAR()

    def ATRIB(self):
        print("#<BLOCO> ::= <VAR> igual <VAR> pv")
        return self.VAR() and self.term('igual') and self.VAR() and self.term('PV')

    def SCOND(self):
        print("#<BLOCO> ::= <SCOND1> ;; <SCOND2>")
        self.anterior = self.cont
        if self.SCOND1():
            return True
        else:
            self.cont = self.anterior
            return self.SCOND2()

    def SCOND1(self):
        print("#<BLOCO> ::= MAIOR")
        return self.term('maior')
    
    def SCOND2(self):
        print("#<BLOCO> ::= MENOR")
        return self.term('menor')

    def PRINT(self):
        print("#<BLOCO> ::= PRINT ap <VAR> fp pv")
        return self.term('PRINT') and self.term('AP') and self.VAR() and self.term('FP') and self.term('PV')

    def VAR(self):
        print("#<BLOCO> ::= <VARAIVAEL> ;; <CONSATNTE")
        self.anterior = self.cont
        if self.VAR1():
            return True
        else:
            self.cont = self.anterior
            return self.VAR2()

    def VAR1(self):
        print("#<BLOCO> ::= VARiavel")
        return self.term('variavel')

    def VAR2(self):
        print("#<BLOCO> ::= constante")
        return self.term('cont')
    
    def TIPO(self):
        print("#<BLOCO> ::= tipo")
        return self.term('int')

    def ESCOPO(self):
        print("#<BLOCO> ::=  <IF> | <PRINT> | <ATRIB>")
        self.anterior = self.cont
        if self.ESCOPO1():
            return True
        else:
            self.cont = self.anterior
            if self.ESCOPO2():
                return True
            else:
                self.cont = self.anterior
                return self.ESCOPO3()
    
    def LISTESCOPO(self):
        print("#<BLOCO> ::=  <ESCOPO> <LISTAESCOPO> | î")
        self.anterior = self.cont
        if self.ESCOPO() and self.LISTESCOPO():
            return True
        else:
            self.cont = self.anterior
            return self.VAZIO()

    def VAZIO(self):
        return True
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

    def E1(self):
        return self.T()

    def E2(self):
        return self.T() and self.term('MAIS') and self.E()

    def E(self):
        self.anterior = self.cont
        if self.E1():
            return True
        else:
            self.cont = self.anterior
            return self.E2()

    def T1(self):
        return self.term('INT')

    def T2(self):
        return self.term('INT') and self.term('MULT') and self.T()

    def T3(self):
        return self.term('AP') and self.E() and self.term('FP')

    def T(self):
        self.anterior = self.cont
        if self.T1():
            print("t1")
            return True
        else:
            self.cont = self.anterior
            if self.T2():
                print("t2")
                return True
            else:
                self.cont = self.anterior
                print("t3")
                return self.T3()
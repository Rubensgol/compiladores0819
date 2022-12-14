from tabelaTransicao import tabelaTransicaoDic
from estadosFinais import estadoFinal

class Lexico:
    posAtual = 0
    listaToken = []

    def __init__(self):
        self.posAtual = 0

    def nextToken(self):
        token = self.listaToken[self.posAtual]
        self.posAtual = self.posAtual + 1
        return token

    def palavra(self, linha, nLinha, estado):
        token = []
        lexema = ""
        posicao = 0
        for letra in linha:
            if letra.strip():
                try:
                    estado = tabelaTransicaoDic[estado][letra.lower()]
                    lexema = lexema + letra
                    posicao = posicao + 1
                except KeyError:
                    try:
                        print("token:", estadoFinal[estado], " lexema:", lexema, " na linha:", nLinha, "POSIcao inicial:", posicao-len(lexema), "posicao final: ", posicao - 1 )
                        token.append([estadoFinal[estado], lexema, posicao-len(lexema), posicao - 1])
                        estado = 0
                        lexema = letra
                        estado = tabelaTransicaoDic[estado][letra.lower()]
                    except KeyError:
                        token.append([0,lexema, posicao-len(lexema), posicao - 1])
                        print("transicao nao conhecida lexema: ", lexema , "Posicao inicial:", posicao-len(lexema) , "posicao final: ", posicao - 1)
            else:
                try:
                    print("token: ", estadoFinal[estado], "lexema: ", lexema, "na linha ", nLinha , "POSIcao inicial:", posicao-len(lexema), "posicao final: ", posicao - 1)
                    token.append([estadoFinal[estado], lexema, posicao-len(lexema), posicao - 1])
                    estado = 0
                    lexema = ""
                except KeyError:
                    continue
        print("token: ", estadoFinal[estado], "lexema: ", lexema, "na linha ", nLinha, "POSIcao inicial:", posicao-len(lexema), "posicao final: ", posicao - 1) 
        token.append([estadoFinal[estado], lexema, posicao-len(lexema), posicao - 1])
        return token

    def lerTokens(self):
        estado = 0
        lines = []
        tokens = []
        while True:
            line = input()
            if line:
                lines.append(line)
            else:
                break

        nlinha = 0
        
        for linha in lines:
            nlinha = nlinha + 1
            try:
                tokens.extend(self.palavra(linha.strip(), nlinha, estado))
                estado = 0
            except KeyError:
                continue
        tokens.append('&')
        self.listaToken = tokens
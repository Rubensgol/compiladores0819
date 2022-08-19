from tabelaTransicao import tabelaTransicaoDic
from estadosFinais import estadoFinal

def palavra(linha, nLinha, estado):
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
                    print("token:", estadoFinal[estado], " lexema:", lexema, " na linha:", nlinha, "POSIcao inicial:", posicao-len(lexema), "posicao final: ", posicao - 1 )
                    estado = 0
                    lexema = letra
                    estado = tabelaTransicaoDic[estado][letra.lower()]
                except KeyError:
                    print("transicao nao conhecida lexema: ", lexema , "POSIcao inicial:", posicao-len(lexema) , "posicao final: ", posicao - 1)
        else:
            try:
                print("token: ", estadoFinal[estado], "lexema: ", lexema, "na linha ", nlinha , "POSIcao inicial:", posicao-len(lexema), "posicao final: ", posicao - 1)
                estado = 0
                lexema = ""
            except KeyError:
                continue
    print("token: ", estadoFinal[estado], "lexema: ", lexema, "na linha ", nlinha, "POSIcao inicial:", posicao-len(lexema), "posicao final: ", posicao - 1) 

estado = 0
lines = []
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
        palavra(linha.strip(), nlinha, estado)
        estado = 0
    except KeyError:
        continue

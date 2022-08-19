estadoFinal = {2: "variavel", 3: "if", 6: "for",  11: "PRINT", 13: "maior", 
12: "constante", 14: "menor" , 15: "abre parentese", 16: "fecha parenteses", 
17: "abre chave", 18: "fecha chave", 19: "menos", 20: "soma", 21: "multiplicar", 
22: "dividir", 23: "igual simples", 24: "igual duplo", 26: "diferente", 31: "while"}

tabelaTransicao = { 0: {'i': 1, 'f': 4, 'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2, 'g': 2, 'h': 2, 'j': 2, 'k': 2, 'l': 2,'m': 2, 'n': 2, 'o': 2,'p': 7, 
'q': 2, 'r':2, 's':2, 't': 2, 'u': 2, 'v': 2, 'w': 27, 'x': 2, 'y': 2, 'z': 2, '0': 12, '1':12, '2':12, '3': 12, '4': 12, '5': 12, '6': 12, '7': 12, 
'8': 12, '9': 12, '>': 13, '<':14, '(':15, ')': 16, '{': 17, '}': 18, '-': 19, '+': 20, '*': 21, '/': 22, '=': 23, '!': 25},

1: {'i':2, 'f': 3, 'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2, 'g': 2, 'h': 2, 'j': 2, 'k': 2, 'l': 2,'m': 2, 'n': 2, 'o': 2,'p': 2, 
'q': 2, 'r':2, 's':2, 't': 2, 'u': 2, 'v': 2, 'w': 2, 'x': 2, 'y': 2, 'z': 2, '0': 2, '1':2, '2':2, '3': 2, '4': 2, '5': 2, '6': 2, 
'7': 2, '8': 2, '9': 2},

2: {'i':2, 'f': 2, 'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2, 'g': 2, 'h': 2, 'j': 2, 'k': 2, 'l': 2,'m': 2, 'n': 2, 'o': 2,'p': 2, 
'q': 2, 'r':2, 's':2, 't': 2, 'u': 2, 'v': 2, 'w': 2, 'x': 2, 'y': 2, 'z': 2, '0': 2, '1':2, '2':2, '3': 2, '4': 2, '5': 2, '6': 2, 
'7': 2, '8': 2, '9': 2},

3: {'i':2, 'f': 2, 'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2, 'g': 2, 'h': 2, 'j': 2, 'k': 2, 'l': 2,'m': 2, 'n': 2, 'o': 2,'p': 2, 
'q': 2, 'r':2, 's':2, 't': 2, 'u': 2, 'v': 2, 'w': 2, 'x': 2, 'y': 2, 'z': 2, '0': 2, '1':2, '2':2, '3': 2, '4': 2, '5': 2, '6': 2, 
'7': 2, '8': 2, '9': 2},

4: {'i':2, 'f': 2, 'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2, 'g': 2, 'h': 2, 'j': 2, 'k': 2, 'l': 2,'m': 2, 'n': 2, 'o': 5,'p': 2, 
'q': 2, 'r':2, 's':2, 't': 2, 'u': 2, 'v': 2, 'w': 2, 'x': 2, 'y': 2, 'z': 2, '0': 2, '1':2, '2':2, '3': 2, '4': 2, '5': 2, '6': 2, 
'7': 2, '8': 2, '9': 2},

5: {'i':2, 'f': 2, 'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2, 'g': 2, 'h': 2, 'j': 2, 'k': 2, 'l': 2,'m': 2, 'n': 2, 'o': 5,'p': 2, 
'q': 2, 'r':6, 's':2, 't': 2, 'u': 2, 'v': 2, 'w': 2, 'x': 2, 'y': 2, 'z': 2,'0': 2, '1':2, '2':2, '3': 2, '4': 2, '5': 2, '6': 2, 
'7': 2, '8': 2, '9': 2},

5: {'i':2, 'f': 2, 'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2, 'g': 2, 'h': 2, 'j': 2, 'k': 2, 'l': 2,'m': 2, 'n': 2, 'o': 5,'p': 2, 
'q': 2, 'r':6, 's':2, 't': 2, 'u': 2, 'v': 2, 'w': 2, 'x': 2, 'y': 2, 'z': 2, '0': 2, '1':2, '2':2, '3': 2, '4': 2, '5': 2, '6': 2, 
'7': 2, '8': 2, '9': 2},

6: {'i':2, 'f': 2, 'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2, 'g': 2, 'h': 2, 'j': 2, 'k': 2, 'l': 2,'m': 2, 'n': 2, 'o': 2,'p': 2, 
'q': 2, 'r':7, 's':2, 't': 2, 'u': 2, 'v': 2, 'w': 2, 'x': 2, 'y': 2, 'z': 2, '0': 2, '1':2, '2':2, '3': 2, '4': 2, '5': 2, '6': 2, 
'7': 2, '8': 2, '9': 2},

7: {'i':2, 'f': 2, 'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2, 'g': 2, 'h': 2, 'j': 2, 'k': 2, 'l': 2,'m': 2, 'n': 2, 'o': 2,'p': 2, 
'q': 2, 'r':8, 's':2, 't': 2, 'u': 2, 'v': 2, 'w': 2, 'x': 2, 'y': 2, 'z': 2, '0': 2, '1':2, '2':2, '3': 2, '4': 2, '5': 2, '6': 2, 
'7': 2, '8': 2, '9': 2},

8: {'i':9, 'f': 2, 'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2, 'g': 2, 'h': 2, 'j': 2, 'k': 2, 'l': 2,'m': 2, 'n': 2, 'o': 2,'p': 2, 
'q': 2, 'r':2, 's':2, 't': 2, 'u': 2, 'v': 2, 'w': 2, 'x': 2, 'y': 2, 'z': 2, '0': 2, '1':2, '2':2, '3': 2, '4': 2, '5': 2, '6': 2, 
'7': 2, '8': 2, '9': 2},

9: {'i':2, 'f': 2, 'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2, 'g': 2, 'h': 2, 'j': 2, 'k': 2, 'l': 2,'m': 2, 'n': 10, 'o': 2,'p': 2, 
'q': 2, 'r':2, 's':2, 't': 2, 'u': 2, 'v': 2, 'w': 2, 'x': 2, 'y': 2, 'z': 2, '0': 2, '1':2, '2':2, '3': 2, '4': 2, '5': 2, '6': 2, 
'7': 2, '8': 2, '9': 2},

10: {'i':2, 'f': 2, 'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2, 'g': 2, 'h': 2, 'j': 2, 'k': 2, 'l': 2,'m': 2, 'n': 10, 'o': 2,'p': 2, 
'q': 2, 'r':2, 's':2, 't': 11, 'u': 2, 'v': 2, 'w': 2, 'x': 2, 'y': 2, 'z': 2, '0': 2, '1':2, '2':2, '3': 2, '4': 2, '5': 2, '6': 2, 
'7': 2, '8': 2, '9': 2},

11: {'i':2, 'f': 2, 'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2, 'g': 2, 'h': 2, 'j': 2, 'k': 2, 'l': 2,'m': 2, 'n': 10, 'o': 2,'p': 2, 
'q': 2, 'r':2, 's':2, 't': 2, 'u': 2, 'v': 2, 'w': 2, 'x': 2, 'y': 2, 'z': 2,'0': 2, '1':2, '2':2, '3': 2, '4': 2, '5': 2, '6': 2, 
'7': 2, '8': 2, '9': 2},

12: {'0': 12, '1':12, '2':12, '3': 12, '4': 12, '5': 12, '6': 12, '7': 12, '8': 12, '9': 12},

23: {'=': 24},

25: {'=': 26},

27: {'i':2, 'f': 2, 'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2, 'g': 2, 'h': 28, 'j': 2, 'k': 2, 'l': 2,'m': 2, 'n': 2, 'o': 5,'p': 2, 
'q': 2, 'r':2, 's':2, 't': 2, 'u': 2, 'v': 2, 'w': 2, 'x': 2, 'y': 2, 'z': 2, '0': 2, '1':2, '2':2, '3': 2, '4': 2, '5': 2, '6': 2, 
'7': 2, '8': 2, '9': 2},

28: {'i':29, 'f': 2, 'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2, 'g': 2, 'h': 2, 'j': 2, 'k': 2, 'l': 2,'m': 2, 'n': 2, 'o': 5,'p': 2, 
'q': 2, 'r':2, 's':2, 't': 2, 'u': 2, 'v': 2, 'w': 2, 'x': 2, 'y': 2, 'z': 2, '0': 2, '1':2, '2':2, '3': 2, '4': 2, '5': 2, '6': 2, 
'7': 2, '8': 2, '9': 2},

29: {'i':2, 'f': 2, 'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2, 'g': 2, 'h': 2, 'j': 2, 'k': 2, 'l': 30,'m': 2, 'n': 2, 'o': 5,'p': 2, 
'q': 2, 'r':6, 's':2, 't': 2, 'u': 2, 'v': 2, 'w': 2, 'x': 2, 'y': 2, 'z': 2, '0': 2, '1':2, '2':2, '3': 2, '4': 2, '5': 2, '6': 2, 
'7': 2, '8': 2, '9': 2},

30: {'i':2, 'f': 2, 'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 31, 'g': 2, 'h': 2, 'j': 2, 'k': 2, 'l': 30,'m': 2, 'n': 2, 'o': 5,'p': 2, 
'q': 2, 'r':6, 's':2, 't': 2, 'u': 2, 'v': 2, 'w': 2, 'x': 2, 'y': 2, 'z': 2, '0': 2, '1':2, '2':2, '3': 2, '4': 2, '5': 2, '6': 2, 
'7': 2, '8': 2, '9': 2},

}

def palavra(linha, nLinha, estado):
    for letra in linha:
        if letra.strip():
            try:
                estado = tabelaTransicao[estado][letra.lower()]
            except KeyError:
                try:
                    print(estadoFinal[estado], "na linha ", nlinha)
                    estado = 0
                    print(estadoFinal[palavra(letra, nLinha, estado)], "na linha ", nlinha)
                except KeyError:
                    print("transicao nao conhecida")
        else:
            try:
                print(estadoFinal[estado], "na linha ", nLinha)
                estado = 0
            except KeyError:
                continue
    return estado

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
        print(estadoFinal[palavra(linha.strip(), nlinha, estado)], "na linha ", nlinha)
        estado = 0
    except KeyError:
        continue

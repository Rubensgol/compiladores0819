
global cont, anterior, listaToken

def term(token):
    ret = listaToken[cont][0] == token
    cont = cont + 1
    return ret

def E1():
    return T()

def E2():
    return T() and term('MAIS') and E()

def E():
    anterior = cont
    if E1():
        return True
    else:
        cont = anterior
        return E2()

def T1():
    return term('mais')

def T2():
    return term('INT') and term('MULT') and T()

def T3():
    return term('AP') and E() and term('FP')

def T():
    anterior = cont
    if T1():
        return True
    else:
        cont = anterior
        if T2():
            return True
        else:
            cont = anterior
            return T3()

def verifica(lista_tk):
    cont = 0
    anterior = 0
    listaToken = lista_tk 
    print(E())
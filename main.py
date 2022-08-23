import anaslisador as sintaxe
import analisadorTeste as gramatico

listToken = sintaxe.lerTokens()

gramatico.verifica(listToken)
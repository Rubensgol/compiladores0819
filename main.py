import anaslisador as sintaxe
import analisadorTeste as gramatico

listToken = sintaxe.lerTokens()

anaGrama = gramatico.AnalisaDor(listToken).E()

print(anaGrama)
import anaslisador as sintaxe
import analisadorTeste2

listToken = sintaxe.lerTokens()

anaGrama = analisadorTeste2.AnalisaDor(listToken)

print(anaGrama.FUNCAO())
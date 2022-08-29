import anaslisador as sintaxe
import analisadorTeste

listToken = sintaxe.lerTokens()

anaGrama = analisadorTeste.AnalisaDor(listToken)

print(anaGrama.E())
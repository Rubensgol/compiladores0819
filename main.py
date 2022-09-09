import lexico as sintaxe
import analisadorDependente

listToken = sintaxe.Lexico()

listToken.lerTokens()

anaGrama = analisadorDependente.AnalisaDor(listToken)

anaGrama.analisa()
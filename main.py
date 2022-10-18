import lexico as sintaxe
import analisadorDependente
import slr

listToken = sintaxe.Lexico()

listToken.lerTokens()

anaGrama = slr.AnalisaDor(listToken)

anaGrama.analisa()
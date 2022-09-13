tabelaTransicaoDic = {  '<FUNCAO>' : {'funcao' : ['funcao', 'variavel', 'AP', '<PARAN>', 'FP', 'AC', '<LISTAESCOPO>', 'FC']},
                        '<ESCOPO>' : {'if' : ['<IF>'], 'PRINT': ['<PRINT>'], 'variavel' : ['<ATRIB>'], 'cont': ['<ATRIB>'] },
                        '<IF>' : {'if' : ['if', 'AP', '<COND>', 'FP', 'AC', '<ESCOPO>', 'FC']},
                        '<COND>' : {'variavel': [ '<VAR>', '<SCOND>', '<VAR>'], 'cont' : ['<VAR>', '<SCOND>', '<VAR>'] },
                        '<SCOND>' : {'maior': ['maior'], 'menor' : ['menor'] },
                        '<PRINT>' : {'PRINT' : ['PRINT', 'AP', '<VAR>', 'FP', 'PV']},
                        '<VAR>' : {'variavel' : ['variavel'], 'cont': ['cont']},
                        '<ATRIB>' : {'variavel' : ['<VAR>', 'igual', '<VAR>', 'PV'], 'cont' : ['<VAR>', 'igual', '<VAR>', 'PV']},
                        '<PARAN>' : {'int' : ['<TIPO>', 'variavel', '<PARANS>'], }, 
                        '<PARANS>' : {'VIRGULA': ['VIRGULA', '<PARAN>'], 'FP' : []},
                        '<TIPO>' : {'int': ['int'], 'string': ['string']},
                        '<LISTAESCOPO>' : {'variavel': ['<ESCOPO>', '<LISTAESCOPO>'], 'if' : ['<ESCOPO>', '<LISTAESCOPO>'], 'print': ['<ESCOPO>', '<LISTAESCOPO>'], 'cont': ['<ESCOPO>', '<LISTAESCOPO>'],
                         'FC' : []}
}
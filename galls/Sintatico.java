public class Sintatico implements Constants
{
    private Token currentToken;
    private Token previousToken;
    private Lexico scanner;
    private Semantico semanticAnalyser;

    public void parse(Lexico scanner, Semantico semanticAnalyser) throws AnalysisError
    {
        this.scanner = scanner;
        this.semanticAnalyser = semanticAnalyser;

        currentToken = scanner.nextToken();
        if (currentToken == null)
            currentToken = new Token(DOLLAR, "$", 0);

        FUNCAO();

        if (currentToken.getId() != DOLLAR)
            throw new SyntaticError(PARSER_ERROR[DOLLAR], currentToken.getPosition());
    }

    private void match(int token) throws AnalysisError
    {
        if (currentToken.getId() == token)
        {
            previousToken = currentToken;
            currentToken = scanner.nextToken();
            if (currentToken == null)
            {
                int pos = 0;
                if (previousToken != null)
                    pos = previousToken.getPosition()+previousToken.getLexeme().length();

                currentToken = new Token(DOLLAR, "$", pos);
            }
        }
        else
            throw new SyntaticError(PARSER_ERROR[token], currentToken.getPosition());
    }

    private void FUNCAO() throws AnalysisError
    {
        switch (currentToken.getId())
        {
            case 16: // funcao
                match(16); // funcao
                match(9); // variavel
                match(3); // AP
                PARAN();
                match(4); // FP
                match(5); // AC
                LISTAESCOPO();
                match(6); // FC
                break;
            default:
                throw new SyntaticError(PARSER_ERROR[17], currentToken.getPosition());
        }
    }

    private void ESCOPO() throws AnalysisError
    {
        switch (currentToken.getId())
        {
            case 2: // if
                IF();
                break;
            case 9: // variavel
            case 10: // cont
                ATRIB();
                break;
            case 12: // print
                PRINT();
                break;
            default:
                throw new SyntaticError(PARSER_ERROR[18], currentToken.getPosition());
        }
    }

    private void IF() throws AnalysisError
    {
        switch (currentToken.getId())
        {
            case 2: // if
                match(2); // if
                match(3); // AP
                COND();
                match(4); // FP
                match(5); // AC
                ESCOPO();
                match(6); // FC
                break;
            default:
                throw new SyntaticError(PARSER_ERROR[19], currentToken.getPosition());
        }
    }

    private void COND() throws AnalysisError
    {
        switch (currentToken.getId())
        {
            case 9: // variavel
            case 10: // cont
                VAR();
                SCOND();
                VAR();
                break;
            default:
                throw new SyntaticError(PARSER_ERROR[20], currentToken.getPosition());
        }
    }

    private void PRINT() throws AnalysisError
    {
        switch (currentToken.getId())
        {
            case 12: // print
                match(12); // print
                match(3); // AP
                VAR();
                match(4); // FP
                match(11); // PV
                break;
            default:
                throw new SyntaticError(PARSER_ERROR[21], currentToken.getPosition());
        }
    }

    private void SCOND() throws AnalysisError
    {
        switch (currentToken.getId())
        {
            case 7: // MAIOR
                match(7); // MAIOR
                break;
            case 8: // MENOR
                match(8); // MENOR
                break;
            default:
                throw new SyntaticError(PARSER_ERROR[22], currentToken.getPosition());
        }
    }

    private void VAR() throws AnalysisError
    {
        switch (currentToken.getId())
        {
            case 9: // variavel
                match(9); // variavel
                break;
            case 10: // cont
                match(10); // cont
                break;
            default:
                throw new SyntaticError(PARSER_ERROR[23], currentToken.getPosition());
        }
    }

    private void ATRIB() throws AnalysisError
    {
        switch (currentToken.getId())
        {
            case 9: // variavel
            case 10: // cont
                VAR();
                match(13); // igual
                VAR();
                match(11); // PV
                break;
            default:
                throw new SyntaticError(PARSER_ERROR[24], currentToken.getPosition());
        }
    }

    private void PARAN() throws AnalysisError
    {
        switch (currentToken.getId())
        {
            case 14: // int
                TIPO();
                match(9); // variavel
                PARANS();
                break;
            default:
                throw new SyntaticError(PARSER_ERROR[25], currentToken.getPosition());
        }
    }

    private void PARANS() throws AnalysisError
    {
        switch (currentToken.getId())
        {
            case 4: // FP
                // EPSILON
                break;
            case 15: // virgula
                match(15); // virgula
                PARAN();
                break;
            default:
                throw new SyntaticError(PARSER_ERROR[26], currentToken.getPosition());
        }
    }

    private void TIPO() throws AnalysisError
    {
        switch (currentToken.getId())
        {
            case 14: // int
                match(14); // int
                break;
            default:
                throw new SyntaticError(PARSER_ERROR[27], currentToken.getPosition());
        }
    }

    private void LISTAESCOPO() throws AnalysisError
    {
        switch (currentToken.getId())
        {
            case 2: // if
            case 9: // variavel
            case 10: // cont
            case 12: // print
                ESCOPO();
                LISTAESCOPO();
                break;
            case 6: // FC
                // EPSILON
                break;
            default:
                throw new SyntaticError(PARSER_ERROR[28], currentToken.getPosition());
        }
    }

}

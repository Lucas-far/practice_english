

inks: tuple = (
        '\033[1:30m', '\033[1:31m', '\033[1:32m', '\033[1:33m', '\033[1:34m', '\033[1:35m', '\033[1:36m', '\033[m'
    )

hello = f"""
    ==================================================
    Welcome to the {inks[3]}TREINO DE ADJETIVOS{inks[7]}
    ==================================================
    """

input_message = '{}Por favor, aperte ENTER{}'

input_message2 = '{}Clique após a seta, digite sua frase, aperte ENTER, ou apenas aperte ENTER ->{} '

controller = '{}Aperte ENTER ou qualquer outra tecla para continuar...{}'

quiz_format = """
    ====================
    O QUE É {}? 
    ==================== 
    1 - {}
    2 - {}
    3 - {}
    4 - {}
    5 - {}

    Digite de 1 a 5, para fornecer sua resposta
    Digite após a seta -> """

success = """
    ==================== RELATÓRIO ====================        
    {}Resposta correta{}
    {}Jogos jogados:{} {}
    {}Placar:{} {}Acertos{} {} x {} {}Erros{}
    ===================================================
    """

failure = """ 
    ==================== RELATÓRIO ====================
    {}Resposta incorreta{}
    {}Resposta correta:{} {} - {}
    {}Jogos jogados:{} {}
    {}Placar:{} {}Acertos{} {} x {} {}Erros{}
    ====================================================
    """

sentence_creation = """
    Sabendo que {}{}{} significa {}{}{}, tente criar uma frase

    DICAS
    ==================================================
    Pronome:               (1) {} {}   
    Adjetivo possessivo:   (1) {} {}
    Pronome possessivo:    (1) {} {}
    Pronome demonstrativo: (1) {} {} 
    Pronome reflexivo:     (1) {} {}        
    Preposição:            (1) {} {}   
    Advérbios:             (1) {} {} (2) {} {} (3) {} {} 
    Conjunção:             (1) {} {} (2) {} {}
    Palavras de dúvida:    (1) {} {} 
    Substantivo:           (1) {} {} (2) {} {} (3) {} {}

    VERBOS SIMPLES: passado/presente/futuro
    ==================================================
    infinitivo:       (1) {} {}
    passado:          (1) {} {}
    presente:         (1) {} {}
    futuro:           (1) {} {}
    to be:            (1) {} {} (2) {} {} (3) {} {}
    can:              (1) {} {} (2) {} {}
    to do (auxiliar): (1) {} {} (2) {} {}
    to have:          (1) {} {} (2) {} {} (3) {} {}
    """

set_error = """
{} ========== Erro de processamento ========== {}
O conjunto não foi capaz de gerar todos os dados de um jogo
"""



inks: tuple = (
        '\033[1:30m', '\033[1:31m', '\033[1:32m', '\033[1:33m', '\033[1:34m', '\033[1:35m', '\033[1:36m', '\033[m'
    )

hello = f"""
    ==================================================
    Welcome to the {inks[3]}TREINO DE ADVÉRBIOS{inks[7]}
    ==================================================
    """

input_message = f'{inks[5]}Por favor, aperte ENTER{inks[7]}'

input_message2 = f'{inks[5]}Clique após a seta, digite sua frase, aperte ENTER, ou apenas aperte ENTER -> {inks[7]} '

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

hints = """
    Sabendo que {} significa {}, tente criar uma frase

    DICAS
    ==================================================
    Adjetivo possessivo:   (1) {} {}
    Pronome:               (1) {} {}   
    Pronome demonstrativo: (1) {} {}
    Pronome possessivo:    (1) {} {}
    Pronome reflexivo:     (1) {} {}   
    Conjunção:             (1) {} {} (2) {} {}      
    Preposição:            (1) {} {}   
    Palavras de dúvida:    (1) {} {} 
    Adjetivo:              (1) {} {} (2) {} {} (3) {} {}
    Substantivo:           (1) {} {} (2) {} {} (3) {} {}

    VERBOS SIMPLES: passado/presente/futuro
    ==================================================
    can:              (1) {} {} (2) {} {}
    to be:            (1) {} {} (2) {} {} (3) {} {}
    to do (auxiliar): (1) {} {} (2) {} {}
    to have:          (1) {} {} (2) {} {} (3) {} {}
    infinitivo:       (1) {} {}
    passado:          (1) {} {}
    presente:         (1) {} {}
    futuro:           (1) {} {}
    
    """

set_error = f"""
{inks[1]} ========== Erro de processamento ========== {inks[7]}
O conjunto não foi capaz de gerar todos os dados de um jogo
"""


from cores.cores import inks

# Pronome:                ||
# Pronome demonstrativo:  ||
# Pronome possessivo:     ||
# Pronome reflexivo:      ||
# Adjetivo possessivo:    ||
# Advérbio:               ||
# Advérbio de frequência: ||
# Advérbio ly:            ||
# Conjunção:              ||
# Preposição:             ||
# Palavra de dúvida:      ||
# Adjetivo:               ||
# Substantivo:            ||
# Verbo can (presente):   ||
# Verbo can (passado):    ||
# To be (passado):        ||
# To be (presente):       ||
# To be (future):         ||
# To do (passado):        ||
# To do (presente):       ||
# To have (passado):      ||
# To have (presente):     ||
# To have (futuro):       ||
# Verbo (infinitivo):     ||
# Verbo (passado):        ||
# Verbo (presente):       ||
# Verbo (futuro):         ||

skip = ' '

four_spaces = '    '

or_ = f" {inks[1]}ou{inks[7]} "

press_enter = f'    {inks[5]}Por favor, aperte ENTER{inks[7]}\n'

type_your_sentence = f'    {inks[5]}Clique após a seta, digite sua frase, aperte ENTER, ou apenas aperte ENTER ->{inks[7]} '

write_vocabulary = '    Clique após a seta e escreva a palavra alvo CORRETAMENTE -> '


write_vocabulary_type2 = '    Clique após a seta e escreva a alternativa em INGLÊS, CORRETAMENTE -> '

typo = '    {}A palavra{} {}{}{} {}foi escrita incorretamente. Tente novamente{}'

titles = {
    'pr': 'Pronome:                || ',
    'dp': 'Pronome demonstrativo:  || ',
    'pp': 'Pronome possessivo:     || ',
    'rp': 'Pronome reflexivo:      || ',
    'pa': 'Adjetivo possessivo:    || ',
    'adv': 'Advérbio:               || ',
    'adv_f': 'Advérbio de frequência: || ',
    'adv_ly': 'Advérbio ly:            || ',
    'conj': 'Conjunção:              || ',
    'prep': 'Preposição:             || ',
    'wh': 'Palavra de dúvida:      || ',
    'adj': 'Adjetivo:               || ',
    'noun': 'Substantivo:            || ',
    'can': 'Verbo can (presente):   || ',
    'could': 'Verbo can (passado):    || ',
    'to_be_past': 'To be (passado):        || ',
    'to_be_pst': 'To be (presente):       || ',
    'to_be_fut': 'To be (future):         || ',
    'to_do_past': 'To do (passado):        || ',
    'to_do_pst': 'To do (presente):       || ',
    'to_have_past': 'To have (passado):      || ',
    'to_have_pst': 'To have (presente):     || ',
    'to_have_fut': 'To have (futuro):       || ',
    'verb_inf': 'Verbo (infinitivo):     || ',
    'verb_past': 'Verbo (passado):        || ',
    'verb_pst': 'Verbo (presente):       || ',
    'verb_fut': 'Verbo (futuro):         || '
}

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

announcement = """
    ==================== ELEMENTOS ====================
    Sabendo que {}, significa {}, tente criar uma frase
    """

set_error = f"""
    {inks[1]} ========== Erro de processamento ========== {inks[7]}
    O conjunto não foi capaz de gerar todos os dados de um jogo
    """

word_report = []

for value in titles.values():
    word_report.append((len(value), value))

word_report = sorted(word_report, key=lambda integer: integer[0], reverse=True)[0]
word_length = word_report[0]
word_name = word_report[1]


if __name__ == '__main__':
    # print(word_report)
    # print(word_length)
    # print(word_name)

    for word in titles.values():
        print(word)

    # for word in categories:
    #     print(word)

    # print(len(categories))
    # print(len(titles_keys))

    # counter = 0
    # while counter < len(categories):
    #     print(f"'{titles_keys[counter]}': '{categories[counter]}'")
    #     counter += 1

    for word in titles.values():
        print(word)

    # for value in titles.values():
    #     print(value)

    # print('===========================================================================================================')

    # for value in titles.values():
    #     if len(value) == biggest_length:
    #         print(value + ' ' * (biggest_length - len(value) - 2) + '|| ')
    #     else:
    #         print(value + ' ' * (biggest_length - len(value)) + '|| ')
    pass

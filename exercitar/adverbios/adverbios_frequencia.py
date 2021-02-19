

from gramatica.adverbios.adverbios import adv_frequency, adv_frequency_keys
from metodos.banco_de_dados import *
from random import choice
from cores.cores import colors

# TOOLS
black, red, green, yellow, blue, purple, cyan, ink = colors[0], colors[1], colors[2], colors[3], colors[4], colors[5], colors[6], colors[7]
bricks = '=' * 20

quiz_format = """
    {}
    O QUE É {}{}{} ?
    {}
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
    {}Resposta correta:{} {}
    {}Jogos jogados:{} {}
    {}Placar:{} {}Acertos{} {} x {} {}Erros{}
    ====================================================
    """

controller = '{}Aperte ENTER ou qualquer outra tecla para continuar...{}'

set_error = """
{} ========== Erro de processamento ========== {}
O conjunto não foi capaz de gerar todos os dados de um jogo
"""

# VARIABLES TO DETERMINE THE PLAYER'S EFFICACY
positive_score = 0
negative_score = 0


while True:

    try:

        box_words = set({})
        box_words_translations = set({})
        box_target_translation = []


        def create_word():
            """"""
            while len(box_words) < 5:

                new_key = choice(adv_frequency_keys)
                new_key_values = adv_frequency[new_key]
                chosen = new_key_values[0]
                value_meaning = new_key_values[1]

                # print(f'{new_key = }')
                # print(f'{new_key_values = }')
                # print(f'{chosen = }')
                # print(f'{value_meaning = }')

                box_words.add(chosen)
                box_words_translations.add(value_meaning)

        create_word()

        box_words = list(box_words)

        box_words_translations = list(box_words_translations)

        chosen_key = choice(box_words)

        values_chosen_key = adv_frequency[chosen_key]

        chosen_value = values_chosen_key[0]

        chosen_value_meaning = values_chosen_key[1]

        box_target_translation.append(chosen_value_meaning)


        def see_variables():
            """"""
            print(f"{box_words = }")
            print(f"{box_words_translations = }")
            print(f'{chosen_key = }')
            print(f'{values_chosen_key = }')
            print(f'{chosen_value = }')
            print(f'{chosen_value_meaning = }')
            print(f'{box_target_translation = }')
            print(f'{box_words = }')
            print(f'{box_words_translations = }')

        # see_variables()

        greetings = welcome('treino de advérbios de frequência', prefix=3, prefix2=7)

        print(greetings)

        answer = get_input_int(
            text=quiz_format.format(
                bricks,
                yellow, chosen_value, ink,
                bricks,
                *box_words_translations),
            start=1,
            limit=5
        )

        # ONE OF THEM IS CORRECT, THE ONLY CORRECT WILL RETURN A NUMBER LESSER THAN 10
        conditions = [
            *[1 if box_words_translations[0] in box_target_translation else 10],
            *[2 if box_words_translations[1] in box_target_translation else 11],
            *[3 if box_words_translations[2] in box_target_translation else 12],
            *[4 if box_words_translations[3] in box_target_translation else 13],
            *[5 if box_words_translations[4] in box_target_translation else 14],
        ]

        # THE ONLY NUMBER LESSER THAN 10 IS PLACED AS INDEX 0
        correct_answer_index = sorted(conditions)[0]

        if answer == correct_answer_index:
            positive_score += 1
            print(success.format(
                blue, ink,
                green, ink, positive_score + negative_score,
                yellow, ink, blue, ink, positive_score, negative_score, red, ink
            ))
        else:
            negative_score += 1
            print(failure.format(
                red, ink,
                blue, ink, box_target_translation[0],
                green, ink, positive_score + negative_score,
                yellow, ink, blue, ink, positive_score, negative_score, red, ink
            ))

        input(controller.format(cyan, ink))
        sleep(1)
    except IndexError as error:
        print(set_error.format(red, ink))

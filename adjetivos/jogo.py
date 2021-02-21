

from adjetivos.bdd_adjetivos import adjectives, adjectives_pt_br
from metodos.bdd import *
from random import choice
from cores.cores import colors

# todo
from metodos.bdd import sentence_maker as _
from adverbios.bdd_adverbios import adv_ly, adv_frequency, adv_others
from pronomes.bdd_pronomes import pro
from pronomes_demonstrativos.bdd_pronomes_demonstrativos import pro_be_gl_u, pro_be_gl_l
from substantivos.bdd_substantivos import nouns
from verbos_be.bdd_presente import be_pst
from verbos_infinitivo.bdd_verbos_infinitivo import verbs_infinitive
from verbos_passado.bdd_verbos_passado import past
from verbos_presente.bdd_verbos_presente import present
from verbos_futuro.bdd_verbos_futuro import future
# todo

# TOOLS
black, red, green, yellow, blue, purple, cyan, ink = \
    colors[0], colors[1], colors[2], colors[3], colors[4], colors[5], colors[6], colors[7]

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
    {}Resposta correta:{} {} - {}
    {}Jogos jogados:{} {}
    {}Placar:{} {}Acertos{} {} x {} {}Erros{}
    ====================================================
    """

controller = '{}Aperte ENTER ou qualquer outra tecla para continuar...{}'

set_error = """
{} ========== Erro de processamento ========== {}
O conjunto não foi capaz de gerar todos os dados de um jogo
"""

positive_score = 0
negative_score = 0

while True:

    try:

        # todo
        element = _(adv_ly)
        element2 = _(adv_frequency)
        element3 = _(adv_others)
        element4 = _(pro)
        element5 = _(pro_be_gl_u)
        element6 = _(pro_be_gl_l)
        element7 = _(nouns)
        element8 = _(verbs_infinitive)
        element9 = _(past)
        element10 = _(present)
        element11 = _(future)
        element_box = [
            element, element2, element3, element4, element5, element6, element7, element8, element9,
            element10, element11
        ]
        print(element_box)
        # todo

        five_words = set({})


        def create_word():
            """"""
            while len(five_words) < 5:
                five_words.add(choice(adjectives))

        create_word()

        five_words = sorted(list(five_words))

        five_indexes = [adjectives.index(word) for word in five_words]

        five_translations = [adjectives_pt_br[index] for index in five_indexes]

        chosen_word = choice(five_words)

        chosen_word_index = five_words.index(chosen_word)

        chosen_word_translation = five_translations[chosen_word_index]

        the_target_translation = [chosen_word_translation]


        def see_variables():
            """"""
            print(f"{five_words = }")
            print(f"{five_indexes = }")
            print(f"{five_translations = }")
            print(f"{chosen_word = }")
            print(f"{chosen_word_index = }")
            print(f"{chosen_word_translation = }")
            print(f"{the_target_translation = }")

        # see_variables()

        greetings = welcome('treino de adjetivos', prefix=3, prefix2=7)

        print(greetings)

        answer = get_input_int(
            text=quiz_format.format(
                bricks,
                yellow, chosen_word, ink,
                bricks,
                *five_translations),
            start=1,
            limit=5
        )

        # ONE OF THEM IS CORRECT, THE ONLY CORRECT WILL RETURN A NUMBER LESSER THAN 10
        conditions = [
            *[1 if five_translations[0] in the_target_translation else 10],
            *[2 if five_translations[1] in the_target_translation else 11],
            *[3 if five_translations[2] in the_target_translation else 12],
            *[4 if five_translations[3] in the_target_translation else 13],
            *[5 if five_translations[4] in the_target_translation else 14],
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
                blue, ink, correct_answer_index, the_target_translation[0],
                green, ink, positive_score + negative_score,
                yellow, ink, blue, ink, positive_score, negative_score, red, ink
            ))

        input(controller.format(cyan, ink))
        sleep(1)

    except IndexError as error:
        print(set_error.format(red, ink))

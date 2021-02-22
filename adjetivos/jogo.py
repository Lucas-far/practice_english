

from adjetivos.bdd_adjetivos import adjectives, adjectives_pt_br
from metodos.bdd import *
from random import choice
from cores.cores import colors

# todo
from metodos.bdd import sentence_maker as _

from pronomes.bdd_pronomes import (pronouns_l, pronouns_pt_br)
from adjetivos_possessivos.bdd_adjetivos_possessivos import (possessive_adjectives_l, possessive_adjectives_l_pt_br)
from pronomes_demonstrativos.bdd_pronomes_demonstrativos import (demonstrative_pronouns_l, demonstrative_pronouns_pt_br)
from preposicoes.bdd_preposicoes import (prepositions, prepositions_pt_br)

from adverbios.bdd_adverbios import (
    adverbs_ly, adverbs_ly_pt_br,
    adverbs_frequency, adverbs_frequency_pt_br,
    adverb_others, adverb_others_pt_br
)

from substantivos.bdd_substantivos import (nouns, nouns_pt_br)

from verbos_be.bdd_verbos_be import (be_present_l, be_present_l_pt_br)
from verbos_can.bdd_verbos_can import (can_present_l, can_present_l_pt_br)
from verbos_do.bdd_verbos_do import (do_present_l, do_present_l_pt_br)
from verbos_have.bdd_verbos_have import (have_present_l, have_present_l_pt_br)

from verbos_infinitivo.bdd_verbos_infinitivo import (verbs_infinitive, verbs_infinitive_pt_br)
from verbos_passado.bdd_verbos_passado import (past, past_pt_br)
from verbos_presente.bdd_verbos_presente import (present, present_pt_br)
from verbos_futuro.bdd_verbos_futuro import (future, future_pt_br)

# from pronomes_possessivos.bdd_pronomes_possessivos import pro_pos
# from wh.bdd_wh import wh_gl
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

# todo
input_message = '{}Clique após a seta, digite sua frase, aperte ENTER, ou apenas aperte ENTER ->{} '

sentence_creation = """
    Sabendo que {}{}{} significa {}{}{}, tente criar uma frase
    
    ==================== DICAS =====================
    Pronome:                 {} {}   
    Adjetivo possessivo:     {} {}
    Pronome demonstrativo:   {} {}         
    Preposição:              {} {}   
    Advérbios:               {} {} -> {} {} -> {} {}   
    Substantivo:             {} {}
    Verbo to be no presente: {} {}
    """

    # [  ]   [ {}Verbo can para presente:{} {}{}{} {}{}{} ]
    # [ {}Verbo to do no presente:{} {}{}{} {}{}{} ]   [ {}Verbo to have no presente:{} {}{}{} {}{}{} ]
    # [ {}Verbo no infinitivo:{} {}{}{} {}{}{} ]   [ {}Verbo no passado:{} {}{}{} {}{}{} ]
    # [ {}Verbo no presente:{} {}{}{} {}{}{} ]   [ {}Verbo no futuro:{} {}{}{} {}{}{} ]
# todo

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

        # todo
        pronoun = _(pronouns_l)
        pronoun_tr = pronouns_pt_br[pronouns_l.index(pronoun)]
        pronoun_inked = f"{blue}{pronoun}{ink}"
        pronoun_tr_inked = f"{yellow}{pronoun_tr}{ink}"

        possessive_adjective = _(possessive_adjectives_l)
        possessive_adjective_tr = possessive_adjectives_l_pt_br[possessive_adjectives_l.index(possessive_adjective)]
        possessive_adjective_inked = f"{blue}{possessive_adjective}{ink}"
        possessive_adjective_tr_inked = f"{yellow}{possessive_adjective_tr}{ink}"

        demonstrative_pronoun = _(demonstrative_pronouns_l)
        demonstrative_pronoun_tr = demonstrative_pronouns_pt_br[demonstrative_pronouns_l.index(demonstrative_pronoun)]
        demonstrative_pronoun_inked = f"{blue}{demonstrative_pronoun}{ink}"
        demonstrative_pronoun_inked_tr = f"{yellow}{demonstrative_pronoun_tr}{ink}"

        preposition = _(prepositions)
        preposition_tr = prepositions_pt_br[prepositions.index(preposition)]
        preposition_inked = f"{blue}{preposition}{ink}"
        preposition_tr_inked = f"{yellow}{preposition_tr}{ink}"

        adverb = _(adverbs_frequency)
        adverb2 = _(adverb_others)
        adverb3 = _(adverbs_ly)
        adverb_inked = f"{blue}{adverb}{ink}"
        adverb2_inked = f"{blue}{adverb2}{ink}"
        adverb3_inked = f"{blue}{adverb3}{ink}"

        adverb_tr = adverbs_frequency_pt_br[adverbs_frequency.index(adverb)]
        adverb2_tr = adverb_others_pt_br[adverb_others.index(adverb2)]
        adverb3_tr = adverbs_ly_pt_br[adverbs_ly.index(adverb3)]
        adverb_tr_inked = f"{yellow}{adverb_tr}{ink}"
        adverb2_tr_inked = f"{yellow}{adverb2_tr}{ink}"
        adverb3_tr_inked = f"{yellow}{adverb3_tr}{ink}"

        noun = _(nouns)
        noun_tr = nouns_pt_br[nouns.index(noun)]
        noun_inked = f"{blue}{noun}{ink}"
        noun_tr_inked = f"{yellow}{noun_tr}{ink}"

        be_present = _(be_present_l)
        be_present_tr = be_present_l_pt_br[be_present_l.index(be_present)]
        be_present_inked = f"{blue}{be_present}{ink}"
        be_present_tr_inked = f"{yellow}{be_present_tr}{ink}"

        can_present = _(can_present_l)
        can_present_tr = can_present_l_pt_br[can_present_l.index(can_present)]

        do_present = _(do_present_l)
        do_present_tr = do_present_l_pt_br[do_present_l.index(do_present)]

        have_present = _(have_present_l)
        have_present_tr = have_present_l_pt_br[have_present_l.index(have_present)]

        verb_infinitive = _(verbs_infinitive)
        verb_infinitive_tr = verbs_infinitive_pt_br[verbs_infinitive.index(verb_infinitive)]

        verb_past = _(past)
        verb_past_tr = past_pt_br[past.index(verb_past)]

        verb_present = _(present)
        verb_present_tr = present_pt_br[present.index(verb_present)]

        verb_future = _(future)
        verb_future_tr = future_pt_br[future.index(verb_future)]
        # todo

        answer = get_input_int(
            text=quiz_format.format(bricks, yellow, chosen_word, ink, bricks, *five_translations),
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

            # todo
            print(sentence_creation.format(
                blue, chosen_word, ink, yellow, the_target_translation[0], ink,
                pronoun_inked, pronoun_tr_inked,
                possessive_adjective_inked, possessive_adjective_tr_inked,
                demonstrative_pronoun_inked, demonstrative_pronoun_inked_tr,
                preposition_inked, preposition_tr_inked,
                adverb_inked, adverb_tr_inked, adverb2_inked, adverb2_tr_inked, adverb3_inked, adverb3_tr_inked,
                noun_inked, noun_tr_inked,
                be_present_inked, be_present_tr_inked,
            ))

            sentence = input(input_message.format(green, ink))
            # sentence_translation = do_translation(sentence, 'pt')  # comentar, caso API falhe
            with open('frases.txt', 'a') as txt_file:
                # txt_file.write(f"{sentence} -> {sentence_translation}\n")  # comentar, caso API falhe
                txt_file.write(f"{sentence}\n")  # comentar, caso API falhe
            # todo

        else:
            negative_score += 1
            print(failure.format(
                red, ink,
                blue, ink, correct_answer_index, the_target_translation[0],
                green, ink, positive_score + negative_score,
                yellow, ink, blue, ink, positive_score, negative_score, red, ink
            ))

            # todo
            print(sentence_creation.format(
                blue, chosen_word, ink, yellow, the_target_translation[0], ink,
                pronoun_inked, pronoun_tr_inked,
                possessive_adjective_inked, possessive_adjective_tr_inked,
                demonstrative_pronoun_inked, demonstrative_pronoun_inked_tr,
                preposition_inked, preposition_tr_inked,
                adverb_inked, adverb_tr_inked, adverb2_inked, adverb2_tr_inked, adverb3_inked, adverb3_tr_inked,
                noun_inked, noun_tr_inked,
                be_present_inked, be_present_tr_inked,
            ))

            sentence = input(input_message.format(green, ink))
            # sentence_translation = do_translation(sentence, 'pt')  # comentar, caso API falhe
            with open('frases.txt', 'a') as txt_file:
                # txt_file.write(f"{sentence} -> {sentence_translation}\n")  # comentar, caso API falhe
                txt_file.write(f"{sentence}\n")  # comentar, caso API falhe
            # todo

        # input(controller.format(cyan, ink))
        sleep(1)

    except IndexError as error:
        print(set_error.format(red, ink))

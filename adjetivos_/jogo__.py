

from random import choice
from strings import *
from metodos.bdd import (create_set, get_input_int, var_printer, painter)

from adjetivos.bdd_adjetivos import (adjectives, adjectives_pt_br)

from pronomes.bdd_pronomes import (pronoun, pronoun_tr)

from adjetivos_possessivos.bdd_adjetivos_possessivos import (
    possessive_adjective, possessive_adjective_tr
)

from pronomes_possessivos.bdd_pronomes_possessivos import (
    possessive_pronoun, possessive_pronoun_tr
)

from pronomes_demonstrativos.bdd_pronomes_demonstrativos import (
    demonstrative_pronoun, demonstrative_pronoun_tr
)

from pronomes_reflexivos.bdd_pronomes_reflexivos import (
    reflexive_pronoun, reflexive_pronoun_tr
)

from preposicoes.bdd_preposicoes import (
    preposition, preposition_tr
)

from adverbios.bdd_adverbios import (
    adverb, adverb_tr,
    adverb2, adverb2_tr,
    adverb3, adverb3_tr,
)

from conjuncoes.bdd_conjuncoes import (
    conjunction, conjunction_tr,
    conjunction2, conjunction2_tr,
)

from substantivos.bdd_substantivos import (
    noun, noun_tr,
    noun2, noun2_tr,
    noun3, noun3_tr,
)

from wh.bdd_wh import (wh, wh_tr)

from verbos_be.bdd_verbos_be_simples import (
    be_present, be_present_tr,
    be_past, be_past_tr,
    be_future, be_future_tr,
)

from verbos_can.bdd_verbos_can import (
    could_past, could_past_tr,
    can_present, can_present_tr,
)

from verbos_do.bdd_verbos_do import (
    do_past, do_past_tr,
    do_present, do_present_tr,
)

from verbos_have.bdd_verbos_have import (
    have_past, have_past_tr,
    have_present, have_present_tr,
    have_future, have_future_tr,
)

from verbos_infinitivo.bdd_verbos_infinitivo import (
    verb_infinitive, verb_infinitive_tr
)

from verbos_passado.bdd_verbos_passado import (
    verb_past, verb_past_tr
)

from verbos_presente.bdd_verbos_presente import (
    verb_present, verb_present_tr
)

from verbos_futuro.bdd_verbos_futuro import (
    verb_future, verb_future_tr
)

all_elements = [
    pronoun, pronoun_tr, possessive_adjective, possessive_adjective_tr,
    possessive_pronoun, possessive_pronoun_tr, demonstrative_pronoun, demonstrative_pronoun_tr,
    reflexive_pronoun, reflexive_pronoun_tr, preposition, preposition_tr, adverb,
    adverb_tr, adverb2, adverb2_tr, adverb3, adverb3_tr, conjunction,
    conjunction_tr, conjunction2, conjunction2_tr, wh, wh_tr, noun, noun_tr,
    noun2, noun2_tr, noun3, noun3_tr, verb_infinitive, verb_infinitive_tr,
    verb_past, verb_past_tr, verb_present, verb_present_tr, verb_future,
    verb_future_tr, be_present, be_present_tr, be_past, be_past_tr, be_future,
    be_future_tr, could_past, could_past_tr, can_present, can_present_tr, do_past,
    do_past_tr, do_present, do_present_tr, have_past, have_past_tr, have_present,
    have_present_tr, have_future, have_future_tr
]

all_elements_inked = []

for the_id, word in enumerate(all_elements):
    if the_id % 2:
        all_elements_inked.append(painter('yellow', word))
    else:
        # all_elements_inked.append(word)
        all_elements_inked.append(painter('green', word))


black, red, green, yellow, blue, purple, cyan, ink = inks[0], inks[1], inks[2], inks[3], inks[4], inks[5], inks[6], inks[7]

positive_score = 0
negative_score = 0

while True:

    try:

        empty_set = set({})

        five_words = sorted(list(create_set(empty_set, 5, adjectives, True)))  # function create_set()
        five_indexes = [adjectives.index(word) for word in five_words]
        five_translations = [adjectives_pt_br[index] for index in five_indexes]

        chosen_word = choice(five_words)
        chosen_word_index = five_words.index(chosen_word)
        chosen_word_translation = five_translations[chosen_word_index]
        the_target_translation = [chosen_word_translation]

        display_variables = var_printer(
            list_var_names="""
            five_words five_indexes five_translations chosen_word chosen_word_index chosen_word_translation
            the_target_translation
            """,
            list_var_values=[five_words, five_indexes, five_translations, chosen_word, chosen_word_index,
                             chosen_word_translation, the_target_translation]
        )  # function var_printer()

        # for word in display_variables:
        #     print(word)

        print(hello)

        chosen_word_inked = painter('yellow', chosen_word)

        answer = get_input_int(text=quiz_format.format(chosen_word_inked, *five_translations), start=1, limit=5)

        # One of them is correct, but only the correct one will return a number lesser than 10
        conditions = [
            # 1 if       'happy'        in         ['sad']        else 10
            *[1 if five_translations[0] in the_target_translation else 10],
            *[2 if five_translations[1] in the_target_translation else 11],
            *[3 if five_translations[2] in the_target_translation else 12],
            *[4 if five_translations[3] in the_target_translation else 13],
            *[5 if five_translations[4] in the_target_translation else 14],
        ]

        # EXAMPLE            = sorted([3, 10, 11, 13, 14]) the only number lesser than 10 is placed as index 0
        correct_answer_index = sorted(conditions)[0]

        if answer == correct_answer_index:

            positive_score += 1

            print(success.format(
                blue, ink,
                green, ink, positive_score + negative_score,
                yellow, ink, blue, ink, positive_score, negative_score, red, ink
            ))

            input(input_message.format(green, ink))

            print(sentence_creation.format(
                blue, chosen_word, ink, red, the_target_translation[0], ink, *all_elements_inked
            ))

            sentence = input(input_message2.format(green, ink))
            # sentence_translation = do_translation(sentence, 'pt')  # comentar, caso API falhe

            with open('frases.txt', 'a') as txt_file:
                txt_file.write(f"{sentence}\n")  # comentar, caso API falhe
                # txt_file.write(f"{sentence} -> {sentence_translation}\n")  # comentar, caso API falhe

        else:

            negative_score += 1

            print(failure.format(
                red, ink,
                blue, ink, correct_answer_index, the_target_translation[0],
                green, ink, positive_score + negative_score,
                yellow, ink, blue, ink, positive_score, negative_score, red, ink
            ))

            input(input_message.format(green, ink))

            print(sentence_creation.format(
                blue, chosen_word, ink, red, the_target_translation[0], ink, *all_elements_inked
            ))

            sentence = input(input_message2.format(green, ink))
            # sentence_translation = do_translation(sentence, 'pt')  # comentar, caso API falhe

            with open('frases.txt', 'a') as txt_file:
                txt_file.write(f"{sentence}\n")  # comentar, caso API falhe
                # txt_file.write(f"{sentence} -> {sentence_translation}\n")  # comentar, caso API falhe
    except IndexError as error:
        print(set_error.format(red, ink))


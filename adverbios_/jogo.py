

from random import choice
from strings import *
from metodos.bdd import (choose_word_paint_word as _, create_set, get_input_int, painter)

from adjetivos.bdd_adjetivos import (adjectives, adjectives_pt_br)

from pronomes.bdd_pronomes import (
    pronouns_l, pronouns_l_pt_br
)

from adjetivos_possessivos.bdd_adjetivos_possessivos import (
    possessive_adjectives_l, possessive_adjectives_l_pt_br
)

from pronomes_possessivos.bdd_pronomes_possessivos import (
    possessive_pronouns_l, possessive_pronouns_l_pt_br
)

from pronomes_demonstrativos.bdd_pronomes_demonstrativos import (
    demonstrative_pronouns_l, demonstrative_pronouns_l_pt_br
)

from pronomes_reflexivos.bdd_pronomes_reflexivos import (
    reflexive_pronouns_l, reflexive_pronouns_l_pt_br
)

from preposicoes.bdd_preposicoes import (
    prepositions_l, prepositions_l_pt_br
)

from adverbios.bdd_adverbios import (
    adverbs_ly, adverbs_ly_pt_br,
    adverbs_frequency, adverbs_frequency_pt_br,
    adverb_others, adverb_others_pt_br
)

from conjuncoes.bdd_conjuncoes import (
    conjunctions_l, conjunctions_l_pt_br
)

from wh.bdd_wh import wh_l, wh_l_pt_br

from substantivos.bdd_substantivos import (
    nouns, nouns_pt_br
)

from verbos_be.bdd_verbos_be_simples import (be_past_l, be_past_l_pt_br)
from verbos_be.bdd_verbos_be_simples import (be_present_l, be_present_l_pt_br)
from verbos_be.bdd_verbos_be_simples import (be_future_l, be_future_l_pt_br)

from verbos_can.bdd_verbos_can import (could_past_l, could_past_l_pt_br, can_present_l, can_present_l_pt_br)

from verbos_do.bdd_verbos_do import (do_present_l, do_present_l_pt_br)
from verbos_do.bdd_verbos_do import (do_past_l, do_past_l_pt_br)

from verbos_have.bdd_verbos_have import (have_past_l, have_past_l_pt_br)
from verbos_have.bdd_verbos_have import (have_present_l, have_present_l_pt_br)
from verbos_have.bdd_verbos_have import (have_future_l, have_future_l_pt_br)

from verbos_infinitivo.bdd_verbos_infinitivo import (verbs_infinitive, verbs_infinitive_pt_br)
from verbos_passado.bdd_verbos_passado import (past, past_pt_br)
from verbos_presente.bdd_verbos_presente import (present, present_pt_br)
from verbos_futuro.bdd_verbos_futuro import (future, future_pt_br)

black, red, green, yellow, blue, purple, cyan, ink = inks[0], inks[1], inks[2], inks[3], inks[4], inks[5], inks[6], inks[7]

positive_score = 0
negative_score = 0

while True:

    try:

        pa, pa_inked, pa_tr, pa_tr_inked = _(possessive_adjectives_l, possessive_adjectives_l_pt_br)

        pr, pr_inked, pr_tr, pr_tr_inked = _(pronouns_l, pronouns_l_pt_br)
        dp, dp_inked, dp_tr, dp_tr_inked = _(demonstrative_pronouns_l, demonstrative_pronouns_l_pt_br)
        pp, pp_inked, pp_tr, pp_tr_inked = _(possessive_pronouns_l, possessive_pronouns_l_pt_br)
        rp, rp_inked, rp_tr, rp_tr_inked = _(reflexive_pronouns_l, reflexive_pronouns_l_pt_br)

        conj, conj_inked, conj_tr, conj_tr_inked = _(conjunctions_l, conjunctions_l_pt_br)
        conj2, conj2_inked, conj2_tr, conj2_tr_inked = _(conjunctions_l, conjunctions_l_pt_br)

        while conj == conj2:
            conj, conj_inked, conj_tr, conj_tr_inked = _(conjunctions_l, conjunctions_l_pt_br)
            conj2, conj2_inked, conj2_tr, conj2_tr_inked = _(conjunctions_l, conjunctions_l_pt_br)

        prep, prep_inked, prep_tr, prep_tr_inked = _(prepositions_l, prepositions_l_pt_br)

        wh, wh_inked, wh_tr, wh_tr_inked = _(wh_l, wh_l_pt_br)

        adj, adj_inked, adj_tr, adj_tr_inked = _(adjectives, adjectives_pt_br)
        adj2, adj2_inked, adj2_tr, adj2_tr_inked = _(adjectives, adjectives_pt_br)
        adj3, adj3_inked, adj3_tr, adj3_tr_inked = _(adjectives, adjectives_pt_br)

        while adj == adj2 or adj == adj3 or adj2 == adj3:
            adj, adj_inked, adj_tr, adj_tr_inked = _(adjectives, adjectives_pt_br)
            adj2, adj2_inked, adj2_tr, adj2_tr_inked = _(adjectives, adjectives_pt_br)
            adj3, adj3_inked, adj3_tr, adj3_tr_inked = _(adjectives, adjectives_pt_br)

        noun, noun_inked, noun_tr, noun_tr_inked = _(nouns, nouns_pt_br)
        noun2, noun2_inked, noun2_tr, noun2_tr_inked = _(nouns, nouns_pt_br)
        noun3, noun3_inked, noun3_tr, noun3_tr_inked = _(nouns, nouns_pt_br)

        while noun == noun2 or noun == noun3 or noun2 == noun3:
            noun, noun_inked, noun_tr, noun_tr_inked = _(nouns, nouns_pt_br)
            noun2, noun2_inked, noun2_tr, noun2_tr_inked = _(nouns, nouns_pt_br)
            noun3, noun3_inked, noun3_tr, noun3_tr_inked = _(nouns, nouns_pt_br)

        can, can_inked, can_tr, can_tr_inked = _(can_present_l, can_present_l_pt_br)
        could, could_inked, could_tr, could_tr_inked = _(could_past_l, could_past_l_pt_br)

        be_past, be_past_inked, be_past_tr, be_past_tr_inked = _(be_past_l, be_past_l_pt_br)
        be_present, be_present_inked, be_present_tr, be_present_tr_inked = _(be_present_l, be_present_l_pt_br)
        be_future, be_future_inked, be_future_tr, be_future_tr_inked = _(be_future_l, be_future_l_pt_br)

        do_past, do_past_inked, do_past_tr, do_past_tr_inked = _(do_past_l, do_past_l_pt_br)
        do_present, do_present_inked, do_present_tr, do_present_tr_inked = _(do_present_l, do_present_l_pt_br)

        have_past, have_past_inked, have_past_tr, have_past_tr_inked = _(have_past_l, have_past_l_pt_br)
        have_present, have_present_inked, have_present_tr, have_present_tr_inked = _(have_present_l, have_present_l_pt_br)
        have_future, have_future_inked, have_future_tr, have_future_tr_inked = _(have_future_l, have_future_l_pt_br)

        verb_inf, verb_inf_inked, verb_inf_tr, verb_inf_tr_inked = _(verbs_infinitive, verbs_infinitive_pt_br)
        verb_past, verb_past_inked, verb_past_tr, verb_past_tr_inked = _(past, past_pt_br)
        verb_present, verb_present_inked, verb_present_tr, verb_present_tr_inked = _(present, present_pt_br)
        verb_future, verb_future_inked, verb_future_tr, verb_future_tr_inked = _(future, future_pt_br)

        all_inked_elements = [
            pa_inked, pa_tr_inked,
            pr_inked, pr_tr_inked,
            dp_inked, dp_tr_inked,
            pp_inked, pp_tr_inked,
            rp_inked, rp_tr_inked,
            conj_inked, conj_tr_inked,
            conj2_inked, conj2_tr_inked,
            prep_inked, prep_tr_inked,
            wh_inked, wh_tr_inked,
            adj_inked, adj_tr_inked, adj2_inked, adj2_tr_inked, adj3_inked, adj3_tr_inked,
            noun_inked, noun_tr_inked, noun2_inked, noun2_tr_inked, noun3_inked, noun3_tr_inked,
            can_inked, can_tr_inked,
            could_inked, could_tr_inked,
            be_past_inked, be_past_tr_inked,
            be_present_inked, be_present_tr_inked,
            be_future_inked, be_future_tr_inked,
            do_past_inked, do_past_tr_inked,
            do_present_inked, do_present_tr_inked,
            have_past_inked, have_past_tr_inked,
            have_present_inked, have_present_tr_inked,
            have_future_inked, have_future_tr_inked,
            verb_inf_inked, verb_inf_tr_inked,
            verb_past_inked, verb_past_tr_inked,
            verb_present_inked, verb_present_tr_inked,
            verb_future_inked, verb_future_tr_inked,
        ]

        # adj_inked, adj_tr_inked, adj2_inked, adj2_tr_inked, adj3_inked, adj3_tr_inked,

        empty_set = set({})

        five_words = sorted(list(create_set(empty_set, 5, adjectives, True)))  # function create_set()
        five_indexes = [adjectives.index(word) for word in five_words]
        five_translations = [adjectives_pt_br[index] for index in five_indexes]

        chosen_word = choice(five_words)
        chosen_word_inked = painter('blue', chosen_word)
        chosen_word_index = five_words.index(chosen_word)
        chosen_word_translation = five_translations[chosen_word_index]
        the_target_translation = [chosen_word_translation]
        the_target_translation_inked = painter('yellow', the_target_translation[0])

        print(hello)

        answer = get_input_int(text=quiz_format.format(chosen_word_inked, *five_translations), start=1, limit=5)

        # One is correct, and it will return a number lesser than 10
        conditions = [
            # 1 if       'feliz'        in        ['triste']      else 10
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

            input(input_message)

            print(hints.format(chosen_word_inked, the_target_translation_inked, *all_inked_elements))

            sentence = input(input_message2)
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

            input(input_message)

            print(hints.format(chosen_word_inked, the_target_translation_inked, *all_inked_elements))

            sentence = input(input_message2)
            # sentence_translation = do_translation(sentence, 'pt')  # comentar, caso API falhe

            with open('frases.txt', 'a') as txt_file:
                txt_file.write(f"{sentence}\n")  # comentar, caso API falhe
                # txt_file.write(f"{sentence} -> {sentence_translation}\n")  # comentar, caso API falhe

    except IndexError as error:
        print(set_error)

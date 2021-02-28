

from bdd_strings.strings import *
from metodos.bdd import choose_word_paint_word as _, create_set, get_input_int, painter, throw_input, greetings
from whole_syntax import *

black, red, green, yellow, blue, purple, cyan, ink = inks[0], inks[1], inks[2], inks[3], inks[4], inks[5], inks[6], inks[7]

positive_score = 0
negative_score = 0

while True:

    try:

        pr, pr_inked, pr_tr, pr_tr_inked = _(pronouns_l, pronouns_l_pt_br)
        pr_frame = titles['pr'] + pr_inked + skip + pr_tr_inked

        dp, dp_inked, dp_tr, dp_tr_inked = _(demonstrative_pronouns_l, demonstrative_pronouns_l_pt_br)
        dp_frame = titles['dp'] + dp_inked + skip + dp_tr_inked

        pp, pp_inked, pp_tr, pp_tr_inked = _(possessive_pronouns_l, possessive_pronouns_l_pt_br)
        pp_frame = titles['pp'] + pp_inked + skip + pp_tr_inked

        rp, rp_inked, rp_tr, rp_tr_inked = _(reflexive_pronouns_l, reflexive_pronouns_l_pt_br)
        rp_frame = titles['rp'] + rp_inked + skip + rp_tr_inked

        pa, pa_inked, pa_tr, pa_tr_inked = _(possessive_adjectives_l, possessive_adjectives_l_pt_br)
        pa_frame = titles['pa'] + pa_inked + skip + pa_tr_inked

        adv, adv_inked, adv_tr, adv_tr_inked = _(adverb_others, adverb_others_pt_br)
        adv_frame = titles['adv'] + adv_inked + skip + adv_tr_inked

        adv_f, adv_f_inked, adv_f_tr, adv_f_tr_inked = _(adverbs_frequency, adverbs_frequency_pt_br)
        adv_f_frame = titles['adv_f'] + adv_f_inked + skip + adv_f_tr_inked

        adv_ly, adv_ly_inked, adv_ly_tr, adv_ly_tr_inked = _(adverbs_ly, adverbs_ly_pt_br)
        adv_ly_frame = titles['adv_ly'] + adv_ly_inked + skip + adv_ly_tr_inked

        conj, conj_inked, conj_tr, conj_tr_inked = _(conjunctions_l, conjunctions_l_pt_br)
        conj2, conj2_inked, conj2_tr, conj2_tr_inked = _(conjunctions_l, conjunctions_l_pt_br)
        conj_frame = titles['conj'] + f'{conj_inked} * {conj_tr_inked} -> {conj2_inked} * {conj2_tr_inked}'

        while conj == conj2:
            conj, conj_inked, conj_tr, conj_tr_inked = _(conjunctions_l, conjunctions_l_pt_br)
            conj2, conj2_inked, conj2_tr, conj2_tr_inked = _(conjunctions_l, conjunctions_l_pt_br)
            conj_frame = titles['conj'] + f'{conj_inked} * {conj_tr_inked} -> {conj2_inked} * {conj2_tr_inked}'

        prep, prep_inked, prep_tr, prep_tr_inked = _(prepositions_l, prepositions_l_pt_br)
        prep_frame = titles['prep'] + prep_inked + skip + prep_tr_inked

        wh, wh_inked, wh_tr, wh_tr_inked = _(wh_l, wh_l_pt_br)
        wh_frame = titles['wh'] + wh_inked + skip + wh_tr_inked

        # adj, adj_inked, adj_tr, adj_tr_inked = _(adjectives, adjectives_pt_br)
        # adj2, adj2_inked, adj2_tr, adj2_tr_inked = _(adjectives, adjectives_pt_br)
        # adj3, adj3_inked, adj3_tr, adj3_tr_inked = _(adjectives, adjectives_pt_br)
        # mandatory_adjectives = titles['adj'] + f'( {adj_inked} * {adj2_inked} * {adj3_inked} ) -> ( {adj_tr_inked} * {adj2_tr_inked} * {adj3_tr_inked} )'
        #
        # while adj == adj2 or adj == adj3 or adj2 == adj3:
        #     adj, adj_inked, adj_tr, adj_tr_inked = _(adjectives, adjectives_pt_br)
        #     adj2, adj2_inked, adj2_tr, adj2_tr_inked = _(adjectives, adjectives_pt_br)
        #     adj3, adj3_inked, adj3_tr, adj3_tr_inked = _(adjectives, adjectives_pt_br)
        #     mandatory_adjectives = titles['adj'] + f'( {adj_inked} * {adj2_inked} * {adj3_inked} ) -> ( {adj_tr_inked} * {adj2_tr_inked} * {adj3_tr_inked} )'

        noun, noun_inked, noun_tr, noun_tr_inked = _(nouns, nouns_pt_br)
        noun2, noun2_inked, noun2_tr, noun2_tr_inked = _(nouns, nouns_pt_br)
        noun3, noun3_inked, noun3_tr, noun3_tr_inked = _(nouns, nouns_pt_br)
        mandatory_nouns = titles['noun'] + f'{noun_inked} * {noun_tr_inked} -> {noun2_inked} * {noun2_tr_inked} -> {noun3_inked} * {noun3_tr_inked}'

        while noun == noun2 or noun == noun3 or noun2 == noun3:
            noun, noun_inked, noun_tr, noun_tr_inked = _(nouns, nouns_pt_br)
            noun2, noun2_inked, noun2_tr, noun2_tr_inked = _(nouns, nouns_pt_br)
            noun3, noun3_inked, noun3_tr, noun3_tr_inked = _(nouns, nouns_pt_br)
            mandatory_nouns = titles['noun'] + f'{noun_inked} * {noun_tr_inked} -> {noun2_inked} * {noun2_tr_inked} -> {noun3_inked} * {noun3_tr_inked}'

        can, can_inked, can_tr, can_tr_inked = _(can_present_l, can_present_l_pt_br)
        can_frame = titles['can'] + can_inked + skip + can_tr_inked

        could, could_inked, could_tr, could_tr_inked = _(could_past_l, could_past_l_pt_br)
        could_frame = titles['could'] + could_inked + skip + could_tr_inked

        be_past, be_past_inked, be_past_tr, be_past_tr_inked = _(be_past_l, be_past_l_pt_br)
        be_past_frame = titles['to_be_past'] + be_past_inked + skip + be_past_tr_inked

        be_present, be_present_inked, be_present_tr, be_present_tr_inked = _(be_present_l, be_present_l_pt_br)
        be_present_frame = titles['to_be_pst'] + be_present_inked + skip + be_present_tr_inked

        be_future, be_future_inked, be_future_tr, be_future_tr_inked = _(be_future_l, be_future_l_pt_br)
        be_future_frame = titles['to_be_fut'] + be_future_inked + skip + be_future_tr_inked

        do_past, do_past_inked, do_past_tr, do_past_tr_inked = _(do_past_l, do_past_l_pt_br)
        do_past_frame = titles['to_do_past'] + do_past_inked + skip + do_past_tr_inked

        do_present, do_present_inked, do_present_tr, do_present_tr_inked = _(do_present_l, do_present_l_pt_br)
        do_present_frame = titles['to_do_pst'] + do_present_inked + skip + do_present_tr_inked

        have_past, have_past_inked, have_past_tr, have_past_tr_inked = _(have_past_l, have_past_l_pt_br)
        have_past_frame = titles['to_have_past'] + have_past_inked + skip + have_past_tr_inked

        have_present, have_present_inked, have_present_tr, have_present_tr_inked = _(have_present_l, have_present_l_pt_br)
        have_present_frame = titles['to_have_pst'] + have_present_inked + skip + have_present_tr_inked

        have_future, have_future_inked, have_future_tr, have_future_tr_inked = _(have_future_l, have_future_l_pt_br)
        have_future_frame = titles['to_have_fut'] + have_future_inked + skip + have_future_tr_inked

        verb_inf, verb_inf_inked, verb_inf_tr, verb_inf_tr_inked = _(verbs_infinitive, verbs_infinitive_pt_br)
        chosen_verb_infinitive = titles['verb_inf'] + verb_inf_inked + skip + verb_inf_tr_inked

        verb_past, verb_past_inked, verb_past_tr, verb_past_tr_inked = _(past, past_pt_br)
        chosen_verb_past = titles['verb_past'] + verb_past_inked + skip + verb_past_tr_inked

        verb_present, verb_present_inked, verb_present_tr, verb_present_tr_inked = _(present, present_pt_br)
        chosen_verb_present = titles['verb_pst'] + verb_present_inked + skip + verb_present_tr_inked

        verb_future, verb_future_inked, verb_future_tr, verb_future_tr_inked = _(future, future_pt_br)
        chosen_verb_future = titles['verb_fut'] + verb_future_inked + skip + verb_future_tr_inked

        all_inked_elements = []

        inked_elements_first_group = [pr_frame, dp_frame, pp_frame, rp_frame]

        inked_elements_second_group = [pa_frame, adv_frame, adv_f_frame, adv_ly_frame, conj_frame, prep_frame, wh_frame]

        inked_elements_third_group = [
            can_frame, could_frame, be_past_frame, be_present_frame, be_future_frame, do_past_frame, do_present_frame,
            have_past_frame, have_present_frame, have_future_frame
        ]

        box = [mandatory_nouns, chosen_verb_infinitive, chosen_verb_past, chosen_verb_present, chosen_verb_future]
        box = set(box)
        while len(box) < 7:
            box.add(choice(inked_elements_first_group))
        while len(box) < 9:
            box.add(choice(inked_elements_second_group))
        while len(box) < 10:
            box.add(choice(inked_elements_third_group))
        box = sorted(list(box), key=len)
        print(box)
        # box_elements = sorted(list(create_set(box, 10, all_inked_elements, True)), key=len)

        empty_set = set({})

        five_words = list(create_set(empty_set, 5, adjectives, True))  # function create_set()
        five_indexes = [adjectives.index(word) for word in five_words]
        five_translations = [adjectives_pt_br[index] for index in five_indexes]

        chosen_word = choice(five_words)
        chosen_word_inked = painter('blue', chosen_word)
        chosen_word_index = five_words.index(chosen_word)
        chosen_word_translation = five_translations[chosen_word_index]
        the_target_translation = [chosen_word_translation]
        the_target_translation_inked = painter('yellow', the_target_translation[0])


        def display_variables():
            """"""
            print(f"{five_words = }")
            print(f"{five_indexes = }")
            print(f"{five_translations = }")
            print(f"{chosen_word = }")
            print(f"{chosen_word_inked = }")
            print(f"{chosen_word_index = }")
            print(f"{chosen_word_translation = }")
            print(f"{the_target_translation = }")
            print(f"{the_target_translation_inked = }")
            # print(pick_five_inked_elements)
            # for word in all_inked_elements:
            #     print(word)

        # display_variables()

        print(hello := greetings('treino de adjetivos', index1=3))

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

            print(success.format(blue, ink, green, ink, positive_score + negative_score, yellow, ink, blue, ink,
                                 positive_score, negative_score, red, ink))

            input(press_enter)

            vocabulary = throw_input(write_vocabulary)

            while vocabulary != chosen_word:
                print(typo.format(red, ink, blue, chosen_word, ink, red, ink))
                vocabulary = throw_input(write_vocabulary)

            print(announcement.format(chosen_word_inked, the_target_translation_inked))

            for word in box:
                print(four_spaces + word)

            print('\n')

            sentence = input(type_your_sentence)
            # sentence_translation = do_translation(sentence, 'pt')  # comentar, caso API falhe

            with open('frases.txt', 'a') as txt_file:
                txt_file.write(f"{sentence}\n")  # comentar, caso API falhe
                # txt_file.write(f"{sentence} -> {sentence_translation}\n")  # comentar, caso API falhe

        else:
            negative_score += 1

            print(failure.format(red, ink, blue, ink, correct_answer_index, the_target_translation[0], green, ink,
                                 positive_score + negative_score, yellow, ink, blue, ink, positive_score,
                                 negative_score, red, ink))

            input(press_enter)

            vocabulary = throw_input(write_vocabulary)

            while vocabulary != chosen_word:
                print(typo.format(red, ink, blue, chosen_word, ink, red, ink))
                vocabulary = throw_input(write_vocabulary)

            print(announcement.format(chosen_word_inked, the_target_translation_inked))

            for word in box:
                print(four_spaces + word)

            print('\n')

            sentence = input(type_your_sentence)
            # sentence_translation = do_translation(sentence, 'pt')  # comentar, caso API falhe

            with open('frases.txt', 'a') as txt_file:
                txt_file.write(f"{sentence}\n")  # comentar, caso API falhe
                # txt_file.write(f"{sentence} -> {sentence_translation}\n")  # comentar, caso API falhe

    except IndexError as error:
        print(set_error)

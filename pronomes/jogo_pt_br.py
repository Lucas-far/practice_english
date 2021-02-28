

from bdd_strings.strings import *
from metodos.bdd import choose_word_paint_word as _, create_set, get_input_int, painter, throw_input, greetings
from whole_syntax import *

black, red, green, yellow, blue, purple, cyan, ink = inks[0], inks[1], inks[2], inks[3], inks[4], inks[5], inks[6], inks[7]

positive_score = 0
negative_score = 0

while True:

    try:

        empty_set = set({})

        five_words = list(create_set(empty_set, 5, pronouns_to_be_simple_pt_br, True))
        five_indexes = [pronouns_to_be_simple_pt_br.index(word) for word in five_words]
        five_translations = [pronouns_to_be_simple[index] for index in five_indexes]

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

        print(hello := greetings('treino de pronomes com verbo to be', index1=3))

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

            vocabulary = throw_input(write_vocabulary_type2)

            while vocabulary != the_target_translation[0]:
                print(typo.format(red, ink, blue, the_target_translation[0], ink, red, ink))
                vocabulary = throw_input(write_vocabulary)

        else:
            negative_score += 1

            print(failure.format(red, ink, blue, ink, correct_answer_index, the_target_translation[0], green, ink,
                                 positive_score + negative_score, yellow, ink, blue, ink, positive_score,
                                 negative_score, red, ink))

            input(press_enter)

            vocabulary = throw_input(write_vocabulary_type2)

            while vocabulary != the_target_translation[0]:
                print(typo.format(red, ink, blue, the_target_translation[0], ink, red, ink))
                vocabulary = throw_input(write_vocabulary)

    except IndexError as error:
        print(set_error)



from gramatica.verbos.verbos_infinitivo import verbs_inf_dict, verbs_inf_dict_keys
from metodos.banco_de_dados import *
from random import choice, shuffle
from cores import colors

# TOOLS
red, purple, yellow, blue, paint = colors[1], colors[2], colors[3], colors[4], colors[7]
break_row = '\n'
indent = '    '
bricks = '=' * 20
report_model = '==================== RELATÓRIO ===================='
splitter = '=' * len(report_model)
controller = f'{break_row}{indent}{indent}Aperte ENTER ou qualquer outra tecla para continuar...'

# VARIABLES TO DETERMINE THE PLAYER'S EFFICACY
positive_score = 0
negative_score = 0


while True:

    box_words = []
    box_words_translations = []
    box_target_translation = []

    ""  # verb_inf_chosen_key = 'to continue'
    verb_inf_chosen_key = choice(verbs_inf_dict_keys)
    # print(f'{verb_inf_chosen_key = }')

    ""  # verb_inf_chosen_values = ('to continue', 'continuar')
    verb_inf_chosen_values = verbs_inf_dict[verb_inf_chosen_key]
    # print(f'{verb_inf_chosen_values = }')

    ""  # verb_inf_chosen = 'to continue'
    verb_inf_chosen = verb_inf_chosen_values[0]
    # print(f'{verb_inf_chosen = }')

    ""  # verb_inf_chosen_meaning = 'continuar'
    verb_inf_chosen_meaning = verb_inf_chosen_values[1]
    # print(f'{verb_inf_chosen_meaning = }')

    ""  # box_words = ['to continue']
    box_words.append(verb_inf_chosen)
    # print(f'{box_words = }')

    ""  # box_target_translation = ['continuar']
    box_target_translation.append(verb_inf_chosen_meaning)
    # print(f'{box_target_translation = }')


    def create_adjectives():
        """"""
        while len(box_words) < 5:

            new_adjective_key = choice(verbs_inf_dict_keys)
            # print(f'{new_adjective_key = }')
            new_adjective_values = verbs_inf_dict[new_adjective_key]
            # print(f'{new_adjective_values = }')
            new_adjective_chosen = new_adjective_values[0]
            # print(f'{new_adjective_chosen = }')
            new_adjective_meaning = new_adjective_values[1]
            # print(f'{new_adjective_meaning = }')

            box_words.append(new_adjective_chosen)
            box_words_translations.append(new_adjective_meaning)

    create_adjectives()

    def scan_for_repeated_adjectives():
        """"""
        check_repeated_data = []

        for word in box_words:
            check_repeated_data.append(box_words.count(word))

        for data in check_repeated_data:
            if data != 1:
                box_words.clear()
                box_words_translations.clear()
                box_words.append(verb_inf_chosen)
                # box_words_translations.append(noun_chosen_meaning)
                create_adjectives()

    scan_for_repeated_adjectives()

    box_words_translations.append(verb_inf_chosen_meaning)

    shuffle(box_words_translations)

    ""  # box_words = ['to continue', 'to happen', 'to suggest', 'to try', 'to see']
    # print(f'{box_words = }')

    ""  # box_words_translations = ['sugerir', 'experimentar/tentar', 'ver', 'continuar', 'acontecer/ocorrer']
    # print(f'{box_words_translations = }')

    greetings = welcome('treino de verbos no infinitivo', prefix=3, prefix2=7)

    print(indent, greetings)

    answer = get_input_int(
        text=f"""
        {bricks}
        O QUE É {yellow}{verb_inf_chosen}{paint} ?
        {bricks}
        1 - {box_words_translations[0]}
        2 - {box_words_translations[1]}
        3 - {box_words_translations[2]}
        4 - {box_words_translations[3]}
        5 - {box_words_translations[4]}

        Digite de 1 a 5, para fornecer sua resposta
        Digite após a seta -> """,
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

    success = f"""
        {report_model}
        {blue}Resposta correta{paint}"""

    failure = f"""
        {report_model}
        {red}Resposta incorreta{paint}
        {blue}Resposta correta:{paint} {box_target_translation[0]}"""

    games_played = "        \033[1:32mJogos jogados:\033[m {}"

    score_table = "        \033[1:33mPlacar:\033[m \033[1:34mAcertos\033[m {} x {} \033[1:31mErros\033[m"

    if answer == correct_answer_index:
        positive_score += 1
        print(success)
        print(games_played.format(positive_score + negative_score))
        print(score_table.format(positive_score, negative_score))
        print(indent + indent + splitter)
    else:
        negative_score += 1
        print(failure)
        print(games_played.format(positive_score + negative_score))
        print(score_table.format(positive_score, negative_score))
        print(indent + indent + splitter)

    input(controller)

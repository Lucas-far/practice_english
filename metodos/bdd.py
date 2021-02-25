

# from gramatica.verbos.infinitivo import verbs_inf_keys
# from gramatica.verbos.passado import past_keys
# from gramatica.verbos.presente import pst_keys
# from gramatica.verbos.futuro import fut_keys


from time import sleep
from random import choice, randint

# from artigos.bdd_artigos import the_u, the_l
# from pronomes.bdd_pronomes import pro_pl_u
# from verbos_have.bdd_have import the_have_l
# from substantivos.bdd_substantivos import nouns_sgl, nouns_pl
# from verbos_be.bdd_presente import is_l, is_u

def check_length(*args):
    """"""
    box = []
    for index in args:
        box.append(len(index))
    return box


def create_set(set_var: set, data_length: int, extraction_from: list, extract_from=False):
    """"""
    while len(set_var) < data_length:
        set_var.add(choice(extraction_from))
    return set_var


def do_translation(text, target_language):
    """"""
    from textblob import TextBlob
    sentence_translated = TextBlob(text).translate(to=target_language)
    return sentence_translated


def get_input_int(the_input: int = 1, text: str = 'Write an integer -> ', start: int = 1, limit: int = 9999) -> int:
    """
    To treat improper data while a proper integer number is not being provided.
    :param the_input:
    :param text:
    :param start:
    :param limit:
    :return: int
    """

    pallet: tuple = (
        '\033[1:30m', '\033[1:31m', '\033[1:32m', '\033[1:33m', '\033[1:34m', '\033[1:35m', '\033[1:36m', '\033[m'
    )

    red, cyan, ink = pallet[1], pallet[6], pallet[7]
    warning = '\n{}Aperte ENTER ou qualquer outra tecla para continuar...{}'

    integer_out_of_range = """
        {}==================== ERRO ===================={}
        As opções são números entre {} até {} :)
        """

    integer_unused = """
        {}==================== ERRO ===================={}
        Você não está usando números. Use números entre {} até {} :)
        """

    while the_input <= start or the_input > limit:
        try:
            the_input = int(input(text))
            if the_input in range(start, limit + 1):
                break
            else:
                print(integer_out_of_range.format(red, ink, start, limit))
                input(warning.format(cyan, ink))
                sleep(1)
        except ValueError:
            print(integer_unused.format(red, ink, start, limit))
            input(warning.format(cyan, ink))
            sleep(1)

    return the_input


def greetings(algorithm_name: str = 'Name of the algorithm', index1: int = 0, index2: int = 7) -> str:
    """
    To receive a string and return it as the name of the algorithm

    :param algorithm_name:
    :param index1: goes from 0 to 6, and combine with prefix2, frozen as 7. EX: prefix = 0 & prefix2 = 7 = black
    :param index2: must always be 7, if it is desired colors to work
    :return: str
    """

    inks: tuple = (
        '\033[1:30m', '\033[1:31m', '\033[1:32m', '\033[1:33m', '\033[1:34m', '\033[1:35m', '\033[1:36m', '\033[m'
    )

    the_message = f"""
    ==================================================
    Bem-vindo ao {inks[index1]}{algorithm_name.upper()}{inks[index2]}
    ==================================================
    """

    return the_message


def painter(color: str = 'blue', text: str = 'texto'):
    """"""
    # keys = conditions / values = actions of the conditions
    colors = {
        'black': '\033[1:30m' + text + '\033[m', 'red': '\033[1:31m' + text + '\033[m',
        'green': '\033[1:32m' + text + '\033[m', 'yellow': '\033[1:33m' + text + '\033[m',
        'blue': '\033[1:34m' + text + '\033[m', 'purple': '\033[1:35m' + text + '\033[m',
        'cyan': '\033[1:36m' + text + '\033[m'
    }

    for key in colors:
        if color == key:
            return colors[key]


def var_printer(list_var_names: str, list_var_values: list):  # parameters as str are, for me, more maintainable
    """"""
    box = []
    names = list_var_names.split()
    counter = 0

    while counter < len(names):
        box.append(f"{names[counter]} = {list_var_values[counter]}")
        counter += 1

    return box


def word_selector(*args):  # removed parameter: example
    """"""
    sentence = []

    for word in args:
        sentence.append(choice(word))
        # print(f'{colors[4]}{choice(word)}{colors[7]}', end='')
    return "".join(sentence)


def data_collector(database):  # removed parameter: example
    """"""
    the_data = choice(database)
    return the_data


def data_collector_(args):  # removed parameter: example
    """"""
    all_data = []
    for database in args:
        all_data.append(choice(database))
    return all_data


def verify(*args, database: list):
    """"""
    print('\n')
    label_found = '=' * 35 + ' ' + 'ENCONTRADOS' + ' ' + '=' * 35
    label_not_found = '=' * 35 + ' ' + 'AUSENTES' + ' ' + '=' * 35
    label_indexes = '=' * 35 + ' ' + 'ÍNDICE DOS DADOS ENCONTRADOS' + ' ' + '=' * 35
    list_found = []
    list_not_found = []
    list_of_indexes = []

    for word in args:
        if word in database:
            word_index = database.index(word)
            list_of_indexes.append(word_index)
            list_found.append(f'\033[1:34m{word}\033[m')
            # print(f'Índice {word_index} -> \033[1:34m{word}\033[m')
        else:
            list_not_found.append(f'\033[1:31m{word}\033[m')
            # print(f'Ausente -> \033[1:31m{word}\033[m')

    print(label_found)
    for id_, word in enumerate(list_found):
        id_ = id_ + 1
        if not id_ % 11:
            print('\n')
            print(id_, word, end=' ')
        else:
            print(id_, word, end=' ')
    print('\n')

    print(label_not_found)
    for id_, word in enumerate(list_not_found):
        id_ = id_ + 1
        if not id_ % 11:
            print('\n')
            print(id_, word, end=' ')
        else:
            print(id_, word, end=' ')
    print('\n')

    print(label_indexes)
    return list_of_indexes


def welcome(algorithm_name: str = 'Name of the algorithm', prefix: int = 0, prefix2: int = 7) -> str:
    """
    To receive a string and return it as the name of the algorithm

    :param algorithm_name:
    :param prefix: goes from 0 to 6, and combine with prefix2, frozen as 7. EX: prefix = 0 & prefix2 = 7 = black
    :param prefix2: must always be 7, if it is desired colors to work
    :return: str
    """

    bricks = '=' * 50

    pallet: tuple = (
        '\033[1:30m', '\033[1:31m', '\033[1:32m', '\033[1:33m', '\033[1:34m', '\033[1:35m', '\033[1:36m', '\033[m'
    )

    return f"""
    {bricks}
    Bem-vindo ao {pallet[prefix]}{algorithm_name.upper()}{pallet[prefix2]}
    {bricks}"""


def choose_word_paint_word(word_location, word_translation_location):
    """"""
    word = choice(word_location)
    word_inked = painter('green', word)
    word_translation = word_translation_location[word_location.index(word)]
    word_translation_inked = painter('blue', word_translation)

    return word, word_inked, word_translation, word_translation_inked


def throw_input(input_text):
    """"""
    the_input = input(input_text)
    return the_input


if __name__ == '__main__':
    x = '  '

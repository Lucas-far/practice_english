

# from gramatica.verbos.infinitivo import verbs_inf_keys
# from gramatica.verbos.passado import past_keys
# from gramatica.verbos.presente import pst_keys
# from gramatica.verbos.futuro import fut_keys


from time import sleep
from random import choice, randint

from artigos.bdd_artigos import the_u, the_l
from pronomes.bdd_pronomes import pro_pl_u
from verbos_have.bdd_have import the_have_l
from substantivos.bdd_substantivos import nouns_sgl, nouns_pl
from verbos_be.bdd_presente import is_l, is_u

def check_length(*args):
    """"""
    box = []
    for index in args:
        box.append(len(index))
    return box


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


def sentence_maker(*args):  # removed parameter: example
    """"""
    sentence = []

    for word in args:
        sentence.append(choice(word))
        # print(f'{colors[4]}{choice(word)}{colors[7]}', end='')
    return "".join(sentence)


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


if __name__ == '__main__':
    x = '  '
    # print(sentence3 := sentence_maker(pro_pl_u, x, the_have_l, x, ['bad'], x, nouns_pl))
    print(sentence3 := sentence_maker(pro_pl_u, x, the_have_l, x, ['bad'], x, nouns_pl))

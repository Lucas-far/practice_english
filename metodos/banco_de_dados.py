

from gramatica.verbos.infinitivo import verbs_inf_keys
from gramatica.verbos.passado import past_keys
from gramatica.verbos.presente import pst_keys
from gramatica.verbos.futuro import fut_keys


def check_length(*args):
    """"""
    box = []
    for index in args:
        box.append(len(index))
    return box


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


if __name__ == '__main__':
    verify('to know', 'to think', 'to determine', 'to resolve', database=verbs_inf_keys)
    verify('to know', 'to think', 'to determine', 'to resolve', database=past_keys)
    verify('to know', 'to think', 'to determine', 'to resolve', database=pst_keys)
    verify('to know', 'to think', 'to determine', 'to resolve', database=fut_keys)
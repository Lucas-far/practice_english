

from metodos.bdd import data_collector as _, painter

pronouns_to_be_simple = [
    "I", "I was", "I am", "I will be", "I was not", "I am not", "I will not be", "I wasn't", "I won't be",
    "You", "You were", "You are", "You will be", "You were not", "You are not", "You will not be", "You weren't", "You aren't", "You won't be",
    "He", "He was", "He is", "He will be", "He was not", "He is not", "He will not be", "He wasn't", "He isn't", "He won't be",
    "She", "She was", "She is", "She will be", "She was not", "She is not", "She will not be", "She wasn't", "She isn't", "She won't be",
    "It", "It was", "It is", "It will be", "It was not", "It is not", "It will not be", "It wasn't", "It isn't", "It won't be",
    "We", "We were", "We are", "We will be", "We were not", "We are not", "We will not be", "We weren't", "We aren't", "We won't be",
    "You", "You were", "You are", "You will be", "You were not", "You are not", "You will not be", "You weren't", "You aren't", "You won't be",
    "They", "They were", "They are", "They will be", "They were not", "They are not", "They will not be", "They weren't", "They aren't", "They won't be",
]

pronouns_to_be_simple_pt_br = [
    'Eu', 'Eu fui/era/estava', 'Eu sou/estou', 'Eu serei/estarei', 'Eu não fui/era/estava', 'Eu não sou/estou', 'Eu não serei/estarei', 'Eu não fui/era/estava (abreviado)', 'Eu não serei/estarei (abreviado)',
    'Você', 'Você foi/era/estava', 'Você é/está', 'Você será/estará', 'Você não foi/era/estava', 'Você não é/está', 'Você não será/estará', 'Você não foi/era/estava (abreviado)', 'Você não é/está (abreviado)', 'Você não será/estará (abreviado)',
    'Ele', 'Ele foi/era/estava', 'Ele é/está', 'Ele será/estará', 'Ele não foi/era/estava', 'Ele não é/está', 'Ele não será/estará', 'Ele não foi/era/estava (abreviado)', 'Ele não é/está (abreviado)', 'Ele não será/estará (abreviado)',
    'Ela', 'Ela foi/era/estava', 'Ela é/está', 'Ela será/estará', 'Ela não foi/era/estava', 'Ela não é/está', 'Ela não será/estará', 'Ela não foi/era/estava (abreviado)',  'Ela não é/está (abreviado)', 'Ela não será/estará (abreviado)',
    'Isso', 'Isso foi/era/estava', 'Isso é/está', 'Isso será/estará', 'Isso não foi/era/estava', 'Isso não é/está', 'Isso não será/estará', 'Isso não foi/era/estava (abreviado)', 'Isso não é/está (abreviado)', 'Isso não será/estará (abreviado)',
    'Nós', 'Nós fomos/eramos/estavamos', 'Nós somos/estamos', 'Nós seremos/estaremos', 'Nós não fomos/eramos/estavamos', 'Nós não somos/estamos', 'Nós não seremos/estaremos', 'Nós não fomos/eramos/estavamos (abreviado)', 'Nós não somos/estamos (abreviado)', 'Nós não seremos/estaremos (abreviado)',
    'Vocês', 'Vocês foram/eram/estavam', 'Vocês são/estão', 'Vocês serão/estarão', 'Vocês não foram/eram/estavam', 'Vocês não são/estão', 'Vocês não serão/estarão', 'Vocês não foram/eram/estavam (abreviado)', 'Vocês não são/estão (abreviado)', 'Vocês não serão/estarão (abreviado)',
    'Eles(as)', 'Eles(as) foram/eram/estavam', 'Eles(as) são/estão', 'Eles(as) serão/estarão', 'Eles(as) não foram/eram/estavam', 'Eles(as) não são/estão', 'Eles(as) não serão/estarão', 'Eles(as) não foram/eram/estavam (abreviado)', 'Eles(as) não são/estão (abreviado)', 'Eles(as) não serão/estarão (abreviado)'
]

pronouns = [
    'I', 'you', 'he', 'she', 'it', 'we', 'you', 'they',
    'I', 'You', 'He', 'She', 'It', 'We', 'You', 'They',
]

pronouns_u = ['I', 'You', 'He', 'She', 'It', 'We', 'You', 'They']

pronouns_u_pt_br = ['Eu', 'Você', 'Ele', 'Ela', 'Isso', 'Nós', 'Vocês', 'Eles(as)']

pronouns_l = ['I', 'you', 'he', 'she', 'it', 'we', 'you', 'they']

pronouns_l_pt_br = ['eu', 'você', 'ele', 'ela', 'isso', 'nós', 'vocês', 'eles(as)']

pronouns_sgl_u = ['I', 'He', 'She', 'It']

pronouns_sgl_l = ['I', 'he', 'she', 'it']

pronouns_sgl_is_u = ['He', 'She', 'It']

he_she_it_l = ['he', 'she', 'it']

pronouns_pl_u = ['We', 'You', 'They']

pronouns_pl_l = ['we', 'you', 'they']

pronouns_pl_others_u = ['I', 'We', 'You', 'They']

pronouns_pl_others_l = ['I', 'we', 'you', 'they']

i_u, you_u, he_u, she_u, it_u, we_u, they_u = \
    ['I'], ['You'], ['He'], ['She'], ['It'], ['We'], ['They']

i_l, you_l, he_l, she_l, it_l, we_l, they_l = \
    ['I'], ['you'], ['he'], ['she'], ['it'], ['we'], ['they']

I_ = ['I', 'eu']
you_ = ['you', 'tu/você']
he_ = ['he', 'ele']
she_ = ['she', 'ela']
it_ = ['it', 'isso']
we_ = ['we', 'nós']
you__ = ['you', 'vós/vocês']
they_ = ['they', 'eles(as)']

# pronoun = _(pronouns_l)
# pronoun_inked = painter('blue', pronoun)
# pronoun_tr = pronouns_l_pt_br[pronouns_l.index(pronoun)]
# pronoun_tr_inked = painter('red', pronoun_tr)


if __name__ == '__main__':
    print('\n')
    for words in zip(pronouns_to_be_simple, pronouns_to_be_simple_pt_br):
        print(words)
    # print(pronoun)
    # print(pronoun_inked)
    # print(pronoun_tr)
    # print(pronoun_tr_inked)

    # bricks = '=' * 100
    #
    # print('\n')
    #
    # print(bricks)
    # print(f'{len(pro_l) = }')
    # print(f'{len(pro_pt_br) = }')
    #
    # print('\n')
    # for word in zip(pro_l, pro_pt_br):
    #     print(word)

    # counter = 0
    # while counter < len(pro_l):
    #     print(f"{pro_l[counter]}_ = ['{pro_l[counter]}', '{pro_pt_br[counter]}']")
    #     counter += 1

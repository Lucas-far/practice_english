

""""""

from metodos.bdd import data_collector as _, painter

"------------------------------------------------------ PRINCIPAL -----------------------------------------------------"
possessive_adjectives_l = ['my', 'your', 'his', 'her', 'its', 'our', 'your', 'their']

possessive_adjectives_l_pt_br = [
    'meu(s) / minha(s)', 'seu / sua', 'dele', 'dela', 'desse / disso', 'nosso(s) / nossa(s)', 'seus / suas',
    'deles / delas / desses'
]

"-------------------------------------------------------- JOGO --------------------------------------------------------"
easy = ['my', 'your', 'his', 'her', 'its', 'our', 'their']

average = [
    'My', 'Your', 'His', 'Her', 'Its', 'Our', 'Their',
    'my', 'your', 'his', 'her', 'its', 'our', 'their'
]
"-------------------------------------------------------- VARS --------------------------------------------------------"
possessive_adjectives = [
    'My', 'Your', 'His', 'Her', 'Its', 'Our', 'Your', 'Their',
    'my', 'your', 'his', 'her', 'its', 'our', 'your', 'their'
]

possessive_adjectives_pt_br = [
    'Meu(s) / Minha(s)', 'Seu / Sua', 'Dele', 'Dela', 'Desse / Disso', 'Nosso(s) / Nossa(s)', 'Seus / Suas',
    'Deles / Delas / Desses',

    'meu(s) / minha(s)', 'seu / sua', 'dele', 'dela', 'desse / disso', 'nosso(s) / nossa(s)', 'seus / suas',
    'deles / delas / desses'
]

# adjectives_possessive_upper = [index.replace(index[0], index[0].upper()) for index in adjectives_possessive_lower]
possessive_adjectives_u = ['My', 'Your', 'His', 'Her', 'Its', 'Our', 'Your', 'Their']

my_ = ['my', 'meu(s) / minha(s)']
your_ = ['your', 'seu / sua']
his_ = ['his', 'dele(s)']
her_ = ['her', 'dela(s)']
its_ = ['its', 'dele(s) / dela(s)']
our_ = ['our', 'nosso(s) / nossa(s)s']
your__ = ['your', 'seu(s) / sua(s)']
their_ = ['their', 'dele(s) / dela(s)']

# possessive_adjective = _(possessive_adjectives_l)
# possessive_adjective_inked = painter('blue', possessive_adjective)
# possessive_adjective_tr = possessive_adjectives_l_pt_br[possessive_adjectives_l.index(possessive_adjective)]
# possessive_adjective_tr_inked = painter('red', possessive_adjective_tr)

if __name__ == '__main__':
    print('\n')
    # print(possessive_adjective)
    # print(possessive_adjective_inked)
    # print(possessive_adjective_tr)
    # print(possessive_adjective_tr_inked)

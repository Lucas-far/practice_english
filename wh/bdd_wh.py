

from random import choice
from metodos.bdd import painter

wh_gl = [
    'How', 'What', 'When', 'Where', 'Which', 'Who', 'Whose', 'Why',
    'how', 'what', 'when', 'where', 'which', 'who', 'whose', 'why'
]

wh_all_u = ['How', 'What', 'When', 'Where', 'Which', 'Who', 'Whose', 'Why']

# PRINCIPAL
"----------------------------------------------------------------------------------------------------------------------"
wh_l = ['how', 'what', 'when', 'where', 'which', 'who', 'whose', 'why']

wh_l_pt_br = [
    'como / quão / quanto', 'o quê / qual(is)', 'quando', 'onde', 'que', 'que / quem (humano)', 'de quem',
    'porque', 'porquê'
]
"----------------------------------------------------------------------------------------------------------------------"

wh_specific_u = ['How', 'Where', 'Who']
wh_specific_l = ['how', 'where', 'who']

# set_box = set({})
#
# while len(set_box) < 1:
#     set_box.add(choice(wh_l))
#
# set_box = list(set_box)
#
# wh = set_box[0]
# wh_inked = painter('blue', wh)
# wh_tr = wh_l_pt_br[wh_l.index(wh)]
# wh_tr_inked = painter('red', wh_tr)

if __name__ == '__main__':
    for word in zip(wh_l, wh_l_pt_br):
        print(word)

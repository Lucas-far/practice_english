

from random import choice
from metodos.bdd import painter

do = [
    "does", "does not", "doesn't",
    "Does", "Does not", "Doesn't",
    "do", "do not", "don't",
    "Do", "Do not", "Don't"
]

do_u = ["Does", "Does not", "Doesn't", "Do", "Do not", "Don't"]

do_present_l = ["does", "does not", "doesn't", "do", "do not", "don't"]
do_present_l_pt_br = ['ênfase para verbo no presente', 'não', 'não', 'ênfase para verbo no presente', 'não', 'não']

does_l = ["does"]
does_not_l = ["does not"]
does_not_short_l = ["doesn't"]

does_u = ["Does"]
does_not_u = ["Does not"]
does_not_short_u = ["Doesn't"]

the_do_l = ["do"]
do_not_l = ["do not"]
do_not_short_l = ["don't"]

the_do_u = ["Do"]
do_not_u = ["Do not"]
do_not_short_u = ["Don't"]


"------------------------------------------------ VERBO DO NO PASSADO -------------------------------------------------"
do_past_l = ["did", "did not", "didn't"]
do_past_l_pt_br = ['ênfase para verbo no passado', 'não', 'não']

did_l = ["does"]
did_not_l = ["does not"]
did_not_short_l = ["doesn't"]

"------------------------------------------------- VERBO DO NO FUTURO -------------------------------------------------"
do_future_l = ["will do", "will not do", "won't do"]
do_future_l_pt_br = ['farei', 'não farei', 'não farei']

will_do_l = ["will do"]
will_not_do_l = ["does not"]
will_not_do_short_l = ["doesn't"]

"----------------------------------------------------------------------------------------------------------------------"
set_box_past = set({})

while len(set_box_past) < 1:
    set_box_past.add(choice(do_past_l))

set_box_past = list(set_box_past)

do_past = set_box_past[0]
do_past_inked = painter('blue', do_past)
do_past_tr = do_past_l_pt_br[do_past_l.index(do_past)]
do_past_tr_inked = painter('red', do_past_tr)

"----------------------------------------------------------------------------------------------------------------------"
set_box_present = set({})

while len(set_box_present) < 1:
    set_box_present.add(choice(do_present_l))

set_box_present = list(set_box_present)

do_present = set_box_present[0]
do_present_inked = painter('blue', do_present)
do_present_tr = do_present_l_pt_br[do_present_l.index(do_present)]
do_present_tr_inked = painter('red', do_present_tr)

if __name__ == '__main__':
    # print(do_past)
    # print(do_past_inked)
    # print(do_past_tr)
    # print(do_past_tr_inked)

    # print(do_present)
    # print(do_present_inked)
    # print(do_present_tr)
    # print(do_present_tr_inked)
    pass

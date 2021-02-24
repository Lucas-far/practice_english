

from random import choice
from metodos.bdd import painter

have = [
    "has", "has not", "hasn't",
    "Has", "Has not", "Hasn't",
    "have", "have not", "haven't",
    "Have", "Have not", "Haven't",
]

have_present_l = [
    'has', 'does not have', "doesn't have",
    'have', 'do not have', "don't have",
]

have_present_l_pt_br = ['tem', 'não tem', 'não tem', 'tem', 'não tem', 'não tem']

have_u = ["Has", "Has not", "Hasn't", "Have", "Have not", "Haven't"]
have_l = ["has", "has not", "hasn't", "have", "have not", "haven't"]

has_l = ["has"]
has_not_l = ["has not"]
has_not_short_l = ["hasn't"]

has_u = ["Has"]
has_not_u = ["Has not"]
has_not_short_u = ["Hasn't"]

the_have_l = ["have"]
have_not_l = ["have not"]
have_not_short_l = ["haven't"]

the_have_u = ["Have"]
have_not_u = ["Have not"]
have_not_short_u = ["Haven't"]

have_past_l = ['had', 'did not have', "didn't have"]
have_past_l_pt_br = ['tinha', 'não tinha(m)', 'não tinha(m)']

have_future_l = ['will have', 'will not have', "won't have"]
have_future_l_pt_br = ['terei', 'não terei(ão)', 'não terei(ão)']

"----------------------------------------------------------------------------------------------------------------------"
set_box_past = set({})

while len(set_box_past) < 1:
    set_box_past.add(choice(have_past_l))

set_box_past = list(set_box_past)

have_past = set_box_past[0]
have_past_inked = painter('blue', have_past)
have_past_tr = have_past_l_pt_br[have_past_l.index(have_past)]
have_past_tr_inked = painter('red', have_past_tr)
"----------------------------------------------------------------------------------------------------------------------"
set_box_present = set({})

while len(set_box_present) < 1:
    set_box_present.add(choice(have_present_l))

set_box_present = list(set_box_present)

have_present = set_box_present[0]
have_present_inked = painter('blue', have_present)
have_present_tr = have_present_l_pt_br[have_present_l.index(have_present)]
have_present_tr_inked = painter('red', have_present_tr)
"----------------------------------------------------------------------------------------------------------------------"
set_box_future = set({})

while len(set_box_future) < 1:
    set_box_future.add(choice(have_future_l))

set_box_future = list(set_box_future)

have_future = set_box_future[0]
have_future_inked = painter('blue', have_future)
have_future_tr = have_future_l_pt_br[have_future_l.index(have_future)]
have_future_tr_inked = painter('red', have_future_tr)

if __name__ == '__main__':
    print(have_past)
    print(have_past_inked)
    print(have_past_tr)
    print(have_past_tr_inked)
    print('\n')
    print(have_present)
    print(have_present_inked)
    print(have_present_tr)
    print(have_present_tr_inked)
    print('\n')
    print(have_future)
    print(have_future_inked)
    print(have_future_tr)
    print(have_future_tr_inked)
    pass

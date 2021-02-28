

from random import choice
from metodos.bdd import painter

"----------------------------------------------------- PRINCIPAIS -----------------------------------------------------"
can_present_l = ["can", "cannot", "can't"]

can_present_l_pt_br = ['consigo / posso', 'não consigo / não posso', 'não consigo / não posso']

could_past_l = ["could", "could not", "couldn't"]

could_past_l_pt_br = [
    'conseguia / podia / poderia',
    'não conseguia / não podia / não poderia',
    'não conseguia / não podia / não poderia'
]
"----------------------------------------------------------------------------------------------------------------------"

# easy
can_pst_easy = ["can", "can't", "cannot"]

# average
can_pst_average = ["can", "can't", "cannot", "could", "couldn't", "could not"]

# fluent
can_pst_fluent = [
    "can", "can't", "cannot",
    "Can", "Can't", "Cannot",
    "could", "couldn't", "could not",
    "Could", "Couldn't", "Could not"
]

can = [
    "can", "can't", "cannot",
    "Can", "Can't", "Cannot",
    "could", "couldn't", "could not",
    "Could", "Couldn't", "Could not"
]

can_u = ["Can", "Cannot", "Can't", "Could", "Could not", "Couldn't"]

can_not = ["cannot", "can't"]
could_not = ["could not", "couldn't"]

the_can_u = ["Can"]
can_l = ["can"]

could_u = ["Could"]
could_l = ["could"]

can_not_u = ["Cannot"]
can_not_l = ["cannot"]

could_not_u = ["Could not"]
could_not_l = ["could not"]

can_not_short_u = ["Can't"]
can_not_short_l = ["can't"]

could_not_short_u = ["Couldn't"]
could_not_short_l = ["couldn't"]

can_pro_not_u = ['Can I not', 'Can you not', 'Can he not', 'Can she not', 'Can it not', 'Can we not', 'Can they not']

could_pro_not_l = [
    'Could I not', 'Could you not', 'Could he not', 'Could she not', 'Could it not', 'Could we not', 'Could they not'
]

"----------------------------------------------------------------------------------------------------------------------"
set_box_past = set({})

while len(set_box_past) < 1:
    set_box_past.add(choice(could_past_l))

set_box_past = list(set_box_past)

could_past = set_box_past[0]
could_past_inked = painter('blue', could_past)
could_past_tr = could_past_l_pt_br[could_past_l.index(could_past)]
could_past_tr_inked = painter('red', could_past_tr)
"----------------------------------------------------------------------------------------------------------------------"
set_box_present = set({})

while len(set_box_present) < 1:
    set_box_present.add(choice(can_present_l))

set_box_present = list(set_box_present)

can_present = set_box_present[0]
can_present_inked = painter('blue', can_present)
can_present_tr = can_present_l_pt_br[can_present_l.index(can_present)]
can_present_tr_inked = painter('red', can_present_tr)

if __name__ == '__main__':
    # print(could_past)
    # print(could_past_inked)
    # print(could_past_tr)
    # print(could_past_tr_inked)

    # print(can_present)
    # print(can_present_inked)
    # print(can_present_tr)
    # print(can_present_tr_inked)
    pass

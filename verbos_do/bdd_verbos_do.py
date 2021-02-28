

""""""
# from random import choice
# from metodos.bdd import painter

"----------------------------------------------------- PRINCIPAIS -----------------------------------------------------"
do_present_l = [
    "does", "does not", "doesn't",
    "do", "do not", "don't"
]

do_present_l_pt_br = [
    'ênfase (ex: does talk = falo)', 'não', 'não',
    'ênfase (ex: do talk = falam) ', 'não', 'não'
]

do_past_l = ["did", "did not", "didn't"]

do_past_l_pt_br = ['ênfase (ex: did talk = falei)', 'não', 'não']

"------------------------------------------------------ PASSADO -------------------------------------------------------"
did = [
    "did", "did not", "didn't",
    "Did", "Did not", "Didn't",
]

did_past_gl_u = ["Did", "Did not", "Didn't"]

did_past_gl_l = ["did", "did not", "didn't"]

did_u = ["Did"]
did_not_u = ["Did not"]
did_not_short_u = ["Didn't"]

did_l = ["did"]
did_not_l = ["did not"]
did_not_short_l = ["didn't"]

"------------------------------------------------------ PRESENTE ------------------------------------------------------"
do = [
    "does", "does not", "doesn't",
    "Does", "Does not", "Doesn't",
    "do", "do not", "don't",
    "Do", "Do not", "Don't"
]

do_pst_gl_u = ["Does", "Does not", "Doesn't", "Do", "Do not", "Don't"]

do_pst_gl_l = ["does", "does not", "doesn't", "do", "do not", "don't"]

do_pst_1st_2nd_u = ["Do", "Do not", "Don't"]

do_pst_1st_2nd_l = ["do", "do not", "don't"]

do_pst_3rd_u = ["Does", "Does not", "Doesn't"]

do_pst_3rd_l = ["does", "does not", "doesn't"]

does_l = ["does"]
does_not_l = ["does not"]
does_not_short_l = ["doesn't"]

does_u = ["Does"]
does_not_u = ["Does not"]
does_not_short_u = ["Doesn't"]

do_u = ["Do"]
do_not_u = ["Do not"]
do_not_short_u = ["Don't"]

do_l = ["do"]
do_not_l = ["do not"]
do_not_short_l = ["don't"]

# "----------------------------------------------------------------------------------------------------------------------"
# set_box_past = set({})
#
# while len(set_box_past) < 1:
#     set_box_past.add(choice(do_past_l))
#
# set_box_past = list(set_box_past)
#
# do_past = set_box_past[0]
# do_past_inked = painter('blue', do_past)
# do_past_tr = do_past_l_pt_br[do_past_l.index(do_past)]
# do_past_tr_inked = painter('red', do_past_tr)
#
# "----------------------------------------------------------------------------------------------------------------------"
# set_box_present = set({})
#
# while len(set_box_present) < 1:
#     set_box_present.add(choice(do_present_l))
#
# set_box_present = list(set_box_present)
#
# do_present = set_box_present[0]
# do_present_inked = painter('blue', do_present)
# do_present_tr = do_present_l_pt_br[do_present_l.index(do_present)]
# do_present_tr_inked = painter('red', do_present_tr)

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



from metodos.bdd import data_collector as _, painter

demonstrative_pronouns = ['this', 'these', 'that', 'those', 'This', 'These', 'That', 'Those']

demonstrative_pronouns_u = ['This', 'These', 'That', 'Those']

demonstrative_pronouns_l = ['this', 'these', 'that', 'those']

demonstrative_pronouns_l_pt_br = ['esse(a)', 'esses(as)', 'aquele(a)', 'aqueles(as)']

demonstrative_pronouns_sgl_u = ['This', 'That']

demonstrative_pronouns_sgl_l = ['this', 'that']

demonstrative_pronouns_pl_u = ['These', 'Those']

demonstrative_pronouns_pl_l = ['these', 'those']

this_u = ['This']

this_l = ['this']

these_u = ['These']

these_l = ['these']

that_u = ['That']

that_l = ['that']

those_u = ['Those']

those_l = ['those']

this_ = ['this', 'esse(a)']

these_ = ['these', 'esses(as)']

that_ = ['that', 'aquele(a)']

those_ = ['those', 'aqueles(as)']


pro_be_gl_u = [
    'This is', "This is not", "This isn't",
    'That is', "That is not", "That isn't",
    'These are', "These are not", "These aren't",
    'Those are', "Those are not", "Those aren't"
]

pro_be_gl_l = [
    'this is', "this is not", "this isn't",
    'that is', "that is not", "that isn't",
    'these are', "these are not", "these aren't",
    'those are', "those are not", "those aren't"
]

pro_be_u = ['This is', 'That is', 'These are', 'Those are']

pro_be_l = ['this is', 'that is', 'these are', 'those are']

pro_be_not_u = [
    "This is not", "This isn't", "That is not", "That isn't", "These are not", "These aren't",
    "Those are not", "Those aren't"
]

pro_be_not_l = [
    "this is not", "this isn't", "that is not", "that isn't", "these are not", "these aren't",
    "those are not", "those aren't"
]

demonstrative_pronoun = _(demonstrative_pronouns_l)
demonstrative_pronoun_inked = painter('blue', demonstrative_pronoun)
demonstrative_pronoun_tr = demonstrative_pronouns_l_pt_br[demonstrative_pronouns_l.index(demonstrative_pronoun)]
demonstrative_pronoun_tr_inked = painter('red', demonstrative_pronoun_tr)

if __name__ == '__main__':
    pass
    # print(demonstrative_pronoun)
    # print(demonstrative_pronoun_inked)
    # print(demonstrative_pronoun_tr)
    # print(demonstrative_pronoun_tr_inked)

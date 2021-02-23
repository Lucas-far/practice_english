

from metodos.bdd import data_collector as _, painter

reflexive_pronouns_l = [
    'myself', 'yourself', 'himself', 'herself', 'itself', 'ourselves', 'yourselves', 'themselves'
]

reflexive_pronouns_l_pt_br = [
    'eu mesmo(a)', 'você mesmo(a)', 'ele mesmo', 'ela mesma', 'esse mesmo',
    'nós mesmos(as)', 'vocês mesmo(a)', 'eles(as) mesmo(a)'
]

reflexive_pronoun = _(reflexive_pronouns_l)
reflexive_pronoun_inked = painter('blue', reflexive_pronoun)
reflexive_pronoun_tr = reflexive_pronouns_l_pt_br[reflexive_pronouns_l.index(reflexive_pronoun)]
reflexive_pronoun_tr_inked = painter('red', reflexive_pronoun_tr)

if __name__ == '__main__':
    pass
    # print(reflexive_pronoun)
    # print(reflexive_pronoun_inked)
    # print(reflexive_pronoun_tr)
    # print(reflexive_pronoun_tr_inked)

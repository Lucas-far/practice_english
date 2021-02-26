

from metodos.bdd import data_collector as _, painter
from cores.cores import inks

reflexive_pronouns_l = [
    'myself', 'yourself', 'himself', 'herself', 'itself', 'ourselves', 'yourselves', 'themselves'
]

reflexive_pronouns_l_pt_br = [
    'eu mesmo(a) (fim da frase)', 'você mesmo(a) (fim da frase)', 'ele mesmo (fim da frase)',
    'ela mesma (fim da frase)', 'esse mesmo (fim da frase)', 'nós mesmos(as) (fim da frase)',
    'vocês mesmo(a) (fim da frase)', 'eles(as) mesmo(a) (fim da frase)'
]


def display_reflexive_pronouns():
    counter = 0
    print('\n==================== PRONOMES REFLEXIVOS ====================\n')
    while counter < len(reflexive_pronouns_l):
        print(f"    {inks[3]}{reflexive_pronouns_l[counter]}{inks[7]} = {reflexive_pronouns_l_pt_br[counter]}")
        counter += 1

# reflexive_pronoun = _(reflexive_pronouns_l)
# reflexive_pronoun_inked = painter('blue', reflexive_pronoun)
# reflexive_pronoun_tr = reflexive_pronouns_l_pt_br[reflexive_pronouns_l.index(reflexive_pronoun)]
# reflexive_pronoun_tr_inked = painter('red', reflexive_pronoun_tr)

if __name__ == '__main__':
    # display_reflexive_pronouns()

    # for words in zip(reflexive_pronouns_l_inked, reflexive_pronouns_l_pt_br):
    #     print(words)
    # print(reflexive_pronouns_l_inked[0])
    # print(reflexive_pronoun)
    # print(reflexive_pronoun_inked)
    # print(reflexive_pronoun_tr)
    # print(reflexive_pronoun_tr_inked)
    pass

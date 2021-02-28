

from metodos.bdd import data_collector as _, painter

possessive_pronouns_l = ['mine', 'yours', 'his', 'hers', 'its', 'ours', 'yours', 'theirs']

possessive_pronouns_l_pt_br = [
    'meu / minha (final da frase)',
    'seu / sua (final da frase)',
    'dele (final da frase)',
    'dela (final da frase)',
    'desse / dessa (final da frase)',
    'nosso(a) (final da frase)',
    'seus / suas (final da frase)',
    'deles(as) / desses (final da frase)'
]

mine_ = ['mine', 'meu / minha']
yours_ = ['yours', 'seu(a)']
his_ = ['his', 'dele']
hers_ = ['hers', 'dela']
its_ = ['its', 'disso']
ours_ = ['ours', 'nosso']
theirs_ = ['theirs', 'deles(as)']

# possessive_pronoun = _(possessive_pronouns_l)
# possessive_pronoun_inked = painter('blue', possessive_pronoun)
# possessive_pronoun_tr = possessive_pronouns_l_pt_br[possessive_pronouns_l.index(possessive_pronoun)]
# possessive_pronoun_tr_inked = painter('red', possessive_pronoun_tr)

if __name__ == '__main__':
    print('\n')

    # print(possessive_pronoun)
    # print(possessive_pronoun_inked)
    # print(possessive_pronoun_tr)
    # print(possessive_pronoun_tr_inked)

    # print(bricks)
    # print(f'{len(possessive_pronouns_l) = }')
    # print(f'{len(possessive_pronouns_l_pt_br) = }')
    #
    # print('\n')
    # for word in zip(possessive_pronouns_l, possessive_pronouns_l_pt_br):
    #     print(word[0])
    #     print(word[1])

    # print('\n')
    # counter = 0
    # while counter < len(possessive_pronouns_l):
    #     print(f"{possessive_pronouns_l[counter]}_ = ['{possessive_pronouns_l[counter]}', '{possessive_pronouns_l_pt_br[counter]}']")
    #     counter += 1

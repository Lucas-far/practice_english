

from random import choice
from collections import deque
from adjetivos.bdd_adjetivos import *
from adjetivos_possessivos.bdd_adjetivos_possessivos import *
from adverbios.bdd_adverbios import *
from conjuncoes.bdd_conjuncoes import *
from preposicoes.bdd_preposicoes import *
from pronomes.bdd_pronomes import *
from pronomes_demonstrativos.bdd_pronomes_demonstrativos import *
from pronomes_possessivos.bdd_pronomes_possessivos import *
from pronomes_reflexivos.bdd_pronomes_reflexivos import *
from substantivos.bdd_substantivos import *
from verbos_be.bdd_verbos_be_simples import *
from verbos_can.bdd_verbos_can import *
from verbos_do.bdd_verbos_do import *
from verbos_have.bdd_verbos_have import *
from verbos_infinitivo.bdd_verbos_infinitivo import *
from verbos_passado.bdd_verbos_passado import *
from verbos_presente.bdd_verbos_presente import *
from verbos_futuro.bdd_verbos_futuro import *
from wh.bdd_wh import *

var = ['adjetivo possessivo', 'pronome', 'pronome demonstrativo', 'pronome possessivo', 'pronome reflexivo',
       'advérbio de frequência', 'advérbio normal', 'advérbio ly', 'conjunção', 'preposição', 'wh', 'substantivo',
]

var2 = [
    'verbo can', 'verbo can negativo',
    'verbo could', 'verbo could negativo',
    'to be passado', 'to be passado negativo',
    'to be presente', 'to be presente negativo',
    'to be futuro', 'to be futuro negativo',
    'to do passado (ênfase)',
    'to do passado negativo',
    'to do presente (ênfase)',
    'to do presente (negativo)',
    'to have passado',
    'to have passado negativo',
    'to have presente',
    'to have presente negativo',
    'to have futuro',
    'to have futuro negativo',
    'infinitivo',
    'verbo passado',
    'verbo passado negativo',
    'verbo presente',
    'verbo presente negativo',
    'verbo futuro',
    'verbo futuro negativo'
]

elements = {
    'adjetivo possessivo': choice(['my', 'your', 'his', 'her', 'its', 'our', 'your', 'their']),
    'pronome': choice(['I', 'he', 'she', 'it', 'we', 'you', 'you', 'they']),
    'pronome demonstrativo': choice(['this', 'these', 'that', 'those']),
    'pronome possessivo': choice(['mine', 'yours', 'his', 'hers', 'its', 'ours', 'yours', 'theirs']),
    'pronome reflexivo': choice(['myself', 'yourself', 'himself', 'herself', 'itself', 'ourselves', 'yourselves', 'themselves']),
    'advérbio de frequência': choice(adverbs_frequency),
    'advérbio normal': choice(adverb_others),
    'advérbio ly': choice(adverbs_ly),
    'conjunção': choice(conjunctions_l),
    'preposição': choice(prepositions_l),
    'wh': choice(['how', 'what', 'when', 'where', 'which', 'who', 'whose', 'why']),
    'substantivo': choice(nouns),
    'verbo can': choice(['can']),
    'verbo can negativo': choice(["cannot", "can't"]),
    'verbo could': choice(['could']),
    'verbo could negativo': choice(["could not", "couldn't"]),
    'to be passado': choice(['was', 'were']),
    'to be passado negativo': choice(['was', 'was not', "wasn't", 'were', 'were not', "weren't"]),
    'to be presente': choice(['am', 'is', 'are']),
    'to be presente negativo': choice(["am not", "is not", "isn't", "are not", "aren't"]),
    'to be futuro': choice(['will be']),
    'to be futuro negativo': choice(['will not be', "won't be"]),
    'to do passado (ênfase)': choice(['did']),
    'to do passado negativo': choice(["did not", "didn't"]),
    'to do presente (ênfase)': choice(['do']),
    'to do presente (negativo)': choice(["does not", "doesn't", "do not", "don't"]),
    'to have passado': choice(['had']),
    'to have passado negativo': choice(["did not have", "didn't have"]),
    'to have presente': choice(['has', 'have']),
    'to have presente negativo': choice(["does not have", "doesn't have"]),
    'to have futuro': choice(['will have']),
    'to have futuro negativo': choice(["will not have", "won't have"]),
    'infinitivo': choice(verbs_infinitive),
    'verbo passado': choice(past),
    'verbo passado negativo': choice(["did not", "didn't"]) + ' ' + choice(present_1st_2nd_persons),
    'verbo presente': choice(present),
    'verbo presente negativo': choice(["does not", "do not"]) + ' ' + choice(present_1st_2nd_persons),
    'verbo futuro': choice(future),
    'verbo futuro negativo': choice(["will not", "won't"]) + ' ' + choice(present_1st_2nd_persons)
}

# elements_ = [
#     choice(['my', 'your', 'his', 'her', 'its', 'our', 'your', 'their']),
#     choice(['I', 'he', 'she', 'it', 'we', 'you', 'you', 'they']),
#     choice(['this', 'these', 'that', 'those']),
#     choice(['mine', 'yours', 'his', 'hers', 'its', 'ours', 'yours', 'theirs']),
#     choice(['myself', 'yourself', 'himself', 'herself', 'itself', 'ourselves', 'yourselves', 'themselves']),
#     choice(adverbs_frequency),
#     choice(adverb_others),
#     choice(adverbs_ly),
#     choice(conjunctions_l),
#     choice(prepositions_l),
#     choice(['how', 'what', 'when', 'where', 'which', 'who', 'whose', 'why']),
#     choice(nouns),
#     choice(['can']),
#     choice(["cannot", "can't"]),
#     choice(['could']),
#     choice(["could not", "couldn't"]),
#     choice(['was', 'were']),
#     choice(['was', 'was not', "wasn't", 'were', 'were not', "weren't"]),
#     choice(['am', 'is', 'are']),
#     choice(["am not", "is not", "isn't", "are not", "aren't"]),
#     choice(['will be']),
#     choice(['will not be', "won't be"]),
#     choice(['did']),
#     choice(["did not", "didn't"]),
#     choice(['do']),
#     choice(["does not", "doesn't", "do not", "don't"]),
#     choice(['had']),
#     choice(["did not have", "didn't have"]),
#     choice(['has', 'have']),
#     choice(["does not have", "doesn't have"]),
#     choice(['will have']),
#     choice(["will not have", "won't have"]),
#     choice(verbs_infinitive),
#     choice(past),
#     choice(["did not", "didn't"]) + ' ' + choice(present_1st_2nd_persons),
#     choice(present),
#     choice(["does not", "do not"]) + ' ' + choice(present_1st_2nd_persons),
#     choice(future),
#     choice(["will not", "won't"]) + ' ' + choice(present_1st_2nd_persons)
# ]

box = []

word_set = set({})
counter = 0
while counter < 5:
    if counter % 2:
        word_set.add(choice(var))
        counter += 1
    else:
        word_set.add(choice(var2))
        counter += 1

word_set = list(word_set)
print(word_set)

for key in elements:
    if key == word_set[0]:
        box.append(elements[key])
    elif key == word_set[1]:
        box.append(elements[key])
    elif key == word_set[2]:
        box.append(elements[key])
    elif key == word_set[3]:
        box.append(elements[key])
    elif key == word_set[4]:
        box.append(elements[key])
print(box)

if __name__ == '__main__':
    pass
    # print(len(var))
    # print(len(elements_))
    # print(elements_)
    # word_set = deque(word_set)
    # print('pronome' in word_set)
    # if 'pronome' in word_set:
    #     word_set.appendleft('pronome')
    #     del word_set[word_set.index('pronome', 1)]
    # word_set = list(word_set)
    # print(word_set)

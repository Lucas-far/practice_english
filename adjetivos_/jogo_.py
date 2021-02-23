

from random import choice
from strings import *
from metodos.bdd import (create_set, var_printer, painter)

from adjetivos.bdd_adjetivos import (adjectives, adjectives_pt_br)

from pronomes.bdd_pronomes import (pronoun, pronoun_inked, pronoun_tr, pronoun_tr_inked)

from adjetivos_possessivos.bdd_adjetivos_possessivos import (
    possessive_adjective, possessive_adjective_inked, possessive_adjective_tr, possessive_adjective_tr_inked
)

from pronomes_possessivos.bdd_pronomes_possessivos import (
    possessive_pronoun, possessive_pronoun_inked, possessive_pronoun_tr, possessive_pronoun_tr_inked
)

from pronomes_demonstrativos.bdd_pronomes_demonstrativos import (
    demonstrative_pronoun, demonstrative_pronoun_inked, demonstrative_pronoun_tr, demonstrative_pronoun_tr_inked
)

from pronomes_reflexivos.bdd_pronomes_reflexivos import (
    reflexive_pronoun, reflexive_pronoun_inked, reflexive_pronoun_tr, reflexive_pronoun_tr_inked
)

from preposicoes.bdd_preposicoes import (
    preposition, preposition_inked, preposition_tr, preposition_tr_inked
)

from adverbios.bdd_adverbios import (
    adverb, adverb_inked, adverb_tr, adverb_tr_inked,
    adverb2, adverb2_inked, adverb2_tr, adverb2_tr_inked,
    adverb3, adverb3_inked, adverb3_tr, adverb3_tr_inked,
)

from conjuncoes.bdd_conjuncoes import (
    conjunction, conjunction_inked, conjunction_tr, conjunction_tr_inked,
    conjunction2, conjunction2_inked, conjunction2_tr, conjunction2_tr_inked,
)

from substantivos.bdd_substantivos import (
    noun, noun_inked, noun_tr, noun_tr_inked,
    noun2, noun2_inked, noun2_tr, noun2_tr_inked,
    noun3, noun3_inked, noun3_tr, noun3_tr_inked,
)

positive_score = 0
negative_score = 0

empty_set = set({})

five_words = sorted(list(create_set(empty_set, 5, adjectives, True)))  # function create_set()
five_indexes = [adjectives.index(word) for word in five_words]
five_translations = [adjectives_pt_br[index] for index in five_indexes]

chosen_word = choice(five_words)
chosen_word_index = five_words.index(chosen_word)
chosen_word_translation = five_translations[chosen_word_index]
the_target_translation = [chosen_word_translation]

display_variables = var_printer(
    list_var_names="""
    five_words five_indexes five_translations chosen_word chosen_word_index chosen_word_translation
    the_target_translation
    """,
    list_var_values=[five_words, five_indexes, five_translations, chosen_word, chosen_word_index,
                     chosen_word_translation, the_target_translation]
)  # function var_printer()

# for word in display_variables:
#     print(word)

print('\n')
print(hello)
print('\n')
print(pronoun)
print(pronoun_inked)
print(pronoun_tr)
print(pronoun_tr_inked)
print('===============================================================================================================')
print(possessive_adjective)
print(possessive_adjective_inked)
print(possessive_adjective_tr)
print(possessive_adjective_tr_inked)
print('===============================================================================================================')
print(possessive_pronoun)
print(possessive_pronoun_inked)
print(possessive_pronoun_tr)
print(possessive_pronoun_tr_inked)
print('===============================================================================================================')
print(demonstrative_pronoun)
print(demonstrative_pronoun_inked)
print(demonstrative_pronoun_tr)
print(demonstrative_pronoun_tr_inked)
print('===============================================================================================================')
print(reflexive_pronoun)
print(reflexive_pronoun_inked)
print(reflexive_pronoun_tr)
print(reflexive_pronoun_tr_inked)
print('===============================================================================================================')
print(preposition)
print(preposition_inked)
print(preposition_tr)
print(preposition_tr_inked)
print('===============================================================================================================')
print(adverb)
print(adverb_inked)
print(adverb_tr)
print(adverb_tr_inked)
print(adverb2)
print(adverb2_inked)
print(adverb2_tr)
print(adverb2_tr_inked)
print(adverb3)
print(adverb3_inked)
print(adverb3_tr)
print(adverb3_tr_inked)
print('===============================================================================================================')
print(conjunction)
print(conjunction_inked)
print(conjunction_tr)
print(conjunction_tr_inked)
print(conjunction2)
print(conjunction2_inked)
print(conjunction2_tr)
print(conjunction2_tr_inked)
print('===============================================================================================================')
print(noun)
print(noun2)
print(noun3)
print(noun_inked)
print(noun2_inked)
print(noun3_inked)
print(noun_tr)
print(noun2_tr)
print(noun3_tr)
print(noun_tr_inked)
print(noun2_tr_inked)
print(noun3_tr_inked)

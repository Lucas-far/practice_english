

from random import choice

def create_set(set_var: set, data_length: int, extraction_from: list, extract_from=False):
    """"""
    while len(set_var) < data_length:
        set_var.add(choice(extraction_from))
    return set_var

if __name__ == '__main__':
    adjectives = ['mad', 'crazy', 'lunatic', 'polite', 'stupid', 'dangerous']
    adjectives_set = set({})
    print(test_create_set := create_set(adjectives_set, 5, adjectives, True))

# create_word()
#
# five_words = sorted(list(five_words))
#
# five_indexes = [adjectives.index(word) for word in five_words]
#
# five_translations = [adjectives_pt_br[index] for index in five_indexes]
#
# chosen_word = choice(five_words)
#
# chosen_word_index = five_words.index(chosen_word)
#
# chosen_word_translation = five_translations[chosen_word_index]
#
# the_target_translation = [chosen_word_translation]

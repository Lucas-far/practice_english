

from adverbios.bdd_adverbios import adverbs_ly, adverbs_frequency, adverb_others
from metodos.bdd import verify

print(target := verify('bravely', database=adverbs_ly))
print(target2 := verify('bravely', database=adverbs_frequency))
print(target3 := verify('bravely', database=adverb_others))

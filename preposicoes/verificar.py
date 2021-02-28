

from preposicoes.bdd_preposicoes import prepositions_l
from metodos.bdd import verify

print(target := verify('by', database=prepositions_l))
# print(target2 := verify('loud', database=adjectives_ble))
# print(target3 := verify('loud', database=adjectives_uncommon))

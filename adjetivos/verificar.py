

from adjetivos.bdd_adjetivos import adjectives, adjectives_ble, adjectives_uncommon
from metodos.bdd import verify

print(target := verify('loud', database=adjectives))
print(target2 := verify('loud', database=adjectives_ble))
print(target3 := verify('loud', database=adjectives_uncommon))

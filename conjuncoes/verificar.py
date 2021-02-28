

from conjuncoes.bdd_conjuncoes import conjunctions_l
from metodos.bdd import verify

print(target := verify('before', 'after', 'and', database=conjunctions_l))

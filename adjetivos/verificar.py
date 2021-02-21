

from adjetivos.bdd_adjetivos import adjectives
from metodos.bdd import verify

print(target := verify('nasty', database=adjectives))

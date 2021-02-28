

from verbos_futuro.bdd_verbos_futuro import future
from metodos.bdd import verify

print(target := verify('will evolve', 'will try', 'will explain', database=future))

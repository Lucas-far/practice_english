

from verbos_presente.bdd_verbos_presente import present
from metodos.bdd import verify

print(target := verify('evolve', 'try', 'explain', database=present))

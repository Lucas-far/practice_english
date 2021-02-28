

from verbos_passado.bdd_verbos_passado import past, past_irregular
from metodos.bdd import verify

print(target := verify('attempted', 'remembered', 'cried', database=past))
print(target2 := verify('attempted', 'remembered', 'cried', database=past_irregular))

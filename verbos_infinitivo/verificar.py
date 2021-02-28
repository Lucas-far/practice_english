

from verbos_infinitivo.bdd_verbos_infinitivo import verbs_infinitive
from metodos.bdd import verify

print(target := verify('to attempt', 'to remember', 'to dive', database=verbs_infinitive))

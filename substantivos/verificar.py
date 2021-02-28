

from substantivos.bdd_substantivos import nouns
from metodos.bdd import verify

print(target := verify('person', database=nouns))

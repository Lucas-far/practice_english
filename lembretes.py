

from metodos.bdd import sentence_maker as _

from pronomes.bdd_pronomes import (pro, pro_sgl_is_u)
from verbos_be.bdd_presente import (is_l)
from adjetivos.bdd_adjetivos import (adjectives_and_article)
from substantivos.bdd_substantivos import nouns_sgl

x = ' '

um = 'Fazer um jogo separado de todos os tempos verbais: "be", "have", "do"'
dois = 'Criar um arquivo para receber texto em forma de variável de lista'
tres = 'Criar frases nos jogos, baseados nas respostas'


# She is a nice person
print(_(pro_sgl_is_u, x, is_l, x, adjectives_and_article, x, nouns_sgl))
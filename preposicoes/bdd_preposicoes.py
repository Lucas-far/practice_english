

""""""
"------------------------------------------------------- GLOBAL -------------------------------------------------------"
prepositions = [
    'about', 'above', 'across', 'after', 'against', 'ago', 'among',
    'around', 'as', 'at', 'before', 'behind', 'below',
    'between', 'by', 'down', 'during', 'for', 'from',
    'in', 'in front of', 'into', 'like', 'next to', 'of',
    'on', 'out', 'over', 'since', 'through', 'to',
    'towards', 'under', 'underneath', 'until', 'up', 'with',
    'without'
]

prepositions_pt_br = [
    'sobre/acerca de', 'acima/sobre (sem contato)', 'através', 'depois', 'contra', 'atrás', 'dentre/entre',
    'ao redor/em volta/por aí', 'como', 'em (sem contato)', 'diante de/perante', 'atrás/detrás', 'abaixo/sob',
    'entre/no meio de', 'junto a/perto de/por', 'abaixo', 'durante', 'para/por/durante', 'de/do/desde/a partir de',
    'em (contato dentro)', 'em frente a/na frente de', 'em/dentro/para dentro', 'como', 'ao lado de/próximo de', 'de',
    'em (contato fora)', 'para fora/fora', 'acima/sobre (contato)', 'a partir de/desde', 'através de', 'para',
    'em direção a', 'debaixo/embaixo/por baixo', 'embaixo/por baixo de/sob', 'até', 'acima/em cima/para cima', 'com',
    'sem'
]
"------------------------------------------------------- COMUNS -------------------------------------------------------"
prepositions_main = [
    'below', 'under', 'above', 'over',
    'behind', 'in front of', 'next to', 'between',
    'in', 'on', 'at'
]

prepositions_main_pt_br = [
    'abaixo/sob', 'debaixo/embaixo/por baixo', 'acima/sobre (sem contato)', 'acima/sobre (contato)',
    'atrás/detrás', 'em frente a/na frente de', 'ao lado de/próximo de', 'entre/no meio de',
    'em (contato dentro)', 'em (contato fora)', 'em (sem contato)'
]
"------------------------------------------------------ DIREÇÃO -------------------------------------------------------"
prepositions_direction_place = [
    'above', 'across', 'among', 'at', 'behind', 'below',
    'between', 'by', 'down', 'from', 'in',
    'in front of', 'on', 'over', 'through', 'to', 'towards',
    'under', 'up'
]

prepositions_direction_place_pt_br = [
    'acima/sobre (sem contato)', 'através', 'dentre/entre', 'em (sem contato)', 'atrás/detrás', 'abaixo/sob',
    'entre/no meio de', 'junto a/perto de/por', 'abaixo', 'de/do/desde/a partir de', 'em (contato dentro)',
    'em frente a/na frente de', 'em (contato fora)', 'acima/sobre (contato)', 'através de', 'para', 'em direção a',
    'debaixo/embaixo/por baixo', 'acima/em cima/para cima'
]
"-------------------------------------------------------- TEMPO -------------------------------------------------------"
prepositions_time = [
    'on', 'ago', 'at', 'before', 'by', 'for',
    'from', 'in', 'since', 'to', 'until'
]

prepositions_time_pt_br = [
    'em (contato fora)', 'atrás', 'em (sem contato)', 'diante de/perante', 'junto a/perto de/por', 'para/por/durante',
    'de/do/desde/a partir de', 'em (contato dentro)', 'a partir de/desde', 'para', 'até'
]
"------------------------------------------------------- CURTAS -------------------------------------------------------"
prepositions_short = [
    'at', 'by', 'down', 'for', 'from',
    'in', 'into', 'like', 'of', 'on', 'out',
    'over', 'to', 'up', 'with'
]

prepositions_short_pt_br = [
    'em (sem contato)', 'junto a/perto de/por', 'abaixo', 'para/por/durante', 'de/do/desde/a partir de',
    'em (contato dentro)', 'em/dentro/para dentro', 'como', 'de', 'em (contato fora)', 'para fora/fora',
    'acima/sobre (contato)', 'para', 'acima/em cima/para cima', 'com'
]
"------------------------------------------------------- FRASAIS ------------------------------------------------------"
# preposititons_phrasal_upper = [index.replace(index, index[0].upper() + index[1:]) for index in preposititons_phrasal_lower]
prepositions_phrasal_u = [
    'According to', 'Along with', 'Apart from', 'Because of', 'By means of', 'Contrary to', 'In addition to',
    'In front of', 'In reference to', 'In regard to', 'In spite of', 'Instead of', 'On account of', 'On top of',
    'Out of', 'With regard to'
]

prepositions_phrasal_l = [
    'according to', 'along with', 'apart from', 'because of', 'by means of', 'contrary to', 'in addition to',
    'in front of', 'in reference to', 'in regard to', 'in spite of', 'instead of', 'on account of', 'on top of',
    'out of', 'with regard to'
]

prepositions_phrasal_pt_br = [
    'de acordo com', 'junto com', 'além de', 'por causa de', 'por meio de', 'contrário a', 'além de',
    'na frente de', 'em referência a', 'em relação a', 'apesar de', 'em vez de', 'devido a', 'em cima de',
    'fora de', 'no que diz respeito ao(s)'
]

about_ = ['about', 'sobre/acerca de']
above_ = ['above', 'acima/sobre (sem contato)']
across_ = ['across', 'através']
after_ = ['after', 'depois']
against_ = ['against', 'contra']
ago_ = ['ago', 'atrás']
among_ = ['among', 'dentre/entre']
around_ = ['around', 'ao redor/em volta/por aí']
as_ = ['as', 'como']
at_ = ['at', 'em (sem contato)']
before_ = ['before', 'diante de/perante']
behind_ = ['behind', 'atrás/detrás']
below_ = ['below', 'abaixo/sob']
between_ = ['between', 'entre/no meio de']
by_ = ['by', 'junto a/perto de/por']
down_ = ['down', 'abaixo']
during_ = ['during', 'durante']
for_ = ['for', 'para/por/durante']
from_ = ['from', 'de/do/desde/a partir de']
in_ = ['in', 'em (contato dentro)']
in_front_of_ = ['in front of', 'em frente a/na frente de']
into_ = ['into', 'em/dentro/para dentro']
like_ = ['like', 'como']
next_to_ = ['next to', 'ao lado de/próximo de']
of_ = ['of', 'de']
on_ = ['on', 'em (contato fora)']
out_ = ['out', 'para fora/fora']
over_ = ['over', 'acima/sobre (contato)']
since_ = ['since', 'a partir de/desde']
through_ = ['through', 'através de']
to_ = ['to', 'para']
towards_ = ['towards', 'em direção a']
under_ = ['under', 'debaixo/embaixo/por baixo']
underneath_ = ['underneath', 'embaixo/por baixo de/sob']
until_ = ['until', 'até']
up_ = ['up', 'acima/em cima/para cima']
with_ = ['with', 'com']
without_ = ['without', 'sem']

if __name__ == '__main__':

    print('\n')
    # print(bricks)
    #
    # print(f'{len(prep) = }')
    # print(f'{len(prep_pt_br) = }')
    # print(bricks)
    # print(f'{len(prep_main) = }')
    # print(f'{len(prep_main_pt_br) = }')
    # print(bricks)
    # print(f'{len(prep_direction_place) = }')
    # print(f'{len(prep_direction_place_pt_br) = }')
    # print(bricks)
    # print(f'{len(prep_time) = }')
    # print(f'{len(prep_time_pt_br) = }')
    # print(bricks)
    # print(f'{len(prep_short) = }')
    # print(f'{len(prep_short_pt_br) = }')
    # print(bricks)
    # print(f'{len(prep_others) = }')
    # print(f'{len(prep_others_pt_br) = }')
    # print(bricks)
    # print(f'{len(prep_phrasal_u) = }')
    # print(f'{len(prep_phrasal_l) = }')
    # print(f'{len(prep_phrasal_pt_br) = }')
    #
    # print('\n')
    # for word in zip(prep, prep_pt_br):
    #     print(word)
    #
    # print('\n')
    # for word in zip(prep_main, prep_main_pt_br):
    #     print(word)
    #
    # print('\n')
    # for word in zip(prep_direction_place, prep_direction_place_pt_br):
    #     print(word)
    #
    # print('\n')
    # for word in zip(prep_time, prep_time_pt_br):
    #     print(word)
    #
    # print('\n')
    # for word in zip(prep_short, prep_short_pt_br):
    #     print(word)
    #
    # print('\n')
    # for word in zip(prep_others, prep_others_pt_br):
    #     print(word)
    #
    # print('\n')
    # for word in zip(prep_phrasal_l, prep_phrasal_pt_br):
    #     print(word)

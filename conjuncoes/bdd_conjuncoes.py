

from metodos.bdd import data_collector as _, painter

conjunctions_l = [
    'and', 'that', 'but', 'or', 'as', 'if', 'when', 'than', 'because', 'while', 'where', 'after', 'though',
    'since', 'until', 'whether', 'before', 'although', 'nor', 'like', 'once', 'unless', 'now', 'except', 'otherwise'
]

conjunctions_l_pt_br = [
    'e', 'que', 'mas/porém', 'ou', 'como/tão quanto', 'se', 'quando', 'do que', 'pois/porque', 'enquanto',
    'aonde/onde', 'depois que', 'embora (final)', 'já que', 'até que', 'se', 'antes', 'embora (início)', 'nem',
    'como', 'uma vez que', 'a menos que/a não ser', 'agora/já', 'exceto', 'caso contrário'
]

conjunction = _(conjunctions_l)
conjunction_inked = painter('blue', conjunction)
conjunction_tr = conjunctions_l_pt_br[conjunctions_l.index(conjunction)]
conjunction_tr_inked = painter('red', conjunction_tr)

conjunction2 = _(conjunctions_l)
conjunction2_inked = painter('blue', conjunction2)
conjunction2_tr = conjunctions_l_pt_br[conjunctions_l.index(conjunction2)]
conjunction2_tr_inked = painter('red', conjunction2_tr)

while conjunction == conjunction2:
    conjunction2 = _(conjunctions_l)
    conjunction2_inked = painter('blue', conjunction)
    conjunction2_tr = conjunctions_l_pt_br[conjunctions_l.index(conjunction)]
    conjunction2_tr_inked = painter('red', conjunction_tr)

if __name__ == '__main__':
    for words in zip(conjunctions_l, conjunctions_l_pt_br):
        print(words[0])
        print(words[1])

    print(conjunction)
    print(conjunction_inked)
    print(conjunction_tr)
    print(conjunction_tr_inked)
    print(conjunction2)
    print(conjunction2_inked)
    print(conjunction2_tr)
    print(conjunction2_tr_inked)

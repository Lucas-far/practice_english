

# from random import choice
# from metodos.bdd import painter

present = [
    'say', 'says', 'go', 'goes', 'get', 'gets', 'make', 'makes', 'know', 'knows', 'think', 'thinks', 'take', 'takes',
    'see', 'sees', 'come', 'comes', 'want', 'wants',

    'look', 'looks', 'use', 'uses', 'find', 'finds', 'give', 'gives', 'tell', 'tells', 'work', 'works', 'call',
    'calls', 'try', 'tries', 'ask', 'asks', 'need', 'needs',

    'feel', 'feels', 'become', 'becomes', 'leave', 'leaves', 'put', 'puts', 'mean', 'means', 'keep', 'keeps', 'let',
    'lets', 'begin', 'begins', 'seem', 'seems', 'help', 'helps',

    'talk', 'talks', 'turn', 'turns', 'start', 'starts', 'show', 'shows', 'hear', 'hears', 'play', 'plays', 'run',
    'runs', 'move', 'moves', 'like', 'likes', 'live', 'lives',

    'believe', 'believes', 'hold', 'holds', 'bring', 'brings', 'happen', 'happens', 'write', 'writes', 'provide',
    'provides', 'sit', 'sits', 'stand', 'stands', 'lose', 'loses', 'pay', 'pays',

    'meet', 'meets', 'include', 'includes', 'continue', 'continues', 'set', 'sets', 'learn', 'learns', 'change',
    'changes', 'lead', 'leads', 'understand', 'understands', 'watch', 'watches', 'follow', 'follows',

    'stop', 'stops', 'create', 'creates', 'speak', 'speaks', 'read', 'reads', 'allow', 'allows', 'add', 'adds',
    'spend', 'spends', 'grow', 'grows', 'open', 'opens', 'walk', 'walks',

    'win', 'wins', 'offer', 'offers', 'remember', 'remembers', 'love', 'loves', 'consider', 'considers', 'appear',
    'appears', 'buy', 'buys', 'wait', 'waits', 'serve', 'serves', 'die', 'dies',

    'send', 'sends', 'expect', 'expects', 'build', 'builds', 'stay', 'stays', 'fall', 'falls', 'cut', 'cuts', 'reach',
    'reaches', 'kill', 'kills', 'remain', 'remains', 'suggest', 'suggests',

    'raise', 'raises', 'pass', 'passes', 'sell', 'sells', 'require', 'requires', 'report', 'reports', 'decide',
    'decides', 'pull', 'pulls', 'break', 'breaks', 'acquire', 'acquires', 'realize', 'realizes',

    'manage', 'manages', 'develop', 'develops', 'trust', 'trusts', 'imagine', 'imagines', 'step', 'steps', 'regret',
    'regrets', 'manipulate', 'manipulates', 'dream', 'dreams', 'discuss', 'discusses', 'drink', 'drinks',

    'eat', 'eats', 'skip', 'skips', 'repeat', 'repeats', 'guess', 'guesses', 'select', 'selects', 'click', 'clicks'
]

present_pt_br = [
    'dizem / falam', 'diz / fala', 'vão', 'vem', 'adquirem / conseguem / obtem / pegam',
    'adquire / consegue / obtem / pega', 'criam / fazem', 'cria / faz', 'conhecem / sabem', 'conhece / sabe',
    'acham / pensam', 'acha / pensa', 'levam / pegam / tomam', 'leva / pega / toma', 'vêem', 'vê', 'chegam / vêm',
    'chega / vêm', 'pretendem / querem', 'pretende / quer',

    'olham / vêem', 'olha / vê', 'usam', 'usa', 'acham / encontram', 'acha / encontra', 'dão', 'dá', 'contam / dizem',
    'conta / diz', 'funcionam / trabalham', 'funciona / trabalha', 'chamam / telefonam', 'chama / telefona',
    'experimentam / tentam', 'experimenta / tenta', 'pedem / perguntam', 'pede / pergunta', 'necessitam / precisam',
    'necessita / precisa',

    'sentem', 'sente', 'tornam-se', 'torna-se', 'abandonam / deixam / saem', 'abandona / deixa / sai', 'colocam / põem',
    'coloca / põe', 'querem dizer / significam', 'quer dizer / significa', 'continuam / guardam / mantêm',
    'continua / guarda / mantêm', 'deixam / permitem', 'deixa / permite', 'começam / iniciam', 'começa / inicia',
    'parecem', 'parece', 'ajudam / auxiliam', 'ajuda / auxilia',

    'conversam / falam', 'conversa / fala', 'transformam / viram', 'transforma / vira', 'começam / iniciam',
    'começa / inicia', 'apresentam / mostram', 'apresenta / mostra', 'escutam / ouvem', 'escuta / ouvi',
    'jogam / tocam', 'joga / toca', 'correm', 'corre', 'movem / mexem', 'move / mexe', 'gostam', 'gosta',
    'moram / vivem', 'mora / vive',

    'acreditam / crêem', 'acredita / crê', 'mantêm / seguram', 'mantêm / segura', 'trazem', 'traz',
    'acontecem / ocorrem', 'acontece / ocorre', 'escrevem', 'escreve', 'fornecem / proporcionam',
    'fornece / proporciona', 'sentam', 'senta', 'ficam / suportam', 'fica / suporta', 'perdem', 'perde', 'pagam',
    'paga',

    'conhecem / encontram', 'conhece / encontra', 'incluem', 'inclui', 'continuam', 'continua',
    'configuram / definem / estabelecem / põem', 'configura / define / estabelece / põe', 'aprendem', 'aprende',
    'alteram / mudam', 'altera / muda', 'conduzem / lideram', 'conduz / lidera', 'compreendem / entendem',
    'compreende / entende', 'olham / observam / vêem', 'olha / observa / vê', 'acompanham / seguem',
    'acompanha / segue',

    'impedem / param', 'impede / para', 'criam', 'cria', 'conversam / falam', 'conversa / fala', 'lêem', 'lê',
    'autorizam / permitem', 'autoriza / permite', 'acrescentam / adicionam', 'acrescenta / adiciona', 'gastam / passam',
    'gasta / passa', 'aumentam / crescem', 'aumenta / cresce', 'abrem', 'abre', 'andam / caminham', 'anda / caminha',

    'ganham / vencem', 'ganha / vence', 'oferecem / propõem', 'oferece / propõe', 'lembram / recordam',
    'lembra / recorda', 'adoram / amam', 'adora / ama', 'consideram', 'considera', 'aparecem', 'aparece', 'compram',
    'compra', 'esperam', 'espera', 'servem', 'serve', 'falecem / morrem', 'falece / morre',

    'enviam / mandam', 'envia / manda', 'esperam', 'espera', 'constroem', 'constroi', 'ficam / permanecem',
    'fica / permanece', 'caem', 'cai', 'cortam', 'corta', 'alcançam / atingem / chegam', 'alcança / atinge / chega',
    'matam', 'mata', 'ficam / permanecem', 'fica / permanece', 'sugerem', 'sugere',

    'aumentam / criam alguém,algo / levantam', 'aumenta / cria alguém,algo / levanta', 'passam', 'passa', 'vendem',
    'vende', 'exigem / necessitam', 'exige / necessita', 'relatam / reportam', 'relata / reporta', 'decidem', 'decide',
    'puxam', 'puxa', 'rompem / quebram', 'rompe / quebra', 'adquirem / compram / obtém', 'adquire / compra / obtém',
    'percebem / realizam', 'percebe / realiza',

    'administram / gerem', 'administra / gere', 'crescem / desenvolvem', 'cresce / desenvolve', 'confiam', 'confia',
    'imaginam', 'imagina', 'pisam', 'pisa', 'arrependem / lamentam', 'arrepende / lamenta', 'manipulam', 'manipula',
    'sonham', 'sonha', 'debatem / discutem', 'debate / discute', 'bebem', 'bebe',

    'comem', 'come', 'pulam / saltam', 'pula / salta', 'repetem', 'repete', 'adivinham / supõem', 'adivinha / supõe',
    'selecionam', 'seleciona', 'clicam', 'clica'
]

present_1st_2nd_persons = [
    'say', 'go', 'get', 'make', 'know', 'think', 'take', 'see', 'come', 'want', 'look', 'use', 'find', 'give', 'tell',
    'work', 'call', 'try', 'ask', 'need',

    'feel', 'become', 'leave', 'put', 'mean', 'keep', 'let', 'begin', 'seem', 'help', 'talk', 'turn', 'start', 'show',
    'hear', 'play', 'run', 'move', 'like', 'live',

    'believe', 'hold', 'bring', 'happen', 'write', 'provide', 'sit', 'stand', 'lose', 'pay', 'meet', 'include',
    'continue', 'set', 'learn', 'change', 'lead', 'understand', 'watch', 'follow',

    'stop', 'create', 'speak', 'read', 'allow', 'add', 'spend', 'grow', 'open', 'walk', 'win', 'offer', 'remember',
    'love', 'consider', 'appear', 'buy', 'wait', 'serve', 'die',

    'send', 'expect', 'build', 'stay', 'fall', 'cut', 'reache', 'kill', 'remain', 'suggest', 'raise', 'pass', 'sell',
    'require', 'report', 'decide', 'pull', 'break', 'acquire', 'realize',

    'manage', 'develop', 'trust', 'imagine', 'step', 'regret', 'manipulate', 'dream', 'discuss', 'drink', 'eat', 'skip',
    'repeat', 'guess', 'select', 'click'
]

present_1st_2nd_persons_pt_br = [
    'dizem / falam', 'vão', 'adquirem / conseguem / obtem / pegam', 'criam / fazem', 'conhecem / sabem',
    'acham / pensam', 'levam / pegam / tomam', 'vêem', 'chegam / vêm', 'pretendem / querem', 'olham / vêem', 'usam',
    'acham / encontram', 'dão', 'contam / dizem', 'funcionam / trabalham', 'chamam / telefonam',
    'experimentam / tentam', 'pedem / perguntam', 'necessitam / precisam',

    'sentem', 'tornam-se', 'abandonam / deixam / saem', 'colocam / põem', 'significam', 'continuam / guardam / mantêm',
    'deixam / permitem', 'começam / iniciam', 'parecem', 'ajudam / auxiliam', 'conversam / falam',
    'transformam / viram', 'começam / iniciam', 'apresentam / mostram', 'escutam / ouvem', 'jogam / tocam', 'correm',
    'movem / mexem', 'gostam', 'moram / vivem',

    'acreditam / crêem', 'mantêm / seguram', 'trazem', 'acontecem / ocorrem', 'escrevem', 'fornecem / proporcionam',
    'sentam', 'levantam / permanecem', 'perdem', 'pagam', 'conhecem / encontram', 'incluem', 'continuam',
    'configuram / definem / estabelecem / põem', 'aprendem', 'alteram / mudam', 'conduzem / lideram',
    'compreendem / entendem', 'olham / observam / vêem', 'acompanham / seguem',

    'impedem / param', 'criam', 'conversam / falam', 'lêem', 'autorizam / permitem', 'acrescentam / adicionam',
    'gastam / passam', 'aumentam / crescem', 'abrem', 'andam / caminham', 'ganham / vencem', 'oferecem / propõem',
    'lembram / recordam', 'adoram / amam', 'consideram', 'aparecem', 'compram', 'esperam', 'servem', 'falecem / morrem',

    'enviam / mandam', 'esperam', 'constroem', 'ficam / permanecem', 'caem', 'cortam', 'alcançam / atingem / chegam',
    'matam', 'ficam / permanecem', 'sugerem', 'aumentam / criam alguém,algo / levantam', 'passam', 'vendem',
    'exigem / necessitam', 'relatam / reportam', 'decidem', 'puxam', 'rompem / quebram', 'adquirem / compram / obtém',
    'percebem / realizam',

    'administram / gerem', 'crescem / desenvolvem', 'confiam', 'imaginam', 'pisam', 'arrependem / lamentam',
    'manipulam', 'sonham', 'debatem / discutem', 'bebem', 'comem', 'pulam / saltam', 'repetem', 'adivinham / supõem',
    'selecionam', 'clicam'
]

present_3rd_person = [
    'says', 'goes', 'gets', 'makes', 'knows', 'thinks', 'takes', 'sees', 'comes', 'wants', 'looks', 'uses', 'finds',
    'gives', 'tells', 'works', 'calls', 'tries', 'asks', 'needs',

    'feels', 'becomes', 'leaves', 'puts', 'means', 'keeps', 'lets', 'begins', 'seems', 'helps', 'talks', 'turns',
    'starts', 'shows', 'hears', 'plays', 'runs', 'moves', 'likes', 'lives',

    'believes', 'holds', 'brings', 'happens', 'writes', 'provides', 'sits', 'stands', 'loses', 'pays', 'meets',
    'includes', 'continues', 'sets', 'learns', 'changes', 'leads', 'understands', 'watches', 'follows',

    'stops', 'creates', 'speaks', 'reads', 'allows', 'adds', 'spends', 'grows', 'opens', 'walks', 'wins', 'offers',
    'remembers', 'loves', 'considers', 'appears', 'buys', 'waits', 'serves', 'dies',

    'sends', 'expects', 'builds', 'stays', 'falls', 'cuts', 'reaches', 'kills', 'remains', 'suggests', 'raises',
    'passes', 'sells', 'requires', 'reports', 'decides', 'pulls', 'breaks', 'acquires', 'realizes',

    'manages', 'develops', 'trusts', 'imagines', 'steps', 'regrets', 'manipulates', 'dreams', 'discusses', 'drinks',
    'eats', 'skips', 'repeats', 'guesses', 'selects', 'clicks'
]

present_3rd_person_pt_br = [
    'diz / fala', 'vem', 'adquire / consegue / obtem / pega', 'cria / faz', 'conhece / sabe', 'acha / pensa',
    'leva / pega / toma', 'vê', 'chega / vêm', 'pretende / quer', 'olha / vê', 'usa', 'acha / encontra', 'dá',
    'conta / diz', 'funciona / trabalha', 'chama / telefona', 'experimenta / tenta', 'pede / pergunta',
    'necessita / precisa',

    'sente', 'torna-se', 'abandona / deixa / sai', 'coloca / põe', 'quer dizer / significa',
    'continua / guarda / mantêm', 'deixa / permite', 'começa / inicia', 'parece', 'ajuda / auxilia', 'conversa / fala',
    'transforma / vira', 'começa / inicia', 'apresenta / mostra', 'escuta / ouvi', 'joga / toca', 'corre',
    'move / mexe', 'gosta', 'mora / vive',

    'acredita / crê', 'mantêm / segura', 'traz', 'acontece / ocorre', 'escreve', 'fornece / proporciona', 'senta',
    'levanta / permanece', 'perde', 'paga', 'conhece / encontra', 'inclui', 'continua',
    'configura / define / estabelece / põe', 'aprende', 'altera / muda', 'conduz / lidera', 'compreende / entende',
    'olha / observa / vê', 'acompanha / segue',

    'impede / para', 'cria', 'conversa / fala', 'lê', 'autoriza / permite', 'acrescenta / adiciona', 'gasta / passa',
    'aumenta / cresce', 'abre', 'anda / caminha', 'ganha / vence', 'oferece / propõe', 'lembra / recorda',
    'adora / ama', 'considera', 'aparece', 'compra', 'espera', 'serve', 'falece / morre',

    'envia / manda', 'espera', 'constroi', 'fica / permanece', 'cai', 'corta', 'alcança / atinge / chega', 'mata',
    'fica / permanece', 'sugeri', 'aumenta / cria alguém,algo / levanta', 'passa', 'vende', 'exige / necessita',
    'relata / reporta', 'decide', 'puxa', 'rompe / quebra', 'adquire / compra / obtém', 'percebe / realiza',

    'administra / gere', 'cresce / desenvolve', 'confia', 'imagina', 'pisa', 'arrepende / lamenta', 'manipula', 'sonha',
    'debate / discute', 'bebe', 'come', 'pula / salta', 'repete', 'adivinha / supõe', 'seleciona', 'clica'
]

# set_box_present = set({})
#
# while len(set_box_present) < 1:
#     set_box_present.add(choice(present))
#
# set_box_present = list(set_box_present)
#
# verb_present = set_box_present[0]
# verb_present_inked = painter('blue', verb_present)
# verb_present_tr = present_pt_br[present.index(verb_present)]
# verb_present_tr_inked = painter('red', verb_present_tr)

if __name__ == '__main__':
    print('\n')

    for words in zip(present_1st_2nd_persons, present_3rd_person):
        print(words)

    print('\n')

    print(f"{len(present)} é igual a {len(present_1st_2nd_persons) + len(present_3rd_person)}? {len(present) == len(present_1st_2nd_persons) + len(present_3rd_person)}")

    print('\n')

    print(f"{len(present_1st_2nd_persons_pt_br) = }")
    print(f"{len(present_3rd_person_pt_br) = }")

    # print(verb_present)
    # print(verb_present_inked)
    # print(verb_present_tr)
    # print(verb_present_tr_inked)

    # for words in zip(present, present_pt_br):
    #     print(words[0])
    #     print(words[1])

    # print(f"{len(pst) = }")
    # print(f"{len(pst_pt_br) = }")
    # for words in zip(pst, pst_pt_br):
    #     print(words)

    # print(f"{len(pst_1st_2nd_persons) = }")
    # print(f"{len(pst_1st_2nd_persons_pt_br) = }")
    # for words in zip(pst_1st_2nd_persons, pst_1st_2nd_persons_pt_br):
    #     print(words)

    # print(f"{len(pst_3rd_person) = }")
    # print(f"{len(pst_3rd_person_pt_br) = }")
    # for words in zip(pst_3rd_person, pst_3rd_person_pt_br):
    #     print(words)

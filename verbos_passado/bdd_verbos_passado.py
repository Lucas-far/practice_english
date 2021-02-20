

# 'was', 'were', 'had', 'did',
# past = [
#     'said', 'went',
#     'got', 'made', 'knew', 'thought', 'took', 'saw',
#     'came', 'wanted', 'looked', 'used', 'found', 'gave', 'told',
#     'worked', 'called', 'tried', 'asked', 'needed',
#     'felt', 'became', 'left', 'put', 'meant', 'kept',
#     'let', 'began', 'seemed', 'helped', 'talked', 'turned',
#     'started', 'showed', 'heard', 'played', 'ran', 'moved', 'liked',
#     'lived', 'believed', 'held', 'brought', 'happened', 'wrote',
#     'provided', 'sat', 'stood', 'lost', 'paid', 'met',
#     'included', 'continued', 'set', 'learned', 'changed', 'led',
#
#     'understood', 'watched', 'followed',
#     'stopped', 'created', 'spoke', 'read', 'allowed', 'added', 'spent',
#     'grew', 'opened', 'walked', 'won', 'offered', 'remembered',
#     'loved', 'considered', 'appeared', 'bought', 'waited', 'served', 'died', 'sent',
#     'expected', 'built', 'stayed', 'fell', 'cut', 'reached', 'killed',
#     'remained', 'suggested', 'rose', 'passed', 'sold', 'required',
#     'reported', 'decided', 'pulled', 'broke', 'acquired', 'realized',
#     'managed', 'developed', 'trusted', 'imagined', 'stepped', 'regreted', 'manipulated',
#     'dreamed', 'discussed', 'drank', 'ate', 'skept', 'saw', 'repeated', 'knew',
#     'guessed', 'selected', 'clicked',
# ]

# 'era/estava/fiquei', 'eram/estavam/ficaram', 'possui/tive', 'fiz',
# past_pt_br = [
#     'disse/falei', 'fui',
#     'adquiri/consegui/obtive/peguei', 'criei/fiz', 'conheci/sabia', 'achei/pensei', 'levei/peguei/tomei', 'vi',
#     'cheguei/vim', 'pretendia/queria', 'olhei/vi', 'usei', 'achei/encontrei', 'dei', 'contei/disse',
#     'funcionei/trabalhei', 'chamei/telefonei', 'experimentei/tentei', 'pedi/perguntei', 'necessitei/precisei',
#     'senti', 'me tornei', 'abandonei/deixei/sai', 'coloquei/pus', 'signifiquei', 'continuei/guardei/mantive',
#     'deixei/permiti', 'começei/iniciei', 'pareci', 'ajudei/auxiliei', 'conversei/falei', 'transformei/virei',
#     'começei/iniciei', 'apresentei/mostrei', 'escutei/ouvi', 'joguei/toquei', 'corri', 'movi/mexi', 'gostei',
#     'morei/vivi', 'acreditei/cri', 'mantive/segurei', 'trouxe', 'aconteci/ocorri', 'escrevi',
#     'forneci/proporcionei', 'sentei', 'levantei/permaneci', 'perdi', 'paguei', 'conheci/encontrei/reuni',
#     'inclui', 'continuei', 'configurei/defini/estabeleci/pus', 'aprendi', 'alterei/mudei', 'conduzi/liderei',
#
#     'compreender/entender', 'olhar/observar/ver', 'acompanhar/seguir',
#     'impedir/parar', 'criar', 'conversar/falar', 'ler', 'autorizar/permitir', 'acrescentar/adicionar', 'gastar/passar',
#     'aumentar/crescer', 'abrir', 'andar/caminhar', 'ganhar/vencer', 'oferecer/propor', 'lembrar/recordar',
#     'adorar/amar', 'considerar', 'aparecer', 'comprar', 'esperar', 'servir', 'falecer/morrer', 'enviar/mandar',
#     'esperar', 'construir', 'ficar/permanecer', 'cair', 'cortar', 'alcançar/atingir/chegar a', 'matar',
#     'ficar/permanecer', 'sugerir', 'aumentar/criar alguém,algo/levantar', 'passar', 'vender', 'exigir/necessitar',
#     'relatar/reportar', 'decidir', 'puxar', 'romper/quebrar', 'adquirir/comprar/obter', 'perceber/realizar',
#     'administrar/gerir', 'crescer/desenvolver', 'confiar', 'imaginar', 'pisar', 'arrepender/lamentar', 'manipular',
#     'sonhar', 'debater/discutir', 'beber', 'comer', 'pular/saltar', 'ver', 'repetir', 'conhecer/saber',
#     'adivinhar/supor', 'selecionar', 'clicar',
# ]

# var = {
#     'to say': ('said', 'disse/falei'),
#     'to go': ('went', 'fui'),
#     'to get': ('got', 'adquiri/consegui/obtive/peguei'),
#     'to make': ('made', 'criei/fiz'),
#     'to know': ('knew', 'conheci/sabia'),
#     'to think': ('thought', 'achei/pensei'),
#     'to take': ('took', 'levei/peguei/tomei'),
#     'to see': ('saw', 'vi'),
#     'to come': ('came', 'cheguei/vim'),
#     'to want': ('wanted', 'pretendia/queria'),
#     'to look': ('looked', 'olhei/vi'),
#     'to use': ('used', 'usei'),
#     'to find': ('found', 'achei/encontrei'),
#     'to give': ('gave', 'dei'),
#     'to tell': ('told', 'contei/disse'),
#     'to work': ('worked', 'funcionei/trabalhei'),
#     'to call': ('called', 'chamei/telefonei'),
#     'to try': ('tried', 'experimentei/tentei'),
#     'to ask': ('asked', 'pedi/perguntei'),
#     'to need': ('needed', 'necessitei/precisei'),
#     'to feel': ('felt', 'senti'),
#     'to become': ('became', 'me tornei'),
#     'to leave': ('left', 'abandonei/deixei/sai'),
#     'to put': ('put', 'coloquei/pus'),
#     'to mean': ('meant', 'quis dizer/signifiquei'),
#     'to keep': ('kept', 'continuei/guardei/mantive'),
#     'to let': ('let', 'deixei/permiti'),
#     'to begin': ('began', 'começei/iniciei'),
#     'to seem': ('seemed', 'pareci'),
#     'to help': ('helped', 'ajudei/auxiliei'),
#     'to talk': ('talked', 'conversei/falei'),
#     'to turn': ('turned', 'transformei/virei'),
#     'to start': ('started', 'começei/iniciei'),
#     'to show': ('showed', 'apresentei/mostrei'),
#     'to hear': ('heard', 'escutei/ouvi'),
#     'to play': ('played', 'joguei/toquei'),
#     'to run': ('ran', 'corri'),
#     'to move': ('moved', 'movi/mexi'),
#     'to like': ('liked', 'gostei'),
#     'to live': ('lived', 'morei/vivi'),
#     'to believe': ('believed', 'acreditei/cri'),
#     'to hold': ('held', 'mantive/segurei'),
#     'to bring': ('brought', 'trouxe'),
#     'to happen': ('happened', 'aconteci/ocorri'),
#     'to write': ('wrote', 'escrevi'),
#     'to provide': ('provided', 'forneci/proporcionei'),
#     'to sit': ('sat', 'sentei'),
#     'to stand': ('stood', 'levantei/permaneci'),
#     'to lose': ('lost', 'perdi'),
#     'to pay': ('paid', 'paguei'),
#     'to meet': ('met', 'conheci/encontrei/reuni'),
#     'to include': ('included', 'inclui'),
#     'to continue': ('continued', 'continuei'),
#     'to set': ('set', 'configurei/defini/estabeleci/pus'),
#     'to learn': ('learned', 'aprendi'),
#     'to change': ('changed', 'alterei/mudei'),
#     'to lead': ('led', 'conduzi/liderei'),
#     'to understand': ('understood', 'compreendi/entendi'),
#     'to watch': ('watched', 'olhei/observei/vi'),
#     'to follow': ('followed', 'acompanhei/segui'),
#     'to stop': ('stopped', 'impedi/parei'),
#     'to create': ('created', 'criei'),
#     'to speak': ('spoke', 'conversei/falei'),
#     'to read': ('read', 'li'),
#     'to allow': ('allowed', 'autorizei/permiti'),
#     'to add': ('added', 'acrescentei/adicionei'),
#     'to spend': ('spent', 'gastei/passei'),
#     'to grow': ('grew', 'aumentei/cresci'),
#     'to open': ('opened', 'abri'),
#     'to walk': ('walked', 'andei/caminhei'),
#     'to win': ('won', 'ganhei/venci'),
#     'to offer': ('offered', 'ofereci/propus'),
#     'to remember': ('remembered', 'lembrei/recordei'),
#     'to love': ('loved', 'adorei/amei'),
#     'to consider': ('considered', 'considerei'),
#     'to appear': ('appeared', 'apareci'),
#     'to buy': ('bought', 'comprei'),
#     'to wait': ('waited', 'esperei'),
#     'to serve': ('served', 'servi'),
#     'to die': ('died', 'faleci/morri'),
#     'to send': ('sent', 'enviei/mandei'),
#     'to expect': ('expected', 'esperei'),
#     'to build': ('built', 'construi'),
#     'to stay': ('stayed', 'fiquei/permaneci'),
#     'to fall': ('fell', 'cai'),
#     'to cut': ('cut', 'cortei'),
#     'to reach': ('reached', 'alcançei/atingi/cheguei a'),
#     'to kill': ('killed', 'matei'),
#     'to remain': ('remained', 'fiquei/permaneci'),
#     'to suggest': ('suggested', 'sugeri'),
#     'to raise': ('rose', 'aumentei/criei alguém,algo/levantei'),
#     'to pass': ('passed', 'passei'),
#     'to sell': ('sold', 'vendi'),
#     'to require': ('required', 'exigi/necessitei'),
#     'to report': ('reported', 'relatei/reportei'),
#     'to decide': ('decided', 'decidi'),
#     'to pull': ('pulled', 'puxei'),
#     'to break': ('broke', 'rompi/quebrei'),
#     'to acquire': ('acquired', 'adquiri/comprei/obtive'),
#     'to realize': ('realized', 'percebi/realizei'),
#     'to manage': ('managed', 'administrei/geri'),
#     'to develop': ('developed', 'cresci/desenvolvi'),
#     'to trust': ('trusted', 'confiei'),
#     'to imagine': ('imagined', 'imaginei'),
#     'to step': ('stepped', 'pisei'),
#     'to regret': ('regreted', 'arrependi/lamentei'),
#     'to manipulate': ('manipulated', 'manipulei'),
#     'to dream': ('dreamed', 'sonhei'),
#     'to discuss': ('discussed', 'debati/discuti'),
#     'to drink': ('drank', 'bebi'),
#     'to eat': ('ate', 'comi'),
#     'to skip': ('skept', 'pulei/saltei'),
#     'to repeat': ('repeated', 'repeti'),
#     'to guess': ('guessed', 'adivinhei/supus'),
#     'to select': ('selected', 'selecionei'),
#     'to click': ('clicked', 'cliquei'),
# }  # 'to say': ('said', 'disse/falei')

var = {
    'to say': ('said', 'disse/falei'),
    'to go': ('went', 'fui'),
    'to get': ('got', 'adquiri/consegui/obtive/peguei'),
    'to make': ('made', 'criei/fiz'),
    'to know': ('knew', 'conheci/sabia'),
    'to think': ('thought', 'achei/pensei'),
    'to take': ('took', 'levei/peguei/tomei'),
    'to see': ('saw', 'vi'),
    'to come': ('came', 'cheguei/vim'),
    'to find': ('found', 'achei/encontrei'),
    'to give': ('gave', 'dei'),
    'to tell': ('told', 'contei/disse'),
    'to feel': ('felt', 'senti'),
    'to become': ('became', 'me tornei'),
    'to leave': ('left', 'abandonei/deixei/sai'),
    'to mean': ('meant', 'quis dizer/signifiquei'),
    'to keep': ('kept', 'continuei/guardei/mantive'),
    'to hear': ('heard', 'escutei/ouvi'),
    'to run': ('ran', 'corri'),
    'to hold': ('held', 'mantive/segurei'),
    'to bring': ('brought', 'trouxe'),
    'to write': ('wrote', 'escrevi'),
    'to sit': ('sat', 'sentei'),
    'to stand': ('stood', 'levantei/permaneci'),
    'to lose': ('lost', 'perdi'),
    'to pay': ('paid', 'paguei'),
    'to meet': ('met', 'conheci/encontrei/reuni'),
    'to lead': ('led', 'conduzi/liderei'),
    'to understand': ('understood', 'compreendi/entendi'),
    'to speak': ('spoke', 'conversei/falei'),
    'to spend': ('spent', 'gastei/passei'),
    'to grow': ('grew', 'aumentei/cresci'),
    'to win': ('won', 'ganhei/venci'),
    'to buy': ('bought', 'comprei'),
    'to send': ('sent', 'enviei/mandei'),
    'to build': ('built', 'construi'),
    'to fall': ('fell', 'cai'),
    'to raise': ('rose', 'aumentei/criei alguém,algo/levantei'),
    'to sell': ('sold', 'vendi'),
    'to break': ('broke', 'rompi/quebrei'),
    'to drink': ('drank', 'bebi'),
    'to eat': ('ate', 'comi'),
    'to skip': ('skept', 'pulei/saltei'),
}

past = [
    'said', 'went', 'got', 'made', 'knew', 'thought', 'took', 'saw', 'came', 'wanted', 'looked', 'used', 'found',
    'gave', 'told', 'worked', 'called', 'tried', 'asked', 'needed',

    'felt', 'became', 'left', 'put', 'meant', 'kept', 'let', 'began', 'seemed', 'helped', 'talked', 'turned', 'started',
    'showed', 'heard', 'played', 'ran', 'moved', 'liked', 'lived',

    'believed', 'held', 'brought', 'happened', 'wrote', 'provided', 'sat', 'stood', 'lost', 'paid', 'met', 'included',
    'continued', 'set', 'learned', 'changed', 'led', 'understood', 'watched', 'followed',

    'stopped', 'created', 'spoke', 'read', 'allowed', 'added', 'spent', 'grew', 'opened', 'walked', 'won', 'offered',
    'remembered', 'loved', 'considered', 'appeared', 'bought', 'waited', 'served', 'died',

    'sent', 'expected', 'built', 'stayed', 'fell', 'cut', 'reached', 'killed', 'remained', 'suggested', 'rose',
    'passed', 'sold', 'required', 'reported', 'decided', 'pulled', 'broke', 'acquired', 'realized',

    'managed', 'developed', 'trusted', 'imagined', 'stepped', 'regreted', 'manipulated', 'dreamed', 'discussed',
    'drank', 'ate', 'skept', 'repeated', 'guessed', 'selected', 'clicked'
]

past_pt_br = [
    'disse/falei', 'fui', 'adquiri/consegui/obtive/peguei', 'criei/fiz', 'conheci/sabia', 'achei/pensei',
    'levei/peguei/tomei', 'vi', 'cheguei/vim', 'pretendia/queria', 'olhei/vi', 'usei', 'achei/encontrei', 'dei',
    'contei/disse', 'funcionei/trabalhei', 'chamei/telefonei', 'experimentei/tentei', 'pedi/perguntei',
    'necessitei/precisei',

    'senti', 'me tornei', 'abandonei/deixei/sai', 'coloquei/pus', 'quis dizer/signifiquei', 'continuei/guardei/mantive',
    'deixei/permiti', 'começei/iniciei', 'pareci', 'ajudei/auxiliei', 'conversei/falei', 'transformei/virei',
    'começei/iniciei', 'apresentei/mostrei', 'escutei/ouvi', 'joguei/toquei', 'corri', 'movi/mexi', 'gostei',
    'morei/vivi',

    'acreditei/cri', 'mantive/segurei', 'trouxe', 'aconteci/ocorri', 'escrevi', 'forneci/proporcionei', 'sentei',
    'levantei/permaneci', 'perdi', 'paguei', 'conheci/encontrei/reuni', 'inclui', 'continuei',
    'configurei/defini/estabeleci/pus', 'aprendi', 'alterei/mudei', 'conduzi/liderei', 'compreendi/entendi',
    'olhei/observei/vi', 'acompanhei/segui',

    'impedi/parei', 'criei', 'conversei/falei', 'li', 'autorizei/permiti', 'acrescentei/adicionei', 'gastei/passei',
    'aumentei/cresci', 'abri', 'andei/caminhei', 'ganhei/venci', 'ofereci/propus', 'lembrei/recordei', 'adorei/amei',
    'considerei', 'apareci', 'comprei', 'esperei', 'servi', 'faleci/morri',

    'enviei/mandei', 'esperei', 'construi', 'fiquei/permaneci', 'cai', 'cortei', 'alcançei/atingi/cheguei a', 'matei',
    'fiquei/permaneci', 'sugeri', 'aumentei/criei alguém,algo/levantei', 'passei', 'vendi', 'exigi/necessitei',
    'relatei/reportei', 'decidi', 'puxei', 'rompi/quebrei', 'adquiri/comprei/obtive', 'percebi/realizei',

    'administrei/geri', 'cresci/desenvolvi', 'confiei', 'imaginei', 'pisei', 'arrependi/lamentei', 'manipulei',
    'sonhei', 'debati/discuti', 'bebi', 'comi', 'pulei/saltei', 'repeti', 'adivinhei/supus', 'selecionei', 'cliquei'
]

past_irregular = [
    'said', 'went', 'got', 'made', 'knew', 'thought', 'took', 'saw', 'came', 'found', 'gave', 'told', 'felt', 'became',
    'left', 'meant', 'kept', 'heard', 'ran', 'held',

    'brought', 'wrote', 'sat', 'stood', 'lost', 'paid', 'met', 'led', 'understood', 'spoke', 'spent', 'grew', 'won',
    'bought', 'sent', 'built', 'fell', 'rose', 'sold', 'broke',

    'drank', 'ate', 'skept'
]

past_irregular_pt_br = [
    'disse/falei', 'fui', 'adquiri/consegui/obtive/peguei', 'criei/fiz', 'conheci/sabia', 'achei/pensei',
    'levei/peguei/tomei', 'vi', 'cheguei/vim', 'achei/encontrei', 'dei', 'contei/disse', 'senti', 'me tornei',
    'abandonei/deixei/sai', 'quis dizer/signifiquei', 'continuei/guardei/mantive', 'escutei/ouvi', 'corri',
    'mantive/segurei',

    'trouxe', 'escrevi', 'sentei', 'levantei/permaneci', 'perdi', 'paguei', 'conheci/encontrei/reuni',
    'conduzi/liderei', 'compreendi/entendi', 'conversei/falei', 'gastei/passei', 'aumentei/cresci',
    'ganhei/venci', 'comprei', 'enviei/mandei', 'construi', 'cai', 'aumentei/criei alguém,algo/levantei',
    'vendi', 'rompi/quebrei',

    'bebi', 'comi', 'pulei/saltei'
]

if __name__ == '__main__':
    print('\n')
    print(f"{len(past) = }")
    print(f"{len(past_pt_br) = }")

    for words in zip(past, past_pt_br):
        print(words)

    print('\n')
    print(f"{len(past_irregular) = }")
    print(f"{len(past_irregular_pt_br) = }")

    for words in zip(past_irregular, past_irregular_pt_br):
        print(words)

    # for words in var.values():
    #     print(f"'{words[0]}',")

    # for words in var.values():
    #     print(f"'{words[1]}',")

    print(past_irregular[40 - 1])

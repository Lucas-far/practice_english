

from random import choice
from metodos.bdd import painter

# 'to be', 'to have', 'to do',
verbs_infinitive = [
    'to say', 'to go', 'to get', 'to make', 'to know', 'to think', 'to take', 'to see', 'to come', 'to want', 'to look',
    'to use', 'to find', 'to give', 'to tell', 'to work', 'to call', 'to try', 'to ask', 'to need',

    'to feel', 'to become', 'to leave', 'to put', 'to mean', 'to keep', 'to let', 'to begin', 'to seem', 'to help',
    'to talk', 'to turn', 'to start', 'to show', 'to hear', 'to play', 'to run', 'to move', 'to like', 'to live',

    'to believe', 'to hold', 'to bring', 'to happen', 'to write', 'to provide', 'to sit', 'to stand', 'to lose',
    'to pay', 'to meet', 'to include', 'to continue', 'to set', 'to learn', 'to change', 'to lead', 'to understand',
    'to watch', 'to follow',

    'to stop', 'to create', 'to speak', 'to read', 'to allow', 'to add', 'to spend', 'to grow', 'to open', 'to walk',
    'to win', 'to offer', 'to remember', 'to love', 'to consider', 'to appear', 'to buy', 'to wait', 'to serve',
    'to die',

    'to send', 'to expect', 'to build', 'to stay', 'to fall', 'to cut', 'to reach', 'to kill', 'to remain',
    'to suggest', 'to raise', 'to pass', 'to sell', 'to require', 'to report', 'to decide', 'to pull', 'to break',
    'to acquire', 'to realize',


    'to manage', 'to develop', 'to trust', 'to imagine', 'to step', 'to regret', 'to manipulate', 'to dream',
    'to discuss', 'to drink', 'to eat', 'to skip', 'to see', 'to repeat', 'to know', 'to guess', 'to select',
    'to click',
]

# 'ser/estar/ficar', 'possuir/ter', 'fazer',
verbs_infinitive_pt_br = [
    'dizer/falar', 'ir', 'adquirir/conseguir/obter/pegar', 'criar/fazer', 'conhecer/saber', 'achar/pensar',
    'levar/pegar/tomar', 'ver', 'chegar/vir', 'pretender/querer', 'olhar/ver', 'usar', 'achar/encontrar', 'dar',
    'contar/dizer', 'funcionar/trabalhar', 'chamar/telefonar', 'experimentar/tentar', 'pedir/perguntar',
    'necessitar/precisar',

    'sentir', 'tornar-se', 'abandonar/deixar/sair', 'colocar/pôr', 'querer dizer/significar',
    'continuar/guardar/manter', 'deixar/permitir', 'começar/iniciar', 'parecer', 'ajudar/auxiliar', 'conversar/falar',
    'transformar/virar', 'começar/iniciar', 'apresentar/mostrar', 'escutar/ouvir', 'jogar/tocar', 'correr',
    'mover/mexer', 'gostar', 'morar/viver',

    'acreditar/crer', 'manter/segurar', 'trazer', 'acontecer/ocorrer', 'escrever', 'fornecer/proporcionar', 'sentar',
    'levantar/permanecer', 'perder', 'pagar', 'conhecer/encontrar/reunir', 'incluir', 'continuar',
    'configurar/definir/estabelecer/pôr', 'aprender', 'alterar/mudar', 'conduzir/liderar', 'compreender/entender',
    'olhar/observar/ver', 'acompanhar/seguir',


    'impedir/parar', 'criar', 'conversar/falar', 'ler', 'autorizar/permitir', 'acrescentar/adicionar', 'gastar/passar',
    'aumentar/crescer', 'abrir', 'andar/caminhar', 'ganhar/vencer', 'oferecer/propor', 'lembrar/recordar',
    'adorar/amar', 'considerar', 'aparecer', 'comprar', 'esperar', 'servir', 'falecer/morrer',

    'enviar/mandar', 'esperar', 'construir', 'ficar/permanecer', 'cair', 'cortar', 'alcançar/atingir/chegar a', 'matar',
    'ficar/permanecer', 'sugerir', 'aumentar/criar alguém,algo/levantar', 'passar', 'vender', 'exigir/necessitar',
    'relatar/reportar', 'decidir', 'puxar', 'romper/quebrar', 'adquirir/comprar/obter', 'perceber/realizar',


    'administrar/gerir', 'crescer/desenvolver', 'confiar', 'imaginar', 'pisar', 'arrepender/lamentar', 'manipular',
    'sonhar', 'debater/discutir', 'beber', 'comer', 'pular/saltar', 'ver', 'repetir', 'conhecer/saber',
    'adivinhar/supor', 'selecionar', 'clicar',
]

set_box_infinitive = set({})

while len(set_box_infinitive) < 1:
    set_box_infinitive.add(choice(verbs_infinitive))

set_box_infinitive = list(set_box_infinitive)

verb_infinitive = set_box_infinitive[0]
verb_infinitive_inked = painter('blue', verb_infinitive)
verb_infinitive_tr = verbs_infinitive_pt_br[verbs_infinitive.index(verb_infinitive)]
verb_infinitive_tr_inked = painter('red', verb_infinitive_tr)

if __name__ == '__main__':
    print('\n')
    # print(verb_infinitive)
    # print(verb_infinitive_inked)
    # print(verb_infinitive_tr)
    # print(verb_infinitive_tr_inked)

    # print(f"{len(verbs_infinitive)}")
    # print(f"{len(verbs_infinitive_pt_br)}")
    # print('\n')
    # for words in zip(verbs_infinitive, verbs_infinitive_pt_br):
    #     print(words)

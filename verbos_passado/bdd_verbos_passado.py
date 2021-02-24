

from random import choice
from metodos.bdd import painter

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
    'fiquei/suportei', 'perdi', 'paguei', 'conheci/encontrei/reuni', 'inclui', 'continuei',
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

set_box_past = set({})

while len(set_box_past) < 1:
    set_box_past.add(choice(past))

set_box_past = list(set_box_past)

verb_past = set_box_past[0]
verb_past_inked = painter('blue', verb_past)
verb_past_tr = past_pt_br[past.index(verb_past)]
verb_past_tr_inked = painter('red', verb_past_tr)

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

    print(verb_past)
    print(verb_past_inked)
    print(verb_past_tr)
    print(verb_past_tr_inked)

    # for words in var.values():
    #     print(f"'{words[0]}',")

    # for words in var.values():
    #     print(f"'{words[1]}',")

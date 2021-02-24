

from random import choice
from metodos.bdd import painter

future = [
    'will say', 'will go', 'will get', 'will make', 'will know', 'will think', 'will take', 'will see', 'will come',
    'will want', 'will look', 'will use', 'will find', 'will give', 'will tell', 'will work', 'will call', 'will try',
    'will ask', 'will need',

    'will feel', 'will become', 'will leave', 'will put', 'will mean', 'will keep', 'will let',
    'will begin', 'will seem', 'will help', 'will talk', 'will turn', 'will start', 'will show', 'will hear',
    'will play', 'will run', 'will move', 'will like', 'will live',

    'will believe', 'will hold', 'will bring', 'will happen', 'will write', 'will provide', 'will sit', 'will stand',
    'will lose', 'will pay', 'will meet', 'will include', 'will continue', 'will set', 'will learn', 'will change',
    'will lead', 'will understand', 'will watch', 'will follow',

    'will stop', 'will create', 'will speak', 'will read', 'will allow', 'will add', 'will spend', 'will grow',
    'will open', 'will walk', 'will win', 'will offer', 'will remember', 'will love', 'will consider', 'will appear',
    'will buy', 'will wait', 'will serve', 'will die',

    'will send', 'will expect', 'will build', 'will stay', 'will fall', 'will cut', 'will reache', 'will kill',
    'will remain', 'will suggest', 'will raise', 'will pass', 'will sell', 'will require', 'will report', 'will decide',
    'will pull', 'will break', 'will acquire', 'will realize',

    'will manage', 'will develop', 'will trust', 'will imagine', 'will step',
    'will regret', 'will manipulate', 'will dream', 'will discuss', 'will drink', 'will eat', 'will skip',
    'will repeat', 'will guess', 'will select', 'will click'
]

future_pt_br = [
    'direi/falarei', 'irei', 'adquirirei/conseguirei/obterei/pegarei', 'criarei/farei', 'conhecerei/saberei',
    'acharei/pensarei', 'levarei/pegarei/tomarei', 'verei', 'chegarei/virei', 'pretenderei/quererei', 'olharei/verei',
    'usarei', 'acharei/encontrarei', 'darei', 'contarei/direi', 'funcionarei/trabalharei', 'chamarei/telefonarei',
    'experimentarei/tentarei', 'pedirei/perguntarei', 'necessitarei/precisarei',

    'sentirei', 'tornarei', 'abandonarei/deixarei/sairei', 'colocarei/porei', 'significarei',
    'continuarei/guardarei/manterei', 'deixarei/permitirei', 'começarei/iniciarei', 'parecerei', 'ajudarei/auxiliarei',
    'conversarei/falarei', 'transformarei/virarei', 'começarei/iniciarei', 'apresentarei/mostrarei',
    'escutarei/ouvirei', 'jogarei/tocarei', 'correrei', 'moverei/mexerei', 'gostarei', 'morarei/viverei',

    'acreditarei/crerei', 'manterei/segurarei', 'trarei', 'acontecerei/ocorrerei', 'escreverei',
    'fornecerei/proporcionarei', 'sentarei', 'levantarei/permanecerei', 'perderei', 'pagarei', 'conhecerei/encontrarei',
    'incluirei', 'continuarei', 'configurarei/definirei/estabelecerei/porei', 'aprenderei', 'alterarei/mudarei',
    'conduzirei/liderarei', 'compreenderei/entenderei', 'olharei/observarei/verei', 'acompanharei/seguirei',

    'impedirei/pararei', 'criarei', 'conversarei/falarei', 'lerei', 'autorizarei/permitirei',
    'acrescentarei/adicionarei', 'gastarei/passarei', 'aumentarei/crescerei', 'abrirei', 'andarei/caminharei',
    'ganharei/vencerei', 'oferecerei/proporei', 'lembrarei/recordarei', 'adorarei/amarei', 'considerarei', 'aparecerei',
    'comprarei', 'esperarei', 'servirei', 'falecerei/morrerei',

    'enviarei/mandarei', 'esperarei', 'construirei', 'ficarei/suportarei', 'cairei', 'cortarei',
    'alcançarei/atingirei/chegarei a', 'matarei', 'ficarei/permanecerei', 'irei sugerir',
    'aumentarei/criarei alguém,algo/levantarei', 'passarei', 'venderei', 'exigirei/necessitarei',
    'relatarei/reportarei', 'decidirei', 'puxarei', 'romperei/quebrarei', 'adquirirei/comprarei/obterei',
    'perceberei/realizarei',

    'administrarei/irei gerir', 'crescerei/desenvolverei', 'confiarei', 'imaginarei',
    'pisarei', 'arrependerei/lamentarei', 'manipularei', 'sonharei', 'debaterei/discutirei', 'beberei', 'comerei',
    'pularei/saltarei', 'repetirei', 'adivinharei/irei supor', 'selecionarei', 'clicarei'
]

set_box_future = set({})

while len(set_box_future) < 1:
    set_box_future.add(choice(future))

set_box_future = list(set_box_future)

verb_future = set_box_future[0]
verb_future_inked = painter('blue', verb_future)
verb_future_tr = future_pt_br[future.index(verb_future)]
verb_future_tr_inked = painter('red', verb_future_tr)

if __name__ == '__main__':
    print('\n')
    print(future[120 - 1])
    # print(verb_future)
    # print(verb_future_inked)
    # print(verb_future_tr)
    # print(verb_future_tr_inked)

    # print(f"{len(future) = }")
    # print(f"{len(future_pt_br) = }")

    # for words in zip(future, future_pt_br):
    #     print(words)

    # for words in fut.values():
    #     print(f"'{words[0]}',")
    # print(future)

    # for words in fut.values():
    #     print(f"'{words[1]}',")
    # print(future_pt_br)
    pass

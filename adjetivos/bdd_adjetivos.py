

"""
TUTORIAL
    - ctrl + f
    - deixar pesquisado: aspas simples
    - Na var [ adjectives ] substituir/recortar uma palavra reservada (deixando as aspas vazias)
    - Na var [ adjectives_uncommon ] ctrl + v
    - Na var [ adjectives_pt_br ] pegar a tradução da palavra indesejada (ctrl + x) (deixando as aspas vazias)
    - Na var [ adjectives_uncommon_pt_br ] ctrl + v
    - Na var [ adjectives_and_article ] substituir a palavra indeseja com artigo pela nova palavra
    - Na var [ adjectives_uncommon_and_article_pt_br ] = inserir a versão da palavra com o artigo apropriado
"""

from bdd_strings.strings import or_

##
adjectives = [
    'cool', 'new', 'good', 'high', 'old', 'great', 'big', 'small', 'large', 'wide', 'young',
    'different', 'persistent', 'long', 'little', 'important', 'tempting', 'bad', 'tenacious', 'invisible',

    'real', 'right', 'flat', 'only', 'public', 'sure', 'low', 'early', 'skinny', 'human', 'healthy', 'unhealthy',
    'hard', 'sick', 'better', 'dirty', 'strong', 'possible', 'drowsy', 'skilled',

    'free', 'disgusting', 'true', 'hidden', 'spotted', 'full', 'special', 'easy', 'clear', 'comfortable', 'nasty',
    'unpleasant', 'open', 'desperate', 'difficult', 'available', 'likely', 'short', 'single', 'upside down',

    'incomparable', 'wrong', 'private', 'brilliant', 'foreign', 'fine', 'common', 'poor', 'natural', 'significant',
    'similar', 'hot', 'dead', 'demented', 'happy', 'serious', 'ready', 'simple', 'concealed', 'unconcerned',

    'silent', 'astonishing', 'perfect', 'slow', 'democratic', 'dark', 'temporary', 'provisory', 'close', 'heavy',
    'religious', 'cold', 'relieved', 'main', 'insistent', 'nice', 'huge', 'famous', 'traditional', 'divorced',

    'stupid', 'irrelevant', 'sweet', 'angry', 'ambitious', 'indifferent', 'marvelous', 'identical', 'clever',
    'enthusiastic', 'vibrant', 'affirmative', 'negative', 'comprehensive', 'intuitive', 'strange', 'weird', 'odd',
    'worthy', 'flexible',

    'obnoxiously', 'fast', 'married', 'closed', 'interesting', 'interested', 'sordid', 'obsessed', 'cautious',
    'prudent', 'loud'
]

##
adjectives_pt_br = [
    'fresco / legal', 'novo(a)', 'bom(a)', 'alto(a) (não humano)', 'velho(a)', 'ótimo(a)', 'grande', 'pequeno(a)',
    'grande', 'amplo / grande', 'jovem / novo(a)', 'diferente', 'persistente', 'longo', 'pequeno', 'importante',
    'atraente / tentador(a)', 'ruim / mau / má', 'persistente / tenaz', 'invisível',

    'real', 'certo / correto', 'liso / plano', 'único(a)', 'público', 'certo / seguro', 'baixo(a)', 'cedo / inicial', 'magro(a)',
    'humano(a)', 'sadio / saudável', 'doente / doentio / insalubre', 'difícil / duro(a)', 'doente', 'melhor', 'sujo(a)',
    'forte', 'possível', 'sonolento', 'hábil / habilidoso',

    'gratuito(a) / livre', 'nojento / repugnante', 'verdadeiro(a)', 'escondido(a) / oculto(a)', 'manchado(a)',
    'cheio / completo', 'especial', 'fácil', 'claro / evidente', 'confortável', 'desagradável / nojento(a)', 'desagradável',
    'aberto(a)', 'desesperado(a)', 'difícil', 'disponível', 'provável', 'baixo(a) / curto(a)', 'solteiro(a) / único(a)',
    'de cabeça para baixo',

    'incomparável', 'errado(a)', 'privado(a)', 'brilhante', 'estrangeiro(a)', 'bom(a) / excelente', 'comum', 'pobre',
    'natural', 'significativo', 'semelhante / similar / parecido', 'quente', 'morto(a)', 'demente', 'feliz', 'sério(a)',
    'pronto(a)', 'simples', 'escondido(a)', 'despreocupado(a) / desinteressado(a) / indiferente',

    'silencioso(a)', 'surpreendente', 'perfeito', 'lento(a)', 'democrático(a)', 'escuro(a)', 'temporário(a)',
    'provisório(a)', 'perto / próximo(a)', 'forte / pesado', 'religioso(a)', 'frio(a)', 'aliviado(a)', 'principal',
    'insistente', 'legal', 'enorme', 'famoso(a)', 'tradicional', 'divorciado(a)',

    'estúpido', 'irrelevante', 'doce', 'com raiva / irritado(a) / zangado(a)', 'ambicioso(a)', 'indiferente',
    'maravilhoso(a)', 'idêntico(a)', 'esperto(a) / inteligente', 'entusiasmado(a)', 'vibrante', 'afirmativo(a)',
    'negativo', 'compreensivo(a)', 'intuitivo(a)', 'estranho(a)', 'estranho(a)', 'ímpar / estranho(a) / esquisito(a)',
    'digno(a)', 'flexível',

    'detestável', 'ligeiro(a) / rápido(a)', 'casado(a)', 'fechado(a)', 'interessante', 'interesado(a)', 'sórdido / vil',
    'obcecado(a)', 'cauteloso(a)', 'prudente', 'alto / barulhento(a)'
]










##
adjectives_ble = [
    'recognizable', 'unexplainable', 'crashable', 'unrecognizable', 'reachable', 'understandable', 'incomprehensible',
    'manageable', 'shapeable'
]

##
adjectives_ble_pt_br = [
    'reconhecível', 'inexplicável', 'quebrável', 'irreconhecível', 'alcançável', 'compreensível', 'incompreensível',
    'administrável', 'moldável'
]








##
adjectives_uncommon = [
    'legal', 'national', 'other', 'whole', 'political', 'social', 'able', 'capable', 'local', 'late', 'major',
    'grown', 'torn', 'economic', 'military', 'baggy', 'faded', 'punishable', 'federal', 'international', 'stuck',
    'straight', 'recent', 'certain', 'personal', 'medical', 'electrifying', 'current', 'central', 'physical',
    'general', 'batty', 'left', 'popular', 'environmental', 'financial', 'lifelong', 'past', 'various', 'entire',
    'final', 'cultural', 'bony', 'blazing'
]

##
adjectives_uncommon_pt_br = [
    'legal', 'nacional', 'outro(a)', 'completo(a)/inteiro(a)', 'político', 'social', 'capaz', 'capaz', 'local',
    'atrasado/tardio', 'principal', 'crescido(a)', 'rasgado(a)', 'econômico(a)', 'militar', 'folgado(a)',
    'desbotado(a)', 'punível', 'federal', 'internacional', 'emperrado(a)', 'direto(a)/reto(a)', 'atual/recente',
    'certo(a)', 'pessoal', 'médico(a)', 'eletrizante', 'atual', 'central', 'físico(a)', 'geral',
    'com deficiência mental', 'esquerdo(a)', 'popular', 'ambiental', 'financeiro(a)', 'vitalício(a)', 'passado',
    'vários(as)', 'inteiro(a)', 'final', 'cultural', 'ossudo(a)/esquelético(a)', 'ardente/em chamas/resplandecente'
]










##
adjectives_color = [
    'red', 'blue', 'green', 'black', 'white', 'golden'
]

##
adjectives_color_pt_br = [
    'vermelho(a)', 'azul', 'verde', 'preto(a)', 'branco(a)', 'dourado(a)'
]



if __name__ == '__main__':
    print('\n')

    print(f'{len(adjectives) = }')
    print(f'{len(adjectives_pt_br) = }')



    "DESCOMENTAR PARA CHECAR ALINHAMENTO"
    # print('\n')
    # for word in zip(adjectives, adjectives_pt_br):
    #     print(word[0])
    #     print(word[1])

    print(adjectives_pt_br[0])
    # print(var := [adjectives.count(word) for word in adjectives])

    # for word in adjectives:
    #     print(f"{word} = {adjectives.count(word)}")

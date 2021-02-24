

from random import choice
from metodos.bdd import create_set, data_collector as _, painter

# 'substantivo inglês no singular', 'substantivo inglês no plural'
nouns = [
    'air', 'airs', 'area', 'areas', 'art', 'arts', 'body', 'bodies', 'book', 'books',
    'business', 'businesses', 'car', 'cars', 'change', 'changes', 'child', 'children', 'city', 'cities',

    'community', 'communities', 'company', 'companies', 'country', 'countries', 'day', 'days', 'door', 'doors',
    'ending', 'endings', 'eye', 'eyes', 'face', 'faces', 'fact', 'facts', 'family', 'families',

    'father', 'fathers', 'strength', 'strengths', 'friend', 'friends', 'game', 'games', 'girl', 'girls',
    'government', 'governments', 'group', 'groups', 'guy', 'guys', 'hand', 'hands', 'head', 'heads',

    'history', 'histories', 'home', 'homes', 'hour', 'hours', 'house', 'houses', 'idea', 'ideas',
    'issue', 'issues', 'job', 'jobs', 'kid', 'kids', 'kind', 'kinds', 'law', 'laws',

    'level', 'levels', 'life', 'lifes', 'line', 'lines', 'man', 'men', 'member', 'members',
    'minute', 'minutes', 'moment', 'moments', 'month', 'months', 'morning', 'mornings', 'mother', 'mothers',

    'name', 'names', 'night', 'nights', 'number', 'numbers', 'office', 'offices', 'other', 'others',
    'parent', 'parents', 'part', 'parts', 'party', 'parties', 'person', 'people', 'piece of information', 'pieces of information',

    'place', 'places', 'point', 'points', 'power', 'powers', 'president', 'presidents', 'problem', 'problems',
    'program', 'programs', 'question', 'questions', 'reason', 'reasons', 'research', 'researches', 'result', 'results',

    'right', 'rights', 'room', 'rooms', 'school', 'schools', 'service', 'services', 'side', 'sides',
    'state', 'states', 'story', 'stories', 'student', 'students', 'study', 'studies', 'system', 'systems',

    'teacher', 'teachers', 'team', 'teams', 'thing', 'things', 'time', 'times', 'war', 'wars',
    'water', 'waters', 'way', 'ways', 'week', 'weeks', 'woman', 'women', 'word', 'words',

    'work', 'works', 'world', 'worlds', 'year', 'years'
]

# 'substantivo inglês no singular traduzido', 'substantivo inglês no plural traduzido'
nouns_pt_br = [
    'ar', 'ares', 'área', 'áreas', 'arte', 'artes', 'corpo', 'corpos', 'livro', 'livros', 'negócios', 'os negócios',
    'carro ', 'carros', 'mudança', 'mudanças', 'criança', 'crianças', 'cidade', 'cidades',

    'comunidade', 'comunidades', 'empresa', 'empresas', 'país', 'países', 'dia', 'dias', 'porta', 'portas',
    'final', 'finais', 'olho', 'olhos', 'rosto', 'rostos', 'fato', 'fatos', 'família', 'famílias',

    'pai', 'pais', 'força', 'forças', 'amigo', 'amigos', 'jogo', 'jogos', 'menina', 'meninas', 'governo', 'governos',
    'grupo', 'grupos', 'cara', 'pessoal', 'mão', 'mãos', 'cabeça', 'cabeças',

    'história', 'histórias', 'casa', 'casas', 'hora', 'horas', 'casa', 'casas', 'ideia', 'ideias',
    'problema', 'problemas', 'emprego', 'empregos', 'criança', 'crianças', 'tipo', 'tipos', 'lei', 'leis',


    'nível', 'níveis', 'vida', 'vidas', 'linha', 'linhas', 'homem', 'homens', 'membro', 'membros ', 'minuto', 'minutos',
    'momento', 'momentos', 'mês', 'meses', 'manhã', 'manhãs', 'mãe', 'mães',

    'nome', 'nomes', 'noite', 'noites', 'número', 'números', 'escritório', 'escritórios', 'outro(a)', 'outros(as)',
    'pai', 'pais', 'parte', 'partes', 'festa', 'festas', 'pessoa', 'pessoas', 'pedaço de informação', 'pedaços de informação',

    'lugar', 'lugares', 'ponto', 'pontos', 'poder', 'poderes', 'presidente', 'presidentes', 'problema', 'problemas',
    'programa', 'programas', 'questão', 'questões', 'razão', 'razões', 'pesquisa', 'pesquisas', 'resultado', 'resultados',

    'direito', 'direitos', 'quarto', 'quartos', 'escola', 'escolas', 'serviço', 'serviços', 'lado', 'lados',
    'estado', 'estados', 'história', 'histórias', 'estudante', 'estudantes', 'estudo', 'estudos', 'sistema', 'sistemas',

    'professor(a)', 'professores', 'equipe', 'equipes', 'coisa', 'coisas', 'tempo', 'tempos', 'guerra', 'guerras',
    'água', 'águas', 'caminho', 'caminhos', 'semana', 'semanas', 'mulher', 'mulheres', 'palavra', 'palavras',

    'trabalho', 'trabalhos', 'mundo', 'mundos', 'ano', 'anos'
]

# 'substantivo inglẽs no singular'
nouns_sgl = [
    'air', 'area', 'art', 'body', 'book', 'business', 'car', 'change', 'child', 'city', 'community', 'company',
    'country', 'day', 'door', 'ending', 'eye', 'face', 'fact', 'family',

    'father', 'strength', 'friend', 'game', 'girl', 'government', 'group', 'guy', 'hand', 'head', 'history', 'home',
    'hour', 'house', 'idea', 'issue', 'job', 'kid', 'kind', 'law',

    'level', 'life', 'line', 'man', 'member', 'minute', 'moment', 'month', 'morning', 'mother', 'name', 'night',
    'number', 'office', 'other', 'parent', 'part', 'party', 'person', 'piece of information',

    'place', 'point', 'power', 'president', 'problem', 'program', 'question', 'reason', 'research', 'result', 'right',
    'room', 'school', 'service', 'side', 'state', 'story', 'student', 'study', 'system',

    'teacher', 'team', 'thing', 'time', 'war', 'water', 'way', 'week', 'woman', 'word', 'work', 'world', 'year'
]

# 'substantivo inglẽs no singular traduzido'
nouns_sgl_pt_br = [
    'ar', 'área', 'arte', 'corpo', 'livro', 'negócios', 'carro ', 'mudança', 'criança', 'cidade', 'comunidade',
    'empresa', 'país', 'dia', 'porta', 'final', 'olho', 'rosto', 'fato', 'família',

    'pai', 'força', 'amigo', 'jogo', 'menina', 'governo', 'grupo', 'cara', 'mão', 'cabeça', 'história', 'casa', 'hora',
    'casa', 'ideia', 'problema', 'emprego', 'criança', 'tipo', 'lei',

    'nível', 'vida', 'linha', 'homem', 'membro', 'minuto', 'momento', 'mês', 'manhã', 'mãe', 'nome', 'noite', 'número',
    'escritório', 'outro(a)', 'pai', 'parte', 'festa', 'pessoa', 'informação',

    'lugar', 'ponto', 'poder', 'presidente', 'problema', 'programa', 'questão', 'razão', 'pesquisa', 'resultado',
    'direito', 'quarto', 'escola', 'serviço', 'lado', 'estado', 'história', 'estudante', 'estudo', 'sistema',

    'professor(a)', 'equipe', 'coisa', 'tempo', 'guerra', 'água', 'caminho', 'semana', 'mulher', 'palavra', 'trabalho',
    'mundo', 'ano'
]

# 'substantivo inglẽs no plural'
nouns_pl = [
    'airs', 'areas', 'arts', 'bodies', 'books', 'businesses', 'cars', 'changes', 'children', 'cities', 'communities',
    'companies', 'countries', 'days', 'doors', 'endings', 'eyes', 'faces', 'facts', 'families',

    'fathers', 'strengths', 'friends', 'games', 'girls', 'governments', 'groups', 'guys', 'hands', 'heads', 'histories',
    'homes', 'hours', 'houses', 'ideas', 'issues', 'jobs', 'kids', 'kinds', 'laws',

    'levels', 'lifes', 'lines', 'men', 'members', 'minutes', 'moments', 'months', 'mornings', 'mothers', 'names',
    'nights', 'numbers', 'offices', 'others', 'parents', 'parts', 'parties', 'people', 'pieces of information',

    'places', 'points', 'powers', 'presidents', 'problems', 'programs', 'questions', 'reasons', 'researches', 'results',
    'rights', 'rooms', 'schools', 'services', 'sides', 'states', 'stories', 'students', 'studies', 'systems',

    'teachers', 'teams', 'things', 'times', 'wars', 'waters', 'ways', 'weeks', 'women', 'words', 'works', 'worlds',
    'years'
]

# 'substantivo inglẽs no plural traduzido'
nouns_pl_pt_br = [
    'ares', 'áreas', 'artes', 'corpos', 'livros', 'os negócios', 'carros', 'mudanças', 'crianças', 'cidades',
    'comunidades', 'empresas', 'países', 'dias', 'portas', 'finais', 'olhos', 'rostos', 'fatos', 'famílias',

    'pais', 'forças', 'amigos', 'jogos', 'meninas', 'governos', 'grupos', 'pessoal', 'mãos', 'cabeças', 'histórias',
    'casas', 'horas', 'casas', 'ideias', 'problemas', 'empregos', 'crianças', 'tipos', 'leis',

    'níveis', 'vidas', 'linhas', 'homens', 'membros ', 'minutos', 'momentos', 'meses', 'manhãs', 'mães', 'nomes',
    'noites', 'números', 'escritórios', 'outros(as)', 'pais', 'partes', 'festas', 'pessoas', 'informações',

    'lugares', 'pontos', 'poderes', 'presidentes', 'problemas', 'programas', 'questões', 'razões', 'pesquisas',
    'resultados', 'direitos', 'quartos', 'escolas', 'serviços', 'lados', 'estados', 'histórias', 'estudantes',
    'estudos', 'sistemas',

    'professores', 'equipes', 'coisas', 'tempos', 'guerras', 'águas', 'caminhos', 'semanas', 'mulheres', 'palavras',
    'trabalhos', 'mundos', 'anos'
]

set_box = set({})

while len(set_box) < 3:
    set_box.add(choice(nouns))

set_box = list(set_box)

noun = set_box[0]
noun_inked = painter('blue', noun)
noun_tr = nouns_pt_br[nouns.index(noun)]
noun_tr_inked = painter('red', noun_tr)

noun2 = set_box[1]
noun2_inked = painter('blue', noun2)
noun2_tr = nouns_pt_br[nouns.index(noun2)]
noun2_tr_inked = painter('red', noun2_tr)

noun3 = set_box[2]
noun3_inked = painter('blue', noun3)
noun3_tr = nouns_pt_br[nouns.index(noun3)]
noun3_tr_inked = painter('red', noun3_tr)

if __name__ == '__main__':
    print(noun)
    print(noun_inked)
    print(noun_tr)
    print(noun_tr_inked)
    print(noun2)
    print(noun2_inked)
    print(noun2_tr)
    print(noun2_tr_inked)
    print(noun3)
    print(noun3_inked)
    print(noun3_tr)
    print(noun3_tr_inked)
    # print(len(nouns))
    # print(len(nouns_pt_br))
    # print(len(nouns_sgl))
    # print(len(nouns_pl))

    # for words in zip(nouns, nouns_pt_br):
    #     print(words)

    # x = 0
    # y = 1

    # while x < len(nouns_pt_br):
    #     print(f"'{nouns_pt_br[x]}',")
    #     x += 2
    # print(nouns_sgl_pt_br)

    # while y < len(nouns_pt_br):
    #     print(f"'{nouns_pt_br[y]}',")
    #     y += 2
    # print(nouns_pl_pt_br)
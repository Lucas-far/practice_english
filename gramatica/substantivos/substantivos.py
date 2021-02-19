

nouns = {
    'air': ('air', 'ar'),
    'area': ('area', 'área'),
    'art': ('art', 'arte'),
    'body': ('body', 'corpo'),
    'book': ('book', 'livro'),
    'business': ('business', 'negócios'),
    'car': ('car', 'carro '),
    'change': ('change', 'mudança'),
    'child': ('child', 'criança'),
    'city': ('city', 'cidade'),
    'community': ('community', 'comunidade'),
    'company': ('company', 'empresa'),
    'country': ('country', 'país'),
    'day': ('day', 'dia'),
    'door': ('door', 'porta'),
    'ending': ('ending', 'final'),
    'eye': ('eye', 'olho'),
    'face': ('face', 'rosto'),
    'fact': ('fact', 'fato'),
    'family': ('family', 'família'),
    'father': ('father', 'pai'),
    'strength': ('strength', 'força'),
    'friend': ('friend', 'amigo'),
    'game': ('game', 'jogo'),
    'girl': ('girl', 'menina'),
    'government': ('government', 'governo'),
    'group': ('group', 'grupo'),
    'guy': ('guy', 'cara'),
    'hand': ('hand', 'mão'),
    'head': ('head', 'cabeça'),
    'history': ('history', 'história'),
    'home': ('home', 'casa'),
    'hour': ('hour', 'hora'),
    'house': ('house', 'casa'),
    'idea': ('idea', 'ideia'),
    'issue': ('issue', 'problema'),
    'job': ('job', 'emprego'),
    'kid': ('kid', 'criança'),
    'kind': ('kind', 'tipo'),
    'law': ('law', 'lei'),
    'level': ('level', 'nível'),
    'life': ('life', 'vida'),
    'line': ('line', 'linha'),
    'man': ('man', 'homem'),
    'member': ('member', 'membro'),
    'minute': ('minute', 'minuto'),
    'moment': ('moment', 'momento'),
    'month': ('month', 'mês'),
    'morning': ('morning', 'manhã'),
    'mother': ('mother', 'mãe'),
    'name': ('name', 'nome'),
    'night': ('night', 'noite'),
    'number': ('number', 'número'),
    'office': ('office', 'escritório'),
    'other': ('other', 'outro(a)'),
    'parent': ('parent', 'pai'),
    'part': ('part', 'parte'),
    'party': ('party', 'festa'),
    'person': ('person', 'pessoa'),
    'piece of information': ('piece of information', 'informação'),
    'place': ('place', 'lugar'),
    'point': ('point', 'ponto'),
    'power': ('power', 'poder'),
    'president': ('president', 'presidente'),
    'problem': ('problem', 'problema'),
    'program': ('program', 'programa'),
    'question': ('question', 'questão'),
    'reason': ('reason', 'razão'),
    'research': ('research', 'pesquisa'),
    'result': ('result', 'resultado'),
    'right': ('right', 'direito'),
    'room': ('room', 'quarto'),
    'school': ('school', 'escola'),
    'service': ('service', 'serviço'),
    'side': ('side', 'lado'),
    'state': ('state', 'estado'),
    'story': ('story', 'história'),
    'student': ('student', 'estudante'),
    'study': ('study', 'estudo'),
    'system': ('system', 'sistema'),
    'teacher': ('teacher', 'professor(a)'),
    'team': ('team', 'equipe'),
    'thing': ('thing', 'coisa'),
    'time': ('time', 'tempo'),
    'war': ('war', 'guerra'),
    'water': ('water', 'água'),
    'way': ('way', 'caminho'),
    'week': ('week', 'semana'),
    'woman': ('woman', 'mulher'),
    'word': ('word', 'palavra'),
    'work': ('work', 'trabalho'),
    'world': ('world', 'mundo'),
    'year': ('year', 'ano'),
}                                             # 'air': ('air', 'ar')
nouns_keys = [word for word in nouns]                     # 'air'
nouns_keys_index0 = [word[0] for word in nouns.values()]  # 'air'
nouns_keys_index1 = [word[1] for word in nouns.values()]  # 'ar'

nouns_pl = {
    'airs': ('airs', 'ares'),
    'areas': ('areas', 'áreas'),
    'arts': ('arts', 'artes'),
    'bodies': ('bodies', 'corpos'),
    'books': ('books', 'livros'),
    'businesses': ('businesses', 'os negócios'),
    'cars': ('cars', 'carros'),
    'changes': ('changes', 'mudanças'),
    'children': ('children', 'crianças'),
    'cities': ('cities', 'cidades'),
    'communities': ('communities', 'comunidades'),
    'companies': ('companies', 'empresas'),
    'countries': ('countries', 'países'),
    'days': ('days', 'dias'),
    'doors': ('doors', 'portas'),
    'endings': ('endings', 'finais'),
    'eyes': ('eyes', 'olhos'),
    'faces': ('faces', 'rostos'),
    'facts': ('facts', 'fatos'),
    'families': ('families', 'famílias'),
    'fathers': ('fathers', 'pais'),
    'strengths': ('strengths', 'forças'),
    'friends': ('friends', 'amigos'),
    'games': ('games', 'jogos'),
    'girls': ('girls', 'meninas'),
    'governments': ('governments', 'governos'),
    'groups': ('groups', 'grupos'),
    'guys': ('guys', 'pessoal'),
    'hands': ('hands', 'mãos'),
    'heads': ('heads', 'cabeças'),
    'histories': ('histories', 'histórias'),
    'homes': ('homes', 'casas'),
    'hours': ('hours', 'horas'),
    'houses': ('houses', 'casas'),
    'ideas': ('ideas', 'ideias'),
    'issues': ('issues', 'problemas'),
    'jobs': ('jobs', 'empregos'),
    'kids': ('kids', 'crianças'),
    'kinds': ('kinds', 'tipos'),
    'laws': ('laws', 'leis'),
    'levels': ('levels', 'níveis'),
    'lifes': ('lifes', 'vidas'),
    'lines': ('lines', 'linhas'),
    'men': ('men', 'homens'),
    'members': ('members', 'membros'),
    'minutes': ('minutes', 'minutos'),
    'moments': ('moments', 'momentos'),
    'months': ('months', 'meses'),
    'mornings': ('mornings', 'manhãs'),
    'mothers': ('mothers', 'mães'),
    'names': ('names', 'nomes'),
    'nights': ('nights', 'noites'),
    'numbers': ('numbers', 'números'),
    'offices': ('offices', 'escritórios'),
    'others': ('others', 'outros(as)'),
    'parents': ('parents', 'pais'),
    'parts': ('parts', 'partes'),
    'parties': ('parties', 'festas'),
    'people': ('people', 'pessoas'),
    'pieces of information': ('pieces of information', 'informações'),
    'places': ('places', 'lugares'),
    'points': ('points', 'pontos'),
    'powers': ('powers', 'poderes'),
    'presidents': ('presidents', 'presidentes'),
    'problems': ('problems', 'problemas'),
    'programs': ('programs', 'programas'),
    'questions': ('questions', 'questões'),
    'reasons': ('reasons', 'razões'),
    'researches': ('researches', 'pesquisas'),
    'results': ('results', 'resultados'),
    'rights': ('rights', 'direitos'),
    'rooms': ('rooms', 'quartos'),
    'schools': ('schools', 'escolas'),
    'services': ('services', 'serviços'),
    'sides': ('sides', 'lados'),
    'states': ('states', 'estados'),
    'stories': ('stories', 'histórias'),
    'students': ('students', 'estudantes'),
    'studies': ('studies', 'estudos'),
    'systems': ('systems', 'sistemas'),
    'teachers': ('teachers', 'professores'),
    'teams': ('teams', 'equipes'),
    'things': ('things', 'coisas'),
    'times': ('times', 'tempos'),
    'wars': ('wars', 'guerras'),
    'waters': ('waters', 'águas'),
    'ways': ('ways', 'caminhos'),
    'weeks': ('weeks', 'semanas'),
    'women': ('women', 'mulheres'),
    'words': ('words', 'palavras'),
    'works': ('works', 'trabalhos'),
    'worlds': ('worlds', 'mundos'),
    'years': ('years', 'anos'),
}                                                # 'airs': ('airs', 'ares')
nouns_pl_keys = [word for word in nouns_pl]                     # 'airs'
nouns_pl_keys_index0 = [word[0] for word in nouns_pl.values()]  # 'airs'
nouns_pl_keys_index1 = [word[1] for word in nouns_pl.values()]  # 'ares'


if __name__ == '__main__':
    bricks = '=' * 100

    print(bricks)
    print(f"{len(nouns) = }")
    print(f"{len(nouns_keys) = }")
    print(f"{len(nouns_keys_index0) = }")
    print(f"{len(nouns_keys_index1) = }")

    print(bricks)
    print(f"{len(nouns_pl) = }")
    print(f"{len(nouns_pl_keys) = }")
    print(f"{len(nouns_pl_keys_index0) = }")
    print(f"{len(nouns_pl_keys_index1) = }")

    print(bricks)
    print(f"{nouns = }")
    print(f"{nouns_keys = }")
    print(f"{nouns_keys_index0 = }")
    print(f"{nouns_keys_index1 = }")

    print(bricks)
    print(f"{nouns_pl = }")
    print(f"{nouns_pl_keys = }")
    print(f"{nouns_pl_keys_index0 = }")
    print(f"{nouns_pl_keys_index1 = }")

    # x = 0
    # while x < len(nouns_keys_index0):
    #     print(f"'{nouns_keys_index0[x]}': ('{nouns_keys_index0[x]}', '{nouns_keys_index2[x]}'),")
    #     x += 1

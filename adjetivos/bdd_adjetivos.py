

adjectives = [
    'other', 'new', 'good', 'high', 'old', 'great', 'big', 'American', 'small', 'large', 'national', 'young',
    'different', 'black', 'long', 'little', 'important', 'political', 'bad', 'white',

    'real', 'best', 'right', 'social', 'only', 'public', 'sure', 'low', 'early', 'able', 'human', 'local', 'late',
    'hard', 'major', 'better', 'economic', 'strong', 'possible', 'whole',

    'free', 'military', 'true', 'federal', 'international', 'full', 'special', 'easy', 'clear', 'recent', 'certain',
    'personal', 'open', 'red', 'difficult', 'available', 'likely', 'short', 'single', 'medical',

    'current', 'wrong', 'private', 'past', 'foreign', 'fine', 'common', 'poor', 'natural', 'significant',
    'similar', 'hot', 'dead', 'central', 'happy', 'serious', 'ready', 'simple', 'left', 'physical',

    'general', 'environmental', 'financial', 'blue', 'democratic', 'dark', 'various', 'entire', 'close', 'legal',
    'religious', 'cold', 'final', 'main', 'green', 'nice', 'huge', 'popular', 'traditional', 'cultural',

    'stupid', 'irrelevant', 'sweet', 'angry', 'ambitious', 'indifferent', 'marvelous', 'identical', 'clever',
    'enthusiastic', 'vibrant', 'affirmative', 'negative', 'comprehensive', 'intuitive', 'strange', 'weird', 'odd',
    'worthy', 'flexible',

    'obnoxiously', 'fast', 'golden'
]

adjectives_pt_br = [
    'outro(a)', 'novo(a)', 'bom(a)', 'alto(a)', 'velho(a)', 'ótimo(a)', 'grande', 'americano(a)',
    'pequeno(a)', 'grande', 'nacional', 'novo(a)', 'diferente', 'preto(a)', 'longo', 'pequeno', 'importante',
    'político', 'ruim/mau/má', 'branco(a)',

    'real', 'melhor', 'certo/correto', 'social', 'único(a)', 'público', 'certo/seguro', 'baixo(a)', 'cedo', 'capaz',
    'humano(a)', 'local', 'atrasado(a)', 'difícil', 'principal', 'melhor', 'econômico', 'forte', 'possível',
    'inteiro/completo',

    'gratuito(a)/livre', 'militar', 'verdadeiro(a)', 'federal', 'internacional', 'cheio/completo', 'especial', 'fácil',
    'claro/evidente', 'recente', 'certo(a)', 'pessoal', 'aberto(a)', 'vermelho(a)', 'difícil', 'disponível', 'provável',
    'baixo(a)/curto(a)', 'solteiro(a)/único(a)', 'médico(a)',

    'atual', 'errado(a)', 'privado(a)', 'passado', 'estrangeiro(a)', 'bom(a)/excelente', 'comum', 'pobre', 'natural',
    'significativo', 'semelhante/similar/parecido', 'quente', 'morto(a)', 'central', 'feliz', 'sério(a)', 'pronto(a)',
    'simples', 'esquerdo(a)', 'físico(a)',

    'geral', 'ambiental', 'financeiro(a)', 'azul', 'democrático(a)', 'escuro(a)', 'vários(as)', 'inteiro(a)',
    'fechado(a)', 'legal', 'religioso(a)', 'frio(a)', 'final', 'principal', 'verde', 'legal', 'enorme', 'popular',
    'tradicional', 'cultural',

    'estúpido', 'irrelevante', 'doce', 'com raiva/irritado(a)/zangado(a)', 'ambicioso(a)', 'indiferente',
    'maravilhoso(a)', 'idêntico(a)', 'esperto(a)/inteligente', 'entusiasmado(a)', 'vibrante', 'afirmativo(a)',
    'negativo', 'abrangente', 'intuitivo(a)', 'estranho(a)', 'estranho(a)', 'estranho(a)',
    'digno(a)', 'flexível',

    'detestável', 'ligeiro(a)/rápido(a)', 'dourado(a)'
]

# var = [word for word in zip(adjectives, adjectives_pt_br)]

if __name__ == '__main__':
    print('\n')
    print(f'{len(adjectives) = }')
    print(f'{len(adjectives_pt_br) = }')

    print('\n')
    for word in zip(adjectives, adjectives_pt_br):
        print(word)

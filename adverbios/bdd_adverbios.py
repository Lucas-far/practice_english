

adverbs_ly = [
    'accidentally', 'actually', 'angrily', 'anxiously', 'awkwardly', 'badly', 'blindly', 'boastfully', 'boldly',
    'bravely', 'brightly', 'certainly', 'cheerfully', 'clearly', 'coyly', 'crazily', 'defiantly', 'deftly',
    'deliberately', 'devotedly',

    'directly', 'doubtfully', 'dramatically', 'dutifully', 'eagerly', 'early', 'elegantly', 'enormously', 'especially',
    'evenly', 'eventually', 'exactly', 'faithfully', 'finally', 'foolishly', 'fortunately', 'frequently', 'gleefully',
    'gracefully', 'happily',

    'hastily', 'honestly', 'hopelessly', 'hourly', 'hungrily', 'innocently', 'inquisitively', 'irritably', 'jealously',
    'justly', 'kindly', 'lazily', 'loosely', 'madly', 'merrily', 'mortally', 'mysteriously', 'nearly', 'nervously',
    'normally',

    'obediently', 'occasionally', 'particularly', 'perfectly', 'politely', 'poorly', 'powerfully', 'probably',
    'promptly', 'quickly', 'rapidly', 'rarely', 'really', 'recently', 'regularly', 'rudely', 'safely', 'selfishly',
    'seriously', 'shakily',

    'sharply', 'silently', 'simply', 'slowly', 'solemnly', 'speedily', 'sternly', 'suddenly', 'technically',
    'tediously', 'unexpectedly', 'usually', 'victoriously', 'vivaciously', 'warmly', 'wearily', 'weekly',
    'wildly', 'yearly', 'consequently',

    'subsequently', 'similarly',
]

adverbs_ly_pt_br = [
    'acidentalmente', 'na verdade', 'com raiva', 'ansiosamente', 'desajeitadamente/estranhamente', 'mal', 'cegamente',
    'orgulhosamente', 'ousadamente', 'corajosamente', 'brilhantemente', 'certamente', 'alegremente', 'claramente',
    'timidamente', 'loucamente (doido)', 'desafiadoramente', 'habilmente', 'deliberadamente', 'devotadamente',

    'diretamente', 'duvidosamente', 'dramaticamente', 'obedientemente', 'ansiosamente', 'cedo', 'elegantemente',
    'enormemente', 'especialmente', 'uniformemente', 'eventualmente', 'exatamente', 'fielmente', 'finalmente',
    'tolamente', 'felizmente', 'frequentemente', 'alegremente', 'graciosamente', 'felizmente',

    'apressadamente/precipitadamente', 'honestamente', 'desesperadamente/desesperançosamente',
    'de hora em hora/por hora', 'avidamente/famintamente', 'inocentemente', 'inquisitivamente', 'irritantemente',
    'ciumentamente', 'justamente', 'gentilmente', 'preguiçosamente', 'folgadamente/livremente/vagamente',
    'loucamente (louco)', 'alegremente', 'mortalmente', 'misteriosamente', 'aproximadamente/quase', 'nervosamente',
    'normalmente',

    'obedientemente', 'ocasionalmente', 'particularmente', 'perfeitamente', 'educadamente',
    'deficientemente/pobremente', 'poderosamente', 'provavelmente', 'imediatamente/prontamente', 'rapidamente',
    'rapidamente', 'raramente', 'realmente', 'recentemente', 'regularmente', 'rudemente', 'com segurança',
    'egoisticamente', 'seriamente', 'tremulamente',

    'bruscamente/nitidamente/rispidamente', 'silenciosamente', 'simplesmente', 'lentamente', 'solenemente',
    'rapidamente', 'severamente', 'repentinamente', 'tecnicamente', 'tediosamente', 'inesperadamente', 'geralmente',
    'vitorioso', 'vivazmente', 'calorosamente', 'cansativamente', 'semanalmente', 'descontroladamente', 'anualmente',
    'consequentemente',

    'subsequentemente', 'semelhantemente/similarmente'
]

# var = [word for word in zip(adv_ly, adv_ly_pt_br)]

adverbs_frequency = [
    'always', 'eventually', 'frequently', 'hourly', 'never', 'occasionally',
    'often', 'rarely', 'regularly', 'seldom', 'sometimes', 'usually', 'weekly', 'yearly'
]

adverbs_frequency_pt_br = [
    'sempre', 'eventualmente', 'frequentemente', 'de hora em hora/por hora', 'nunca', 'ocasionalmente',
    'com frequência', 'raramente', 'regularmente', 'com raridade', 'às vezes', 'normalmente', 'semanalmente',
    'anualmente'
]

adv_action = ['promptly', 'quickly', 'rapidly', 'slowly', 'speedily', 'tediously']

adv_action_pt_br = ['prontamente', 'rapidamente', 'rapidamente', 'lentamente', 'rapidamente', 'tediosamente']

adv_negativity = [
    'angrily', 'anxiously', 'badly', 'boastfully', 'foolishly', 'hopelessly',
    'irritably', 'jealously', 'lazily', 'poorly', 'rudely', 'selfishly',
    'wearily'
]

adv_negativity_pt_br = [
    'com raiva', 'ansiosamente', 'mal', 'orgulhosamente', 'tolamente', 'desesperadamente/desesperançosamente',
    'irritantemente', 'ciumentamente', 'preguiçosamente', 'deficientemente/pobremente', 'rudemente', 'egoisticamente',
    'cansativamente',
]

adv_positivity = [
    'boldly', 'bravely', 'brightly', 'cheerfully', 'deftly', 'devotedly', 'eagerly',
    'elegantly', 'faithfully', 'fortunately', 'gleefully', 'gracefully', 'happily', 'honestly',
    'innocently', 'justly', 'kindly', 'merrily', 'obediently', 'perfectly', 'politely',
    'powerfully', 'safely', 'victoriously', 'vivaciously', 'warmly'
]

adv_positivity_pt_br = [
    'ousadamente', 'corajosamente', 'brilhantemente', 'alegremente', 'habilmente', 'devotadamente', 'ansiosamente',
    'elegantemente', 'fielmente', 'felizmente', 'alegremente', 'graciosamente', 'felizmente', 'honestamente',
    'inocentemente', 'justamente', 'gentilmente', 'alegremente', 'obedientemente', 'perfeitamente', 'educadamente',
    'poderosamente', 'com segurança', 'vitorioso', 'vivazmente', 'calorosamente'
]

adverb_others = [
    'about', 'again', 'ago', 'ahead', 'almost', 'alone', 'also', 'always', 'anyway', 'around', 'as', 'back', 'before',
    'besides', 'certainly', 'consequently', 'else', 'elsewhere', 'enough', 'even',

    'ever', 'fast', 'forward', 'furthermore', 'hard', 'here', 'how', 'in', 'in fact', 'indeed', 'instead', 'just',
    'later', 'least', 'less', 'likewise', 'maybe', 'meanwhile', 'more', 'most',

    'much', 'never', 'nevertheless', 'nonetheless', 'now', 'off', 'often', 'once', 'otherwise', 'out', 'over',
    'perhaps', 'quite', 'seldom', 'similarly', 'so', 'sometimes', 'soon', 'still', 'subsequently',

    'then', 'there', 'therefore', 'thus', 'together', 'tonight', 'up', 'when', 'where', 'yet'
]

adverb_others_pt_br = [
    'acerca/aproximadamente', 'de novo/novamente/outra vez', 'atrás', 'adiante/à frente', 'por pouco/quase',
    'apenas/só', 'também', 'sempre', 'em todo o caso/de qualquer maneira', 'ao redor/em torno/em volta', 'como',
    'de volta/para trás', 'antes/anteriormente', 'além de/além disso/também', 'certamente', 'conseqüentemente', 'outro',
    'em outro lugar', 'bastante/suficiente', 'até/mesmo',

    'já/sempre/nunca/jamais', 'rapidamente/velozmente',
    'adiante/para a frente', 'ademais/além disso', 'duramente', 'aqui, cá', 'como/quão', 'dentro', 'de fato/na verdade',
    'de fato/realmente', 'em vez/em vez disso', 'somente', 'mais tarde', 'menos', 'menos', 'igualmente/também',
    'talvez', 'enquanto isso/entretanto', 'mais', 'mais',

    'muito', 'jamais/nunca', 'ainda assim/mesmo assim/porém/todavia', 'apesar disso', 'agora/já', 'fora',
    'frequentemente', 'outrora/uma vez', 'de outro modo', 'fora', 'através/sobre', 'talvez', 'bastante/muito',
    'raramente', 'similarmente', 'assim/tão/então/portanto', 'às vezes/por vez', 'em breve/logo/rapidamente', 'ainda',
    'subsequentemente',

    'depois/então', 'ali/lá', 'por isso/portanto', 'assim/portanto/deste modo', 'junto(s)/justamente',
    'hoje à noite/esta noite', 'em cima/para cima', 'quando', 'aonde/onde', 'ainda'
]

if __name__ == '__main__':
    print('\n')

    # print(f"{len(adv_ly)}")
    # print(f"{len(adv_ly_pt_br)}")
    # print('\n')
    # for words in zip(adv_ly, adv_ly_pt_br):
    #     print(words)

    # print(f"{len(adv_frequency)}")
    # print(f"{len(adv_frequency_pt_br)}")
    # print('\n')
    # for words in zip(adv_frequency, adv_frequency_pt_br):
    #     print(words)

    # print(f"{len(adv_others)}")
    # print(f"{len(adv_others_pt_br)}")
    # print('\n')
    # for words in zip(adv_others, adv_others_pt_br):
    #     print(words)

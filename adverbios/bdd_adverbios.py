

from random import choice
from metodos.bdd import painter

adverbs_ly = [
    'accidentally', 'actually', 'angrily', 'anxiously', 'awkwardly', 'badly', 'blindly', 'boastfully', 'boldly',
    'bravely', 'brightly', 'certainly', 'cheerfully', 'clearly', 'coyly', 'crazily', 'defiantly', 'deftly',
    'deliberately', 'devotedly',

    'directly', 'doubtfully', 'dramatically', 'dutifully', 'eagerly', 'early', 'elegantly', 'enormously', 'especially',
    'evenly', 'exactly', 'faithfully', 'finally', 'foolishly', 'fortunately', 'gleefully',
    'gracefully', 'happily',

    'hastily', 'honestly', 'hopelessly', 'hungrily', 'innocently', 'inquisitively', 'irritably', 'jealously',
    'justly', 'kindly', 'lazily', 'loosely', 'madly', 'merrily', 'mortally', 'mysteriously', 'nearly', 'nervously',
    'normally',

    'obediently', 'particularly', 'perfectly', 'politely', 'poorly', 'powerfully', 'probably',
    'promptly', 'quickly', 'rapidly', 'really', 'recently', 'rudely', 'safely', 'selfishly',
    'seriously', 'shakily',

    'sharply', 'silently', 'simply', 'slowly', 'solemnly', 'speedily', 'sternly', 'suddenly', 'technically',
    'tediously', 'unexpectedly', 'victoriously', 'vivaciously', 'warmly', 'wearily',
    'wildly', 'consequently',

    'subsequently', 'similarly',
]

adverbs_ly_pt_br = [
    'acidentalmente', 'na verdade', 'com raiva', 'ansiosamente', 'desajeitadamente / estranhamente', 'mal', 'cegamente',
    'orgulhosamente', 'ousadamente', 'corajosamente', 'brilhantemente', 'certamente', 'alegremente', 'claramente',
    'timidamente', 'loucamente', 'desafiadoramente', 'habilmente', 'deliberadamente', 'devotadamente',

    'diretamente', 'duvidosamente', 'dramaticamente', 'obedientemente', 'ansiosamente', 'cedo', 'elegantemente',
    'enormemente', 'especialmente', 'uniformemente', 'exatamente', 'fielmente', 'finalmente',
    'tolamente', 'felizmente', 'alegremente', 'graciosamente', 'felizmente',

    'apressadamente / precipitadamente', 'honestamente', 'desesperadamente / desesperançosamente',
    'avidamente / famintamente', 'inocentemente', 'inquisitivamente', 'irritantemente',
    'ciumentamente', 'justamente', 'gentilmente', 'preguiçosamente', 'folgadamente / livremente / vagamente',
    'com loucura', 'alegremente', 'mortalmente', 'misteriosamente', 'aproximadamente / quase', 'nervosamente',
    'normalmente',

    'obedientemente', 'particularmente', 'perfeitamente', 'educadamente',
    'deficientemente / pobremente', 'poderosamente', 'provavelmente', 'imediatamente / prontamente', 'rapidamente',
    'rapidamente', 'realmente', 'recentemente', 'rudemente', 'com segurança',
    'egoisticamente', 'seriamente', 'tremulamente',

    'bruscamente / nitidamente / rispidamente', 'silenciosamente', 'simplesmente', 'lentamente', 'solenemente',
    'rapidamente', 'severamente', 'repentinamente', 'tecnicamente', 'tediosamente', 'inesperadamente', 'vitorioso',
    'vivazmente', 'calorosamente', 'cansativamente', 'descontroladamente', 'consequentemente',

    'subsequentemente', 'semelhantemente / similarmente'
]

# var = [word for word in zip(adv_ly, adv_ly_pt_br)]

adverbs_frequency = [
    'always', 'eventually', 'frequently', 'hourly', 'never', 'occasionally',
    'often', 'rarely', 'regularly', 'seldom', 'sometimes', 'usually', 'weekly', 'yearly'
]

adverbs_frequency_pt_br = [
    'sempre', 'eventualmente', 'frequentemente', 'de hora em hora / por hora', 'nunca', 'ocasionalmente',
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
    'com raiva', 'ansiosamente', 'mal', 'orgulhosamente', 'tolamente', 'desesperadamente / desesperançosamente',
    'irritantemente', 'ciumentamente', 'preguiçosamente', 'deficientemente / pobremente', 'rudemente', 'egoisticamente',
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
    'about', 'again', 'ago', 'ahead', 'almost', 'alone', 'also', 'anyway', 'around', 'as', 'back', 'before',
    'besides', 'else', 'elsewhere', 'enough', 'even',

    'ever', 'fast', 'forward', 'furthermore', 'hard', 'here', 'how', 'in', 'in fact', 'indeed', 'instead', 'just',
    'later', 'least', 'less', 'likewise', 'maybe', 'meanwhile', 'more', 'most',

    'much', 'nevertheless', 'nonetheless', 'now', 'off', 'once', 'otherwise', 'out', 'over',
    'perhaps', 'quite', 'so', 'soon', 'still',

    'then', 'there', 'therefore', 'thus', 'together', 'tonight', 'up', 'when', 'where', 'yet'
]

adverb_others_pt_br = [
    'acerca / aproximadamente', 'de novo / novamente / outra vez', 'atrás', 'adiante / à frente', 'por pouco / quase',
    'apenas / só', 'também', 'em todo o caso / de qualquer maneira', 'ao redor / em torno / em volta', 'como',
    'de volta / para trás', 'antes / anteriormente', 'além de / além disso / também', 'do contrário', 'em outro lugar',
    'bastante / suficiente', 'até / mesmo',

    'já / sempre / nunca / jamais', 'rapidamente / velozmente',
    'adiante / para a frente', 'ademais / além disso', 'duramente', 'aqui, cá', 'como / quão', 'dentro',
    'de fato / na verdade', 'de fato / realmente', 'em vez / em vez disso', 'somente', 'mais tarde', 'menos', 'menos',
    'igualmente / também', 'talvez', 'enquanto isso / entretanto', 'mais', 'mais',

    'muito', 'ainda assim / mesmo assim / porém / todavia', 'apesar disso', 'agora / já', 'fora', 'outrora / uma vez',
    'de outro modo', 'fora', 'através / sobre', 'talvez', 'bastante / muito', 'assim / tão / então / portanto',
    'em breve / logo / rapidamente', 'ainda',

    'depois / então', 'ali / lá', 'por isso / portanto', 'assim / portanto / deste modo', 'junto(s) / justamente',
    'hoje à noite / esta noite', 'em cima / para cima', 'quando', 'aonde / onde', 'ainda (final de frase)'
]

# set_box = set({})
#
# while len(set_box) < 3:
#     set_box.add(choice(adverbs_frequency))
#     set_box.add(choice(adverb_others))
#     set_box.add(choice(adverbs_ly))
#     set_box = list(set_box)
#     ""  # there are repeated data among these three variables
#     ""  # in order to avoid any mistakes, we need to know if each data belongs to a different variable
#     see_if_repeats = [set_box[0] in adverbs_frequency, set_box[1] in adverb_others, set_box[2] in adverbs_ly]
#     if False in see_if_repeats:
#         set_box = set(set_box)
#         set_box.clear()

# set_box = list(set_box)

# adverb = set_box[0]
# adverb_inked = painter('blue', adverb)
# adverb_tr = adverbs_frequency_pt_br[adverbs_frequency.index(adverb)]
# adverb_tr_inked = painter('red', adverb_tr)

# adverb2 = set_box[1]
# adverb2_inked = painter('blue', adverb2)
# adverb2_tr = adverb_others_pt_br[adverb_others.index(adverb2)]
# adverb2_tr_inked = painter('red', adverb2_tr)

# adverb3 = set_box[2]
# adverb3_inked = painter('blue', adverb3)
# adverb3_tr = adverbs_ly_pt_br[adverbs_ly.index(adverb3)]
# adverb3_tr_inked = painter('red', adverb3_tr)

if __name__ == '__main__':
    print('\n')

    print(f"{len(adverbs_ly) = }")
    print(f"{len(adverbs_ly_pt_br) = }")
    print(f"{len(adverbs_frequency) = }")
    print(f"{len(adverbs_frequency_pt_br) = }")
    print(f"{len(adverb_others) = }")
    print(f"{len(adverb_others_pt_br) = }")

    # print(adverb)
    # print(adverb_inked)
    # print(adverb_tr)
    # print(adverb_tr_inked)

    # print(adverb2)
    # print(adverb2_inked)
    # print(adverb2_tr)
    # print(adverb2_tr_inked)

    # print(adverb3)
    # print(adverb3_inked)
    # print(adverb3_tr)
    # print(adverb3_tr_inked)

    # print(set_box)

    # print('\n')
    # for words in zip(adverbs_ly, adverbs_ly_pt_br):
    #     print(words)

    # print('\n')
    # for words in zip(adverbs_frequency, adverbs_frequency_pt_br):
    #     print(words)

    # print('\n')
    # for words in zip(adverb_others, adverb_others_pt_br):
    #     print(words)

    # var = set(adverbs_frequency).intersection(set(adverbs_ly))
    # print(var)



from adjetivos.bdd_adjetivos import adjectives, adjectives_pt_br
from metodos.bdd import *
from random import choice
from cores.cores import colors

# todo
from metodos.bdd import sentence_maker as _

from pronomes.bdd_pronomes import (
    pronouns_l, pronouns_pt_br
)

from adjetivos_possessivos.bdd_adjetivos_possessivos import (
    possessive_adjectives_l, possessive_adjectives_l_pt_br
)

from pronomes_possessivos.bdd_pronomes_possessivos import (
    possessive_pronouns_l, possessive_pronouns_l_pt_br
)

from pronomes_demonstrativos.bdd_pronomes_demonstrativos import (
    demonstrative_pronouns_l, demonstrative_pronouns_l_pt_br
)

from pronomes_reflexivos.bdd_pronomes_reflexivos import (
    reflexive_pronouns_l, reflexive_pronouns_l_pt_br
)

from preposicoes.bdd_preposicoes import (
    prepositions, prepositions_pt_br
)

from adverbios.bdd_adverbios import (
    adverbs_ly, adverbs_ly_pt_br,
    adverbs_frequency, adverbs_frequency_pt_br,
    adverb_others, adverb_others_pt_br
)

from conjuncoes.bdd_conjuncoes import (
    conjunctions_l, conjunctions_l_pt_br
)

from wh.bdd_wh import wh_l, wh_l_pt_br

from substantivos.bdd_substantivos import (
    nouns, nouns_pt_br
)

from verbos_be.bdd_verbos_be_simples import (be_past_l, be_past_l_pt_br)
from verbos_be.bdd_verbos_be_simples import (be_present_l, be_present_l_pt_br)
from verbos_be.bdd_verbos_be_simples import (be_future_l, be_future_l_pt_br)

from verbos_can.bdd_verbos_can import (could_past_l, could_past_l_pt_br, can_present_l, can_present_l_pt_br)

from verbos_do.bdd_verbos_do import (do_present_l, do_present_l_pt_br)
from verbos_do.bdd_verbos_do import (do_past_l, do_past_l_pt_br)

from verbos_have.bdd_verbos_have import (have_past_l, have_past_l_pt_br)
from verbos_have.bdd_verbos_have import (have_present_l, have_present_l_pt_br)
from verbos_have.bdd_verbos_have import (have_future_l, have_future_l_pt_br)

from verbos_infinitivo.bdd_verbos_infinitivo import (verbs_infinitive, verbs_infinitive_pt_br)
from verbos_passado.bdd_verbos_passado import (past, past_pt_br)
from verbos_presente.bdd_verbos_presente import (present, present_pt_br)
from verbos_futuro.bdd_verbos_futuro import (future, future_pt_br)
# todo

# TOOLS
black, red, green, yellow, blue, purple, cyan, ink = \
    colors[0], colors[1], colors[2], colors[3], colors[4], colors[5], colors[6], colors[7]

bricks = '=' * 20

quiz_format = """
    {}
    O QUE É {}{}{} ?
    {}
    1 - {}
    2 - {}
    3 - {}
    4 - {}
    5 - {}

    Digite de 1 a 5, para fornecer sua resposta
    Digite após a seta -> """

success = """
    ==================== RELATÓRIO ====================        
    {}Resposta correta{}
    {}Jogos jogados:{} {}
    {}Placar:{} {}Acertos{} {} x {} {}Erros{}
    ===================================================
    """

# todo
input_message = '{}Por favor, aperte ENTER{}'
input_message2 = '{}Clique após a seta, digite sua frase, aperte ENTER, ou apenas aperte ENTER ->{} '

sentence_creation = """
    Sabendo que {}{}{} significa {}{}{}, tente criar uma frase
    
    DICAS
    ==================================================
    Pronome:               (1) {} {}   
    Adjetivo possessivo:   (1) {} {}
    Pronome possessivo:    (1) {} {}
    Pronome demonstrativo: (1) {} {} 
    Pronome reflexivo:     (1) {} {}        
    Preposição:            (1) {} {}   
    Advérbios:             (1) {} {} (2) {} {} (3) {} {} 
    Conjunção:             (1) {} {} (2) {} {}
    Palavras de dúvida:    (1) {} {} 
    Substantivo:           (1) {} {} (2) {} {} (3) {} {}
    
    VERBOS SIMPLES: passado/presente/futuro
    ==================================================
    infinitivo:       (1) {} {}
    passado:          (1) {} {}
    presente:         (1) {} {}
    futuro:           (1) {} {}
    to be:            (1) {} {} (2) {} {} (3) {} {}
    can:              (1) {} {} (2) {} {}
    to do (auxiliar): (1) {} {} (2) {} {}
    to have:          (1) {} {} (2) {} {} (3) {} {}
    """
# todo

failure = """ 
    ==================== RELATÓRIO ====================
    {}Resposta incorreta{}
    {}Resposta correta:{} {} - {}
    {}Jogos jogados:{} {}
    {}Placar:{} {}Acertos{} {} x {} {}Erros{}
    ====================================================
    """

controller = '{}Aperte ENTER ou qualquer outra tecla para continuar...{}'

set_error = """
{} ========== Erro de processamento ========== {}
O conjunto não foi capaz de gerar todos os dados de um jogo
"""

positive_score = 0
negative_score = 0

while True:

    try:

        five_words = set({})


        def create_word():
            """"""
            while len(five_words) < 5:
                five_words.add(choice(adjectives))

        create_word()

        five_words = sorted(list(five_words))

        five_indexes = [adjectives.index(word) for word in five_words]

        five_translations = [adjectives_pt_br[index] for index in five_indexes]

        chosen_word = choice(five_words)

        chosen_word_index = five_words.index(chosen_word)

        chosen_word_translation = five_translations[chosen_word_index]

        the_target_translation = [chosen_word_translation]


        def see_variables():
            """"""
            print(f"{five_words = }")
            print(f"{five_indexes = }")
            print(f"{five_translations = }")
            print(f"{chosen_word = }")
            print(f"{chosen_word_index = }")
            print(f"{chosen_word_translation = }")
            print(f"{the_target_translation = }")

        # see_variables()

        greetings = welcome('treino de adjetivos', prefix=3, prefix2=7)

        print(greetings)

        # todo
        pronoun = _(pronouns_l)
        pronoun_inked = painter('blue', pronoun)
        pronoun_tr = pronouns_pt_br[pronouns_l.index(pronoun)]
        pronoun_tr_inked = painter('red', pronoun_tr)

        possessive_adjective = _(possessive_adjectives_l)
        possessive_adjective_inked = painter('blue', possessive_adjective)
        possessive_adjective_tr = possessive_adjectives_l_pt_br[possessive_adjectives_l.index(possessive_adjective)]
        possessive_adjective_tr_inked = painter('red', possessive_adjective_tr)

        possessive_pronoun = _(possessive_pronouns_l)
        possessive_pronoun_inked = painter('blue', possessive_pronoun)
        possessive_pronoun_tr = possessive_pronouns_l_pt_br[possessive_pronouns_l.index(possessive_pronoun)]
        possessive_pronoun_tr_inked = painter('red', possessive_pronoun_tr)

        demonstrative_pronoun = _(demonstrative_pronouns_l)
        demonstrative_pronoun_inked = painter('blue', demonstrative_pronoun)
        demonstrative_pronoun_tr = demonstrative_pronouns_l_pt_br[demonstrative_pronouns_l.index(demonstrative_pronoun)]
        demonstrative_pronoun_tr_inked = painter('red', demonstrative_pronoun_tr)

        reflexive_pronoun = _(reflexive_pronouns_l)
        reflexive_pronoun_inked = painter('blue', reflexive_pronoun)
        reflexive_pronoun_tr = reflexive_pronouns_l_pt_br[reflexive_pronouns_l.index(reflexive_pronoun)]
        reflexive_pronoun_tr_inked = painter('red', reflexive_pronoun_tr)

        preposition = _(prepositions)
        preposition_inked = painter('blue', preposition)
        preposition_tr = prepositions_pt_br[prepositions.index(preposition)]
        preposition_tr_inked = painter('red', preposition_tr)

        adverb = _(adverbs_frequency)
        adverb_inked = painter('blue', adverb)
        adverb2 = _(adverb_others)
        adverb2_inked = painter('blue', adverb2)
        adverb3 = _(adverbs_ly)
        adverb3_inked = painter('blue', adverb3)

        adverb_tr = adverbs_frequency_pt_br[adverbs_frequency.index(adverb)]
        adverb_tr_inked = painter('red', adverb_tr)
        adverb2_tr = adverb_others_pt_br[adverb_others.index(adverb2)]
        adverb2_tr_inked = painter('red', adverb2_tr)
        adverb3_tr = adverbs_ly_pt_br[adverbs_ly.index(adverb3)]
        adverb3_tr_inked = painter('red', adverb3_tr)

        conjunction = _(conjunctions_l)
        conjunction_inked = painter('blue', conjunction)
        conjunction_tr = conjunctions_l_pt_br[conjunctions_l.index(conjunction)]
        conjunction_tr_inked = painter('red', conjunction_tr)

        conjunction2 = _(conjunctions_l)
        conjunction2_inked = painter('blue', conjunction2)
        conjunction2_tr = conjunctions_l_pt_br[conjunctions_l.index(conjunction2)]
        conjunction2_tr_inked = painter('red', conjunction2_tr)

        while conjunction == conjunction2:
            conjunction2 = _(conjunctions_l)
            conjunction2_inked = painter('blue', conjunction)
            conjunction2_tr = conjunctions_l_pt_br[conjunctions_l.index(conjunction)]
            conjunction2_tr_inked = painter('red', conjunction_tr)

        noun = _(nouns)
        noun_inked = painter('blue', noun)
        noun_tr = nouns_pt_br[nouns.index(noun)]
        noun_tr_inked = painter('red', noun_tr)

        noun2 = _(nouns)
        noun2_inked = painter('blue', noun2)
        noun2_tr = nouns_pt_br[nouns.index(noun2)]
        noun2_tr_inked = painter('red', noun2_tr)

        noun3 = _(nouns)
        noun3_inked = painter('blue', noun3)
        noun3_tr = nouns_pt_br[nouns.index(noun3)]
        noun3_tr_inked = painter('red', noun3_tr)

        while noun == noun2 or noun == noun3 or noun2 == noun3:
            noun = _(nouns)
            noun_inked = painter('blue', noun)
            noun_tr = nouns_pt_br[nouns.index(noun)]
            noun_tr_inked = painter('red', noun_tr)

            noun2 = _(nouns)
            noun2_inked = painter('blue', noun2)
            noun2_tr = nouns_pt_br[nouns.index(noun2)]
            noun2_tr_inked = painter('red', noun2_tr)

            noun3 = _(nouns)
            noun3_inked = painter('blue', noun3)
            noun3_tr = nouns_pt_br[nouns.index(noun3)]
            noun3_tr_inked = painter('red', noun3_tr)

        wh = _(wh_l)
        wh_inked = painter('blue', wh)
        wh_tr = wh_l_pt_br[wh_l.index(wh)]
        wh_tr_inked = painter('red', wh_tr)

        be_present = _(be_present_l)
        be_present_inked = painter('blue', be_present)
        be_present_tr = be_present_l_pt_br[be_present_l.index(be_present)]
        be_present_tr_inked = painter('red', be_present_tr)

        be_past = _(be_past_l)
        be_past_inked = painter('blue', be_past)
        be_past_tr = be_past_l_pt_br[be_past_l.index(be_past)]
        be_past_tr_inked = painter('red', be_past_tr)

        be_future = _(be_future_l)
        be_future_inked = painter('blue', be_future)
        be_future_tr = be_future_l_pt_br[be_future_l.index(be_future)]
        be_future_tr_inked = painter('red', be_future_tr)

        could_past = _(could_past_l)
        could_past_inked = painter('blue', could_past)
        could_past_tr = could_past_l_pt_br[could_past_l.index(could_past)]
        could_past_tr_inked = painter('red', could_past_tr)

        can_present = _(can_present_l)
        can_present_inked = painter('blue', can_present)
        can_present_tr = can_present_l_pt_br[can_present_l.index(can_present)]
        can_present_tr_inked = painter('red', can_present_tr)

        do_past = _(do_past_l)
        do_past_inked = painter('blue', do_past)
        do_past_tr = do_past_l_pt_br[do_past_l.index(do_past)]
        do_past_tr_inked = painter('red', do_past_tr)

        do_present = _(do_present_l)
        do_present_inked = painter('blue', do_present)
        do_present_tr = do_present_l_pt_br[do_present_l.index(do_present)]
        do_present_tr_inked = painter('red', do_present_tr)

        have_past = _(have_past_l)
        have_past_inked = painter('blue', have_past)
        have_past_tr = have_past_l_pt_br[have_past_l.index(have_past)]
        have_past_tr_inked = painter('red', have_past_tr)

        have_present = _(have_present_l)
        have_present_inked = painter('blue', have_present)
        have_present_tr = have_present_l_pt_br[have_present_l.index(have_present)]
        have_present_tr_inked = painter('red', have_present_tr)

        have_future = _(have_future_l)
        have_future_inked = painter('blue', have_future)
        have_future_tr = have_future_l_pt_br[have_future_l.index(have_future)]
        have_future_tr_inked = painter('red', have_future_tr)

        verb_infinitive = _(verbs_infinitive)
        verb_infinitive_inked = painter('blue', verb_infinitive)
        verb_infinitive_tr = verbs_infinitive_pt_br[verbs_infinitive.index(verb_infinitive)]
        verb_infinitive_tr_inked = painter('red', verb_infinitive_tr)

        verb_past = _(past)
        verb_past_inked = painter('blue', verb_past)
        verb_past_tr = past_pt_br[past.index(verb_past)]
        verb_past_tr_inked = painter('red', verb_past_tr)

        verb_present = _(present)
        verb_present_inked = painter('blue', verb_present)
        verb_present_tr = present_pt_br[present.index(verb_present)]
        verb_present_tr_inked = painter('red', verb_present_tr)

        verb_future = _(future)
        verb_future_inked = painter('blue', verb_future)
        verb_future_tr = future_pt_br[future.index(verb_future)]
        verb_future_tr_inked = painter('red', verb_future_tr)
        # todo

        answer = get_input_int(
            text=quiz_format.format(bricks, yellow, chosen_word, ink, bricks, *five_translations),
            start=1,
            limit=5
        )

        # ONE OF THEM IS CORRECT, THE ONLY CORRECT WILL RETURN A NUMBER LESSER THAN 10
        conditions = [
            *[1 if five_translations[0] in the_target_translation else 10],
            *[2 if five_translations[1] in the_target_translation else 11],
            *[3 if five_translations[2] in the_target_translation else 12],
            *[4 if five_translations[3] in the_target_translation else 13],
            *[5 if five_translations[4] in the_target_translation else 14],
        ]

        # THE ONLY NUMBER LESSER THAN 10 IS PLACED AS INDEX 0
        correct_answer_index = sorted(conditions)[0]

        if answer == correct_answer_index:
            positive_score += 1
            print(success.format(
                blue, ink,
                green, ink, positive_score + negative_score,
                red, ink, blue, ink, positive_score, negative_score, red, ink
            ))

            # todo
            input(input_message.format(green, ink))

            print(sentence_creation.format(
                blue, chosen_word, ink, red, the_target_translation[0], ink,
                pronoun_inked, pronoun_tr_inked,
                possessive_adjective_inked, possessive_adjective_tr_inked,
                possessive_pronoun_inked, possessive_pronoun_tr_inked,
                demonstrative_pronoun_inked, demonstrative_pronoun_tr_inked,
                reflexive_pronoun_inked, reflexive_pronoun_tr_inked,
                preposition_inked, preposition_tr_inked,
                adverb_inked, adverb_tr_inked, adverb2_inked, adverb2_tr_inked, adverb3_inked, adverb3_tr_inked,
                conjunction_inked, conjunction_tr_inked,
                conjunction2_inked, conjunction2_tr_inked,
                wh_inked, wh_tr_inked,
                noun_inked, noun_tr_inked,
                noun2_inked, noun2_tr_inked,
                noun3_inked, noun3_tr_inked,
                verb_infinitive_inked, verb_infinitive_tr_inked,
                verb_past_inked, verb_past_tr_inked,
                verb_present_inked, verb_present_tr_inked,
                verb_future_inked, verb_future_tr_inked,
                be_present_inked, be_present_tr_inked,
                be_past_inked, be_past_tr_inked,
                be_future_inked, be_future_tr_inked,
                could_past_inked, could_past_tr_inked,
                can_present_inked, can_present_tr_inked,
                do_past_inked, do_past_tr_inked,
                do_present_inked, do_present_tr_inked,
                have_past_inked, have_past_tr_inked,
                have_present_inked, have_present_tr_inked,
                have_future_inked, have_future_tr_inked,
            ))

            sentence = input(input_message2.format(green, ink))
            # sentence_translation = do_translation(sentence, 'pt')  # comentar, caso API falhe
            with open('frases.txt', 'a') as txt_file:
                # txt_file.write(f"{sentence} -> {sentence_translation}\n")  # comentar, caso API falhe
                txt_file.write(f"{sentence}\n")  # comentar, caso API falhe
            # todo

        else:
            negative_score += 1
            print(failure.format(
                red, ink,
                blue, ink, correct_answer_index, the_target_translation[0],
                green, ink, positive_score + negative_score,
                red, ink, blue, ink, positive_score, negative_score, red, ink
            ))

            # todo
            input(input_message.format(green, ink))

            print(sentence_creation.format(
                blue, chosen_word, ink, red, the_target_translation[0], ink,
                pronoun_inked, pronoun_tr_inked,
                possessive_adjective_inked, possessive_adjective_tr_inked,
                possessive_pronoun_inked, possessive_pronoun_tr_inked,
                demonstrative_pronoun_inked, demonstrative_pronoun_tr_inked,
                reflexive_pronoun_inked, reflexive_pronoun_tr_inked,
                preposition_inked, preposition_tr_inked,
                adverb_inked, adverb_tr_inked, adverb2_inked, adverb2_tr_inked, adverb3_inked, adverb3_tr_inked,
                conjunction_inked, conjunction_tr_inked,
                conjunction2_inked, conjunction2_tr_inked,
                wh_inked, wh_tr_inked,
                noun_inked, noun_tr_inked,
                noun2_inked, noun2_tr_inked,
                noun3_inked, noun3_tr_inked,
                verb_infinitive_inked, verb_infinitive_tr_inked,
                verb_past_inked, verb_past_tr_inked,
                verb_present_inked, verb_present_tr_inked,
                verb_future_inked, verb_future_tr_inked,
                be_present_inked, be_present_tr_inked,
                be_past_inked, be_past_tr_inked,
                be_future_inked, be_future_tr_inked,
                could_past_inked, could_past_tr_inked,
                can_present_inked, can_present_tr_inked,
                do_past_inked, do_past_tr_inked,
                do_present_inked, do_present_tr_inked,
                have_past_inked, have_past_tr_inked,
                have_present_inked, have_present_tr_inked,
                have_future_inked, have_future_tr_inked,
            ))

            sentence = input(input_message2.format(green, ink))
            # sentence_translation = do_translation(sentence, 'pt')  # comentar, caso API falhe
            with open('frases.txt', 'a') as txt_file:
                # txt_file.write(f"{sentence} -> {sentence_translation}\n")  # comentar, caso API falhe
                txt_file.write(f"{sentence}\n")  # comentar, caso API falhe
            # todo

        # input(controller.format(cyan, ink))
        sleep(1)

    except IndexError as error:
        print(set_error.format(red, ink))

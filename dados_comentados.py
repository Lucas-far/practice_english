

# pa, pa_inked, pa_tr, pa_tr_inked = _(possessive_adjectives_l, possessive_adjectives_l_pt_br)
# pr, pr_inked, pr_tr, pr_tr_inked = _(pronouns_l, pronouns_l_pt_br)
# dp, dp_inked, dp_tr, dp_tr_inked = _(demonstrative_pronouns_l, demonstrative_pronouns_l_pt_br)
# pp, pp_inked, pp_tr, pp_tr_inked = _(possessive_pronouns_l, possessive_pronouns_l_pt_br)
# rp, rp_inked, rp_tr, rp_tr_inked = _(reflexive_pronouns_l, reflexive_pronouns_l_pt_br)
#
# adv, adv_inked, adv_tr, adv_tr_inked = _(adverbs_frequency, adverbs_frequency_pt_br)
# adv2, adv2_inked, adv2_tr, adv2_tr_inked = _(adverb_others, adverb_others_pt_br)
# adv3, adv3_inked, adv3_tr, adv3_tr_inked = _(adverbs_ly, adverbs_ly_pt_br)
#
# conj, conj_inked, conj_tr, conj_tr_inked = _(conjunctions_l, conjunctions_l_pt_br)
# conj2, conj2_inked, conj2_tr, conj2_tr_inked = _(conjunctions_l, conjunctions_l_pt_br)
#
# while conj == conj2:
#     conj, conj_inked, conj_tr, conj_tr_inked = _(conjunctions_l, conjunctions_l_pt_br)
#     conj2, conj2_inked, conj2_tr, conj2_tr_inked = _(conjunctions_l, conjunctions_l_pt_br)
#
# prep, prep_inked, prep_tr, prep_tr_inked = _(prepositions_l, prepositions_l_pt_br)
#
# wh, wh_inked, wh_tr, wh_tr_inked = _(wh_l, wh_l_pt_br)
#
# noun, noun_inked, noun_tr, noun_tr_inked = _(nouns, nouns_pt_br)
# noun2, noun2_inked, noun2_tr, noun2_tr_inked = _(nouns, nouns_pt_br)
# noun3, noun3_inked, noun3_tr, noun3_tr_inked = _(nouns, nouns_pt_br)
#
# while noun == noun2 or noun == noun3 or noun2 == noun3:
#     noun, noun_inked, noun_tr, noun_tr_inked = _(nouns, nouns_pt_br)
#     noun2, noun2_inked, noun2_tr, noun2_tr_inked = _(nouns, nouns_pt_br)
#     noun3, noun3_inked, noun3_tr, noun3_tr_inked = _(nouns, nouns_pt_br)
#
# can, can_inked, can_tr, can_tr_inked = _(can_present_l, can_present_l_pt_br)
# could, could_inked, could_tr, could_tr_inked = _(could_past_l, could_past_l_pt_br)
#
# be_past, be_past_inked, be_past_tr, be_past_tr_inked = _(be_past_l, be_past_l_pt_br)
# be_present, be_present_inked, be_present_tr, be_present_tr_inked = _(be_present_l, be_present_l_pt_br)
# be_future, be_future_inked, be_future_tr, be_future_tr_inked = _(be_future_l, be_future_l_pt_br)
#
# do_past, do_past_inked, do_past_tr, do_past_tr_inked = _(do_past_l, do_past_l_pt_br)
# do_present, do_present_inked, do_present_tr, do_present_tr_inked = _(do_present_l, do_present_l_pt_br)
#
# have_past, have_past_inked, have_past_tr, have_past_tr_inked = _(have_past_l, have_past_l_pt_br)
# have_present, have_present_inked, have_present_tr, have_present_tr_inked = _(have_present_l, have_present_l_pt_br)
# have_future, have_future_inked, have_future_tr, have_future_tr_inked = _(have_future_l, have_future_l_pt_br)
#
# verb_inf, verb_inf_inked, verb_inf_tr, verb_inf_tr_inked = _(verbs_infinitive, verbs_infinitive_pt_br)
# verb_past, verb_past_inked, verb_past_tr, verb_past_tr_inked = _(past, past_pt_br)
# verb_present, verb_present_inked, verb_present_tr, verb_present_tr_inked = _(present, present_pt_br)
# verb_future, verb_future_inked, verb_future_tr, verb_future_tr_inked = _(future, future_pt_br)
#
# all_inked_elements = [
#     pa_inked, pa_tr_inked,
#     pr_inked, pr_tr_inked,
#     dp_inked, dp_tr_inked,
#     pp_inked, pp_tr_inked,
#     rp_inked, rp_tr_inked,
#     adv_inked, adv_tr_inked,
#     adv2_inked, adv2_tr_inked,
#     adv3_inked, adv3_tr_inked,
#     conj_inked, conj_tr_inked,
#     conj2_inked, conj2_tr_inked,
#     prep_inked, prep_tr_inked,
#     wh_inked, wh_tr_inked,
#     noun_inked, noun_tr_inked, noun2_inked, noun2_tr_inked, noun3_inked, noun3_tr_inked,
#     can_inked, can_tr_inked,
#     could_inked, could_tr_inked,
#     be_past_inked, be_past_tr_inked,
#     be_present_inked, be_present_tr_inked,
#     be_future_inked, be_future_tr_inked,
#     do_past_inked, do_past_tr_inked,
#     do_present_inked, do_present_tr_inked,
#     have_past_inked, have_past_tr_inked,
#     have_present_inked, have_present_tr_inked,
#     have_future_inked, have_future_tr_inked,
#     verb_inf_inked, verb_inf_tr_inked,
#     verb_past_inked, verb_past_tr_inked,
#     verb_present_inked, verb_present_tr_inked,
#     verb_future_inked, verb_future_tr_inked,
# ]

# print('\n', pa, pa_inked, pa_tr, pa_tr_inked,
#       '\n', pr, pr_inked, pr_tr, pr_tr_inked, '\n', dp, dp_inked, dp_tr, dp_tr_inked,
#       '\n', pp, pp_inked, pp_tr, pp_tr_inked, '\n', rp, rp_inked, rp_tr, rp_tr_inked,
#       '\n', adv, adv_inked, adv_tr, adv_tr_inked, '\n', adv2, adv2_inked, adv2_tr, adv2_tr_inked,
#       '\n', adv3, adv3_inked, adv3_tr, adv3_tr_inked, '\n', conj, conj_inked, conj_tr, conj_tr_inked,
#       '\n', conj2, conj2_inked, conj2_tr, conj2_tr_inked, '\n', prep, prep_inked, prep_tr, prep_tr_inked,
#       '\n', wh, wh_inked, wh_tr, wh_tr_inked, '\n', noun, noun_inked, noun_tr, noun_tr_inked,
#       '\n', noun2, noun2_inked, noun2_tr, noun2_tr_inked, '\n', noun3, noun3_inked, noun3_tr, noun3_tr_inked,
#       '\n', can, can_inked, can_tr, can_tr_inked, '\n', could, could_inked, could_tr, could_tr_inked,
#       '\n', be_past, be_past_inked, be_past_tr, be_past_tr_inked,
#       '\n', be_present, be_present_inked, be_present_tr, be_present_tr_inked,
#       '\n', be_future, be_future_inked, be_future_tr, be_future_tr_inked,
#       '\n', do_past, do_past_inked, do_past_tr, do_past_tr_inked,
#       '\n', do_present, do_present_inked, do_present_tr, do_present_tr_inked,
#       '\n', have_past, have_past_inked, have_past_tr, have_past_tr_inked,
#       '\n', have_present, have_present_inked, have_present_tr, have_present_tr_inked,
#       '\n', have_future, have_future_inked, have_future_tr, have_future_tr_inked,
#       '\n', verb_inf, verb_inf_inked, verb_inf_tr, verb_inf_tr_inked,
#       '\n', verb_past, verb_past_inked, verb_past_tr, verb_past_tr_inked,
#       '\n', verb_present, verb_present_inked, verb_present_tr, verb_present_tr_inked,
#       )

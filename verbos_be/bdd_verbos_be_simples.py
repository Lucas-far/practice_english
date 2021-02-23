

""""""

"--------------------------------------------- VARS PARA PROJETO DE JOGO ----------------------------------------------"
# fácil -> cacha baixa -> sem negação
be_pst_easy = ['am', 'is', 'are']

# médio -> cacha baixa -> com negação
be_pst_average = ['am', 'is', 'are', "am not", "is not", "are not", "isn't", "aren't"]

# fluente -> cacha dupla -> com negação -> negação curta
be_pst_fluent = [
    "am", "is", "are", "am not", "is not", "are not", "isn't", "aren't",
    "Am", "Is", "Are", "Am not", "Is not", "Are not", "Isn't", "Aren't"
]
"-------------------------------------------------------- VARS --------------------------------------------------------"

# global -> dupla cacha
be_pst = [
    "am", "is", "are", "am not", "is not", "are not", "isn't", "aren't",
    "Am", "Is", "Are", "Am not", "Is not", "Are not", "Isn't", "Aren't"
]

# global -> cacha alta
be_pst_u = ["Am", "Is", "Are", "Am not", "Is not", "Are not", "Isn't", "Aren't"]

# global -> cacha baixa
be_present_l = [
    "am", "am not",
    "is", "is not", "isn't",
    "are", "are not", "aren't"
]

be_present_l_pt_br = [
    'sou/estou', 'não sou/estou',
    'é/está', 'não é/está', 'não é/está',
    'são/estão', 'não são/estão', 'não são/estão'
]

am_is_are_u = ['Am', 'Is', 'Are']

am_is_are_l = ['am', 'is', 'are']

am_not = ['Am I not']

is_not = ['Is he not', 'Is she not', 'Is it not', "Isn't he", "Isn't she", "Isn't it"]

are_not = ['Are you not', 'Are we not', 'Are they not', "Aren't you", "Aren't we", "Aren't they"]

am_is_are_not_short_u = ["Isn't", "Aren't"]  # to be [ presente ] cacha alta, negativo curto
am_is_are_not_short_l = ["isn't", "aren't"]  # to be [ presente ] cacha baixa, negativo curto

am_u = ["Am"]
am_l = ["am"]
am_not_u = ["Am not"]
am_not_l = ["am not"]

is_u = ["Is"]
is_l = ["is"]
is_not_u = ["Is not"]
is_not_l = ["is not"]
is_not_short_u = ["Isn't"]
is_not_short_l = ["isn't"]

are_u = ["Are"]
are_l = ["are"]
are_not_u = ["Are not"]
are_not_l = ["are not"]
are_not_short_u = ["Aren't"]
are_not_short_l = ["aren't"]

"------------------------------------------------------ PASSADO -------------------------------------------------------"
# [ passado ] global, dupla cacha
be_past = [
    'was', 'were', "was not", "were not", "wasn't", "weren't",
    'Was', 'Were', "Was not", "Were not", "Wasn't", "Weren't"
]

be_past_u = ['Was', 'Was not', "Wasn't", 'Were', 'Were not', "Weren't"]  # to be [ passado ] global, cacha alta

be_past_l = ['was', 'was not', "wasn't", 'were', 'were not', "weren't"]  # to be [ passado ] global, cacha baixa

be_past_l_pt_br = [
    'fui/era/estava', 'não fui/era/estava', 'não fui/era/estava', 'foram/eram/estavam',
    'não foram/eram/estavam', 'não foram/eram/estavam'
]

be_past_sgl_u = ["Was", "Was not", "Wasn't"]    # to be [ passado ] 1a e 3a pessoa, cacha alta
be_past_sgl_l = ["was", "was not", "wasn't"]    # to be [ passado ] 1a e 3a pessoa, cacha baixa
be_past_pl_u = ['Were', 'Were not', "Weren't"]  # to be [ passado ] 2a pessoa, cacha alta
be_past_pl_l = ['were', 'were not', "weren't"]  # to be [ passado ] 2a pessoa, cacha baixa

was_u = ['Was']               # to be [ passado ] 1a e 3a pessoa, cacha alta
was_l = ['was']               # to be [ passado ] 1a e 3a pessoa, cacha baixa
was_not_u = ["Was not"]       # to be [ passado ] 1a e 3a pessoa, cacha alta, negação
was_not_l = ["was not"]       # to be [ passado ] 1a e 3a pessoa, cacha baixa, negação
was_not_short_u = ["Wasn't"]  # to be [ passado ] 1a e 3a pessoa, cacha alta, negação curta
was_not_short_l = ["wasn't"]  # to be [ passado ] 1a e 3a pessoa, cacha baixa, negação curta

were_u = ['Were']               # to be [ passado ] 2a pessoa, cacha alta
were_l = ['were']               # to be [ passado ] 2a pessoa, cacha baixa
were_not_u = ['Were not']       # to be [ passado ] 2a pessoa, cacha alta, negação
were_not_l = ['were not']       # to be [ passado ] 2a pessoa, cacha baixa, negação
were_not_short_u = ["Weren't"]  # to be [ passado ] 2a pessoa, cacha alta, negação curta
were_not_short_l = ["weren't"]  # to be [ passado ] 2a pessoa, cacha baixa, negação curta

"--------------------------------------------------- FUTURE SIMPLE ----------------------------------------------------"
be_future_l = ['will be', 'will not be', "won't be"]

be_future_l_pt_br = ['será/estará', 'não será/estara', 'não será/estara']

be_future_sgl_u = ["Was", "Was not", "Wasn't"]
be_future_sgl_l = ["was", "was not", "wasn't"]
be_future_pl_u = ['Were', 'Were not', "Weren't"]
be_future_pl_l = ['were', 'were not', "weren't"]

will_u = ['Will']
will_l = ['will']
will_not_u = ["Will not"]
will_not_l = ["will not"]
will_not_short_u = ["Won't"]
will_not_short_l = ["won't"]

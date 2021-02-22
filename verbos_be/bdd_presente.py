

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

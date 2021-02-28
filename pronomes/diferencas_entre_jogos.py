

# Quando o enunciado for em inglês e as opções em português
def en_pt():
    """
    five_words = list(create_set(empty_set, 5, var, True))
    five_indexes = [var.index(word) for word in five_words]
    five_translations = [var_pt_br[index] for index in five_indexes]

    var 1 = lista em inglês    = var
    var 2 = lista em inglês    = var
    var 3 = lista em português = var_pt_br
    """


# Quando o enunciado for em português e as opções em inglês
def pt_en():
    """
    five_words = list(create_set(empty_set, 5, var_pt_br, True))
    five_indexes = [var_pt_br.index(word) for word in five_words]
    five_translations = [var[index] for index in five_indexes]

    var 1 = lista em português = var_pt_br
    var 2 = lista em português = var_pt_br
    var 3 = lista em inglês    = var
    """


# Mudar o enunciado
def codigo():
    """
    EN_PT
    vocabulary = throw_input(write_vocabulary)

    PT_EN
    vocabulary = throw_input(write_vocabulary_type2)
    """



from gramatica.adjetivos.adjetivos import adjectives_keys

from metodos.banco_de_dados import (check_length, verify)


if __name__ == '__main__':

    "--------------------------------------- Verificar quantidade de ADJETIVOS ----------------------------------------"
    print(check_length(
        adjectives_keys
    ))

    "------------------- Procurar ADJETIVOS para saber se devem ser adicionados ou evitar repetição -------------------"
    ""  # um ou mais adjetivos são adicionados em formato de string (entre aspas) (dado escrito em cor verde, abaixo)
    ""  # pesquisar palavras com letra minúscula

    the_report = verify(
        '...', 'soon', 'nice', 'round', 'straigth',
        database=adjectives_keys
    )
    print(the_report)

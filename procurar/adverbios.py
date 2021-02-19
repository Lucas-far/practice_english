

from gramatica.adverbios.adverbios import adv_ly_keys

from metodos.banco_de_dados import (check_length, verify)


if __name__ == '__main__':

    "-------------------------------------- Verificar quantidade de ADVÉRBIOS LY --------------------------------------"
    print(check_length(
        adv_ly_keys
    ))

    "----------------- Procurar ADVÉRBIOS LY para saber se devem ser adicionados ou evitar repetição ------------------"
    ""  # um ou mais advérbios são adicionados em formato de string (entre aspas) (dado escrito em cor verde, abaixo)
    ""  # pesquisar palavras com letra minúscula

    the_report = verify(
        '...', 'lately', 'oddly', 'strangely', 'happily',
        database=adv_ly_keys
    )
    print(the_report)

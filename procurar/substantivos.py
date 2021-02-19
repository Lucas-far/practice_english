

from gramatica.substantivos.substantivos import nouns_keys

from metodos.banco_de_dados import (check_length, verify)


if __name__ == '__main__':

    "-------------------------------------- Verificar quantidade de SUBSTANTIVOS --------------------------------------"
    print(check_length(
        nouns_keys
    ))

    "----------------- Procurar SUBSTANTIVOS para saber se devem ser adicionados ou evitar repetição ------------------"
    ""  # um ou mais substantivos são adicionados em formato de string (entre aspas) (dado escrito em cor verde, abaixo)
    ""  # pesquisar palavras com letra minúscula

    the_report = verify(
        '...', 'castle', 'car', 'windmill', 'girl',
        database=nouns_keys
    )
    print(the_report)

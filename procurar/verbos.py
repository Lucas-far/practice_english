

from gramatica.verbos.infinitivo import verbs_inf_keys
from gramatica.verbos.passado import past_keys
from gramatica.verbos.presente import pst_keys
from gramatica.verbos.futuro import fut_keys

from metodos.banco_de_dados import (check_length, verify)


if __name__ == '__main__':

    "--------------------------------- Verificar se VERBOS estão em mesma quantidade ----------------------------------"
    print(check_length(
        verbs_inf_keys, pst_keys, past_keys, fut_keys
    ))

    "-------------------- Procurar VERBOS para saber se devem ser adicionados ou evitar repetição ---------------------"
    ""  # todos os verbos têm como chave, a forma infinitiva dos verbos
    ""  # portanto, é preciso apenas um dicionário de verbos, já que todos têm a mesma chave
    ""  # o dicionário escolhido foi: [ verbs_inf_keys ]
    the_report = verify(
        'to know', 'to think', 'to determine', 'to resolve',
        database=verbs_inf_keys
    )
    print(the_report)

TAMANHO_DESEJADO = 20


def preenche_caractere_menor_que_20(char: str) -> str:
    return char.zfill(TAMANHO_DESEJADO)


if __name__ == '__main__':
    dados = ["sei", "la", "123", "0", "0800", "dado aleatorio     ", "            e assim", "                    "]

    dicionario = {
        "campo1": preenche_caractere_menor_que_20(dados[0]),
        "campo2": preenche_caractere_menor_que_20(dados[1]),
        "campo3": preenche_caractere_menor_que_20(dados[2]),
        "campo4": preenche_caractere_menor_que_20(dados[3]),
        "campo5": preenche_caractere_menor_que_20(dados[4]),
        "campo6": preenche_caractere_menor_que_20(dados[5]),
        "campo7": preenche_caractere_menor_que_20(dados[6]),
        "campo8": preenche_caractere_menor_que_20(dados[7]),
    }

    for k, v in dicionario.items():
        print(f'{k}:{v}')

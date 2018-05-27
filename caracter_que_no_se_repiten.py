def no_se_repiten(cadena):
    tupla = tuple(cadena)
    caracter_no_repetido = ''
    for i in range(len(tupla)):
        repetido = tupla.count(tupla[i])

        if repetido == 1:
            caracter_no_repetido = tupla[i]
            break
        else:
            caracter_no_repetido = '_'

    return caracter_no_repetido


if __name__ == '__main__':
    print('''
    Se evaluara una secuencia de caracteres y 
    se regresara el primer caracter que no se repita.
    ''')
    cadena = input('    Ingresa todos los caracteres que gustes: ')
    print('')

    resultado = no_se_repiten(cadena)

    if resultado == '_':
        print('    Todos los caracteres se repiten')
    else:
        print(f'   El primer caracrer no repetido es: {resultado}')

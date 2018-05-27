def busqueda_binaria(numeros, numero_buscar, inicio, final):

    mitad = int((inicio + final) / 2)

    if inicio > final:
        return False
    elif numeros[mitad] == numero_buscar:
        return True
    elif numeros[mitad] > numero_buscar:
        return busqueda_binaria(numeros, numero_buscar, inicio, mitad - 1)
    else:
        return busqueda_binaria(numeros, numero_buscar, mitad + 1, final)


if __name__ == '__main__':
    numeros = [1, 2, 3, 5, 8, 9, 10, 11, 13, 16,
               17, 19, 20, 21, 23, 25, 29, 31, 32, 34, 40]
    numero_buscar = int(input('Ingresa un muero: '))
    resultado = busqueda_binaria(numeros, numero_buscar, 0, len(numeros) - 1)

    if resultado:
        print('El número si esta en la lista')
    else:
        print('El número no esta en la lista')

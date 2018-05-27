import os

LETRAS = {
    'a': 'w',
    'b': 'E',
    'c': 'x',
    'd': '1',
    'e': 'a',
    'f': 't',
    'g': '0',
    'h': 'C',
    'i': 'b',
    'j': '!',
    'k': 'z',
    'l': '8',
    'm': 'M',
    'n': 'I',
    'o': 'd',
    'p': '.',
    'q': 'U',
    'r': 'Y',
    's': 'i',
    't': '3',
    'u': ',',
    'v': 'J',
    'w': 'N',
    'x': 'f',
    'y': 'm',
    'z': 'W',
    'A': 'G',
    'B': 'S',
    'C': 'j',
    'D': 'n',
    'E': 's',
    'F': 'Q',
    'G': 'o',
    'H': 'e',
    'I': 'u',
    'J': 'g',
    'K': '2',
    'L': '9',
    'M': 'A',
    'N': '5',
    'O': '4',
    'P': '?',
    'Q': 'c',
    'R': 'r',
    'S': 'O',
    'T': 'P',
    'U': 'h',
    'V': '6',
    'W': 'q',
    'X': 'H',
    'Y': 'R',
    'Z': 'l',
    '0': 'k',
    '1': '7',
    '2': 'X',
    '3': 'L',
    '4': 'p',
    '5': 'v',
    '6': 'T',
    '7': 'V',
    '8': 'y',
    '9': 'K',
    '.': 'Z',
    ',': 'D',
    '?': 'F',
    '!': 'B',
}


def cifrar_inicio():
    def verificar(mensaje):
        mensaje_correcto = False
        for letra in mensaje:
            if letra.isalnum():
                mensaje_correcto = True
            else:
                if letra == '.' or letra == ',' or letra == '?' or letra == '!':
                    mensaje_correcto = True
                else:
                    mensaje_correcto = False
        return mensaje_correcto

    def otra_vez():
        print("""    Quieres salir?
    [S]i
    [N]o
    """)
        salir = input('    Ingresa la opción: ')
        if salir.lower() == 's':
            exit()
        elif salir.lower() == 'n':
            os.system('clear')
            cifrar_inicio()
        else:
            print('Opción no valida. Saliendo.')
            os.system('clear')
            otra_vez()

    def cifrar(true, letra):
        if letra == 'c':
            mensaje = input('    Ingresa el mensaje a cifra: ')
            mensaje_valido = verificar(mensaje)
            if mensaje_valido:
                palabras = mensaje.split(' ')
                mensaje_cifrado = []

                for palabra in palabras:
                    palabra_cifrada = ''
                    for letra in palabra:
                        palabra_cifrada += LETRAS[letra]

                    mensaje_cifrado.append(palabra_cifrada)
                mensaje_procesado = ' '.join(mensaje_cifrado)
                print('')
                print(
                    f'    --- el mensaje cifrado es: {mensaje_procesado} ---')
                print('')
                otra_vez()
            else:
                print('')
                print(
                    '    Mensaje no valido: Solo se aceptan a-z, A-Z, 0-9, ".", ",", "?" y "!".')
                print('')
                otra_vez()

        else:
            mensaje = input('    Ingresa el mensaje a decifra: ')
            mensaje_valido = verificar(mensaje)
            if mensaje_valido:
                palabras = mensaje.split(' ')
                mensaje_decifrado = []

                for palabra in palabras:
                    palabra_decifrada = ''
                    for letra in palabra:
                        for indice, valor in LETRAS.items():
                            if valor == letra:
                                palabra_decifrada += indice

                    mensaje_decifrado.append(palabra_decifrada)
                mensaje_procesado = ' '.join(mensaje_decifrado)
                print('')
                print(
                    f'    --- el mensaje decifrado es {mensaje_procesado} ---')
                print('')
                otra_vez()
            else:
                print('')
                print(
                    '    Mensaje no valido: Solo se aceptan a-z, A-Z, 0-9, ".", ",", "?" y "!".')
                print('')
                otra_vez()


    os.system('clear')
    mensaje = """
    C I F R A D O R  D E  M E N S A J E S
    Qué es lo que te gustaría hacer?

    [c]ifrar un mensaje.
    [d]ecifrar un mensaje.
    [s]alir.

    Solo se aceptan a-z, A-Z, 0-9, ".", ",", "?" y "!".

  """
    print(mensaje)
    letra = input('    Ingres la opción: ')
    print('')

    opcion_correcta = False

    if letra.lower() == 'c':
        opcion_correcta = True
    elif letra.lower() == 'd':
        opcion_correcta = True
    elif letra.lower() == 's':
        exit()
    else:
        print('    Opción no valida.')
        cifrar_inicio()

    cifrar(opcion_correcta, letra.lower())


if __name__ == '__main__':
    cifrar_inicio()

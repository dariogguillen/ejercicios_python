
import random

AHORCADO = ['''
         +---+
         |   |
             |
             |
             |
             |
    ===============''', '''
         +---+
         |   |
         O   |
             |
             |
             |
    ===============''', '''
         +---+
         |   |
         O   |
         |   |
             |
             |
    ===============''', '''
         +---+
         |   |
         O   |
        /|   |
             |
             |
    ===============''', '''
         +---+
         |   |
         O   |
        /|\  |
             |
             |
    ===============''', '''
         +---+
         |   |
         O   |
        /|\  |
        /    |
             |
    ===============''', '''
         +---+
         |   |
         O   |
        /|\  |
        / \  |
             |
    ===============''']

PALABRAS = ['sombra', 'animal', 'django', 'oveja', 'aprender', 'ejercicios', 'caballo', 'perro', 'vaca', 'computadora', 'python', 'abeja', 'diente', 'conejo', 'mantel', 'mesa', 'basura', 'escritorio', 'gorro', 'parque,' 'amuleto', 'cama', 'cuarto', 'descargar', 'curso', 'diario', 'vaso', 'cuadro', 'foto', 'revista', 'esdrujula', 'parlantes', 'radio', 'tutorial', 'naranja', 'manzana', 'celular', 'casco', 'ventana', 'silla', 'pileta', 'juegos', 'televisor', 'heladera', 'modulos', 'cocina', 'timbre', 'estufa', 'enchufe', 'futbol', 'pelota', 'pizarron', 'cargador', 'factura', 'papel', 'impresora', 'telefono', 'remedio', 'planta', 'vegetal', 'aves', 'luna', 'electricidad', 'copa', 'google', 'lenguaje', 'internet', 'jarra', 'microondas', 'manual', 'sarten', 'cortina', 'musica', 'pato']


def seleccion_palabra():
    numero_random = random.randint(0, len(PALABRAS) - 1)
    palabra_seleccionada = PALABRAS[numero_random]
    return palabra_seleccionada


def mostrar_ahorcado(intento, palabra_escondida):
    print(AHORCADO[intento])
    print('')
    print(palabra_escondida)
    print('')
    print('--- * --- * --- * --- * --- * ---')


def ganaste(palabra, intentos):
    print('')
    print('¡¡¡¡Has Ganado!!!!')
    print('')
    print(AHORCADO[intentos])
    print('')
    print(palabra)
    print('')
    exit()


def intentos_restantes(intentos):
    intentos_faltan = len(AHORCADO) - intentos - 1
    print(f'Restan {intentos_faltan} intentos')


def letraRepetida(letra, palabra):
    if letra in palabra:
        print('Esa letra ya esta, prueba con otra.')


def comprobarcion(palabra, intentos):
    letas_faltan = 0

    if '-' in palabra:
        for i in palabra:
            if i == '-':
                letas_faltan += 1
        print('')
        print(f'Faltan {letas_faltan} letras')
        print('')
        intentos_restantes(intentos)
        print('')
    else:
        ganaste(palabra, intentos)


def ahorcado():
    palabra_random = seleccion_palabra()

    ####
    # palabra_fija = 'python'
    # palabra_random = palabra_fija
    ####
    intentos = 0
    palabra_escondida = ['-'] * len(palabra_random)

    while True:

        mostrar_ahorcado(intentos, palabra_escondida)
        print('')
        letra = input('Ingresa una letra: ').lower()
        letraRepetida(letra, palabra_escondida)

        while True:
            try:
                if len(letra) == 1:
                    if letra.isalpha():
                        break
                    else:
                        raise NameError('Solo se aceptan letras')
                elif len(letra) < 1:
                    raise ValueError('Tienes que ingresar una letra')
                else:
                    raise TypeError('Solo ingresa una letra')

            except NameError as ErrorSoloLetras:
                intentos += 1
                print(ErrorSoloLetras)
                intentos_restantes(intentos)
                print('')
                letra = input('Ingresa una letra: ').lower()
                letraRepetida(letra, palabra_escondida)
            except TypeError as ErrorMasDeUnaLetra:
                intentos += 1
                intentos_restantes(intentos)
                print(ErrorMasDeUnaLetra)
                print('')
                letra = input('Ingresa una letra: ').lower()
                letraRepetida(letra, palabra_escondida)
            except ValueError as ErrorMasDeUnaLetra:
                print(ErrorMasDeUnaLetra)
                print('')
                letra = input('Ingresa una letra: ').lower()
                letraRepetida(letra, palabra_escondida)

        checar_letras = []

        for index in range(len(palabra_random)):
            if palabra_random[index] == letra:
                checar_letras.append(letra)

        if len(checar_letras) == 0:
            intentos += 1
        else:
            for index in range(len(palabra_random)):
                if palabra_random[index] == letra:
                    palabra_escondida[index] = letra

        checar_letras = []

        if intentos > 5:
            print(AHORCADO[intentos])
            print('')
            print("GAME OVER")
            print('')
            print(f'La palabra escondida era {palabra_random}')
            print('')
            break
        elif intentos <= 5:
            comprobarcion(palabra_escondida, intentos)


if __name__ == '__main__':

    print('JUEGO DEL AHORCADO')
    ahorcado()

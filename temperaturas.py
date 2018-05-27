def temperaturas(temps):
    suma_temperaturas = 0
    for temp in temps:
        suma_temperaturas += temp

    return suma_temperaturas / len(temps)


if __name__ == '__main__':
    temps = [21, 24, 24, 22, 20, 23, 24]

    resultado = temperaturas(temps)
    print(f'El promedio de las temperaturas es {resultado}')

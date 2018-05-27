def fibonacci(n):
    result = []
    a, b = 0, 1
    while n > b:
      result.append(b)
      a, b = b, b + a
    return result


if __name__ == '__main__':
    print('Función Fibonacci')
    n = int(input('Ingresa numero limite: '))
    print(fibonacci(n))

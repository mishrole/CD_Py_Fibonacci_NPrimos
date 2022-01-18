# Escribe una función llamada fibonacci. Esta función recibe como parámetro un 
# número entero positivo. La función se encarga de imprimir la serie de fibonacci.
# El número recibido como parámetro es la cantidad de números a imprimir.
# 0 1 1 2 3 5 8 13 21 34 55 89

def fibonacci(size):
    counter = 0

    left = 0
    right = 1

    print(left)
    print(right)

    while counter < size - 2:
        current = left + right
        print(current)
        left = right
        right = current
        counter += 1

fibonacci(12)

# Escribe una función llamada numerosPrimos. Esta función recibe como parámetro
# un número entero positivo. La función se encarga de crear un arreglo con los
# números primos desde el 1 hasta el número proporcionado. La función retorna
# el arreglo como resultado.
# 30 => [ 1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29 ]

def numerosPrimos(size):

    result = []

    for num in range(1, size + 1):
        contador = 0

        for i in range(1, num + 1):
            if(num % i == 0):
                contador += 1

        if contador == 2:
            result.append(num)
    
    return result

print(numerosPrimos(30))
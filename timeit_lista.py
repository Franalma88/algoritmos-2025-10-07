import timeit

# Lista de números
numeros = [73, 2, 45, 99, 12, 87, 34, 56, 12, 78, 5, 63, 44, 3, 100, 19, 8, 91, 0, 65,
           77, 45, 33, 25, 18, 97, 46, 59, 80, 12, 41, 23, 71, 69, 22, 84, 60, 90, 7, 53,
           14, 6, 64, 72, 57, 4, 1, 85, 49, 40, 9, 13, 16, 30, 55, 17, 61, 43, 98, 47,
           83, 11, 42, 88, 29, 26, 31, 68, 93, 10, 32, 70, 15, 95, 24, 28, 20, 92, 27, 37,
           36, 38, 81, 35, 75, 39, 48, 62, 67, 21, 89, 50, 51, 79, 82, 58, 66, 76, 54, 94]


def sumar_numeros():
    
    suma = 0
    for i in numeros:
        print(i)
        suma += i
    return suma



duracion = timeit.timeit(stmt="sumar_numeros()", globals=globals(), number=1)

print(f"¡Tarda {duracion} segundos en ejecutarse!")
print(f"La suma total es: {sum(numeros)}")


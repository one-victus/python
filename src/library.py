import os, math, random, datetime, statistics

def lib_test():
    # Manejo de archivos

    cwd = os.getcwd()
    print(cwd)

    files = os.listdir(cwd + '/src')
    print(files)

    files = [file for file in files if file.endswith('.py')]
    print(files)

    # Manejo de matemáticas

    print(math.pi)
    print(math.e)
    print(math.sqrt(2))
    print(math.pow(2, 3))

    # Manejo de aleatoriedad

    print(random.randint(1, 10))
    print(random.random())
    print(random.choice([1, 2, 3, 4, 5]))

    # Manejo de fechas y horas

    print(datetime.datetime.now())
    print(datetime.datetime.now().date())
    print(datetime.datetime.now().time())

    # Manejo de estadísticas

    ventas = [random.randint(150, 1000) for _ in range(1, 26)]
    print(ventas)

    # Media
    print(statistics.mean(ventas))

    # Mediana
    print(statistics.median(ventas))

    # Moda
    print(statistics.mode(ventas))

    # Desviación estándar
    print(statistics.stdev(ventas))

    # Varianza
    print(statistics.variance(ventas))

    # Rango
    print(max(ventas) - min(ventas))

if __name__ == "__main__":
    lib_test()
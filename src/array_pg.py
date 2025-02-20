def array_test():
    # lists
    
    nombres = ['Juan', 'Maria', 'Pedro', 'Ana']
    print(nombres)

    nombres.append('Luis')
    print(nombres)

    nombres.insert(2, 'Chris')
    print(nombres)

    nombres.remove('Ana')
    print(nombres)

    print(nombres[0])
    print(nombres[:2])
    print(nombres[2:])
    print(nombres[-1])
    
    nombres.pop()
    print(nombres)

    nombres.clear()
    print(nombres)

    numbers = [1, 2, 3, 4, 5]
    print(numbers)

    print(numbers.count(3))

    print(numbers.index(3))

    print(max(numbers))

    print(min(numbers))

    print(sum(numbers))

    numbers2 = numbers.copy() # se debe copiar el array para que no se modifique el original
    print(numbers2)    

    #slicing examples
    print(numbers2[1:3])
    print(numbers2[:3])
    print(numbers2[3:])
    print(numbers2[-3:])
    print(numbers2[::2])
    print(numbers2[::-1])

    #matrix

    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(matrix)

    print(matrix[0])
    print(matrix[0][0])
    print(matrix[0][1])
    print(matrix[0][2])

    #tuples

    tupla1 = (1, "hola", True, 4.5)
    print(tupla1)

    tupla3 = (2, "adios", False, -3.14)
    print(tupla3)

    #comprehensions lists

    numbers = [1, 2, 3, 4, 5]
    squares = [x**2 for x in numbers]
    print(squares)
    
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    transposed = [[row[cell] for row in matrix] for cell in range(len(matrix))]

    print(matrix)
    print(transposed)

    data = [
        {
            'name': 'Juan',
            'age': 25
        },
        {
            'name': 'Maria',
            'age': 30
        },
        {
            'name': 'Pedro',
            'age': 35
        }
    ]

    ages = [int(person['age']) for person in data]
    print(ages)

if __name__ == "__main__":
    array_test()
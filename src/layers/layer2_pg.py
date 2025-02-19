def ly2_test():
    # ------------- Inputs -------------

    # nombre = input('Ingrese su nombre: ')
    # print(f'Hola {nombre}')

    # edad = int(input('Ingrese su edad: ')) # int porque input devuelve un string
    # print(f'Edad: {edad}')

    # ------------- Condicionales -------------

    # name = "Isabelle"
    # limit = 8

    # if len(name) > limit:
    #     print("Too large")
    # elif len(name) == limit:
    #     print("Perfect")
    # else:
    #     print("Too short")

    # ------------- Loops -------------

    # colors = ['red', 'green', 'blue', 'yellow', 'purple']

    # for color in colors:
    #     if color == 'red':
    #         continue
    #     print(color)

    # for x in range(len(colors)):
    #     if colors[x] == 'purple':
    #         break
    #     print(x, colors[x])

    # x = 0
    # while x < len(colors):
    #     print(colors[x], "while loop")
    #     x += 1

    # ------------- Iteradores y Generadores -------------

    # names = ["Isabelle", "Juan", "Maria"]

    # for name in names:
    #     print(name)

    # names = iter(names)
    # print(next(names), "next")

    # for name in names: # Iter permite hacer una copia iterable de una lista sin ocupar el mismo espacio en memoria
    #     print(name, "iter")

    # def num_generator(limit): # Misma logica usando yield para crear un generador iterable
    #     num = 1
    #     while num <= limit:
    #         yield num
    #         num += 1

    # nums = num_generator(3)
    # print(next(nums), "next gen")

    # for num in nums:
    #     print(num, "iter gen")

    # ------------- Funciones -------------

    # def plus1(num = False):
    #     if num and isinstance(num, int) and num >= 0:
    #         return num + 1
    #     else:
    #         return "Invalid input"

    # print(plus1(1))
    # print(plus1("1"))

    # ------------- Lambda -------------

    # numbers = [1, 2, 3, 4, 5]
    # plus2 = lambda x: x + 2

    # numbers_plus2 = list(map(plus2, numbers))
    # print(numbers_plus2)

    # filtered_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    # print(filtered_numbers)

    # ------------- Try Except -------------

    def divide(num1, num2):
        if not isinstance(num1, int) or not isinstance(num2, int):
            raise ValueError("Los inputs deben ser enteros")
        return num1 / num2

    try:
        print(divide("1", 0))
    except ZeroDivisionError as e:
        print(e)
    except Exception as e:
        print(e)
    finally:
        print("Finally")

if __name__ == "__main__":
    ly2_test()

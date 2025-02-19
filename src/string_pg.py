def str_test():
    prueba = 'hola'
    prueba_2 = '  victus  '
    prueba_3 = 'vi?c?t?u?s?2'

    print(prueba[-1])
    print(prueba * 3)
    print(len(prueba) > 2)
    print(prueba_2.strip()) # equivalente a trim
    print(prueba_3.replace('?', ''))
    print(prueba, prueba_2.strip(), prueba_3, sep=', ')
    print(f'Prueba 1: {prueba}, Prueba 2: {prueba_2.strip()}, Prueba 3: {prueba_3}')
    print('Probando saltos \nde linea')
    print('Probando escape \'de caracteres\'')

if __name__ == "__main__":
    str_test()
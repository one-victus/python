def num_test():
    x = 10.3556
    y = 5

    print(x + y)
    print(x - y)
    print(x * y)
    print(x / y)
    print(x % y) # resto
    print(x ** y) # potencia
    print(x // y) # division entera
    print(f'Valor de x: {x:.2f}')
    
    y += 1
    x /= 2
    print(y, x)

if __name__ == "__main__":
    num_test()
def dict_test():
    #dictionaries

    products = {
        'cod001': {
            'name': 'laptop',
            'price': 1000
        },
        'cod002': {
            'name': 'mouse',
            'price': 100
        },
        'cod003': {
            'name': 'monitor',
            'price': 200
        },
        'cod004': {
            'name': 'teclado',
            'price': 50
        }
    }

    print(products)

    print(products['cod001'])
    print(products['cod001']['name'])
    print(products['cod001']['price'])

if __name__ == "__main__":
    dict_test()
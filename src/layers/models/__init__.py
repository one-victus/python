from .ly3_employee import Employee

# __all__ define qué símbolos serán exportados cuando se use 'from <módulo> import *'
# En este caso, solo la clase 'Employee' será accesible al importar con '*'
__all__ = ["Employee"]
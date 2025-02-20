# ejemplo de uso no aplicado:

from typing import Callable, TypeVar, Any
from functools import wraps

F = TypeVar("F", bound=Callable)

def validate_chips(func: F) -> F:
    @wraps(func)
    def wrapper(self, key: str, value: int, *args, **kwargs) -> Any:
        if not isinstance(key, str) or not isinstance(value, int):
            raise ValueError("Las fichas deben ser un diccionario con string como keys y enteros como values")
        
        key = key.lower().strip()

        if len(key) == 0:
            raise ValueError("El nombre de la ficha no puede ser vacio")
        
        if value < 0:
            raise ValueError("El valor de la ficha no puede ser negativo")
        
        if key not in self._chips.keys():
            raise ValueError("La ficha no existe")
        
        return func(self, *args, **kwargs)
    
    return wrapper
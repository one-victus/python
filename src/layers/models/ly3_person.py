from abc import ABC, abstractmethod

class Person(ABC):
    # 0. Métodos abstractos
    @abstractmethod
    def introduce_yourself(self):
        """Método abstracto que debe ser implementado por las clases hijas"""
        pass

    # 1. Métodos mágicos/dunder
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self._id = id

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, ID: {self._id}"
    
    def __repr__(self):
        return f"Person(name={self.name}, age={self.age}, id={self._id})"

    # 2. Propiedades (getters y setters)
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        if len(value) < 4:
            raise ValueError("El ID debe tener al menos 4 caracteres")
        self._id = value

    # 3. Métodos públicos
    def celebrate_birthday(self):
        self.age = self._plus_number(self.age)
        print(f"Feliz cumpleaños {self.name}, ahora tienes {self.age} años")

    # 4. Métodos protegidos/privados (si los hubiera)
    def _plus_number(self, number, plus = 1):
        return number + plus
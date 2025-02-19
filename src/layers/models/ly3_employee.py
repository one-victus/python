from .ly3_person import Person

class Employee(Person):
    # 1. Métodos mágicos/dunder
    def __init__(self, name, age, id, position, salary):
        super().__init__(name, age, id)
        self.name = name
        self.age = age
        self._id = id
        self.position = position
        self._salary = salary

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, ID: {self._id}, Position: {self.position}, Salary: {self._salary}"
    
    def __repr__(self):
        return f"Employee(name={self.name}, age={self.age}, id={self._id}, position={self.position}, salary={self._salary})"

    # 2. Propiedades (getters y setters)
    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if not isinstance(value, int):
            raise ValueError("El salario debe ser un número entero")
        if value < 0:
            raise ValueError("El salario no puede ser negativo")
        self._salary = value

    # 3. Métodos públicos
    def introduce_yourself(self):
        print(f"Hola, me llamo {self.name}, tengo {self.age} años y trabajo como {self.position}")

    # 4. Métodos protegidos/privados (si los hubiera)
from layers.models import Employee

def ly3_test():
    employee = Employee("John", 20, "30568777", "Desarrollador", 1000)
    employee.celebrate_birthday()
    print(employee.id)
    print(employee)
    print(repr(employee))
    employee.introduce_yourself()

if __name__ == "__main__":
    ly3_test()
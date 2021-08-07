# Uma aula simples de herança.
# Criar um overload para a classe Employee.
#   nela podemos add outros tipos de atributos
#   que não devem fazer parte da class mãe.


class Person:
    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last

    def info(self):
        print(f"firstname: {self.first_name}")
        print(f"lastname: {self.last_name}")


class Employee(Person):
    def __init__(self, first, last, employee_id, salary):
        self.first_name = first
        self.last_name = last
        self.employee_id = employee_id
        self.salary = salary

    def info(self):
        print(f"firstname: {self.first_name}")
        print(f"lastname: {self.last_name}")
        print(f"employee: {self.employee_id}")
        print(f"salary: {self.salary}")


person = Person('Tom', 'Brady')
employee = Employee('marcos', 'leme', 12, 20000)

person.info()
employee.info()

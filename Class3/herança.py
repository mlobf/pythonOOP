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
        # mesmo usando o super eu tenho que declarar os atributos como parametros
        #   da classe pai dentro no metodo init

        super().__init__(first, last)
        self.employee_id = employee_id
        self.salary = salary

    def info(self):
        super().info()
        print(f"employee: {self.employee_id}")
        print(f"salary: {self.salary}")

    def get_raise(self):
        self.salary += 1.005 * self.salary


class LowPerformanceEmployee(Employee):
    def get_raise(self):
        self.salary += 1.001 * self.salary

    def info(self):
        super().info()
        print('Low performance employee !!')


person = Person('Tom', 'Brady')
employee = Employee('marcos', 'leme', 12, 1000)
low_employee = LowPerformanceEmployee('Joao', 'Filho', 12, 1000)


print('----------------------------------')

low_employee.info()
low_employee.get_raise()
low_employee.get_raise()
low_employee.get_raise()
low_employee.get_raise()
low_employee.info()

print('----------------------------------')


print(dir(low_employee))


for m in dir(low_employee):
    print(m)

class Employee:
    """
        Class name, short name is better.
    """

    def __init__(self, name, age, level='junior'):
        self.__name = name
        self._age = age
        self._level = level
        self._salary = self._compute_salary()

    def promote(self):
        if self._level == 'junior':
            self._level = 'senior'
        elif self._level == 'senior':
            self._level = 'CEO'
        self._salary = self._compute_salary()

    def _compute_salary(self):
        if self._level == 'junior':
            return 10000
        elif self._level == 'senior':
            return 20000
        elif self._level == 'CEO':
            return 1000000
        else:
            print('unknown level')

    def get_salary(self):
        return self._salary

    def get_name(self):
        return self.__name

    def get_age(self):
        return self._age

        # Private atribute.
        # Python hands encapsulation with:
        # _name_of_varible or _name_of_method.


'''
    name mangling
        Python changes the name when it has __ 

'''
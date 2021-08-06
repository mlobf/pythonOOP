class Student:
    def __init__(self,  first_name: str, last_name: str) -> None:
        """
            | A sample Student class 
        """
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def from_fullname_to_separate_name(cls, full_name: str):
        # Used to separate creation to use
        # In this case we got a class method that return a object
        # Factory pattern is a pattern where you call a method on the class
        #   to create an object
        first, last = full_name.split(' ')
        return cls(first, last)  # equivalent to Student(first,last)


s1 = Student('Alex', 'Baldwin')
fuull = s1.from_fullname_to_separate_name('Alex Baldwin')

print(s1.first_name)
print(s1.last_name)

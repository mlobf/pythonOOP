class Person:

    def __init__(self, name='Messi'):
        self.name = name

# Test on Correct
# p = Person()
# print(p.name)

# Test two Correct
# p = Person()
# p.name = 'CR7'
# print(p.name)


# Test Three Correct
# p = Person("CR7")
# print(Person().name)

# Test Four 1
# p1 = Person()
# p2 = Person()
# print(p1 is p2)  # True or False? Correct !

# Test Five
# p1 = Person("CR7")
# p2 = Person("CR7")
# print(id(p1) != id(p2))  # True or False? True. Correct
# print(id(Person) == id(Person()))  # True or False? False. Correct

'''
Problem 5:
As an exercise, try to brainstorm all the different objects involved in MaxHandWins. There is not
one single solution to this and there is usually more than one way to design your classes.
'''


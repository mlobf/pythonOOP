# class Person:

#    def __init__(self, name='Messi'):
#        self.name = name

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
CARD = {
    'suits': {
        'spades': 4,
        'hearts': 3,
        'diamonds': 2,
        'clubs': 1
    },
    'numbers': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'court': {
        'valete': 1,
        'dama': 2,
        'rei': 3},
}


class Player():

    def __init__(self, name, points, rounds):
        self.name = name
        self.points = points
        self.rounds = rounds

    def get_up_points(self):
        self.points += 1
        return print(self.points)

    def get_down_points(self):
        self.points -= 1
        return print(self.points)


print(CARD['suits']['spades'])
print(CARD['numbers'])

class Apple:
    food_type = 'fruit'
    calories_per_100_gram = 50

    def __init__(self, color, weight):
        self.color = color
        self.weight = weight

    def get_calories(self):
        return self.weight/100 * self.calories_per_100_gram


# print(Apple.food_type)
# print(Apple.calories_per_100_gram)

e1 = Apple('red', 100)

e1.food_type = "obrigação"
e2 = Apple('green', 150)

Apple.food_type = 'banana'

# print(e1.food_type, 'e1')
# print(e2.food_type, 'e2')
# print(Apple.food_type, 'Class apple')

print(
    e1.get_calories()
)

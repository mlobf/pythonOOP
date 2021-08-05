class Apple:
    food_type = 'fruit'
    calories = 50

    def __init__(self, color, weight):
        self.color = color
        self.weight = weight

    def set_color(self, color):
        self.color = color

    @classmethod
    def set_calories(cls, calories):
        pass

class Apple:
    """
        Python has no function Overloading
        Use Python 'Method Overwriting insead'
        
    """
    food_type = 'fruit'
    calories = 50

    def __init__(self, color, weight):
        self.color = color
        self.weight = weight

    def set_color(self, color):
        self.color = color

    @classmethod
    def _set_calories(cls, c):
        print(f'cls is of type {type(cls)} and id {id(cls)}')
        cls.calories = c

    @staticmethod
    def volume(r):
        return 4/3*3.14*(r**3)


a = Apple('red', 100)
print(f'id of Apple class : {id(Apple)}')
print(f'id of Apple instance a : {id(Apple)}')


Apple._set_calories(100)

print(a.volume(10))

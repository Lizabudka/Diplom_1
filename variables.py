
class BunVariables:
    name = 'космическая булка'
    price = 119.99


class IngredientVariables:
    ingredient_type = ['SAUCE', 'FILLING']
    name = ['Сычуаньский соус', 'Мясо плюмбуса']
    price = [19.99, 399]


class DatabaseVariables:
    def __init__(self):
        self.buns = BunVariables()
        self.ingredients = IngredientVariables()

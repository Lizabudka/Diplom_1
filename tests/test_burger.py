import pytest
from variables import BunVariables, IngredientVariables
from praktikum.ingredient import Ingredient


class TestBurger:

    def test_set_buns_true(self, create_burger, create_bun):
        create_burger.set_buns(create_bun)
        assert create_burger.bun == create_bun

    def test_add_ingredient_true(self, create_burger, create_ingredient_sauce):
        create_burger.add_ingredient(create_ingredient_sauce)
        assert create_burger.ingredients[0] == create_ingredient_sauce

    def test_remove_ingredient_true(self, create_burger, create_ingredient_sauce):
        create_burger.add_ingredient(create_ingredient_sauce)
        create_burger.remove_ingredient(0)
        assert create_burger.ingredients == []

    def test_move_ingredient_true(self, create_burger, create_ingredient_sauce,
                                  create_ingredient_meat):
        create_burger.add_ingredient(create_ingredient_meat)
        create_burger.add_ingredient(create_ingredient_sauce)
        create_burger.move_ingredient(1, 0)
        assert create_burger.ingredients == [create_ingredient_sauce, create_ingredient_meat]

    def test_get_price_true(self, create_bun, create_ingredient_sauce,
                            create_ingredient_meat, create_burger):
        create_burger.set_buns(create_bun)
        create_burger.add_ingredient(create_ingredient_meat)
        create_burger.add_ingredient(create_ingredient_sauce)
        test_price = create_burger.get_price()
        real_price = BunVariables.price * 2 + sum(IngredientVariables.price)
        assert test_price == real_price

    @pytest.mark.parametrize('ingredients', [{'type': [], 'name': []},
                                             {'type': [IngredientVariables.ingredient_type[0]],
                                              'name': [IngredientVariables.name[0]]},
                                             {'type': [IngredientVariables.ingredient_type[0],
                                                       IngredientVariables.ingredient_type[1]],
                                              'name': [IngredientVariables.name[0],
                                                       IngredientVariables.name[1]]}])
    def test_get_receipt_true(self, create_burger, ingredients, create_bun):
        ingr_price = 0
        create_burger.set_buns(create_bun)

        receipt = [f'(==== {BunVariables.name} ====)']
        for i in range(len(ingredients['type'])):
            receipt.append(f'= {ingredients['type'][i].lower()} {ingredients['name'][i]} =')
            ingr_price += IngredientVariables.price[i]
            ingredient = Ingredient(IngredientVariables.ingredient_type[i],
                                    IngredientVariables.name[i],
                                    IngredientVariables.price[i])
            create_burger.add_ingredient(ingredient)

        receipt.append(f'(==== {BunVariables.name} ====)\n')
        receipt.append(f'Price: {BunVariables.price * 2 + ingr_price}')
        receipt = '\n'.join(receipt)

        test_receipt = create_burger.get_receipt()
        assert receipt == test_receipt

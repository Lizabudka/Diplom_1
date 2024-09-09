from variables import IngredientVariables


class TestIngredient:

    def test_set_type_true(self, create_ingredient_sauce):
        assert create_ingredient_sauce.type == IngredientVariables.ingredient_type[0]

    def test_set_name_true(self, create_ingredient_sauce):
        assert create_ingredient_sauce.name == IngredientVariables.name[0]

    def test_set_price_true(self, create_ingredient_sauce):
        assert create_ingredient_sauce.price == IngredientVariables.price[0]

    def test_get_type_true(self, create_ingredient_sauce):
        assert create_ingredient_sauce.get_type() == IngredientVariables.ingredient_type[0]

    def test_get_name_true(self, create_ingredient_sauce):
        assert create_ingredient_sauce.get_name() == IngredientVariables.name[0]

    def test_get_price_true(self, create_ingredient_sauce):
        assert create_ingredient_sauce.get_price() == IngredientVariables.price[0]

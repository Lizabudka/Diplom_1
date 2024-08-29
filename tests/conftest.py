import pytest
from unittest.mock import patch
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from variables import BunVariables, IngredientVariables, DatabaseVariables


@pytest.fixture(scope='function')
def create_bun():
    bun = Bun(BunVariables.name, BunVariables.price)
    return bun


@pytest.fixture(scope='function')
def create_ingredient_sauce():
    ingredient = Ingredient(IngredientVariables.ingredient_type[0],
                            IngredientVariables.name[0],
                            IngredientVariables.price[0])
    return ingredient


@pytest.fixture(scope='function')
def create_ingredient_meat():
    ingredient = Ingredient(IngredientVariables.ingredient_type[1],
                            IngredientVariables.name[1],
                            IngredientVariables.price[1])
    return ingredient


@patch.object(Database, '__init__', DatabaseVariables.__init__)
@pytest.fixture(scope='function')
def create_database():
    db_test = Database()
    db = DatabaseVariables()
    db_test.ingredients = db.ingredients
    db_test.buns = db.buns
    database = {'db_test': db_test, 'db': db}
    return database


@pytest.fixture(scope='function')
def create_burger():
    burger = Burger()
    return burger

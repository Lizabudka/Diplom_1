
class TestDatabase:

    def test_get_available_buns_true(self, create_database):
        db_test = create_database['db_test']
        db = create_database['db']
        assert db_test.available_buns() == db.buns

    def test_get_available_ingredients_true(self, create_database):
        db_test = create_database['db_test']
        db = create_database['db']
        assert db_test.available_ingredients() == db.ingredients

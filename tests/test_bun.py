from variables import BunVariables


class TestBun:

    def test_set_name_true(self, create_bun):
        assert create_bun.name == BunVariables.name

    def test_set_price_true(self, create_bun):
        assert create_bun.price == BunVariables.price

    def test_get_name_true(self, create_bun):
        assert create_bun.get_name() == BunVariables.name

    def test_get_price_true(self, create_bun):
        assert create_bun.get_price() == BunVariables.price

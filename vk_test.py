import pytest

class TestFloat:
    # Distance between 2 float equal
    def test_one(self):
        a = 10 / 3
        b = 20 / 6

        assert type(a) == type(b) == float

        lam = 10 ** (-10)
        assert (a - b) < lam

    # Operation between floats
    @pytest.mark.parametrize("input,expected", [('1.1*1.1', 1.21), ('1.1+1.1', 2.2), ('1.1-1.1', 0), ('1.1/1.1', 1)])
    def test(self, input, expected):
        lam = 10 ** (-10)
        assert eval(input) - expected < lam

class TestStr:
    # Negative test and concatination
    def test_one(self):
        s_1 = "Cat"
        s_2 = "Meow"
        assert type(s_1) == type(s_2) == str
        assert s_1 + s_2 == "CatMeow"
        with pytest.raises(TypeError):
            s_1 + 1

    # isSomething str test
    @pytest.mark.parametrize("input,something", [('1234', 'digit()'), ('vk', "lower()"), (" ", "space()"), ("FCS", "upper()")])
    def test(self, input, something):
        assert eval(f'"{input}.is{something}"')

class TestSet:
    # Without dublicate
    def test_one(self):
        tree = set()
        tree.add(1)
        tree.add(1)

        assert list(tree).count(1) == 1

    # Empty pop
    def test_two(self):
        tree = set()
        tree.add(1)
        assert tree.pop()
        with pytest.raises(KeyError):
            tree.pop()



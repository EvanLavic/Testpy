import pytest


class TestClass:
    def test_str_case(self):
        try:
            assert "SenTEnCe" == "senTencE"
        except AssertionError:
            pass
    
    def test_str_reverse(self):
        x = "hello"
        assert "olleh" == x[::-1]

    @pytest.mark.parametrize("input_str, result", [("This sentence contains only one H letter", True), ("This sentence contains only h letter", False)])
    def test_str_letter(input_str, result):
        assert "H" in input_str == result

    
    def test_float_eq_int(self):
        x = 15
        y = 5
        assert x / y == int(x/y)
    
    @pytest.mark.parametrize("input_float, result", [(7.0, 3.5), (4.0, 2.0)])
    def test_float_div(input_float, result):
        assert input_float / 2 == result

    def test_three_float(self):
        try:
            assert 2.5 == "two and half"
        except AssertionError:
            pass

import pytest
from calculator.calculator import Calculator

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected

    def test_subtract(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.subtract(a, b)

        # assert
        expected = 3087
        assert result == expected

    def test_multiply(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.multiply(a, b)

        # assert
        expected = 5332114
        assert result == expected

    def test_divide(self):
        # arrange
        a = 27
        b = 9
        cal = Calculator()

        # act
        result = cal.divide(a, b)

        # assert
        expected = 3
        assert result == expected

    def test_divide0(self):
        # arrange
        a = 0
        b = 0
        cal = Calculator()

        # act & assert
        with pytest.raises(ZeroDivisionError, match="division by zero"):
            cal.divide(a, b)




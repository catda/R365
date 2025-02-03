# tests/test_string_calculator.py

import pytest
from calculator.string_calculator import StringCalculator

class TestStringCalculator:
    """Test suite for StringCalculator class."""
    
    @pytest.fixture
    def calculator(self):
        """Fixture to create calculator instance for each test."""
        return StringCalculator()

    def test_empty_string(self, calculator):
        assert calculator.add("") == 0
        
    def test_single_number(self, calculator):
        assert calculator.add("20") == 20
        
    def test_two_numbers(self, calculator):
        assert calculator.add("1,2") == 3
        
    def test_invalid_numbers(self, calculator):
        assert calculator.add("5,tytyt") == 5
        
    def test_multiple_numbers(self, calculator):
        assert calculator.add("1,2,3,4,5,6,7,8,9,10") == 55
        
    def test_multiple_numbers_with_invalid(self, calculator):
        assert calculator.add("1,2,invalid,4,bad,6") == 13

    def test_numbers_greater_than_1000(self, calculator):
        assert calculator.add("2,1001,6") == 8

    def test_exactly_1000(self, calculator):
        assert calculator.add("1000,2") == 1002

    def test_mixed_valid_and_invalid_numbers(self, calculator):
        assert calculator.add("1,2000,3,4000,5") == 9

    def test_negative_numbers_exception(self, calculator):
        with pytest.raises(ValueError, match="Negatives not allowed: \\[-1, -2, -3\\]"):
            calculator.add("1,-1,2,-2,3,-3")

    def test_single_negative_number_exception(self, calculator):
        with pytest.raises(ValueError, match="Negatives not allowed: \\[-5\\]"):
            calculator.add("-5")

    def test_newline_delimiter(self, calculator):
        assert calculator.add("1\n2,3") == 6

    def test_mixed_delimiters(self, calculator):
        assert calculator.add("1\n2\n3,4,5\n6") == 21

    def test_custom_single_char_delimiter(self, calculator):
        assert calculator.add("//#\n2#5") == 7

    def test_custom_delimiter_with_invalid(self, calculator):
        assert calculator.add("//,\n2,ff,100") == 102

    def test_custom_delimiter_with_large_numbers(self, calculator):
        assert calculator.add("//@\n2@1001@5") == 7

    def test_custom_long_delimiter(self, calculator):
        assert calculator.add("//[***]\n11***22***33") == 66

    def test_custom_long_delimiter_with_special_chars(self, calculator):
        assert calculator.add("//[@@##]\n1@@##2@@##3") == 6

    def test_custom_long_delimiter_with_numbers(self, calculator):
        assert calculator.add("//[123]\n1123212323") == 6

    def test_empty_long_delimiter(self, calculator):
        assert calculator.add("//[]\n1,2,3") == 6

    def test_multiple_custom_delimiters(self, calculator):
        assert calculator.add("//[*][!!][r9r]\n11r9r22*hh*33!!44") == 110

    def test_multiple_delimiters_with_numbers(self, calculator):
        assert calculator.add("//[1][2][3]\n11122233") == 6

    def test_multiple_delimiters_with_special_chars(self, calculator):
        assert calculator.add("//[@][#][$]\n1@2#3$4") == 10

    def test_multiple_delimiters_different_lengths(self, calculator):
        assert calculator.add("//[**][!!!][^]\n1**2!!!3^4") == 10

    def test_multiple_empty_delimiters(self, calculator):
        assert calculator.add("//[][]\n1,2,3") == 6
import pytest
import re

# Req6: Support custom single-character delimiter

# Tests for the StringCalculator class
def test_custom_single_char_delimiter():
    calc = StringCalculator()
    assert calc.add("//#\n2#5") == 7

def test_custom_delimiter_with_invalid():
    calc = StringCalculator()
    assert calc.add("//,\n2,ff,100") == 102

def test_custom_delimiter_with_large_numbers():
    calc = StringCalculator()
    assert calc.add("//@\n2@1001@5") == 7

def test_numbers_greater_than_1000():
    calc = StringCalculator()
    assert calc.add("2,1001,6") == 8  # 1001 should be ignored

def test_exactly_1000():
    calc = StringCalculator()
    assert calc.add("1000,2") == 1002  # 1000 should be included

def test_mixed_valid_and_invalid_numbers():
    calc = StringCalculator()
    assert calc.add("1,2000,3,4000,5") == 9  # 2000 and 4000 should be ignored

def test_negative_numbers_exception():
    calc = StringCalculator()
    with pytest.raises(ValueError, match="Negatives not allowed: \\[-1, -2, -3\\]"):
        calc.add("1,-1,2,-2,3,-3")

def test_single_negative_number_exception():
    calc = StringCalculator()
    with pytest.raises(ValueError, match="Negatives not allowed: \\[-5\\]"):
        calc.add("-5")

def test_newline_delimiter():
    calc = StringCalculator()
    assert calc.add("1\n2,3") == 6

def test_mixed_delimiters():
    calc = StringCalculator()
    assert calc.add("1\n2\n3,4,5\n6") == 21

def test_empty_string():
    calc = StringCalculator()
    assert calc.add("") == 0
    
def test_single_number():
    calc = StringCalculator()
    assert calc.add("20") == 20
    
def test_two_numbers():
    calc = StringCalculator()
    assert calc.add("1,5000") == 5001
    
def test_negative_numbers():
    calc = StringCalculator()
    assert calc.add("4,-3") == 1
    
def test_invalid_numbers():
    calc = StringCalculator()
    assert calc.add("5,tytyt") == 5
    
def test_multiple_numbers():
    calc = StringCalculator()
    assert calc.add("1,2,3,4,5,6,7,8,9,10,11,12") == 78

def test_multiple_numbers_with_invalid():
    calc = StringCalculator()
    assert calc.add("1,2,invalid,4,bad,6") == 13

class StringCalculator:
    """A calculator that performs addition on strings of numbers."""
    
    def add(self, numbers: str) -> int:
        """
        Add numbers provided in a string format.
        
        Args:
            numbers: String containing numbers separated by delimiters
            Supports default delimiters (comma, newline) and custom delimiter format: //{delimiter}\n{numbers}
            Numbers greater than 1000 are treated as invalid and ignored
            
        Returns:
            Sum of the valid numbers, with empty or invalid numbers treated as 0
            
        Raises:
            ValueError: If negative numbers are provided
        """
        if not numbers:
            return 0
        
        # Handle custom delimiter format
        delimiter = ','
        if numbers.startswith('//'):
            # Extract custom delimiter and remaining numbers
            delimiter_end = numbers.find('\n')
            if delimiter_end != -1:
                delimiter = numbers[2:delimiter_end]
                numbers = numbers[delimiter_end + 1:]
        
        # Replace newlines with delimiter for consistent splitting
        numbers = numbers.replace('\n', delimiter)
            
        # Split numbers using delimiter
        nums = numbers.split(delimiter)
        
        # Check for negative numbers
        negative_nums = []
        for num in nums:
            try:
                n = int(num)
                if n < 0:
                    negative_nums.append(n)
            except ValueError:
                continue
                
        if negative_nums:
            raise ValueError(f"Negatives not allowed: {negative_nums}")
            
        # Convert and sum valid numbers (≤ 1000), treating invalid as 0
        total = 0
        for num in nums:
            try:
                n = int(num)
                if n <= 1000:  # Only add numbers that are not greater than 1000
                    total += n
            except ValueError:
                total += 0
                
        return total


import pytest

# Req3: Support newline delimiter no failure

# Tests for the StringCalculator class
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
    def add(self, numbers: str) -> int:
        """
        Add numbers provided in a string format.
        
        Args:
            numbers: String containing numbers separated by comma or newline
            
        Returns:
            Sum of the numbers, with empty or invalid numbers treated as 0
        """
        if not numbers:
            return 0
            
        # Replace newlines with commas for consistent splitting
        numbers = numbers.replace('\n', ',')
            
        # Split numbers by comma
        nums = numbers.split(',')
            
        # Convert and sum numbers, treating invalid as 0
        total = 0
        for num in nums:
            try:
                total += int(num)
            except ValueError:
                total += 0
                
        return total


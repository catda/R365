# src/calculator/string_calculator.py

import re
from typing import List, Tuple

class StringCalculator:
    """A calculator that performs addition on strings of numbers."""
    
    def _parse_delimiters(self, numbers: str) -> Tuple[List[str], str]:
        """
        Parse delimiters and return them along with the remaining numbers.
        
        Args:
            numbers: Input string that may contain custom delimiters
            
        Returns:
            Tuple of (list_of_delimiters, remaining_numbers)
        """
        if not numbers.startswith('//'):
            return [','], numbers
            
        # Remove // prefix
        numbers = numbers[2:]
        delimiter_end = numbers.find('\n')
        if delimiter_end == -1:
            return [','], numbers
            
        delimiter_part = numbers[:delimiter_end]
        numbers_part = numbers[delimiter_end + 1:]
        
        delimiters = []
        
        # Check if we have multiple delimiters
        if delimiter_part.startswith('['):
            # Find all bracketed delimiters
            bracket_delimiters = re.findall(r'\[(.*?)\]', delimiter_part)
            if bracket_delimiters:
                delimiters.extend(bracket_delimiters)
            else:
                # Empty brackets case
                delimiters.append(',')
        else:
            # Single delimiter case
            delimiters.append(delimiter_part)
            
        return delimiters or [','], numbers_part
    
    def add(self, numbers: str) -> int:
        """
        Add numbers provided in a string format.
        
        Args:
            numbers: String containing numbers separated by delimiters
            Supports:
            - Default delimiters (comma, newline)
            - Custom delimiter format: //{delimiter}\n{numbers}
            - Custom delimiter format: //[{delimiter}]\n{numbers}
            - Multiple delimiters format: //[{delimiter1}][{delimiter2}]...\n{numbers}
            Numbers greater than 1000 are treated as invalid and ignored
            
        Returns:
            Sum of the valid numbers, with empty or invalid numbers treated as 0
            
        Raises:
            ValueError: If negative numbers are provided
        """
        if not numbers:
            return 0
        
        # Parse delimiters and get remaining numbers
        delimiters, numbers = self._parse_delimiters(numbers)
        
        # Replace all delimiters and newlines with a common separator
        processed_numbers = numbers.replace('\n', ',')
        for delimiter in delimiters:
            processed_numbers = processed_numbers.replace(delimiter, ',')
            
        # Split numbers using common separator
        nums = processed_numbers.split(',')
        
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
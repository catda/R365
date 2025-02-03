"""Configuration file for pytest."""

import pytest
from calculator.string_calculator import StringCalculator

@pytest.fixture(scope="function")
def calculator():
    """Provide a fresh calculator instance for each test."""
    return StringCalculator()

# Add custom markers
def pytest_configure(config):
    """Configure custom pytest markers."""
    config.addinivalue_line(
        "markers", "integration: mark test as an integration test"
    )
    config.addinivalue_line(
        "markers", "unit: mark test as a unit test"
    )
import pytest

from main import BooksCollector

# Fixture to create a new instance of BooksCollector for each test
@pytest.fixture
def collector():
    return BooksCollector()
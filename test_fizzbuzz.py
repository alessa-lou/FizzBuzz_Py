import pytest

from fizzbuzz import fizzbuzz

def test_three_returns_fizz():
    assert fizzbuzz(3) == "Fizz"

def test_five_returns_buzz():
    assert fizzbuzz(5) == "Buzz"

def test_fifteen_returns_fizzbuzz():
    assert fizzbuzz(15) == "FizzBuzz"

def test_non_multiples_return_themselves():
    assert fizzbuzz(7) == 7

def test_unhappy_paths():
    with pytest.raises(TypeError):
        fizzbuzz("Alessaaaa")

from basics.src.inverse import inverse
import pytest

def test_long_list():
    assert inverse(["a","b","c","d","e"]) == "edcba"

def test_four_elements_list():
    assert inverse(["a","b","c","d"]) == "cba"

def test_fail_wheninteger():
    with pytest.raises(TypeError):
        inverse(87)

def test_lower_cases():
    assert inverse("hello") == "olleh"

def test_lower_cases_four_elements():
    assert inverse("hell") == "lleh"

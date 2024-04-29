from exercices.src.fonctions_simples import add, divide, add_integer, alea_uniform
import pytest

    ## test ADD

def test_add_integer():
    assert add_integer(1,3) == 4
    assert add(0,0) == 0
    assert add(-1,1) == 0
    assert add(-1,-1) == -2

def test_add_integer_float():
    assert add(1.2,3) == 4.2


def test_add_floats():
    assert add(2.3,0.6) == 2.9
    assert add (0.0,0.0) == 0.0
    assert add(-1.0,1.0) == 0.0
    assert add(-1.0,-1.0) == -2.0


def test_add_strings():
    assert add("a","b") == "ab"
    assert add("","") == ""

def test_add_list():
    assert add([1,2,3],[5,6]) == [1,2,3,5,6]

def test_add_error_mixedtype():
    with pytest.raises(TypeError):
        add(1,"a")

    ## test DIVIDE

def test_divide_ok():
    assert divide(1,1) == 1

def test_divide_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1,0)

    ## test ADD_INTEGER
def test_add_integer_with_negativenumbers():
    assert add_integer(1,-3) == -2


def test_add_integer_fail_with_string():
    with pytest.raises(TypeError):
        assert add_integer(2,"a")   


def test_add_integer_fail_type_error():
    with pytest.raises(TypeError):
        assert add_integer(1.2,2.6)   

    ## test ALEA_UNIFORM
def test_alea_uniform():
    assert isinstance(alea_uniform(0,10), float)
    assert alea_uniform(0,10) >= 0
    assert alea_uniform(0,10) <= 10

def test_alea_uniform_error():
    with pytest.raises(TypeError):
        alea_uniform(0,"a")

    










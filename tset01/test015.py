import pytest
def inc(x):
    return x+1
def test_answer():
    assert inc(x)==5
def test_true():
    assert 7 is True
def setup_module(module):
    print("每个模块之前")
def teardown_module(module):
    print("每个模块之后")
def setup_function(function):
    print("每个函数之前")
def teardown_function(function):
    print("每个函数之后")
if __name__=="__main__":
    pytest.main()
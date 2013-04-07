from nose.tools import assert_equal, assert_almost_equal, assert_true, \
    assert_false, assert_raises, assert_is_instance
    
from fib import fib

def test_fib1():
    obs = fib(2)
    exp = 1
    assert_equal(obs, exp)

def test_fib2():
    obs = fib(0)
    exp = 0
    assert_equal(obs, exp)

    obs = fib(1)
    exp = 1
    assert_equal(obs, exp)


def test_fib3():
    obs = fib(3)
    exp = 2
    assert_equal(obs, exp)

    obs = fib(6)
    exp = 8
    assert_equal(obs, exp)


def test_fib4():
    obs = fib(13.37)
    exp = NotImplemented
    assert_equal(obs, exp)

    obs = fib(-9000)
    exp = NotImplemented
    assert_equal(obs, exp)
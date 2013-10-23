from nose.tools import assert_equal, assert_almost_equal, assert_true, \
    assert_false, assert_raises, assert_is_instance

from mean import mean

def test_all_zeroes():
    obs = mean([0, 0, 0, 0])
    exp = 0
    assert_equal(obs, exp)

def test_average_string():
    assert_raises(TypeError,mean,["hello","goodbye"])

def test_mean_ten_tenths():
    assert_almost_equal(mean([0.1]*10),0.1)

def test_mean1():
    obs = mean([0, 200])
    exp = 100
    assert_equal(obs, exp)

    obs = mean([0, -200])
    exp = -100
    assert_equal(obs, exp)

    obs = mean([0]) 
    exp = 0
    assert_equal(obs, exp)

def test_floating_mean1():
    obs = mean([1.0, 2.0])
    exp = 1.5
    assert_equal(obs, exp)

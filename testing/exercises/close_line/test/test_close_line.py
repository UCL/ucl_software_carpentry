from nose.tools import assert_equal, assert_almost_equal, assert_true, \
    assert_false, assert_raises, assert_is_instance

from close_line import \
   closest_data_to_line1,closest_data_to_line2,closest_data_to_line3,closest_data_to_line4

import numpy.testing

def assert_behaviour_of_method(input_data, point1, point2,
      correct_index, correct_point, method_to_test):
      data=numpy.array(input_data)

      line_first_point=numpy.array(point1)
      line_second_point=numpy.array(point2)
      
      result=method_to_test(data, line_first_point, line_second_point)
                                    
      # Output is an index of the minimum, and then the minimum
      assert_equal(correct_index, result[0])
      numpy.testing.assert_array_equal(result[1], correct_point)

def assert_behaviour_of_all_methods(input_data,point1,point2,
      correct_index,correct_point):
      for method_to_test in [
        closest_data_to_line1,
        closest_data_to_line2,
        closest_data_to_line3,
        closest_data_to_line4
      ]:
        assert_behaviour_of_method(input_data, point1, point2,
      correct_index, correct_point, method_to_test)

# Here's an example test function, you should add more:
def test_one_point():
    assert_behaviour_of_all_methods([
      [0., 0.]
      ],
      [1.0, 0.0], [0.0, 1.0],
      0, [0., 0.])

def test_two_points():
    assert_behaviour_of_all_methods([
        [0., 0.],
        [0.5, 0.5]
        ],[1., 0.],[0., 1.], 1, [0.5, 0.5])


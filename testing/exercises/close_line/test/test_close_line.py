from nose.tools import *

from close_line import \
   closest_data_to_line1,closest_data_to_line2,closest_data_to_line3,closest_data_to_line4

import numpy

# Here's an example test function, you should add more:
def test_one_point_method_1():
      data=numpy.array([
        [0.,0.] # This data scatter has one point
        ])

      line_first_point=numpy.array([1.,0.])
      line_second_point=numpy.array([0.,1.])

      result=closest_data_to_line1(data,line_first_point,line_second_point)
                                     
      # Output is an index of the minimum, and then the minimum
      assert_equal(0, result[0])
      numpy.testing.assert_array_equal(result[1], [0., 0.])

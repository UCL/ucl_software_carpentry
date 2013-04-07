from nose.tools import assert_equal, assert_almost_equal, assert_true, \
    assert_false, assert_raises, assert_is_instance

from close_line import \
   closest_data_to_line1,closest_data_to_line2,closest_data_to_line3,closest_data_to_line4
 
# Here's an example test function, you should add more:
def test_one_point_method_1():
    

      data=[
        [0.,0.] # This data scatter has one point
        ]

      line_first_point=[1.,0.]
      line_second_point=[0.,1.]

      result=closest_data_to_line1(data,line_first_point,line_second_point)
                                     
      # Output is an index of the minimum, and then the minimum
      assert_equal((0, [0.,0.]),result) 
## Exercise: Writing tests for mean()

There are a few tests for the mean() function that we listed in this
lesson. What are some tests that should fail? Add at least three test
cases to this set. Edit the `test_mean.py` file which tests the mean()
function in `mean.py`.

*Hint:* Think about what form your input could take and what you should
do to handle it. Also, think about the type of the elements in the list.
What should be done if you pass a list of integers? What if you pass a
list of strings?

**Example**:

    nosetests test_mean.py

# Quality Assurance Exercise

    Can you think of other tests to make for the fibonacci function? I promise there 
    are at least two. 

    Implement one new test in test_fib.py, run nosetests, and if it fails, implement 
    a more robust function for that case.

    And thus - finally - we have a robust function together with working
    tests!
    
# Exercise

**The Problem:** In 2D or 3D, we have two points (p1 and p2) which
define a line segment. Additionally there exists experimental data which
can be anywhere in the domain. Find the data point which is closest to
the line segment.

In the `close_line.py` file there are four different implementations
which all solve this problem. [You can read more about them
here.](http://inscight.org/2012/03/31/evolution_of_a_solution/) 

Please write from scratch a `test_close_line.py`
file which tests the closest\_data\_to\_line() functions.

*Hint:* you can use one implementation function to test another. Below
is some sample data to help you get started.

![image](https://github.com/thehackerwithin/UofCSCBC2012/raw/scopz/5-Testing/evo_sol1.png)
> -

```python
import numpy as np

p1 = np.array([0.0, 0.0])
p2 = np.array([1.0, 1.0])
data = np.array([[0.3, 0.6], [0.25, 0.5], [1.0, 0.75]])
```                                                  
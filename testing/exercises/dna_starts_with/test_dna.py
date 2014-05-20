# This file tests the dna package
def test_dna_starts_with():
    from dna import dna_starts_with

    test_cases = [
        ('cgttga', 'c', True),
        ('cgttga', 'g', False),
        ('cgttga', 'cg', True),
        ('cgttga', 'ct', False),
    ]
    for dna, pattern, expected in test_cases: 
       assert dna_starts_with(dna, pattern) == expected

def test_dna_starts_with_UPPER_CASE_INPUT():
    from dna import dna_starts_with

    test_cases = [
        ('CGTTGA', 'C', True),
        ('CGTTGA', 'G', False),
        ('cGttga', 'cg', True),
        ('gcttga', 'gC', True),
    ]
    for dna, pattern, expected in test_cases: 
       assert dna_starts_with(dna, pattern) == expected

def test_failure_on_incorrect_input():
    from dna import dna_starts_with

    for dna, pattern in [('cgx', 'c'), ('cgt', 'xa')]:
        try: dna_starts_with(dna, pattern)
        except ValueError: assert True
        else: assert False


def test_convert_genotypes_one_element_list():
  from dna import convert_genotypes
  from nose.tools import assert_list_equal

  for base, i in {'AA': 0, 'AG': 1, 'GG': 2}.iteritems():
    assert_list_equal(
         convert_genotypes([base]),
         [i],
         "Checks {0} is converted acurately to {1}".format(base, i)
    )
  
def test_convert_genotypes_nelement_list():
  from dna import convert_genotypes
  from nose.tools import assert_list_equal

  assert_list_equal(
       convert_genotypes(["AA", "GG"]),
       [0, 2],
       "Checks list with more than one element"
  )
  
def test_convert_genotypes_fails_on_incorrect_input():
  from dna import convert_genotypes
  from nose.tools import assert_raises

  # Same as try: execpt: else:, but using functionality provided by nosetests 
  with assert_raises(Exception): 
    convert_genotypes(["QQ"])

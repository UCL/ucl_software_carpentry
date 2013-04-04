# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <markdowncell>

# # Python: Functions and Modules

# <markdowncell>

# Materials by: [John Blischak](https://github.com/jdblischak "GitHub") and other Software Carpentry instructors (Joshua R. Smith, Milad Fatenejad, Katy Huff, Tommy Guy and many more)

# <markdowncell>

# As you saw in the last lesson, computers are very useful for doing the same operation over and over. When you know you will be performing the same operation many times, it is best to abstract this functionality into a function (aka method). For example, you used the function `open` in an earlier section. This allowed you to easily open a conncetion to a file without worrying about the underlying code that made it possible (this idea is known as abstraction).   

# <markdowncell>

# # Built-in string methods
# The base distribution comes with many useful functions. When a function works on a specific type of data (lists, strings, dictionaries, etc.), it is called a method.  I will cover some of the basic string methods since they are very useful for reading data into Python.

# <codecell>

# Find the start codon of a gene
dna = 'CTGTTGACATGCATTCACGCTACGCTAGCT'
dna.find('ATG')

# <codecell>

# parsing a line from a comma-delimted file
lotto_numbers = '4,8,15,16,23,42\n'
lotto_numbers.strip().split(',')

# <codecell>

question = '%H%ow%z%d%@d%z%th%ez$%@p%ste%rzb%ur%nz%$%@szt%on%gue%?%'
print question.replace('%', '').replace('@', 'i').replace('$', 'h').replace('z', ' ')

# <codecell>

answer = '=H=&!dr=a=nk!c=~ff&&!be=f~r&=!i=t!w=as!c=~~l.='
print answer.replace('=', '').replace('&', 'e').replace('~', 'o').replace('!', ' ')

# <markdowncell>

# ## Short Exercise: Calculate GC content of DNA

# <markdowncell>

# Because the binding strength of guanine (G) to cytosine (C) is different from the binding strength of adenine (A) to thymine (T) (and many other differences), it is often useful to know the fraction of a DNA sequence that is G's or C's. Go to the [string method section](http://docs.python.org/2/library/string.html) of the Python documentation and find the string method that will allow you to calculate this fraction.

# <codecell>

# Calculate the fraction of G's and C's in this DNA sequence
seq1 = 'ACGTACGTAGCTAGTAGCTACGTAGCTACGTA'
gc = 

# <markdowncell>

# Check your work:

# <codecell>

round(gc, ndigits = 2) == .47

# <markdowncell>

# # Creating your own functions!
# When there is not an available function to perform a task, you can write your own functions.

# <codecell>

def square(x):
    return x * x

# <codecell>

print square(2), square(square(2))

# <codecell>

def hello(time, name):
    """Print a nice message. Time and name should both be strings.
    
    Example: hello('morning', 'Software Carpentry')
    """
    print 'Good ' + time + ', ' + name + '!'

# <codecell>

hello('afternoon', 'Software Carpentry')

# <markdowncell>

# The description right below the function name is called a docstring. For best practices on composing docstrings, read [PEP 257 -- Docstring Conventions](http://www.python.org/dev/peps/pep-0257/).

# <markdowncell>

# ## Short exercise: Write a function to calculate GC content of DNA
# Make a function that calculate the GC content of a given DNA sequence. For the more advanced participants, make your function able to handle sequences of mixed case (see the third test case).

# <codecell>

def calculate_gc(x):
    """Calculates the GC content of DNA sequence x.
    x: a string composed only of A's, T's, G's, and C's."""

# <markdowncell>

# Check your work:

# <codecell>

print round(calculate_gc('ATGC'), ndigits = 2) == 0.50
print round(calculate_gc('AGCGTCGTCAGTCGT'), ndigits = 2) == 0.60
print round(calculate_gc('ATaGtTCaAGcTCgATtGaATaGgTAaCt'), ndigits = 2) == 0.34

# <markdowncell>

# # Modules
# Python has a lot of useful data type and functions built into the language, some of which you have already seen. For a full list, you can type `dir(__builtins__)`. However, there are even more functions stored in modules. An example is the sine function, which is stored in the math module. In order to access mathematical functions, like sin, we need to `import` the math module. Lets take a look at a simple example:

# <codecell>

print sin(3) # Error! Python doesn't know what sin is...yet

# <codecell>

import math # Import the math module
math.sin(3)

# <codecell>

print dir(math) # See a list of everything in the math module

# <codecell>

help(math) # Get help information for the math module

# <markdowncell>

# It is not very difficult to use modules - you just have to know the module name and import it. There are a few variations on the import statement that can be used to make your life easier. Lets take a look at an example:

# <codecell>

from math import *  # import everything from math into the global namespace (A BAD IDEA IN GENERAL)
print sin(3)        # notice that we don't need to type math.sin anymore
print tan(3)        # the tangent function was also in math, so we can use that too

# <codecell>

reset # Clear everything from IPython

# <codecell>

from math import sin  # Import just sin from the math module. This is a good idea.
print sin(3)          # We can use sin because we just imported it
print tan(3)          # Error: We only imported sin - not tan

# <codecell>

reset                 # Clear everything

# <codecell>

import math as m      # Same as import math, except we are renaming the module m
print m.sin(3)        # This is really handy if you have module names that are long

# <markdowncell>

# ## The General Problem
# ![xkcd](http://imgs.xkcd.com/comics/the_general_problem.png "I find that when someone's taking time to do something right in the present, they're a perfectionist with no ability to prioritize, whereas when someone took time to do something right in the past, they're a master artisan of great foresight.")
# From [xkcd](http://www.xkcd.com)
# 
# Now that you can write your own functions, you too will experience the dilemma of deciding whether to spend the extra time to make your code more general, and therefore more easily reused in the future.

# <markdowncell>

# # Longer exercise: Reading Cochlear implant into Python
# For this exercise we will return to the cochlear implant data first introduced in the section on the shell. In order to analyse the data, we need to import the data into Python. Furthermore, since this is something that would have to be done many times, we will write a function to do this. As before, beginners should aim to complete Part 1 and more advanced participants should try to complete Part 2 and Part 3 as well.

# <markdowncell>

# ## Part 1: View the contents of the file from within Python
# Write a function `view_cochlear` that will open the file and print out each line. The only input to the function should be the name of the file as a string. 

# <codecell>

def view_cochlear(filename):
    """Write your docstring here.
    """
       

# <markdowncell>

# Test it out:

# <codecell>

view_cochlear('data/alexander/data_216.DATA')

# <codecell>

view_cochlear('data/Lawrence/Data0525')

# <markdowncell>

# ## Part 2: 
# Adapt your function above to exclude the first line using the flow control techniques we learned in the last lesson. The first line is just `#` (but don't forget to remove the `'\n'`).

# <codecell>

def view_cochlear(filename):
    """Write your docstring here.
    """
    

# <markdowncell>

# Test it out:

# <codecell>

view_cochlear('data/alexander/data_216.DATA')

# <codecell>

view_cochlear('data/Lawrence/Data0525')

# <markdowncell>

# ## Part 3:
# Adapt your function above to return a dictionary containing the contents of the file. Split each line of the file by a colon followed by a space (': '). The first half of the string should be the key of the dictionary, and the second half should be the value of the dictionary.

# <codecell>

def save_cochlear(filename):
    """Write your docstring here.
    """

# <markdowncell>

# Check your work:

# <codecell>

data_216 = save_cochlear("data/alexander/data_216.DATA")
print data_216["Subject"]

# <codecell>

Data0525 = save_cochlear("data/alexander/data_216.DATA")
print Data0525["CI type"]

# <markdowncell>

# # Bonus Exercise: Transcribe DNA to RNA
# ### Motivation:
# During transcription, an enzyme called RNA Polymerase reads the DNA sequence and creates a complementary RNA sequence. Furthermore, RNA has the nucleotide uracil (U) instead of thymine (T). 
# ### Task:
# Write a function that mimics transcription. The input argument is a string that contains the letters A, T, G, and C. Create a new string following these rules: 
# 
# * Convert A to U
# 
# * Convert T to A
# 
# * Convert G to C
# 
# * Convert C to G
# 
# Hint: You can iterate through a string using a for loop similary to how you loop through a list.

# <codecell>

def transcribe(seq):
    """Write your docstring here.
    """

# <markdowncell>

# Check your work:

# <codecell>

transcribe('ATGC') == 'UACG'

# <codecell>

transcribe('ATGCAGTCAGTGCAGTCAGT') == 'UACGUCAGUCACGUCAGUCA'


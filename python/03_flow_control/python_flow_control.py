# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <markdowncell>

# # Python: Flow Control

# <markdowncell>

# Materials by: [John Blischak](https://github.com/jdblischak "GitHub") and other Software Carpentry instructors (Joshua R. Smith, Milad Fatenejad, Katy Huff, Tommy Guy and many more)

# <markdowncell>

# In this lesson we will cover how to write code that will execute only if specified conditions are met and also how to automate repetitive tasks using loops.

# <markdowncell>

# # If statements
# 
# A conditional (if statement) is some statement that in general says :
# "When some boolean is true, do the following. Otherwise, do this other
# thing."
# 
# Many equivalence test statements exist in Python that are similar in
# other languages: `< > <= >= == !=`

# <codecell>

x = 5
if x < 0:
    print "x is negative"

# <codecell>

x = -5
if x < 0:
    print "x is negative"

# <codecell>

x = 5
if x < 0:
    print "x is negative"
else:
    print "x in non-negative"

# <codecell>

x = 5
if x < 0:
    print "x is negative"
elif x == 0:
    print "x is zero"
else:
    print "x is positive"

# <markdowncell>

# Be careful because the computer interprets comparisons very literally.

# <codecell>

'1' < 2

# <codecell>

True == 'True'

# <codecell>

False == 0

# <codecell>

'Bears' > 'Packers'

# <markdowncell>

# Python has other equivalence test statements that are fairly
# unique to python. To check whether an object is contained in a list :

# <codecell>

beatle="John"
beatles=["George", "Ringo","John", "Paul"]
print beatle in beatles # is John one of the beatles? : TRUE
print "Katy" not in beatles # this is also TRUE. 

# <markdowncell>

# ## Indentation
# The indentation is a feature of python that some people hate. Some other programming languages use brackets to denote a command block. Python uses indentation. The amount of indentation doesn't matter, so long as everything in the same block is indented the same amount.

# <markdowncell>

# ## Short Exercise
# Write an if statement that prints whether x is even or odd.

# <markdowncell>

# # Loops
# Loops come in two flavors: `while` and `for`.

# <codecell>

fruits = ['apples', 'oranges', 'pears', 'bananas']
i = 0
while i < len(fruits):
    print fruits[i]
    i = i + 1

# <codecell>

for fruit in fruits:
    print fruit

# <codecell>

# Use range for a range on integers
for i in range(len(fruits)):
    print i, fruits[i]

# <codecell>

# Use zip to iterate over two lists at once
fruits = ['apples', 'oranges', 'pears', 'bananas']
prices = [0.49, 0.99, 1.49, 0.32]
for fruit, price in zip(fruits, prices):
    print fruit, "cost", price, "each"
    

# <codecell>

# Use "items" to iterate over a dictionary
# Note the order is non-deterministic
prices = {'apples': 0.49, 'oranges': 0.99, 'pears': 1.49, 'bananas': 0.32}
for fruit, price in prices.items():
    print fruit, "cost", price, "each"
          

# <codecell>

# Calculating a sum
values = [1254, 95818, 61813541, 1813, 4]
sum = 0
for x in values:
    sum = sum + x
sum

# <markdowncell>

# ## Short Exercise
# Using a loop, calculate the factorial of 42 (the product of all integers up to and including 42).

# <markdowncell>

# ## break, continue, and else
# 
# A break statement cuts off a loop from within an inner loop. It helps
# avoid infinite loops by cutting off loops when they're clearly going
# nowhere.

# <codecell>

reasonable = 10
for n in range(1,2000):
    if n == reasonable :
        break
    print n

# <markdowncell>

# Something you might want to do instead of breaking is to continue to the
# next iteration of a loop, giving up on the current one.

# <codecell>

reasonable = 10
for n in range(1,20):
    if n == reasonable :
      continue
    print n

# <markdowncell>

# What is the difference between the output of these two?
# 
# Importantly, Python allows you to use an else statement in a for loop.
# 
# That is :

# <codecell>

knights={"Sir Belvedere":"the Wise", "Sir Lancelot":"the Brave", \
        "Sir Galahad":"the Pure", "Sir Robin":"the Brave", "The Black Knight":"John Clease"} 

favorites=knights.keys()
favorites.remove("Sir Robin")
for name, title in knights.iteritems() : 
    string = name + ", "
    for fav in favorites :
        if fav == name :
            string += title
            break
    else:
        string += title + ", but not quite so brave as Sir Lancelot." 
    print string

# <markdowncell>

# # Reading from a file

# <codecell>

less example.txt

# <codecell>

my_file = open("example.txt")
for line in my_file:
    print line.strip()
my_file.close()

# <markdowncell>

# # Writing to a file

# <codecell>

new_file = open("example2.txt", "w")
dwight = ['bears', 'beets', 'Battlestar Galactica']
for i in dwight:
    new_file.write(i + '\n')
new_file.close()

# <codecell>

less example2.txt

# <markdowncell>

# # Longer Exercise: Convert genotypes
# If most of this material is brand new to you, your goal is to complete Part 1. If you are more experienced, please move on to Part 2 and Part 3. And don't forget to talk to your neighbor!

# <markdowncell>

# ### Motivation:
# A biologist is interested in the genetic basis of height. She measures the heights of many subjects and sends off their DNA samples to a core for genotyping arrays. These arrays determine the DNA bases at the variable sites of the genome (known as single nucleotide polymorphisms, or SNPs). Since humans are diploid, i.e. have two of each chromosome, each data point will be two DNA bases corresponding to the two chromosomes in each individual. At each SNP, there will be only three possible genotypes, e.g. AA, AG, GG for an A/G SNP. In order to test the correlation between a SNP genotype and height, she wants to perform a regression with an additive genetic model. However, she cannot do this with the data in the current form. She needs to convert the genotypes, e.g. AA, AG, and GG, to the numbers 0, 1, and 2, respectively (in the example the number corresponds the number of G bases the person has at that SNP). Since she has too much data to do this manually, e.g. in Excel, she comes to you for ideas of how to efficiently transform the data.

# <markdowncell>

# ## Part 1:
# Create a new list which has the converted genotype for each subject ('AA' -> 0, 'AG' -> 1, 'GG' -> 2).

# <codecell>

genos = ['AA', 'GG', 'AG', 'AG', 'GG']
genos_new = []
# Use your knowledge of if/else statements and loop structures below.

# <markdowncell>

# Check your work:

# <codecell>

genos_new == [0, 2, 1, 1, 2]

# <markdowncell>

# ## Part 2:
# Sometimes there are errors and the genotype cannot be determined. Adapt your code from above to deal with this problem (in this example missing data is assigned NA for "Not Available").

# <codecell>

genos_w_missing = ['AA', 'NA', 'GG', 'AG', 'AG', 'GG', 'NA']
genos_w_missing_new = []
# The missing data should not be converted to a number, but remain 'NA' in the new list

# <markdowncell>

# Check your work:

# <codecell>

genos_w_missing_new == [0, 'NA', 2, 1, 1, 2, 'NA']

# <markdowncell>

# ## Part 3:
# The file genos.txt has a column of genotypes. Read in the data and convert the genotypes as above. Hint: You'll need to use the built-in string method strip to remove the new-line characters (See the example of reading in a file above. We will cover string methods in the next section).

# <codecell>

# Store the genotypes from genos.txt in this list
genos_from_file = []

# <markdowncell>

# Check your work:

# <codecell>

genos_from_file[:15] == [2, 2, 1, 1, 0, 0, 2, 2, 2, 0, 'NA', 1, 0, 0, 2]

# <markdowncell>

# # Bonus material: List comprehensions

# <markdowncell>

# Python has another way to perform iteration called list comprehensions.

# <codecell>

# Multiply every number in a list by 2 using a for loop
nums1 = [5, 1, 3, 10]
nums2 = []
for i in range(len(nums1)):
    nums2.append(nums1[i] * 2)
    
print nums2

# <codecell>

# Multiply every number in a list by 2 using a list comprehension
nums2 = [x * 2 for x in nums1]

print nums2

# <codecell>

# Multiply every number in a list by 2, but only if the number is greater than 4
nums1 = [5, 1, 3, 10]
nums2 = []
for i in range(len(nums1)):
    if nums1[i] > 4:
        nums2.append(nums1[i] * 2)
    
print nums2

# <codecell>

# And using a list comprehension
nums2 = [x * 2 for x in nums1 if x > 4]

print nums2


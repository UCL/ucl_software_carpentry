# Python 1: Variables and types

* * * * 

**Based on Lecture Materials By: Milad Fatenejad, Katy Huff, Tommy Guy, Joshua R. Smith, Will Trimble, and many more**

## Variables

All programming languages have variables, and python is no different. To create a variable, just name it and set it with the equals sign. One important caveat: variable names can only contain letters, numbers, and the underscore character. Lets set a variable.

```python
In [1]: experiment = "current vs. voltage"

In [2]: print experiment
current vs. voltage

In [3]: voltage = 2

In [4]: current = 0.5

In [5]: print voltage, current
2 0.5
```

## Types and Dynamic Typing

Like most programming languages, things in python are typed. The type refers to the type of data. We've already defined three different types of data in experiment, voltage, and current. The types are string, integer, and float. You can inspect the type of a variable by using the type command.

```python
In [6]: type(experiment)
Out[6]: <type 'str'>

In [7]: type(voltage)
Out[7]: <type 'int'>

In [8]: type(current)
Out[8]: <type 'float'>
```

Python is a dynamically typed language (unlike, say, C++). If you know what that means, you may be feeling some fear and loathing right now. If you don't know what dynamic typing means, the next stuff may seem esoteric and pedantic. Its actually important, but its importance may not be clear to you until long after this class is over.

Dynamic typing means that you don't have to declare the type of a variable when you define it; python just figures it out based on how you are setting the variable. Lets say you set a variable. Sometime later you can just change the type of data assigned to a variable and python is perfectly happy about that. Since it won't be obvious until (possibly much) later why that's important, I'll let you marinate on that idea for a second. 

Here's an example of dynamic typing. What's the type of data assigned to voltage?

```python
In [9]: type(voltage)
Out[9]: <type 'int'>
```

Lets assign a value of 2.7 (which is clearly a float) to voltage. What happens to the type?

```python
In [10]: voltage = 2.7

In [11]: type(voltage)
Out[11]: <type 'float'>
```

You can even now assign a string to the variable voltage and python would be happy to comply.

```python
In [12]: voltage = "2.7 volts"

In [13]: type(voltage)
Out[13]: <type 'str'>
```

I'll let you ruminate on the pros and cons of this construction while I change the value of voltage back to an int:

```python
In [14]: voltage = 2
```

## Coersion
It is possible to coerce (a fancy and slightly menacing way to say "convert") certain types of data to other types. For example, its pretty straightforward to coerce numerical data to strings.

```python
In [19]: voltageString = str(voltage)

In [20]: currentString = str(current)

In [21]: voltageString
Out[21]: '2'

In [22]: type(voltageString)
Out[22]: <type 'str'>
``` 

As you might imagine, you can go the other way in certain cases. Lets say you had numerical data in a string.

```python
In [23]: resistanceString = "4.0"

In [24]: resistance = float(resistanceString)

In [25]: resistance
Out[25]: 4.0

In [26]: type(resistance)
Out[26]: <type 'float'>
```

What would happen if you tried to coerce resistanceString to an int? What about coercing resistance to an int? Consider the following:

```python
In [27] resistanceString = "4.0 ohms"
```

Do you think you can coerce that string to a numerical type?

## On Being Precise with floats and ints

Again, the following may seem esoteric and pedantic, but it is very important. So bear with me.

Lets say you had some voltage data that looks like the following

```
0
0.5
1
1.5
2
```

Obviously, if you just assigned this data individually to a variable, you'd end up with the following types

```
0   -> int
0.5 -> float
1   -> int
1.5 -> float
2   -> int
```

But what if you wanted all of that data to be floats on its way in? You could assign the variable and then coerce it to type float:

```python
In [28]: voltage = float(1)
```

But that's ugly. If you want whats otherwise an integer to be a float, just add a period at the end

```python
In [29]: voltage = 1.

In [30]: type(voltage)
Out[30]: <type 'float'>
```

This point becomes important when we start operating on data in the next section.

## Data Operations

In this section all of the discussion in the previous section becomes important. I don't know if I'd call this stuff fundamental to the language, but its pretty important and it will zing you if you aren't careful. The takeaway is that you need to be precise with what you are doing. Lets say you want to add some integers.

```python
In [31]: a = 1

In [32]: b = 2

In [33]: c = a+b

In [34]: c
Out[34]: 3

In [38]: type(a), type(b), type(c)
Out[38]: (<type 'int'>, <type 'int'>, <type 'int'>)
```

So we got a vale of three for the sum, which also happens to be an integer. Any operation between two integers is another integer. Makes sense.

So what about the case where a is an integer and b is a float?

```python
In [39]: a = 1

In [40]: b = 2.

In [41]: c = a + b

In [42]: c
Out[42]: 3.0

In [43]: type(a), type(b), type(c)
Out[43]: (<type 'int'>, <type 'float'>, <type 'float'>)
```

You can do multiplication on numbers as well.

```python
In [44]: a = 2

In [45]: b = 3

In [46]: c = a * b

In [47]: c
Out[47]: 6

In [48]: type(a), type(b), type(c)
Out[48]: (<type 'int'>, <type 'int'>, <type 'int'>)
```

Also division.

```python
In [49]: a = 1

In [50]: b = 2

In [51]: c = a / b

In [52]: c
Out[52]: 0
```

**ZING!**

Here's why type is important. Divding two integers returnes an integer: this operation calculates the quotient and floors the result to get the answer.

If everything was a float, the division is what you would expect.

```python
In [53]: a = 1.

In [54]: b = 2.

In [55]: c = a / b

In [56]: c
Out[56]: 0.5

In [57]: type(a), type(b), type(c)
Out[57]: (<type 'float'>, <type 'float'>, <type 'float'>)
```

There are operations that can be done with strings.

```python
In [58]: firstName = "Johann"

In [59]: lastName = "Gambolputty"

In [60]: fullName = firstName + lastName

In [61]: print fullName
JohannGambolputty
```

When concatenating strings, you have to be explicit since computers don't understand context.

```python
In [62]: fullName = firstName + " " + lastName

In [63]: print fullName
Johann Gambolputty
```

There are other operations deined on string data. Use the dir comnand to find them. One example I'll show is the upper method. Lets take a look at the documentation.

```python
In [64]: str.upper?
Type:           method_descriptor
Base Class:     <type 'method_descriptor'>
String Form:    <method 'upper' of 'str' objects>
Namespace:      Python builtin
Docstring:
    S.upper() -> string                                                                                                                        
    
    Return a copy of the string S converted to uppercase.
```

So we can use it to upper-caseify a string. 

```python
In [65]: fullName.upper()
Out[65]: 'JOHANN GAMBOLPUTTY'
```

You have to use the parenthesis at the end because upper is a method of the string class.

For what its worth, you don't need to have a variable to use the upper() method, you could use it on the string itself.

```python
In [66]: "Johann Gambolputty".upper()
Out[66]: 'JOHANN GAMBOLPUTTY'
```

What do you think should happen when you take upper of an int?  What about a string representation of an int?

That wraps up this lesson. We tried out the iPython shell and got some experience with ints, floats, and strings. Along the way we talked about some philosophy and how programming is about people.


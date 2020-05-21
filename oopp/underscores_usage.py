"""
1. Leading single uderscore: Its just a convention to tell developer not to 
use this variable or method externally. But calling the variable or  method
is technically ok for the interpreter.

2. Trailing single uderscore: Its is used to resolve conflict with python 
keywords. E.g. if you want to name your variable or method to be class, 
normally you can not do that. But adding a underscore you can do so. calss_
is okay.

3. Leading double underscore: It is also called name mangling in python. 
When we use double leading underscore in variable name or method name, python
changes the name by appending class name to it to avoid conflict in subclasses
in case of overriding methods. And also, you can not access a variable or 
method from outside of class just by the variable name or method name. This 
also give some kind of abstraction.

N.B. __ in python community is reffered as "dunders". E.g. __baz will be called
as "dunder baz" or __init__ will be called as "dunder init".

4. Double leading and training underscores: When leading and trailing double
underscores are used, the methods are sometimes reffered as "magic methods"
And these methos have special use cases. e.g. __init__ as constructor of a 
class or __call__ to make an object callable.

5. Single standallone underscore: 
- It signifies a "don't care" variable. We can use it when we do not care about
the values assigned to it.

- In an interactive python shell, _ refers the result of last expression. 
e.g.
>> 5 + 7
>> 12
>> _
# _ will result in the previous output
>> 12

lets see another example,

>>> list()
[]
>>> _.append(1)
>>> _.append(2)
>>> _.append(3)
>>> _
[1, 2, 3]



"""
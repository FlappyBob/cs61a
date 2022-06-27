# Note of *cs61a*: *Recap of Python basics* (from 1-1 to 1-5)
**Author** : ***FlappyHimself*** edited by June.27th 

## Purpose: Recap grammar
### Some key words:
1. **prompt** : >>>, meaning "提示"
2. **infix** : An affix inserted inside a word stem .
3. **call expression**: function with some arguments.
![](photo/1.jpg)
4. **bind**: A intrinsic designed object is referred to a name.

### Fast commands during interactive session
<**control -P**> previous  
<**control -N**> next
<**control -D**> exits a session

### Interpreter procedures:
Literally Statements typically describe actions, like the use of "=" operator, while expression describes computation. Interpreter is the program that follows certain procedures to understand the complex expressions in program. 

<br>

> "A programming language is more than just a means for instructing a computer to perform tasks. The language also serves as a framework within which we organize our ideas about computational processes."   --1.2 beginning

*Insane Quote, fabulous...*
<br>


**How interpreter assignment statement?**: 
1. evaluate all the expressions to the right of the = (from left to right), which also includes the value of the function as well.
```python
1   f = max 
2   # This statement first evaluates the max function, then bound the function to name "f". 
```
2. bind all the name to the values from the right. 
<br>

**How python interpreter evaluates a call expression?**
1. Python evaluates the function name first.
2. Then evaluate its operand
3. If the operand is complex, then use method of evaluating the call expression again. 
4. Repeating the process until the operand is successfully evaluated. 
![](photo/2.jpg)
*Expression tree* : The tree conventionally grows from the top down.

<br>

### The environment matters!
The name would bind to different things, so that interpreter would interpret them into different values based on different environment. And call expression, name and even numerals are interpreted as well. 
```python
>>> print(print(1), print(2))
1
2
None
None
```
This is *impure function*.

#### Functions in environment:
*Functions has two names: one is **intrinsic** name, another is its **bound** name.*

**About function evaluation:**
Function also follows certain computational process in Python. Firstly look at function name. When we execute the function. The system leaves extra memory for a local frame. 

**About name evaluation:**
The value we found is bound to the value it attached to in the earliest frame where we found the name. 
Basically, 
> We say that the scope of a local name is limited to the body of the user-defined function that defines it. 

But,
>Well-chosen function and parameter names are essential for the human interpretability of function definitions!
<br>

**Some rules for choosing names:**
1. Function name should describes the function it employs,characterizable in a single line of text.
2. Parameters should be clear in its use, as well as simplicity
3. Depending on the function's ability, make the code as clean as possible. 
>If you find yourself copying and pasting a block of code, you have probably found an opportunity for functional abstraction. Functions should be defined generally.

**Considering function abstraction:**
1. Domain
2. Range.
3. Intent(Relationship between input and output)
*Basically,just as what we've done in high school when designing the function*
<br>

#### Docstring in python:
*Example:*
```python
>>> def pressure(v, t, n):
        """Compute the pressure in pascals of an ideal gas.

        Applies the ideal gas law: http://en.wikipedia.org/wiki/Ideal_gas_law

        v -- volume of gas, in cubic meters
        t -- absolute temperature in degrees kelvin
        n -- particles ofzw gas
        """
        k = 1.38e-23  # Boltzmann's constant
        return n * k * t / v
```
You can also type
```python
>>> help(pressure)
# This would help you to understand the function "pressure"
# And type q to quite the help page.
```
🔗：[docString 规范](https://peps.python.org/pep-0257/)
<br>

#### Boolean context: 
***0, None, False** indicates false in boolean context.*
<br>

**Boolean operators:**
Using **and, or, not**. 
```python
>>> True and False
False
>>> True or False
True
>>> not False
True
```
<br>

#### Test:
```python
1       from fib import fib
2       def fib_test():
3           assert fib(2) == 1
4           assert fib(3) == 1
5           assert fib(50) == 7778742049
```
It's quite common to generates another file with the suffix “.test”. And most of the time we just use **doctest.**

**Doctest:**
```python
def fib(k):
    curr = 1
    pred = 1
    n = 2
    while n < k:
        pred, curr = curr, curr + pred
        n += 1
    return curr
'''
>>> fib(8)
13
'''
```

*Use this command to run the doctest*
```python
>>> python3 -m doctest <python_source_file>
```

***Long way to go... 刚把爹马休***
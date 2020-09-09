

# a = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# print(a)

# person_1 = 18
# person_2 = 20
# person_3 = 33
# if(
#     person_1 > 1 and
#     person_2 > 2 and
#     person_3 > 3
# ):
#     print("That is good.")

# a = 1 +\
#     2 + 3\
#     + 4
# print(a)

# a = 'Faizan ' \
#     'is ' \
#     'a ' \
#     'good ' \
#     'boy.'
# print(a)

"""This is for
    multiple line
    comments"""
# a = 'How old are you'
"""The above is a 
    variable containing the string
    'How old are you'. """

# x = 10
# flag = (x == 10) and (x < 12)
# print(flag)
# """Readable code."""

# import keyword
# print(keyword.iskeyword('False'))
# print(keyword.iskeyword('for'))
# print(keyword.iskeyword('Django'))

# import keyword
# print("List of all keywords : \n", keyword.kwlist)

# a = 5
# print('The value of a is ' + str(a))
# print('or')
# print('The value of a is', a)

# # One liner if-else instead of Conditional Operator (?:) in Python
# a = 1 if 20 > 10 else 0
# print(a)

# a, b, c = [1, 2, 3] # a=1, b=2, c=3
# print(a, b, c)

# # ----------- sep(separator) parameter in print -----------
# print('09', '03', '2020', sep='-')
# print('faizan', 'gmail.com', sep='@')
# l = ['faizan', 'owais', 'taha', 'moaz']
# for name in l:
#     print(name, 'gulzar', sep='---')

# # -------- Formatting output using string module operator(%) -----------
# """The general syntax for a format placeholder is :
#     %[flags][width][.precision]type
#     """
# print('---%2d , -%5.2f' %(3, 6.345))
# # prints interger and float value
# print('--%10.2E--' %(345.4567))
# # prints exponential value





# # --------- Formatting output using format method ---------
# print( 'I am {}. He is {}'.format('Faizan', 'Owais'))
# """using format() method and
#     referring a position of the object"""
# print( 'I am {0}. He is {1}'.format('Faizan', 'Owais'))
# print( 'I am {1}. He is {0}'.format('Faizan', 'Owais'))
# """using format() method and
#     combining positional and keyword arguments"""
# print( 'I am {0}. He is {1}.'
#        ' and {other1} and {other2}'.format('Faizan', 'Owais', other1='Taha', other2='Moaz'))
# # using format() method with number
# # {0:3d} => 0 = position of argument , 3d = integer type with width of 3 characters
# print('Faizan = {0:3d} and Owais = {1:7.2f}'.format(99, 43.343))
# # with keyword argument
# print('Faizan = {num:3d} and Owais = {mark:7.2f}'.format(num=99, mark=43.343))

# """To show format() used for
#     dictionary"""
# dic = { 'faizan':99, 'owais':88, 'taha':77 }
# # using format() in dictionary
# print( "Faizan's Marks = {0[faizan]}. "
#        "Owais's Marks = {0[owais]}. "
#        "Taha's Marks = {0[taha]}. ".format(dic))
# # another way
# print( "Faizan's Marks = {faizan}. "
#        "Owais's Marks = {owais}. "
#        "Taha's Marks = {taha}. ".format(**dic))
#




# # ----- Formatting output using string method ------------
# # str.ljust(), str.rjust(), str.centre()
#
# # Python program to
# # format a output using
# # string() method
#
# st = "I love Pakistan."
#
# # Printing the center aligned string with fillchr
# print("Center aligned string with fillchr: ")
# print(st.center(40, '-'))
#
# # Printing the left aligned string with "-" padding
# print("The left aligned string is : ")
# print(st.ljust(40, '-'))
#
# # Printing the right aligned string with "-" padding
# print("The right aligned string is : ")
# print(st.rjust(40, '-'))




# ---------- Creating a String -------------
# """
# Strings in python can be created using single quotes or
# double quotes or even triple quotes.
# """
# string1 = 'Welcome to the Pakistan'
# string1 = 'Welcome to ' \
#           'the Pakistan'
# # output = Welcome to the Pakistan
# string2 = "I'm Faizan"
# string3 = '''I am a string
# with triple quotes. Creating String with
# triple quotes allow multiple lines and print
# as it is.'''
# print(string3)
# """
# output =
# I am a string
# with triple quotes. Creating String with
# triple quotes allow multiple lines and print
# as it is.
# """

# --------- String Slicing ----------
# string1 = 'My name is faizan'
# # slicing from index '3' to '2nd last index - 1'
# print(string1[3:-2])
#
# # string1[3] = 'p' # error
# # # string object does not support item assignment
# # del string1[3] # error
# # # string object does not support item deletion
#
# # deleting entire string object is possible
# del string1
# print(string1) # NameError: name 'string1' is not defined



# ------- Escape Sequencing in Python ---------
"""
While printing Strings with single and double quotes 
in it causes SyntaxError because String already contains
 Single and Double Quotes and hence cannot be printed
  with the use of either of these. Hence, to print such
   a String either Triple Quotes are used or Escape
    sequences are used to print such Strings.
Escape sequences start with a backslash and can be 
interpreted differently. If single quotes are used 
to represent a string, then all the single quotes 
present in the string must be escaped and same is 
done for Double Quotes.
"""
# # Initial String
# String1 = '''I'm a "Geek"'''
# print("Initial String with use of Triple Quotes: ")
# print(String1)
#
# # Escaping Single Quote
# String1 = 'I\'m a "Geek"'
# print("\nEscaping Single Quote: ")
# print(String1)
#
# # Escaping Double Quotes
# String1 = "I'm a \"Geek\""
# print("\nEscaping Double Quotes: ")
# print(String1)
#
# # Printing Paths with the
# # use of Escape Sequences
# String1 = "C:\\Python\\Geeks\\"
# print("\nEscaping Backslashes: ")
# print(String1)

"""
To ignore the escape sequences in a String,
 r or R is used, this implies that the string is 
 a raw string and escape sequences inside it are 
 to be ignored.
"""
# # Printing Geeks in HEX
# String1 = "This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
# print("\nPrinting in HEX with the use of Escape Sequences: ")
# print(String1)
#
# # Using raw String to
# # ignore Escape Sequences
# String1 = r"This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
# print("\nPrinting Raw String in HEX Format: ")
# print(String1)
#
# # Output:
# #
# # Printing in HEX with the use of Escape Sequences:
# # This is Geeks in HEX
# #
# # Printing Raw String in HEX Format:
# # This is \x47\x65\x65\x6b\x73 in \x48\x45\x58





# ----------- Formatting of String --------
"""
A string can be left(<), right(>) or center(^) 
justified with 
the use of format specifiers, separated by colon(:).
"""
# # String alignment
# String1 = "|{:<10}|{:^10}|{:>10}|".format('Geeks', 'for', 'Geeks')
# print("\nLeft, center and right alignment with Formatting: ")
# print(String1)
# # To demonstrate aligning of spaces
# String1 = "\n{0:^16} was founded in {1:<4}!".format("GeeksforGeeks", 2009)
# print(String1)



# # ---- Logical Operators on String in Python -------
#
# str1 = ''
# str2 = 'faizan'
# # 'repr' is used to print the string along with the quotes
# print(repr(str1 and str2)) # empty
# print(repr(str1 or str2)) # output = 'faizan'
#
# str1 = 'for'
# print(repr(str1 and str2)) # Returns str2(last string)
# print(repr(str2 and str1 and 'owais'))
# # Returns 'owais' (last string)
# # if not any string is empty then output will be the
# # last string in case of 'and' logical operator.
#
# print(repr(str1 or str2))  # Returns str1(first string)
# print(repr(str2 or str1))  # Returns str2(first string)
# # if not any string is empty then output will be the
# # first string in case of 'or' logical operator.
#
# print(repr(not 'faizan')) #output= False
# print(repr(not '')) #output= True

# Note that the
# bitwise operators (| , &) don’t work for strings.




# # not important
# # A Python program to demonstrate working of string template
# from string import Template
#
# # List Student stores the name and marks of three students
# Student = [('Ram', 90), ('Ankit', 78), ('Bob', 92)]
#
# # We are creating a basic structure to print the name and
# # marks of the students.
# t = Template('Hi $name, you have got $marks marks')
#
# for i in Student:
#     print(t.substitute(name=i[0], marks=i[1]))
#
# # output=
# # Hi Ram, you have got 90 marks
# # Hi Ankit, you have got 78 marks
# # Hi Bob, you have got 92 marks

# -------------------------------------------------



"""
Declaring Docstrings: The docstrings are declared 
using “””triple double quotes””” just below the 
class, method or function declaration. All functions 
should have a docstring.

Accessing Docstrings: The docstrings can be accessed 
using the __doc__ method of the object or using the 
help function.
"""
# def my_function():
#     """Demonstrates docstrings and does nothing really."""
#     return None
#
# print("Access docstring using my_function.__doc__")
# print(my_function.__doc__)
# # or
# help(my_function)

# ----- Multi-line Docstrings
# def my_function(arg1):
#     """
#     Summary line.
#
#     Extended description of function.
#
#     Parameters:
#     arg1 (int): Description of arg1
#
#     Returns:
#     int: Description of return value
#
#     """
#
#     return arg1
#
# print(my_function.__doc__)


# ------------------------------------------------------

"""
Program to String slicing in Python to check if a string can 
become empty by recursive deletion
"""
# # This is orginal string in which have to slice and
# # identify whether the string will become empty.
# # ( string )
# ori_str = 'faifaizanzan'
# # matching string ( sub_string )
# str = 'faizan'
#
# while True:
#     s = ori_str
#     # index i = 0 to 6 and range(7)
#     # if ori_str = 'faifaizanzan' and
#     # str = 'faizan'
#     for i in range(len(ori_str)-len(str)+1):
#         # matching after slicing at every index
#         if ori_str[i:i+len(str)] == str:
#             # string found
#             # Now deletion of matched string
#             ori_str = ori_str[0:i] + ori_str[i+len(str):]
#             # now size of orginal string ( ori_str ) is
#             # changed so we have to recall the for loop
#             break
#
#     # if orignal string is same after any round.
#     # then it means that there is not any sub-str in
#     # orinal string.
#     if s == ori_str:
#         print('No. String can "not" become empty.')
#         break
#     if ori_str == '':
#         print("Yes. String can become empty.")
#         break
#
# print(repr(ori_str))


# --------------------------------------------------------

# -------- String functions ----------

# link : https://www.geeksforgeeks.org/python-strings/

# ord('w') function is used to convert character to its
# ascii code

# #--- string.translate() function
# # specifying the mapping
# # using ASCII
# table = {ord('w'):ord('g'), ord('y'): ord('f'),
#          ord('u'):None}
# print(ord('w')) # ord() convert character to ascii
# # target string
# trg = "weeksyourweeks"
#
# # Printing original string
# print("The string before translating is : ", end="")
# print(trg)
#
# # using translate() to make translations.
# print("The string after translating is : ", end="")
# print(trg.translate(table))


# v = 'aeiou'
# c = {}.fromkeys(v)
# print(c)
# # out= {'a': None, 'e': None, 'i': None, 'o': None, 'u': None}
# c = {}.fromkeys(v,0)
# print(c)
# # output= {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}


# --------------------------------------------------------



# import string
#
# print(string.ascii_letters)
# # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.digits)
# print(string.hexdigits)
# print(string.octdigits)
# print(string.punctuation)
# # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# print(string.printable)
# # 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# print(string.whitespace)


# str = "My name is Faizan. I am a professional developer."
# str1 = str + 'I work on Python Language.'
# print(id(str))
# print(id(str1))


# ---------------------------------



# -------------- List -------------

# list1 = [1, 2]
# print(len(list1))
# t = [5, 6]
# # append(value)
# list1.append(t)
# print(list1) # [1, 2, [5, 6]]

# list.insert(position, value)

# # list.extend() => add multiple elements at a time
# list = [1, 2, 3]
# print(id(list))
# list.extend([8, 'Geeks', 'Always'])
# print(list)
# print(id(list)) # same id as above
# # out= [1, 2, 3, 8, 'Geeks', 'Always']

# --- remove() method
#  Remove method in List will only remove the first
#  occurrence of the searched element.
# list.remove(2)

# ---- pop() - remove last element
# ---- pop(index) - remove element at index
# optional: index

# clear() - removes all items from the list

# index() - returns the index of first matched item
# list_name.index(element, start, end)

# count() - returns the count of number of items
# passed as an argument

# sort()
# reverse()
# copy()

# reduce(fun,seq)
# - https://www.geeksforgeeks.org/reduce-in-python/
# from functools import reduce
# lis = [ 1, 2, 3, 4, ]
# print (reduce(lambda a,b: a+b, lis))
# At first step, first two elements of sequence
# are picked and the result is obtained.
# import operator
# print(reduce(operator.add, lis))
# print(reduce(operator.mul, lis))
# print(reduce(operator.add, ['faizan', 'gulzar']))

# from itertools import accumulate
# print(list(accumulate(lis, lambda a,b: a+b)))

# print(sum(lis))

# a = list(filter(lambda x: (x == 2),lis))
# print(a)

# result = map(lambda x: x + x, lis)
# print(list(result))

# numbers1 = [1, 2, 3]
# numbers2 = [4, 5, 6]
# result = map(lambda x, y: x + y, numbers1, numbers2)
# print(list(result))
# # out = [5, 7, 9]


# # List of strings
# l = ['sat', 'bat', 'cat', 'mat']
# # map() can listify the list of strings individually
# test = list(map(list, l))
# print(test)
# # out= [['s', 'a', 't'], ['b', 'a', 't'], ['c', 'a', 't'], ['m', 'a', 't']]






# ---- Tuple ----------

# print(tuple('faizan'))
# # string to tuple
# # ('f', 'a', 'i', 'z', 'a', 'n')

# tup = ()
# print(type(tup))
# # <class 'tuple'>

# tup = ('faizan',) * 3
# print(tup)
# # ('faizan', 'faizan', 'faizan')

# mydict = {0 : "Apple", 1 : "Orange"}
# x = all(mydict)
# print(x)
# # Returns False because the first key is false.
# # For dictionaries the all() function checks the keys, not the values.

# all()
# any()
# len()
# enumerate()
# max()
# min()
# sum()
# sorted()
# tuple()






# ---- set ---

# set1 = set()
# set1 = set('faizan')
# print(set1)

# Note – Lists cannot be added to a set as elements
# because Lists are not hashable whereas Tuples can
# be added because tuples are immutable and hence
# Hashable.

# set1. add(8)

# For addition of two or more elements
# Update() method is used.

# set1 = set([4, 5, (6, 7)])
# set1.update([10, 11])
# print(set1)
# # {10, 11, 4, 5, (6, 7)}

# set1 = set([1, 2, 3, 4, 5, 6,
#             7, 8, 9, 10, 11, 12])
# set1.remove(5)
# set1.remove(6)
# print(set1)
# # {1, 2, 3, 4, 7, 8, 9, 10, 11, 12}
# set1.discard(8)
# set1.discard(9)
# print(set1)
# # {1, 2, 3, 4, 7, 10, 11, 12}

# # Removing last element from the
# # Set using the pop() method
# set1.pop()

# set1.clear()


# Python program to demonstrate
# working of a FrozenSet

# # Creating a Frozenset Set
# String = ('G', 'e', 'e', 'k', 's', 'F', 'o', 'r')
# print(type(String))
# Fset1 = frozenset(String)
# # Frozen sets in Python are immutable objects
# print("The FrozenSet is: ")
# print(Fset1)
# # To print Empty Frozen Set
# # No parameter is passed
# print("\nEmpty FrozenSet: ")
# print(frozenset())







# -------- Dictionary Data type -----------

# dic = dict([(1, 'faizan'), (2, 'owais')])
# print(dic)

# dic = {1: 'faizan', 2: 'owais',
#        3: {'a': 'taha', 'b': 'moaz'}}
# dic['value_set'] = 2, 3, 4
# print(dic)
# # {1: 'faizan', 2: 'owais', 3: {'a': 'taha', 'b': 'moaz'}, 'value_set': (2, 3, 4)}

# dic = {}
# dic.get(key)

# # Deleting a Key value
# del Dict[6]

# https://www.geeksforgeeks.org/python-dictionary/

# dictionary_name.values()

# # str()
# s = str({1:'faizan'})
# print(type(s))







# ------------ Array -----------
#
# import array
# # array.array(datatype, value_list)
#
# # int type
# a = array.array('i', [1, 2, 3])
# print(a)
# print(type(a))
#
# # float type
# b = array.array('d', [1.1, 2.2])
#
# # https://www.geeksforgeeks.org/python-arrays/








# --------- Variables ----------

# # int(string, base in which string is)
# s = '10010'
# c = int(s, 2)
# print(c)
# print(int('10010'))
# print(float(s))
#
# print(ord('0')) # 48
# print(chr(48))
#
# print(complex(34, 3))
# print(type(complex(34, 3)))


# # -------- Encoding and Decoding -------
# # string object
# a = 'faizangulzar'
# # byte object
# c = b'faizangulzar'
# d = a.encode('ASCII')
# print(c == d) # True
#
# e = d.decode('ASCII')
# print(a == e) # True

# print(__name__)
# __main__







# -------- Operators -----------------

# # ---- Bitwise operators
# x = int('1001', 2) # binary to int
# y = int('0011', 2)
# print(x & y)
# print(x | y)
# print(y)
# print(~y)



# ------- Ternary Operator in Python------

# a, b = 10, 20
# min = a if a < b else b
# print(min)
# # 10


# # Python program to demonstrate ternary operator
# a, b = 10, 20
#
# # Use tuple for selecting an item
# # (if_test_false,if_test_true)[test]
# print((b, a)[a < b]) # 10
#
# # Use Dictionary for selecting an item
# print({True: a, False: b}[a < b]) # 10
#
# # lambda is more efficient than above two methods
# # because in lambda  we are assure that
# # only one expression will be evaluated unlike in
# # tuple and Dictionary
# print((lambda: b, lambda: a)[a < b]()) # 10
#


# ------- Operator overloading --------
# class A:
#     def __init__(self, a):
#         self.a = a
#
#     # adding two objects
#     def __add__(self, other):
#         return self.a + other.a
#
# ob1 = A(1)
# ob2 = A(2)
# ob3 = A('Faizan')
# ob4 = A('Gulzar')
#
# print(ob1 + ob2)
# print(ob3 + ob4)

# https://www.geeksforgeeks.org/operator-overloading-in-python/

# expression list1 += [1, 2, 3, 4] modifies
# the list in-place, means it extends the
# list such that “list1” and “list2” still
# have the reference to the same list.

# expression list1 = list1 + [1, 2, 3, 4]
# creates a new list and changes “list1”
# reference to that new list and “list2”
# still refer to the old list.


# -----------------------------------------------------


# -------- Control Flow ------------


# module 'itertools' provide three type of
# infinite iterators:

# # - count(start, step)
# import itertools
# # for in loop
# for i in itertools.count(5, 5):
#     if i == 35:
#         break
#     else:
#         print(i, end=" ")
# # 5 10 15 20 25 30

# https://www.geeksforgeeks.org/python-itertools/

"""
cycle(iterable):
    This iterator prints all values in order
    from the passed container. It restarts 
    printing from the beginning again when 
    all elements are printed in a cyclic 
    manner.
"""
# import itertools
# count = 0
# # for in loop
# for i in itertools.cycle('AB'):
#     if count > 7:
#         break
#     else:
#         print(i, end=" ")
#         count += 1
#
# # A B A B A B A B

"""
repeat(val, num):
    This iterator repeatedly prints the passed
    value infinite number of times. if the 
    optional keyword num is mentioned, then
    it repeatedly prints num number of times.
"""
# import itertools
# print(list(itertools.repeat(3, 5)))



# listA = ['a', 'e', 'i', 'o', 'u']
# iter_listA = iter(listA)
# # or
# iter_listA = listA.__iter__()
#
# print(next(iter_listA))
# # or
# print(iter_listA.__next__())




# class Counter:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.start > self.end:
#             raise StopIteration
#         else:
#             num = self.start
#             self.start += 1
#             return num
#
# c = Counter(1, 5)


# def simple_generator_fun():
#     yield 1
#     yield 2
#     yield 3
#
# for value in simple_generator_fun():
#     print(value)
# # 1
# # 2
# # 3
#
# """
# Generator function returns a generator object.
# Generator objects are used either by calling
# the next method on the generator object or using
# the generator object in a 'for' loop.
# """
#
# x = simple_generator_fun()
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# # 1
# # 2
# # 3


# # -- generator --
# def fib(limit):
#     # initializing first two fibonacci numbers
#     a, b = 0, 1
#     # one by one yield next fibonacci number
#     while a < limit:
#         yield a
#         a, b = b, a + b
#
# x = fib(5)
# for i in x:
#     print(i)


# generator = (num ** 2 for num in range(10))
# print(type(generator))
# # <class 'generator'>





# ---------- Functions ----------

# # anonymous functions
# square = lambda x: x*x
# cube = lambda x: x*x*x
# mul = lambda x,y: x*y
# print(square(2))
# print(cube(2))
# print(mul(2, 3))



# # Python program to demonstrate use of
# # class method and static method.
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @classmethod
#     def from_birthyear(cls, name, year):
#         from datetime import date
#         return cls(name, date.today().year - year)
#
#     @staticmethod
#     def is_adult(age):
#         return age > 18
#


# class Test:
#     def __init__(self):
#         self.str = 'Faizan'
#         self.x = 20
#
# def fun():
#     return Test()
#
# t = fun()
# print(t.str, t.x)


# def fun():
#     str = 'Faizan'
#     x = 20
#     return str, x # return tuple
#
# a = fun()
# print(a)
# # ('Faizan', 20)



# # This function returns a list
# def fun():
#     str = "geeksforgeeks"
#     x = 20
#     return [str, x];
#
# list = fun()
# print(list)
# # ['geeksforgeeks', 20]


# def myFuntion(a, b, c, d):
#     return a+b+c+d
#
# from functools import partial
# g = partial(myFuntion, b=1, c=2, d=3)
# print(g(a=4))


# def shout(text):
#     return text
# print(shout('Hello'))
# yell = shout
# print(yell('Faizan'))


# def shout(text):
#     return text.upper()
# def whisper(text):
#     return text.lower()
# def greet(func):
#     greeting = func('Hi, I am created.')
#     print(greeting)
# greet(shout)
# greet(whisper)


# def create_adder(x):
#     def adder(y):
#         return x + y
#     return adder
# add_15 = create_adder(15)
# print(add_15(10))


# def decor(fun):
#     def inner():
#         print("Start...")
#         fun()
#         print("End.")
#     return inner
# @decor
# def hello():
#     print("Hello!")
#
# print(hello())


# def decor(func):
#     func.data = 3
#     func.num = 7
#     return func
#
# @decor
# def add(x, y):
#     return x + y
#
# print(add(2, 3))
# print(add.data, add.num)


# def decor(func):
#
#     def inner(*args, **kwargs):
#         print('inner...')
#         func(*args, **kwargs)
#
#     return inner
#
# @decor
# def factorial(num):
#     import math
#     print(math.factorial(num))
#
# factorial(3)


# def decor(func):
#
#     def wrapper(*args):
#         print('Before Execution.')
#         return_value = func(*args)
#         print('After Execution.')
#         return return_value
#
#     return wrapper
#
# @decor
# def add(a, b):
#     return a + b
#
# print(add(2, 3))


# Syntax for decorators with parameters –
#
# @decorator(params)
# def fun_name():
#     pass
#
# The above code is equivalent to
#
# def func_name():
#     pass
#
# func_name = (decorator(params))(func_name)


# # Python code to illustrate
# # Decorators with parameters in Python
# def decorator_func(x, y):
#     def Inner(func):
#         def wrapper(*args, **kwargs):
#             print("I like Geeksforgeeks")
#             print("Summation of values - {}".format(x + y))
#
#             func(*args, **kwargs)
#
#         return wrapper
#
#     return Inner
#
#
# # Not using decorator
# def my_fun(*args):
#     for ele in args:
#         print(ele)
#
#     # another way of using dacorators
#
#
# decorator_func(12, 15)(my_fun)('Geeks', 'for', 'Geeks')
# # output =
# # I like Geeksforgeeks
# # Summation of values - 27
# # Geeks
# # for
# # Geeks



# # Factorial program with memorization using
# # decorators.
# def memorize_factorial(func):
#     memory = {}
#
#     def inner(num):
#         if num not in memory:
#             memory[num] = func(num)
#         return memory[num]
#
#     return inner
#
# @memorize_factorial
# def facto(num):
#     if num == 1:
#         return num
#     else:
#         return num * facto(num - 1)
#
# print(facto(5))



"""
The python help function is used to display 
the documentation of modules, classes, 
functions and keywords, etc.

help([object])

If the help function is passed without an 
argument, then the interactive 
help utility starts up on the console.
"""

# help(print)

# class Helper:
#     def __init__(self):
#         '''The init function.'''
#
#     def print_help(self):
#         '''The print_help function.'''
#
# help(Helper)


"""
# Python | __import__() function
Syntax: __import__(name, globals, locals, 
                    fromlist, level)

Parameters:
name : Name of the module to be imported
globals and locals : Interpret names
formlist : Objects or submodules to be
            imported (as a list)
level : Specifies whether to use absolute 
or relative imports. Default is
-1(absolute and relative).

"""

# # importing numpy module
# # it is equivalent to "import numpy"
# np = __import__('numpy', globals(), locals(),
#                 [], 0)
# # array from numpy
# a = np.array([1, 2, 3])
# # prints the type
# print(type(a))


# # from numpy import complex as comp,
# # # array as arr
# # np = __import__('numpy', globals(), locals(),
# #                 ['complex', 'array'], 0)
# #
# # comp = np.complex
# # arr = np.array


# # Python3 program for demonstrating
# # coroutine execution
#
# def print_name(prefix):
#     print("Searching prefix:{}".format(prefix))
#     while True:
#         name = (yield)
#         if prefix in name:
#             print(name)
#
# # calling coroutine, nothing will happen
# corou = print_name("Dear")
# # This will start execution of coroutine and
# # Prints first line "Searchig prefix..."
# # and advance execution to the first yield expression
# corou.__next__()
# # sending inputs
# corou.send("Atul")
# corou.send("Dear Atul")
#
# # output =
# # Searching prefix:Dear
# # Dear Atul





# ---------- Object Oriented Concepts --------


# class Pet:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# class Cat(Pet):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#
#
# pet = Pet('pet', 2)
# cat = Cat('cat', 3)
#
# print('Is pet a Pet?', isinstance(pet, Pet))
# print('Is pet a Cat?', isinstance(pet, Cat))
# print('Is cat a Pet?', isinstance(cat, Pet))
# print('Is cat a Cat?', isinstance(cat, Cat))


# class Reverse:
#     def __init__(self, data):
#         self.data = data
#         self.index = len(data)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index == 0:
#             raise StopIteration
#         self.index -= 1
#         return self.data[self.index]
#
# r = Reverse('Faizan')
# for i in r:
#     print(i)


# def reverse(data):
#     for index in range(len(data)-1, -1, -1):
#         yield data[index]
#
# rev = reverse('Owais')
# for i in rev:
#     print(i)


# class A:
#     x = 3
#
# a = A()
# b = A()
# print(a.x)
# print(b.x)
# print(A.x)
# a.x = 5 # generates the instance variable x,
# # it is not the class variable x
# print(a.x)
# print(b.x)
# print(A.x)


"""
Destructors:
    The __del__() method is known as a 
    destructor method in Python. It is 
    called when all the reference to the
    object have been deleted.
    
    def __del__(self):
"""


"""
---- Creating Custom Metaclass
"""



# a = [1, 2]
# try:
#     print((a[3]))
# except Exception as e:
#     print(e.__str__())



# try:
#     a = 5
#     if a < 4:
#         b = a/(a-3)
#
#     print('Value of b =', b)
#
# except(ZeroDivisionError, NameError):
#     print("exception.")



# # A Python program to create a user-defined
# #exception
#
# class MyException(Exception):
#     # Constructor or Initializer
#     def __init__(self, value):
#         self.value = value
#
#     # __str__ is to print the exception error
#     def __str__(self):
#         return repr(self.value)
#
# try:
#     raise MyException(3)
# except MyException as error:
#     print(error.__str__())


# class A:
#     def __init__(self):
#         self._protected = 'protected'
#         self.public = 'public'























































# -*- coding: utf-8 -*-
"""
Data Mining 1- Python intro coding

"""

import os as os

os.getcwd()

##################
# running python #
##################

## this is the code that python runs when we submit in spyder
#runfile('C:/SMU Data science/Data Mining I/code copies/unit 1 code copy.py', wdir='C:/SMU Data science/Data Mining I/code copies')

print 'hello world'


##################
# syntax #########
##################

# variables example

int_val = 8
long_val = 2342342325L
float_val = 2.5436767556
bool_val = False

print 'variable type examples:'

print type(int_val)
print type(long_val)
print type(float_val)
print type(bool_val)

# testing for the type of variable

temp = isinstance(float_val,float)
# testing to see is the variable matches the type
print temp
print isinstance(float_val,int)

# arithmatic and casting

print '\nArithmatic examples'

print 8/3

print float(8)/3

print float(8)/float(3)

print True and False # logicals
print 8==3 # logical equality
print 5<=6 # logical comparison
print 2.0*4.0 # multiplication
print 65%6 # modulus
print 3**4 # 3 to the 4th power

# strings

print '\nString Examples:'

str_val = ' A string is double or single quotes'
str_val_long = '''Three quotes means that a string 
encompasses multiple lines '''
str_val_no_newline = '''This also spans multiple lines \
but goes to no new line'''

print str_val
print str_val_long
print str_val_no_newline

    # strings can be accessed multiple ways

print str_val[0] # first element in string
print str_val[3:5] # 3rd through 5th element in string
print str_val[-1] # the last element in the string
print str_val[-5] # the last 5 elements in the string
print str_val[0:5] + str_val[5:] # print the first 5 elements, then from the 5th element on

    # ERROR: str_val[5] = 'G' String values are immutable after they are set.

   # Common operations for strings
print str_val*2 # multiple is like assing the number of times to repeat (2x in this case)
print 'Python'> 'Java' # compare the strings alphbetically
print 'eric'.capitalize() # will capitalize the phrase
print str_val.lower()
print str_val.upper()

print 'this, is, separated, by, commas'.split(',') # returns the results as a list

###########################################
# Tuples, lists, and dictionaries #########
###########################################

print '\nTuples, lists, and dictionaries'
    # a list is one of the most powerful tools in python
    # lists are mutable versions of tuples and can hold any type of information

a_list = [45, 67, 'not a number']

print a_list

# can add to a list via the append function

a_list.append('A string, appended as a new element in the list')

print a_list

# a list can have other lists in them

tmp_list = ['a list','within another list', 442]
a_list.append(tmp_list)
print a_list

# indexing still works with lists

print a_list[1]
print a_list[-1]
print a_list[-2:]


# tuples are immutable lists and separated by commas
# anything can be stored in a tuple - complex object container

a_tuple = 45, 67, 'not a number'

print a_tuple

# access a tuple with square brackets

print a_tuple[2]

# YOU CANNOT CHANGE A TUPLE SINCE IT IS IMMUTABLE

#a_tuple[2] = 'hey' 


#SETS:  from python sets tutorial: # https://docs.python.org/2/tutorial/datastructures.html#sets


basket = ['apple','orange', 'apple', 'pear', 'orange', 'banana']

fruit = set(basket) # create a set without duplicates.  W

print fruit
print basket # see, it removed the second orange and apple

print 'orange' in fruit # fast membership testing
print 'crabgrass' in fruit

a = set('abracadabra')
b = set('alacazam')

a.add('!') # also add the same punctuation

print a # unique letters in a
print a-b # letters in a but not in b
print a|b # letters in either a or b
print a&b # letters in both a and b
print a ^ b # letters in a or b but not in both

a_immutable = frozenset(a)
#a_immutable.add('e') # the set is immutable, so we cannot add to it, this will give an error


# dictionaries map keys to values

# setup a key as a string and the value as a number

num_legs = {'dog': 4, 'cat': 4, 'human':2}

print num_legs
print num_legs['dog']
print num_legs['human']
print '======================='

# entries can but updated, added, and deleted

# just conatiners for any memory type

num_legs['human']='two'
num_legs['bird'] = 'two and some wings'
num_legs[45] = 'a key that is not a string' # notice that the key does not need to be a string
# the keyjust needs t obe some immutable memory

del num_legs['cat']
print num_legs


###########################################
# ADTs, loops, and conditionals ###########
###########################################

# for the validates variable, good article : https://pypi.python.org/pypi/val/0.6

print "\nfor loop output:"

list_example = [int_val, long_val, float_val, bool_val]
list_example.insert (0,"dataMining") # position at which to insert the value followed by value

# loop ends in ":" and is designated by a tab alignment

for val in list_example:
    print str(val) + ' ' + str(type(val))
    print ' this statement is in the loop'

print 'this statement is outside the loop'


import random
print '=============='
val = 0
for i in range(0,random.randint(1,10) ):
    val +=i
    print val
    if val>20:
        print ' A.leaving the loop on break'
        break
else: # this else belongs to the for loop
    print 'B.exiting the loop without break'
    
# more for loop examples

# you can also get the index using hte enumerate example

for index, val in enumerate(list_example) :
    print str(val), '\t is at index \t',index

# so we can go through all of the values in the list and tell which index they are with the simple loop


print "==============="

# classic example for zipping from the official python tutorial (references monty python)
# zip creates a list of alternating variables from 2 other lists
 # try printing: zip questions, answers, then run: type on that to see that it is a list.
 # %s- converts to a string
 

questions = ['name','quest','favorite color'] 

answers = ['lancelot','the holy grail', 'blue']

for q, a in zip(questions, answers):
    print 'what is your %s? It is %s.' % (q,a)
    
# Looping through dictionaries

print "============="

# get all of the keys

print num_legs.keys()
for k in num_legs.keys():
    print k, '=>', num_legs[k]
 
print "============="
# you can also use the iter_items function : Return an iterator over the dictionary’s (key, value) pairs

for k, v in num_legs.iteritems():
    print k, '=>', v
    
print "============="


# test for presence of a key

for t in ['human','beast','cat','dog', 45]:
    print t,
    if num_legs.has_key(t):
        print '=>', num_legs[t]
    else:
        print 'is not present'
        
# dictionary and list comprehensions.
# comprehensions are like shorthand for loops where each pas throug hte loop saves the result in a list or a dictionary

# for example, imafine we want to take every elemnt in a range ato the 4th power
print "============="
times_four = [x**4 for x in range(10)]

print times_four
# see, the result is saved in a list: type(times_four)

# this save the fourth power of the numbers 0 through 9
# the result of each pass through the loop saves a value
# in other languages this is also known as "lambda functions"

# you can also call functions insides a comrpehension, and take advatnage of the data type.  For example, if each element is a string,
# we can usethe string memeber methods

questions = ['name','quest','favorite color']
quest_upper = [x.upper() for x in questions]
print quest_upper

# can also do comrpehensions with dictionaries
times_four = {x:x**4 for x in range(10)}
# notice that the comprehension is wrapped in curly braces and the key for the value 
# is given inside the code itself, followed by a colon             
        
# all of the enumerate, zipping, and slicing also applies to lists

x_array = [10,20,30]
y_array = [7,5,3]

# this prints the sum of the multiplication of the arrays
print sum(x*y for x,y in zip(x_array, y_array))

#============================================
# array as a stack


print '\nStack Example:'
list_example = []
list_example.append('LIFO')

for i in range(0,5):
    list_example.append(i)

print list_example
print "============="

val = list_example.pop()
print val

print "============"
print list_example
print "==========="


### array as a queue
# queue: is a fast container that pops on either end
print "\nQueue Example:"
from collections import deque # this is an import, we will get back to that later
# essentially this is a set of utility functions shipped with python

q_example = deque()
q_example.appendleft("FIFO")
for i in range(5, 10):
    q_example.appendleft(i)

print q_example
print "============="
val = q_example.pop()
print val
print "============="
print q_example
print "============="

# pop and print each element
while len(q_example) > 0:
    print q_example.pop()
    

# conditional example

print '\nconditional example:'

a, b = True, False

if a: 
    print 'a is true'
elif a or b:
    print 'b is true'
else:
    print 'neither a nor b are true'

# conditional assignment

val = 'b is true' if b else 'b is false'
print val

# more on conditionals "is" versus ==

# I. the traditional == works as expected

a = 5
b = 5
if a == b:
    print 'I. Everybody is a five!'
else: 
    print 'I. Wish we had fives'

# II. the "is" function is for hte object comparison, much like comparing pointers

a = 327676
b = a

if a is b:
    print 'II.These are the same object'
else: 
    print 'II.wish we had the same objects...'
    
# III. while these have the same value, they are not the same memory

a = 327676
b = 327675+1

if a is b: # testing the object not the value
    print 'III.these are the same object'
else:
    print 'III.wish we had the same objects'
    
# Iv. you woud expect this to say we we had fives, ut small intergers like this are cached so 
#       right now they do point to the same memory

a = 5
b = 4+1

if a is b:
    print 'IV. Everybody is a five'
else:
    print 'IV. wish we had some fives...'

# v. but if we change the memory, that cashing gets released

b = b*2.0
b = b/2.0

if a is b:
    print 'V. Everybody is a five'
else:
    print 'V. Wish we had some fives...'
    
# you can also perform nested conditionals, like bounding

if 5<8<6: # not true because 6 < 8
    print 'VI. How di we get here?'
elif 4<18<22:
    print 'VI.Got through the nested conditional'
    
###########################################
# Pythonic ################################
###########################################

# run the import this statement

import this

# which is more pythonic

N = 128

sum_value = 0
for i in range(N):
    sum_value += i
print sum_value

# OR
print sum(range(N))

# OR
print N*(N-1)/2 


###########################################
# Functions and classes ###################
########################################### 

print '\nFunction Example:'

# create and call the function
# the function can be defined almost anywhere in the file, as long as definition comes before use

def make_strings_lowercase(str_input):
    assert isinstance(str_input,str) # test the type of input
    return str_input.lower()

print make_strings_lowercase("UPPER CASE")
print make_strings_lowercase("Data Mining")

    
# more function examples

def show_data(data):
    # print the data
    print data

some_data = [1, 2, 3, 4, 5]
show_data(some_data)

# you can also define default values for the functions

print '================='

def show_data(data, x = None, y = None):
    # print the data
    print data
    if x is not None:
        print x
    if y is not None:
        print y

        
some_data = [1, 2, 3, 4, 5]

show_data(some_data);
show_data(some_data, x = 'a cool X value')
show_data(some_data, y = 'a cool Y value', x = 'a cool X value')

# as well as have multiple return types in the function

print '==============='

def get_square_and_tenth_power(x):
    return x**2, x**10


print get_square_and_tenth_power(2)


# this is a class that inherits from a generic object

class BodyPart(object):
    kind = "this is a long string meant to be so long that the memory for it is not cached by python"
    def __init__(self,name):
        self.name = name # the name attribute is unique to each instance of hte bodypart class

# now define a class that sub classes from the deined bodypart class

class Heart(BodyPart):
    def __init__(self,rate = 60, units = 'minute'):
        self.rate = rate
        self.units = units
        super(Heart, self).__init__("Heart")
    
    def print_rate(self):
        print "name: " + str(self.name) + "has" + str(self.rate) + "beats per " + self.units

my_heart = Heart(1, "second")
my_heart.print_rate()

generic_part = BodyPart('Foot')
print my_heart.kind
print my_heart.kind is generic_part.kind # true these are the same memory location

# take the following for example, these are not the same object

# take the following for example, these are not the same object
a = "This is a long string meant to be so long that the memory for it is not cached by python"
b = "This is a long string meant to be so long that the memory for it is not cached by python"
print a is b # not the same memory location

# error handling and exceptions

print '\nError handling and exceptions:'

import random

i = random.randrange(0,8)
j = random.randrange(-1, 6)

print i, j


# getr a nice little array, then try a bunch of dangerous stuff

some = [3, 10, 0, 8, 18]
try:
    # we try to execute this block
    den = some[j] / i
    print "A:", den
    frac = (i+j) / den
    print "B: ", frac
    if frac <  2:
        k = 3
    else: 
        k = 'mike'
    print 'C: ', k
    print 'D: ', some[k]

# this is the catch block

except ZeroDivisionError:
    print '\nDivision by zero'
except TypeError, detail:
    # The detail provides extra information about the exception.
    print "\nSome type mismatch:", detail
except IndexError, detail:
    print "\nSome value is out of range:", detail
except:
    # Except without an exception name catches any exception.
    print "\nSomething else went wrong."

# An else attached to an except block is run if no exception occurrs.
else:
    print "\nThat's odd, nothing went wrong."
    
# the with command and opening a file

# the regular way of opening a file, lots of error checking
try:
    file = open("some_file.txt")
    data = file.read()
except IOError, detail:
    print "\nCould not read file:", detail
else:
    print "Read successfully, file contents:"
    print data
finally:
    # this always gets called, close the file if its open
    if not file.closed:
        file.close()
        
        
# the "file" class actually has a built in __init__ and __exit__
# so we can really on their class implemntation to close the file propoerly
# and handle any exceptions gracefully

# in that respect, the "with" statement is a protocol that the "file class" adopts

with open("some_file.txt") as file:
    data = file.read()
    print "Read successfully, file contents:"
    print data

# is the file closed? Let's check
print file.closed


# you can also define your own classes that adopt the "with" protocol,
# if you are interested check out the example 
class BodyPart(object):
    def __init__(self,name):
        self.name = name
        print '1. Just initialized body part with name', name
        
    def __enter__(self):
        print '2. Building up from "with" command' 
        return self
        
    def __exit__(self, type, value, traceback):
        if value is not None:
            print '4. An error occurred,', value
        else:
            print '4. Exit was called, no errors'
            
    def print_self(self):
        # 5/0 # uncomment to raise an error
        print '3. Hi, my name is:', self.name

with BodyPart("Lungs") as bp:
    bp.print_self()
    
    















    






    






























































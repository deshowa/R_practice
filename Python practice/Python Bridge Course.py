# -*- coding: utf-8 -*-
"""
Spyder Editor

Python Bridge Course - SMU data science - (probaboly for Data Mining I)
"""
## git hub page: 

###########################################
########### Unit 1 ########################
###########################################


# intro to python part II

# he opens a terminal in specific file in folder - sets wd

notebooks which python # doesnt seem to work for me


#%% 

print "hello world from interpreter"

# crtl + D closes python

#%%
var1 = 32

# can use the terminal to do alot of the coding

#%%

# can run from a text editor as well: he uses sublime text editor

print "Hello World From File"

# he saves the file in a directory

# saves hello_world.py
# sublime does syntaxes of python

# goes back to editor

# ls *.py # lists the python files

# so then just type hello_world.py and it will open the file

#%% jupyter notbook

# opens local hosted web server, so that when you look at interpreted notebook, this is a development environment
jupyter notebook # installed with anaconda - open from your directory

# go to new python XX, shows you the IN [] can type code in box and see what output looks like
# hello world from notebook

# variables stored globally in session
############################################
#%% Python Basics - Part I

############################################
#%% comments variables, and variable types

int_val = 8 # creates variable called int val with value of 8, do not need to declare the variable like other languages - python guesses the type
long_val = 235432345432L
float_val = 2.0
bool_val = True

print 'Variable type examples: '
print type(int_val)
print type(long_val)
print type(float_val)
print type(bool_val)

# can also test for the type of variable with is instance
print isinstance(float_val,float)
print isinstance(float_val,int)

# get True and False returned

#%% arithmetic and casting

# in python 2, integer/integer will return an integer

print '\nArithmetic examples: '
print 8/3
print 8*1.00/3
print float(8)/3
print float(8)/float(3)
# they do the same thing

print True and False # notice python uses explicit values - and, or, is, etc.
print 8 ==3
print 5 <=6

print 2.0*4.0 # multiplication
print 65%6 # remainder - modulus
print 3**4 # raising 3 to the fourth power

#%% string operations
# can use single our double quote

str_val  = 'A string is a double or single quote'
print str_val

str_val_long = '''Three quotes means the the string goes over
multiple lines'''

print "======================"
    
print str_val_long

print "======================"
    
str_val_no_newline = '''This also spans multiple lines \
but has no new line when printing'''
    
print str_val_no_newline

#%% other string operations

# they are just like vectors and arrays in other languages (like in R)

print str_val[0] # print the 0th element

print str_val[3:5] # print elements 3 and 4 but not 5

print str_val[-1] # print the last element of the string # go grab the very last char of the string

print str_val [-5:] # print the last five elements

print str_val[0:5] + str_val[5:] # print the first five elements, then from the fifth element and on, 5 all the way to the end, 5th element back
            # the plus concatenates in this case
#str_val[5] = 'G' # this is an error since strings are immutable once they are set, onec you set the value, you cannot change them. 
# you can overwrite a string, but cannot change


#%% more string operations

print str_val *2 # interpretted as string value twice, if did *3, would do 3 times

print 'Python'>'Java' # compare the strings alphabetically

print 'eric'.capitalize() # the dot operator works like most other languages

print str_val.lower()
print str_val.upper()

# can create a pythong list with the .split command
print 'this, is, separated, by, commas'.split(',') # the result is returned as a list, goes through and separated everything into separated string


#%% quick example of calculator 
# can enter numbers and signs and will interpret the string variables and do a caluclation, like graphing calculator
from __future__ import print_function

from os import sys
##print (sys.version) # pulls future version of print (3.0)




var1 = input() # whatever user inputs, will be saved as string
print (var1)

# this will print whatever the user enters
#%%
# define a function

def convert_user_input(value):
    return value # returns the input value

print ('Calculator Prompt')

user_input = convert_user_input(input(""))
print (user_input, type(user_input)) # prints out the user input and the type


############################################
#%% Python Basics - Part II

############################################ 

#%% Conditionals

print '\n Conditional example: '

a,b = True, False # syntax to set multiple assignments with 1 operator

if a: # : means at the end of the conditional statement; how python defines the scope of the statement
    print 'a is true'
elif a or b:
    print 'b is true' # b has to be true in this case
else: 
    print 'neither a or b are true'

# conditional assignment
val = 'b is true' if b else 'b is false' # very expressive way of variable assignment with else statement
print val
    
#%% conditionals continued   
# nitty gritty of conditionals

a = 5
b = 5

if a == b: # traditional == works as expected
    print 'I.everybody is a five!'
else:
    print 'I.wish we had fives...'
    

# II. the is function for object comparison - > is is a pointer; remember "==" is not whether something is same memory location, just equality

a = 35737
b = a # setting these to the exact same memory location

if a is b:
    print 'II. these are the same object!'
else:
    print 'II. wish we had the same objects...'
    

# III. while these have the same value, they are not hte same memory

a = 327676
b = 327675+1 # while values are equal, the memory location is different, but memory location is not the same

if a is b:
    print 'III. These are the same object'
else:
    print 'III. Wish we had the same objects...'
    
# wrinkle in the story: what about the value below?  Seems like it will print the else statement

a = 5
b = 4+1

if a is b:
    print 'IV. Everybody is a five'
else:
    print 'IV. Wish we had fives...'
    
    # this happens because of the size of the value, an artifact of python memory storage.  Something very small, gets cached
    # so that a and b are pointing to the exact same memory location.  It does this to quickly grab from memory.  When you manipulate
    # the caching takes more memory and they are no longer the same object:

        # for example
# V. changing hte memory, caching is released:
b = b*2.0
b = b/2.0

if a is b:
    print 'V.Everybody is a five'
else:
    print 'V.Wish we had fives...'
    
# you can also next conditionals, like bounding

if 5<8<6:  # not true bc 8 is not less than 6
    print 'VI.How did we get here'
elif 4<18<22:
    print 'VI. Got through nested conditional'
    
# take what we know about conditionals and apply to calculator
#%% Calculator part II 
def isfloat(value):
    try:
        tmp = float(value) # try to do this, if can, return true
        return True
    except ValueError: # otherwise, if you get valueerror, return false
        return False

def convert_user_input(value):
    if isfloat(value): # no float function so need to write our own "try catch block"
        return float(value)
    elif(value == '+' or value =='-' or value == '/' or value =='*' or value =='q'): # expecting user ot enter operator or a number
        return value # leave as is and interpret operation later

print ('calculator_prompt')
user_input = convert_user_input(input(""))
print(user_input, type(user_input))

############################################
#%% Python Basics - Part III

############################################ 

#%% lists adn tuples

# to enhance functionalities in the program need lists and loops

# Lists: indexed by numbers in python, each item in list can point to anything.  Can be different objects that are part of python
    # can have lists in lists with elements that point to other lists
    # can be changed, can insert anything of any data type into the list
    # hold many different data types and workhorse of python
# tuples: denoted with parentesis, immutable.  A list is just a mutable version of a tuple


# tuples:
a_tuple = 45, 67, 'not a number'
print a_tuple # know it is a tuple, encased in "()"

print a_tuple[2] # not a number

# lists

a_list = [45, 67, 'not a number']

# can add values via the append function since it is mutable
a_list.append('a string, appended as a new element in the list')
print a_list

# lsits can contain other lists
tmp_list = ['a_list','within another_list',442]
a_list.append(tmp_list)

print a_list

# all of the indexing we learned from before still works with lists

a_list[-1] # get back the other element 
a_list[-2:] # get the long string plus another list

# very functional variable type 

# can build stacks and queues from lists

###Stack ###

# a stack looks like a column.  Can do a pop operation after insertion to pull value out of the stack LIFO process

###queue ##
# similar, but does FIFO removal


### STACK EXAMPLE ###
print '/nstack example:'
list_example = [] # create empty list
list_example.append('LIFO') # append value into the empty list

for i in range (0,5): # for i in the range 0 to 5; for each value of i, append to the list
    list_example.append(i) # for loop populates the list, for loop is very simple

print list_example
val = list_example.pop()
print val
print list_example
# see that we have taken the last value out of the stack. Simply uses the functions of hte python list


### Queue example ###
# using deque, which is a special kind of list - that has special function called append left

from collections import deque
q_example = deque()
q_example.appendleft('FIFO')
for i in range(5, 10):
    q_example.appendleft(i)

print q_example
val = q_example.pop() # now you pop off the very first elment
print val
print q_example

# so we pop off the FIFO element

#%% Python loops

# need to be able to get things into lists, etc.

import random # basically module that allows us to grab random numbers

print '=========='
val = 0
for i in range(0, random.randint(1, 10)) : # rand int winds up being some value
    val += i
    print val
    if val>20:
        print 'A.leaving the loop on break'
        break # break out of the loop
else: # the else belongs to the for loop based on indentation, allows else as part of for loop, anytime you exit for loop, else gets caught, but if you exit on a break, it wont evaluate
    print 'B.exiting the for loop without a break'
    

# the loop is adding something to val each time it goes through the loop.  once the val gets above 20, we leave the loop

#%% for loop with a list

print '\nfor loop output'
# just recreating the variables from the first part of the tutorial
int_val = 8 
long_val = 235432345432L
float_val = 2.0
bool_val = True

list_example = [int_val, long_val, float_val, bool_val]
list_example.insert(0,'DataMining') # insert datamining at hte oth element

# notice that the loop ends with a colon and is designated by the tab alignent

for val in list_example: # for value in the list
    print str(val) + ' '+str(type(val)) # like a for each statement, lists each element and prints the type
    print 'this statement is in the loop'
    
print 'this statement is outside the loop' # just to be sure that the for loop is complete


#%% Very common to want to see index value in a list when looping

# we can use the enumerate function # enumerate enumerates through the list, but sets an index value for the list
for index, val in enumerate(list_example):
    print str(val), '\t is at index \t', index # can add +1 for row number

# can do the zip operation, zip lists together and go through lists row by row

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot','the holy grail','blue']

for q,a in zip(questions,answers):
    print 'what is your %s? it is %s.' % (q,a) # syntax for creating formatted strings '%s' is another way to insert a string
    
# use the modulus operator '%' to assign, and then give it sa tuple of the values that you want inserted into the string


############################################
#%% Python Basics - Part IV

############################################ 

# building a functional calculator

# use everything we have learned to build a functonal calc: he uses jupyter notebook

# uses reverse polish notation: enter number, second number and then plus, add operator to the end of the calculation string
    # speeds up the calculator
    
    # will do this via stacks

# try to make the code more and more readable 

def isfloat(value):
    try:
        tmp = float(value) # try to do this, if can, return true
        return True
    except ValueError: # otherwise, if you get valueerror, return false
        return False

def convert_user_input(value):
    if isfloat(value): # no float function so need to write our own "try catch block"
        return float(value)
    elif(value == '+' or value =='-' or value == '/' or value =='*' or value =='q'): # expecting user ot enter operator or a number
        return value # leave as is and interpret operation later

print ('calculator_prompt')

user_input =''
eval_queue = []

while user_input != 'q': # arbitrary ending for RPN, will fix later
    user_input = convert_user_input(input(''))
    eval_queue.append(user_input) # append value user enters into list, but each time you loop, potentially something inserted
#%%

 
###########################################
########### Unit 2 ########################
###########################################

# this is the code from unit II of the tutorial class

#%%overview
# discuss basic syntax in python and build out hte object oriented nature of python

#%% Pythonic

# terms for different styles of coding in python
# terms for hte best practices and best way to do something 
# note: constantly changing as language evolves
# simple and readable - type: 'import this' - explanation of the code
# invented to make something readable

# conventions: legacy.python pep -008

# variable names - all lowercase and with underscores ex: this_is_my_variable - makes everything more readable

# us indentation to increase clarity: when you can, do it.  It is king in python - 4 spaces or a tab are an indent

# one space before "=" sign

# space mathematics well: x*x + y*y - order of operations meaning ful

# one line between code sections

# use of dictionaries is pythonic - key value/array pair = dictionaries defined with curly braces


# Dictionary example: 
    # key value/array pair
    # key always on left of colon, value on right of colon
    
    num_legs={'dog': 4, 'cat': 4, 'human': 2} # The way it is accessed is very simple, just like an array where you would use 0 or 1
    # keys point to container; no hard and fast rule as to the datatype of the key in the dictionary
    # can access scripts via the key ( just like in an array would use index value number)
    # key can be anything that is immutable. format doesnt matter for the key in a dictionary
    print num_legs
    print num_legs['dog']
    print num_legs['human']

# if want to add a key to an existing dictionary; simply add a new key

# can overwrite and add
num_legs['human'] = 2
num_legs['bird'] = 'two and some wings' # will add in the bird key
num_legs[45] = 'a key that is not a string' # adds in the 45 key and in this case is not a string
del num_legs['cat'] # dicts are mutable 
print num_legs # now cat is gone and 45 and bird are added


#%% Sets

# start with a list
basket = ['apple','orange','apple','pear','orange','banana']
fruit = set(basket)
# now when look at fruit, the set only has the unique items that are in the basket
print fruit
print 'orange' in fruit # fast membership testing, get true because it is in the set
print 'crabgrass' in fruit # tget false because not in the set

# show the error
#a = set((45,'eric',4.0, [5,6])) # get a type error, cannot have a list in the set.  It is not hashable, because hte list is mutable.
# everything in the set has to be immutable

a = set('abrcadabra')
b = set('alacazam')

a.add('!') # can add in some punctuation to the set

# set operations

print a # unique letters

print a-b # either in a or b

print a|b # either a or b

print a & b # in both a and b

print a^b # a or b, not both


#%% frozen set

# if needed to create a set that was immutable 'FROZEN SET'
# once created, cannot change it anymore, try to add something to it, will get an error

a_immutable = frozenset(a)

a_immutable.add('e') # the set is immutable so you will get an error

# AttributeError: 'frozenset' object has no attribute 'add'

# this is useful because you can always use it as a key inside of a dictionary

##########################################
#%% organizing code will be very important 

# done via functions in python

# look at being a little more explicit in python and the power of a function in Python

def show_data(data):
    print data

some_data = [1, 2, 3, 4, 5]

show_data(some_data)

# can change this function to have arguments x and y - redefine show_data with optional arguments

def show_data(data, x = None, y= None): # x and y have a default value, if they dont pass in value, the data is none data type
    # print the data
    print data
    if x is not None:
        print x
    if y is not None:
        print y

some_data = [1, 2, 3, 4, 5]


show_data(some_data)

show_data(some_data, x = 'a cool X value') # now can say "x equals" or "y equals" in any order in the function

show_data(some_data, y = 'a cool Y value', x = 'a cool X value')

# can get multiple returns

def get_square_and_tenth_power(x):
    return x**2, x**10 # returning tuple that can be any size you want it to be
    
print get_square_and_tenth_power(2) # returns a tuple of any size you specify

# makes the code more readable and more intuitive

#%% calculator example II-2
##### goes to calculator example in ipython notebook.  WE will just switch over to this:
# example: II-2

from __future__ import print_function

import operator as oper # operator is a module with all basic opertions in python, cna now get access via dot notation
# add dictionary of operations and function passing
operations_list = {'+':oper.add, # each of these is actually functions
                   '-':oper.sub,
                   '*':oper.mul,
                   '/':oper.truediv,
                   '^':oper.pow,
                   '%':oper.mod,
                  }
def isoperation(value):
    if value in operations_list.keys(): # in the explicitly defined keys from above in operations list.  Return true if in the list
        return True
    else:
        return False
    
def isfloat(value):
    try:
        tmp = float(value)
        return True
    except ValueError:
        return False
    
def convert_user_input(value):
    if isfloat(value):
        return float(value)
    
    elif(isoperation(value) or value=='q'):
        return value # leave as is and interpret operation later
    
def perform_operation(op,vals): # perform operation block much simpler. op is a string that want to perform
    if isoperation(op):
        func = operations_list[op] # goes into dictionary defined in operations list and grabs value and operation imported
        return func(vals[0],vals[1]) # now can pass vals to function
    
    return op

print("Calculator prompt")
user_input = ''
eval_queue = []
while user_input != 'q': #arbitrary ending for RPN, will fix later
    user_input = convert_user_input(input(""))
    eval_queue.append(user_input)
    
    if isoperation(eval_queue[-1]): # if it is an operation at the end of the evaluation entry, then do actions
            
        result = eval_queue.pop()
        
        v2 = eval_queue.pop()
        v1 = eval_queue.pop()
        
        result = perform_operation(result,(v1,v2))
        eval_queue.append(result)
        
    print(eval_queue)

############################################################    
#%% Python Unit 2: 2.1.1 More Python Basics Part II: Classes
############################################################

#%% Object oriented programming in python

# define 2 different classes
class BodyPart(object):# show the process for class creation
    def __init__(self,name): # self always the first argument for a method that is part of a class, init expects us to add properties
        self.name = name # the name attribute is unique to each instance of the class # name is a property, 


# the object inherits from python object, anything part of object will be part of bodypart
# every class has __init__ - any class given by __ and end in __ # init hidden fro mthe user, called for us

# create the heart class that inherits from bodypart with same initialization function, but adding another init function
# overwrite init function that is already there

class Heart(BodyPart):
    def __init__(self,rate = 60, units = 'minute'):
        self.rate = rate
        self.units = units # units default to minutes
        super(Heart,self).__init__('heart') # call initialization of super class, superclass of heart = bodypart, calls self inside superclass and initialize to heart
        # this allows you to have acces to methods later in class
    
    def print_rate(self):
        print ('name: ' + str(self.name) + ' has ' + str(self.rate) + ' beats per ' + self.units)

my_heart = Heart(1,'second')
my_heart.print_rate()

# shows how inheritance works in python


#%% class that inheits from generic object

class BodyPart(object): # first thin in class is define the variable set to really long string
    kind = 'this is al ong string meant to be so long that the memory for it is not cached in python'
    
# no matter how many instances of a variable we crate, the kind variable is the same across all variables created
    
    # this is a class variable shared across all instances
    def __init__(self,name):
        self.name = name # the name attribute is unique to each instance of the class

my_heart = Heart(1,'second')
generic_part = BodyPart('foot')
print my_heart.kind # test whether the kind is pointing to the exact same kind string
print my_heart.kind is generic_part.kind # true these are the same memory location
# rare to use, but important to understand.
# used large string so that not cached by python.  Now, when you print a is b, it is not same memory location

#%% Loops and Dictionaries

# looping through dictionaries
print '============'
# get all the keys 

print num_legs.keys()
for k in num_legs.keys(): # num_les is dictionary, and grab keys and set equal to K, will print out values and keys
    print k, '=>',num_legs[k]

print '=========='
# can use the iter items function

for k, v in num_legs.items(): # in python 2, need '.items in 3, dont.  THe items attribute is each record in the dict
    print k, '=>', v
# simpler version of the code prior

print '========='
# test for presence of the key

for t in ['human','beast','cat','dog',45]: # for t in list that we provide, print ,and if t is in, then print else not present
    print t,
    if t in num_legs:
        print '=>', num_legs[t]
    else:
        print 'is not present'
        
# typically, very simple operations with for loops, can even do it in one line of code and return a list

#%% comprehensions

# very common syntax
# give it an operation to do on every element of a list or dictionary

times_four = [x**4 for x in range(10)] # x from 0 to 9 evaluate what x is to the 4th, brackets tell you to create a list of those outputs from for loop
# will ooutput 0 to 9 to the 4th power
print times_four

# you can also call functions inside a comprehension

questions =[ 'name','quest','favorite color']
quest_upper = [x.upper() for x in questions] # for each element in list, returns new list (comprehensiton) where everything upper
print quest_upper

# comprehensions with dictionaries

times_four = {x:x**4 for x in range(10)} # inside curly braces allows you to give key and value that you want it to store in dictionary
# allows very easy creation of something in lists, but may be more readable to do it this way
print times_four
              
              
# Finally, all of hte enumerat, supping, and slicing that was performed up to now, applies to list comprehensions
x_array = [10, 20, 30]
y_array = [7, 5, 3]

# this prints the sum of the multiplication of the arrays
print sum(x*y for x, y in zip(x_array, y_array)) # this defines the dt product of the 2 vectors

#%% calculatore example II-4
######### going back to calculator: example II-4
# now make into class structure, first pass
class Calculator: # has now defined class called calculator
    def __init__(self):
        
        import operator as oper # only doing this piece in init function, so wouldnt be overriding oper for global application
        # add dictionary of operations and function passing
        self.operations_list = {'+':oper.add, # operations list is a property of the class now
                           '-':oper.sub,
                           '*':oper.mul,
                           '/':oper.truediv,
                           '^':oper.pow,
                           '%':oper.mod,
                          }
        
    def isoperation(self, value): # pass in self, because always first and pass the value to check
        if value in self.operations_list.keys(): # check for the operations defined
            return True
        else:
            return False

    def isfloat(self, value): # checking the value of float
        try:
            tmp = float(value)
            return True
        except ValueError:
            return False

    def convert_user_input(self, value): # testing within the convert input operation
        if self.isfloat(value):
            return float(value)

        elif(self.isoperation(value) or value=='q'):
            return value # leave as is and interpret operation later
        
        # else this will return NoneType

    def perform_operation(self, op,vals):
        if self.isoperation(op):
            return self.operations_list[op](vals[0],vals[1])

        return op


print("Calculator prompt") # way you call changes slightly
user_input = ''
eval_queue = []
calc = Calculator() # now get instance of calculator, which calls init function and sets up operations list
while user_input != 'q': #arbitrary ending for RPN, will fix later
    user_input = calc.convert_user_input(input("")) # now can use do notation to call poertaions of the class
    eval_queue.append(user_input)
    
    if calc.isoperation(eval_queue[-1]):
            
        result = eval_queue.pop()
        
        v2 = eval_queue.pop() 
        v1 = eval_queue.pop()
        
        result = calc.perform_operation(result,(v1,v2)) # dont need to pass in self, it is automatically passed in
        eval_queue.append(result)
        
    print(eval_queue)

# still really problem here, functionality not separated out.  want the while to only deal with user input.
# want calculator (class) to do everything independently
#%% more object oriented approach (still in example II-4)

# now lets make this more object oriented and really make the interface and model separate entities
# Class stucture, second pass
class Calculator: # redefined calculator class
    def __init__(self):
        
        import operator as oper
        # add dictionary of operations and function passing
        self.operations_list = {'+':oper.add,
                                '-':oper.sub,
                                '*':oper.mul,
                                '/':oper.truediv,
                                '^':oper.pow,
                                '%':oper.mod,
                               }
        self.eval_queue = [] # now have self.evaluation q
       
    #==Queue Operations========
    def clear_queue(self):
        self.eval_queue = []
    
    def print_queue(self):
        print(self.eval_queue)
        
    def addto_queue(self,value): # when add to queue this is when you perform operations on the queue
        self.eval_queue.append( self.convert_user_input(value) ) # when someone performs, we append to q
    
        # evaluate operation if it was entered
        if self.isoperation(self.eval_queue[-1]): # if it is an operation, pop off values and add back

            result = self.eval_queue.pop()
            v2 = self.eval_queue.pop()
            v1 = self.eval_queue.pop()

            result = calc.perform_operation(result,(v1,v2))
            self.eval_queue.append(result)
            
    def print_operations(self): # adding one more function - convenience method that prints off operations performed
        # print supported operations
        print('Operations List:', end=' ')
        [print(x, end=', ') for x in self.operations_list.keys()] # print x for x in the operations list key and space at the end
        print('')      # this chunk prints all operations that cal supports
        
    #==check type Operations========
    def isoperation(self, value):
        if value in self.operations_list.keys():
            return True
        else:
            return False

    def isfloat(self, value):
        try:
            tmp = float(value)
            return True
        except ValueError:
            return False

    #===evalaute operations============
    def convert_user_input(self, value):
        if self.isfloat(value):
            return float(value)

        elif self.isoperation(value) :
            return value # leave as is and interpret operation later
        
        # else this will return NoneType

    def perform_operation(self, op,vals):
        if self.isoperation(op):
            return self.operations_list[op](vals[0],vals[1])
        return op

print("Calculator")
calc = Calculator()
calc.print_operations()
while True: #arbitrary ending for RPN, will fix later
    user_input = input("") # get user input
    if user_input == 'q':  # otherwise add to q ueue and print
        break
        
    # otherwise use calculator model to get results
    calc.addto_queue(user_input)
    calc.print_queue()
# big thing we havent done is any error checking on the file
# have made this nearly 100% object oriented.
# functionality is hidden from user, but need to create ways to handle the errors that might happen when user enters incorrect information

#%%
############################################################    
#%% Python Unit 2: 2.1.2 More Python Basics Part III: Exceptions
############################################################
#%% Exceptions

# can use exceptions to raise and catch code exceptions

# create and call a functions
# the function can be defined almost anywhere in the file as long as it is defined before it is used

def make_strings_lowercase(str_input):
    assert isinstance(str_input,str) # test the input type 
    return str_input.lower()
# can define types of variables passed into function
# expecting a string input - so can assert an error is evalutaiont is false
# otherwise , change to lowercase

print make_strings_lowercase('UPPER CASE')
print make_strings_lowercase('DataMining')


#%% exception handling

# code below, lots that can go wrong

import random as rd

i = rd.randrange(0,8)
j = rd.randrange(-1,6)
print i,j

# try a bunch of dangerous things
some = [3, 10, 0, 8, 18]

try:
    den = some[j]/i
    print 'A: ", den
    frac = (i +j) /den
    print 'B: ",frac   
    if frac <2:
        k = 3
    else:
        k = 'mike'
    print 'C: ', some[k] # cant do this with a list only dictionary

# every excpetion that gets raised has a name
except ZeroDivisionError:
    print '\n Division by zero'
except TypeError, detail:
    print'\nSome type mismatch', detail
except IndexError, detail:
    print '\nSome value is out of range:',detail
except:
    print '\nSomething else went wrong'
else:
    print 'nThat''s odd nothing went wrong'       

#%% Culculator ipython example II-6
#Calculator example Ipython notebook                
                            

class CalculatorError(ValueError): # inherit from value error
    '''raise this when the user causes a mistake from the calculator'''

class Calculator:
    def __init__(self):
        
        import operator as oper
        # add dictionary of operations and function passing
        self.operations_list = {'+':oper.add,
                                '-':oper.sub,
                                '*':oper.mul,
                                '/':oper.truediv,
                                '^':oper.pow,
                                '%':oper.mod,
                               }
        self.eval_queue = []
       
    #==Queue Operations========
    def clear_queue(self):
        self.eval_queue = []
    
    def print_queue(self):
        print(self.eval_queue)
        
    def addto_queue(self,value):
        self.eval_queue.append( self.convert_user_input(value) )
    
        
        # evaluate operation if it was entered
        if self.isoperation(self.eval_queue[-1]):

            result = self.eval_queue.pop()
            
            if len(self.eval_queue)<2: # if not 2 elelemtns that can grab, raise calculator error
                # not enough elements to perform an operation
                raise CalculatorError('Not enough values to perform operation') # give user a very real error with description
                
            v2 = self.eval_queue.pop()
            v1 = self.eval_queue.pop()

            result = calc.perform_operation(result,(v1,v2))
            self.eval_queue.append(result)
            
    def print_operations(self):
        # print supported operations
        print('Operations List:', end=' ')
        [print(x, end=', ') for x in self.operations_list.keys()]
        print('')
        
    #==check type Operations======== ######
    def isoperation(self, value):
        if value in self.operations_list.keys():
            return True
        else:
            return False

    def isfloat(self, value):
        try:
            tmp = float(value)
            return True
        except ValueError:
            return False

    #===evalaute operations============
    def convert_user_input(self, value):
        if self.isfloat(value):
            return float(value)

        elif self.isoperation(value) :
            return value # leave as is and interpret operation later
        
        # else this will return NoneType

    def perform_operation(self, op,vals):
        if self.isoperation(op):
            return self.operations_list[op](vals[0],vals[1])
        return op

print("Calculator")
calc = Calculator()
calc.print_operations()
while True: #arbitrary ending for RPN, will fix later
    user_input = input("")
    if user_input == 'q':
        break
        
    try: # put in the try catch block.  Adding an exception that we do not want to debug, know it is a user error and that didnt have enough information
        # otherwise use calculator model to get results
        calc.addto_queue(user_input)
    except CalculatorError as Err:
        print("Error: ", Err)
    calc.print_queue() # wont raise exception here, we will raise, but keep going

#%% Calculator II-6 continued with user exception errors added into the code

# add in some exception handling
# Class stucture, fourth pass
class CalculatorError(ValueError):
    '''raise this when the user causes a mistake from the calculator'''

class Calculator:
    def __init__(self):
        
        import operator as oper
        # add dictionary of operations and function passing
        self.operations_list = {'+':oper.add,
                                '-':oper.sub,
                                '*':oper.mul,
                                '/':oper.truediv,
                                '^':oper.pow,
                                '%':oper.mod,
                               }
        self.eval_queue = []
       
    #==Queue Operations========
    def clear_queue(self):
        self.eval_queue = []
    
    def print_queue(self):
        print("Current Stack:", self.eval_queue)
        
    def addto_queue(self,value):
        tmp = self.convert_user_input(value)
        self.eval_queue.append( tmp )
    
        
        # evaluate operation if it was entered
        if self.isoperation(self.eval_queue[-1]):

            result = self.eval_queue.pop()
            
            if len(self.eval_queue)<2:
                # not enough elements to perform an operation
                raise CalculatorError('Not enough values to perform operation')
                
            v2 = self.eval_queue.pop()
            v1 = self.eval_queue.pop()

            result = calc.perform_operation(result,(v1,v2))
            self.eval_queue.append(result)
            
    def print_operations(self):
        # print supported operations
        print('Operations List:', end=' ')
        [print(x, end=', ') for x in self.operations_list.keys()]
        print('')
        
    #==check type Operations========
    def isoperation(self, value):
        if value in self.operations_list.keys():
            return True
        else:
            return False

    def isfloat(self, value):
        try:
            tmp = float(value)
            return True
        except ValueError:
            return False

    
    def convert_user_input(self, value):
        if self.isfloat(value):
            return float(value)
        elif self.isoperation(value) :
            return value # leave as is and interpret operation later
        else:
            raise CalculatorError('Invalid entry. Entry must be number or supported operator.')
        

    #===evalaute operations============
    def perform_operation(self, op,vals):
        if self.isoperation(op):
            return self.operations_list[op](vals[0],vals[1])
        return op

print("Calculator")
calc = Calculator()
calc.print_operations()
while True: #arbitrary ending for RPN, will fix later
    user_input = input("")
    if user_input == 'q':
        break

    try: 
        # otherwise use calculator model to get results
        calc.addto_queue(user_input)
    except CalculatorError as Err:
        print("Error: ", Err)
    calc.print_queue()
#%%
############################################################    
#%% Python Unit 2: 2.1.3 More Python Basics Part III: Opening a file
############################################################
#%% Opening a file

# the regular way of opening a file
# very common usage of try and except blocks

try:
    file = open('some_file.txt') # handle to the file
    data = file.read() # read the dile in
except IOError, detail: # if file doesnt not exist and print out details
    print '\nCould not read file', detail
else:
    print 'read successfully, file contents: ' # successful
    print data # print the data
finally: # finaly block will always get read no matter what, in thise case always clsoe hte file
    # This always gets called, close the file if it is open
    if not file.closed:
        file.close() # always want to clsoe file if it is open
        
# turns out that this is such a common appraoch that we can use object oriented programming

#%% With statement
# put everything in an open and catch block

with open('some_file.txt') as file:
    data = file.read()
    print 'read successfully, file contents: '
    print data

# with statement guarantees that if there is file error that it gives error and closes file
# otherwise, read successfully, and close hte file

# nothing magical, can use in classes
# must define enter and exit protocol

class BodyPart(object):
    def __init__(self,name):
        self.name = name
        print '1. Just initialized body part with name', name
    def __enter__(self): # basically, calling when entering the with statement, returns self
        print '2. Building up from ''with''command'
        return self
    def __exit__(self, type, value, traceback): # has inputs self, type, traceback, gets called when error occurs, can put something you want to happen
        if value is not None:
            print '4. An error occured,',value # will reraise the error
        else:
            print '4. Exit was called, no errors'

def print_self(self): 
    print '3. Hi my name is: ', self.name
    
with BodyPart('lungs') as bp:
    bp.print_self()
    
# will add custom functions from user file, and assume single arguments in evaluation stack.

#%%
############################################################    
#%% Python Unit 2: 2.1.4 More Python Basics Part V: Start Example
############################################################


# continuing calculator example
######## Start Example II-8

# add in custom user functions from JSON file
# Class structure, fifth pass
class CalculatorError(ValueError):
    '''raise this when the user causes a mistake from the calculator''' # keeping the same calc error, but now allowing custom commands read from file

class Operator: # define simple operator class, give initialization and # arguments
    def __init__(self, func, num_args=2): # shows how many operations to pop from the stack
        self.func = func
        self.num_args = num_args
    # going to come up with array that uses these items
    
class CustomCalculator(Calculator):
    def __init__(self):
        # THIS OVERWRITES THE INIT FUNCTION OF INHERITED CLASS
        import operator as oper
        # add dictionary of operations and function passing, include basic operations here
        self.operations_list = {'+':Operator(oper.add), # so + is operator, oper is add and will have 2 arguments unles specified
                                '-':Operator(oper.sub),
                                '*':Operator(oper.mul),
                                '/':Operator(oper.truediv),
                                '^':Operator(oper.pow),
                                '%':Operator(oper.mod),
                                'abs':Operator(oper.abs,num_args=1),
                               }
        self.eval_queue = []
        
    def add_custom_operations(self,filename):
        import json
        with open(filename) as file:
            data = json.loads(file.read()) # Grab file data

        import math
        for key,module in data.items():
            if hasattr(math, module):
                self.operations_list[key] = Operator(getattr(math, module), num_args = 1)
                
    def addto_queue(self,value):
        tmp = self.convert_user_input(value)
        self.eval_queue.append( tmp )
    
        
        # evaluate operation if it was entered
        if self.isoperation(self.eval_queue[-1]):

            result = self.eval_queue.pop() # check for operation and save result
            num_args = self.operations_list[result].num_args # grab operatior class instance, get class and # of arguments
            
            if len(self.eval_queue)<num_args: # see if have the number of arguments or throw cal error
                # not enough elements to perform an operation
                raise CalculatorError('Not enough values to perform operation')
                
            args = [] # grab num of arguments needed
            for i in range(num_args): # for # arguments append and pop to list
                args.append(self.eval_queue.pop())

            result = self.perform_operation(result,args) # operation and arguments rather than tuple of arguments
            self.eval_queue.append(result)
            
    def perform_operation(self, op, vals):
        if self.isoperation(op): # if a valid operation, go into operator class
            return self.operations_list[op].func(*vals) # pass list as arguments, since dont know how many args will have, * defeferences and each becomes part of the function, pass each argument into function
        return op

print("Calculator")
calc = CustomCalculator()
calc.add_custom_operations('operators.json') # new function
calc.print_operations() # inherited function

while True: 
    user_input = input("")
    if user_input == 'q':
        break
        
    try: 
        # otherwise use calculator model to get results
        calc.addto_queue(user_input) # overwritten function
    except CalculatorError as Err:
        print("Error: ", Err) 
        
    calc.print_queue()

#%% Allow calculator to read from a json file that is saved in operators.json

# adding decorators
# Class structure, sixth pass
class CalculatorError(ValueError):
    '''raise this when the user causes a mistake from the calculator'''

class Operator:
    def __init__(self, func, num_args=2):
        self.func = func
        self.num_args = num_args
    
    
class CustomCalculator(Calculator):
    def __init__(self):
        # THIS OVERWRITES THE INIT FUNCTION OF INHERITED CLASS
        import operator as oper
        # add dictionary of operations and function passing, include basic operations here
        self.operations_list = {'+':Operator(oper.add),
                                '-':Operator(oper.sub),
                                '*':Operator(oper.mul),
                                '/':Operator(oper.truediv),
                                '^':Operator(oper.pow),
                                '%':Operator(oper.mod),
                                'abs':Operator(oper.abs,num_args=1),
                               }
        self.eval_queue = []
        
    def add_custom_operations(self,filename):
        import json
        with open(filename) as file:
            data = json.loads(file.read()) # Grab file data

        import math
        for key,module in data.items():
            if hasattr(math, module):
                self.operations_list[key] = Operator(getattr(math, module), num_args = 1)
                
    def addto_queue(self,value):
        tmp = self.convert_user_input(value)
        self.eval_queue.append( tmp )
    
        
        # evaluate operation if it was entered
        if self.isoperation(self.eval_queue[-1]):

            result = self.eval_queue.pop()
            num_args = self.operations_list[result].num_args
            
            if len(self.eval_queue)<num_args:
                # not enough elements to perform an operation
                raise CalculatorError('Not enough values to perform operation')
                
            args = []
            for i in range(num_args):
                args.append(self.eval_queue.pop())

            result = self.perform_operation(result,args)
            self.eval_queue.append(result)
            
    def perform_operation(self, op, vals):
        if self.isoperation(op):
            return self.operations_list[op].func(*vals) # pass list as arguments
        return op
    
    @staticmethod # so can replace the asfloat with this, python decorator, tells python, that function immediately follows decorator
    def isfloat(value): # want to change the function of wht python does, eliminates requirement to pass in self
        try:
            tmp = float(value)
            return True
        except ValueError:
            return False

print("Calculator")
calc = CustomCalculator()
calc.add_custom_operations('operators.json') # new function
calc.print_operations() # inherited function

while True: 
    user_input = input("")
    if user_input == 'q':
        break
        
    try: 
        # otherwise use calculator model to get results
        calc.addto_queue(user_input) # overwritten function
    except CalculatorError as Err:
        print("Error: ", Err) 
        
    calc.print_queue()
##################################################    
#%%
############################################################    
#%% Python Unit 3###########################
############################################################


#################################
#%% 3.1 working with different scripting environments with anaconda
###################################

# can switch between environments on the computer.  Like a fresh install of python on the computer
# retains links to master packages when they are installed in the root.  Would still be using the environment in the root.

# why install environments?
# dont want ot mess up system architecture - mac and linux have python 2 installed already
# install older versions to check for older compatability


# the conda enviroment:
    # need to name enviroment
    # tell conda which packages to install
    conda create --name MyFirstEnv numpy
    # he uses MLEV - machine learning environment - numpy is the install of the package to put into env
    conda create --name MyPython2 env python = 2 numpy scipy
    # install a python 2 enviromnet and install numpy and scipy with those compatable packages
    
    source activate MyPython2Env
    # must switch environments in order to not log in as root
    
    # once you are in, you can also install additional packages
    conda install jupyter
    # weill install jupyter within the environment
    source deactivate
    # removes you from env and brings to root
    
    # can use the conda package to find the right package for the right system - search the conda cloud to see if someone has installed for your system
    
    anaconda search -t conda rpy2
    # tell it to use the conda version of Rpy2
    # tells you which people have installed Rpy2 system and which packages it supports and is built for
    # fidn hte version for your system r/rpy2 example
        # know you want ot install this packages
        conda install - c r rpy2
        
        # found package on conda cloud (-c) that user 'r' has uploaded or created

#%% example of using the system


# type python

source deactivate 
#brings you to the root directory
source activate gl-env # his other environment where python 2 installed
python
# now would show python 2.7
source deavtivate

# jupyter notebook works very well with the different environments

import sys
print (sys.version)

import numpy as np

np.__version__

#%% say wanted to run python 2.7

# he tries running print and doesnt have parenthesis
# need to switch environment
# kernel-> go to gl environment that contains new session of python
# now will work

#%% try to use rpy2 in python 3

# conda install -c r rpy2 # installs the package in the command line

import sys
print(sys_.version)

%load_ext rpy2.ipython # jupyter magic
# percent sign installs jupyter magics that are sub modules that work within the jupyter notebook
# wants to call because you can use R code with % R and call R code right off the bat

# issue with the RHome directory, but doesnt know where to find R
# in the terminal let's see if we can run R
R
# type R in terminal doesnt know where R is unless you are launched from Rpy2, which is where R is installed
# must open Jupyyter notebook

# %% example II-2 in video 3.1

# have access in that kernal

import sys
print (sys.version)

% load_ext rpy2.ipython
%R -o var var =5 # expects R code -o is the output called variable, run aR code after the var as output into python save value of var in python


# must run jupyter notebook from with a specific source

%%R # everything in this block of code will be R code

var = var 5

print (var) # not updated in python

# if you want to synchronize, need to give the %% R magics how to use input and output

%%R -i var -o var

# whenever you are done with code, save the output in python where you have taken the input var

var = var*5

var

print(var) # in python environment , defaults to numpy array
print(type(var))

# use as glue to speak between the 2 environments

# %% R syntax is next- got to R file
#%%
###########################################
########### Unit 4 ########################
###########################################
#%%
############################################################    
#%% Python Unit 4: 4.0 Introduction
############################################################
#%%

# numerical optimization tools in python

############################################################    
#%% Python Unit 4: 4.1 vectorized coding in Pythin, Part I
############################################################

# talking about numpy
    # numpy allows us to use vectorized coding in python, means we will use the linear algebra equivalent
    # created by travis oliphant, also authored scipy, numpy, numba (just in time compiler
    # wrapper written in python with c++ codebase - made for linear algebra and numerical computing tools
    # python wrapper allows for many numerical operations inutitively while calling c++ codes
    # opensource and allows people to pick wrappers that makde things ver yquick
    # most scientific packages use numpy in the background to make thigns efficient
        # used in scipy, scikit learn, pandas, scikit image, opencv, matplotlib, and many more
    # we are often interested in table data
        # each row means something to us and each column means something to us - turned into 2-d matrix with features reppd by column
        
############################################################    
#%% Python Unit 4: 4.1.1 vectorised coding in Python, Part II- review of linear algebra
############################################################

# # quick review of operations and at same time, using them in numpy equivalents

#%% ipython notbook 04 optimize
# Example III -1 review of linear algebra

import numpy as np
a = np.array([[0,1,2]
             ,[3,4,5]]) # our matrix is the same as feeding python 2 lists, list of lists, so gives 2d matrix
       
print (a)
print ("-------")

print (a.T) # gives the transpose # essentially turns the first row into the first column and the second row into the second column

# transpose matrix is produced

# typically when we do that, we write as a^T

print ( a.flatten()) # many times want to take all values and represent as flattened vector
# assumed we want to take the first row and assumt those are the columns, takes second row and appends to the right
# just gets concatentated

# if did o nthe transpose, 

print ((a.T).flatten()) # so just gives the order that was done in the transpose

#%%
# numpy has many built in concatentation operations

a = np.array([1,2], float)
b = np.array([3, 4, 5,], float)
c = np.array([7, 8, 9], float)
np.concatenate((a, b, c)) # each has the same number of rows, so put them on a tuple - parenthesis, makes single input value


# %% now, make it a little more complex

a = np.array([[1,2],[3,4]], float) # 2x2 matrix
b = np.array([[5,6],[7,8]], float) # 2x2 matrix
np.concatenate((a, b)) # simply concatenates a and b on top of eachother, assumes on very first dimension to stack

# could have stacked horizontally

print(np.concatenate((a,b), axis = 0)) # now you saw axis = 0, meaning that you want to stack vertically - row concat
print(np.concatenate((a,b),axis = 1)) # axis 1 means stack horizonatlly - column concat

#%% get a little more specific with internal representation of matrices

a = np.array([1, 2, 3],float) # just has a shape of 3; now rows and cols

print (a)
print('---')
print(a[:,np.newaxis]) # manipulating a and returning a whole new object on a new axis
print('---')
print(a[:,np.newaxis].shape) # make this to be part of the first column and add a new axis, which is the number of rows
# says you want the existing axis to be 3 and one columns

#%% change up b

print( b[np.newaxis,:]) # want to add a 3rd dimension to the matrix, make sure the 3rd is the very first dimensio
# could stack another 1*2 matrix on top of this one as well
# typically only concerned with 2 dimensions
# so usually just want a row vector to be turned into cloumn vector

print('---')

print(b[np.newaxis,:].shape)

#%% operations on new vectors

a = np.array([1, 2, 3], float)
b = np.array([5, 2, 6,], float)

# numpy interprests different operations differently


print('+', a + b)
print('-',a-b)
print('*', a*b) # not simple element by element, but numpy supports - with the asterisk, 1*5, 2*5, 3*6
print('/',a/b) # same for division
print('%',a%b) # modulus
print('**',b**a) # taken to the power, taking B to the a power
print('@ ', a @ b)  # to do matrix operations, special function or the @, this has been overloaded in py 3, @ for dot product
# a returns the do product, element by element and add them up = 27

# matrix multiplciation between vectors can look alot different

# get n rows by m columns

#%% broadcasting operations in numpy

# do operations like addition, but have different sized matrices

a = np.array([[1, 2],[3,4],[5,6]], float)
b = np.array([-1,3], float)

print (a)
print(b)

print (a+b)

np.unique([1, 2, 3, 3, 5,3, 6,76, 264, 8]) # pulls uniqure values for each calue in the array

# braoadcasting would be repeat the 'b' element for each of hte rows, what is 1, will try to broadcast ingot a

#%% indexing 
# since writtein in c++, can do some things easier than in c++

a = np.array([[1, 4.5, 1500],
              [5, 3.5, 800],
              [2, 0.5, 1300]]) # 3x3 matrix

              # indexing int othe matrix is something called slicing
              # because we are slicing pieces of this matrix one at a time
              

print (a[:, 0]) # A at all of the rows and the oth column, dont care about the row, just care about the column
print (a[0, :]) # now printing whichever column but oth row

    # gives rise to some interesting operations that can be done here
    
# want the oth column >=2

# where is that vector >= 2

print ( a[:,0]>=2)
# first row false, second row true, third row true

# internally, numpy prints out as logical vector: Fales, true, True

# can use this to index into the matrix A

print(a[ a[:,0]>=2])
# give me the rows of A where that is true, give me only those rows
# very powerful for slicing different values in the matrix
# able to grab each rows for a certain column value and create and entirely new motrix

#%% typical operations for matrices

# using A again

print(np.trace(a)) # trace operation says ok, I want to grab the diagonal of the matrix and sum the values up

# for A, it would be 1, 3.5, 1,300

print ('---')

print(np.diagonal(a)) # creates a totally new vector

print('---')

v = np.diagonal(a) # save the diagonal vector of v

print(np.sum(v)) #should get same value as trace
print('---')

print(np.diag(v)) # this creates a square matrix with diagonal 1, 3.5, 1300, and every other element equals 0
# very important for optimization techniques

#%% numpy linear algebra built in

# determinant of matrix

# for 2x2 matrix  a :
   # a b
    #c d # the determinant of this matrix would be = a*d-b*c
# have many different properties for geometric areas and values
# shows what scale of transformation of hte matrix is, 

# determinants are used to calculate inverses

from numpy import linalg as lin

print (lin.det(a))

print ('---')

print (lin.inv(a)) # inverse doesnt exist if det = 0

# inverse of a mtrix

# 2 matrices: A and B 
# A*B = Y

# forms the identity matrix
#A^-1*A*B = A^-1*Y
# B = A^-1*Y

#%% eigen values

# very important for things like principle components, gradients

# eigenvalues tell you what the (values and vectors) for a 3*x matrix, have 3 eigenvalues associated with 3 eigenvectors

vals, vects = lin.eig(a)

print(vals)
print('---')
print(vects)

# will talk more and more about these in program, geometric interpretation
# eigenvectors, transform the space via matrix operation, but will always be in the same direction regardless of the space

############################################################    
#%% Python Unit 4: 4.2 optimization with Scipy/Numpy Part I
############################################################
# bonus adding visualization in matplotlib

# combining numpy with scipy to perform curve fitting
# assuming that darta follows sigmoid curve with x data that is input and y variable in table that we want to predict
# sigmoid = f(x) = 1/(1+e^-Bx) # where x is the axis
    # just takes the function and fits to alot of different areas
    # will join up with matrix multiplication to define a curve

# Goes to course example III-1

import numpy as np
x = np.array ([[-1,-2],
               [3,1],
               [4,5]
               ,]) # make column
# showing an x array (3X2) 
# pretend that this matrix is observational measurments that map to a Y vector with certain values [0,1, 0.5] 
# the first row of x I want to use to predict the first row of Y and second to predict second, etc.
# with sigmoid, we define a sigmoid,w, of which we do not know the values, but know can take W and multiply by X


w = np.array([[0.2, 0.8]])
               # just values that we are guessing
               # multipling 

#x * w^T = -1.8, 1,4, 4,8

# take functions and map between o and 1           
print (x)
print('---')
print(w)
print('---')
np.dot(x, w.T)

# if y values are between 0 and 1 then pass to f(x) then y_hat = f(x*w)^t

def yhat (x, w):
    return 1/(1+np.exp(-np.dot(x,w.T))) # this is equal  to the Y hat or the prediction of thwat it is
    
yhat(x,w) # 3 neumeric values that might use to predict Y values from

# want w that when multiple by x, what is best w such that hte difference between y and yhat is extremely small
# for each row of y and yhat both column vectors, what is value of difference between first element of a and first vlue of yhat
#( y-y_hat) is what we are asking
# we can sqwuare this and sum the whole thing up sum(y-y_hat)^2 - sum squared error of difference between what I want and what i have predicted, 
# this is known as objective function : what hte minimum

# obj(w) = sum(y-y_hat)^2

# really want ot sum over each row of x and each row of y

# need notation to say entire row: x = (x ^(1), x ^(2)) <- read as x of 1 or x of 2

# this means y is a column vectorm which is single value that we want to predict, so simply draw y and yhat as vectors that coincid with x

# define objective function in python:

def obj(w,x,y):
    return np.sum((y-yhat(x,w))**2) # after create vector, can square each element (element-wise)
  # calling function previously created with yhat  
  
  # as change values of w, will change output of eobjective function
#%%
# example:

x_rand = (np.random.rand(100,2) - 0.5)*2 # n_rows by n_cols # random matrix # 100 row, by 2 column matrix
# 2 columns of x x^(1) will have x^1 of 1 and x^2 of 2, w for this is w1 and w2

w_exact = np.array([5,3]) # some w that I know

y = yhat(x_rand, w_exact) # generate a function # taking hte logistic function of the sigmoid values

y = y+np.random.randn(*y.shape)*0.055 # add random guassian # adding random noise on top of y; now y is not an exact value

w_temp = np.array([5.5, 3.2]) # say w is actually these values

print(obj(w_temp, x_rand,y))

print('--')

w_temp  = np. array([5.1,3.1])

print(obj(w_temp, x_rand, y))

print('---')

print(obj(w_exact, x_rand, y))

# can get very small sse

#%% let's graph out the values as w changes

from matplotlib import pyplot as plt

%matplotlib inline

plt.subplot (1, 2, 1)
plt.plot(np.dot(x_rand,w_exact.T),y,'.') # dot product of x times w exact
plt.title('Close to actual')

w_temp = np.array([5.5,0.2]) # different w exact

plt.subplot(1,2,2)

plt.plot(np.dot(x_rand,w_temp.T),y,'.') # dot product

plt.title('not so close w to actual')

# when w close to actual values, starts to look like a sigmoid, however, when w not close to actual, something more random shows up

# trying a buns of different values will help you get something cloes

# scipy has tool called minimize that allows you to try to minimize as much as possible

#%% take first pass at optimization

from scipy.optimize import minimize

w_start = np.random.rand(*w_exact.shape)
w_found = minimize(obj, w_start, method = 'Nelder-mead', args = (x_rand, y))

print(w_found)
print('Exact values: ', w_exact)
# nfev number of times is evaluates 
# exact values are vary close to 5, 3

# can make optimization far more successful by taking the derivative of the objective function
#%%
############################################################    
#%% Python Unit 4: 4.2.1 optimization with Scipy/Numpy Part II (optional)
############################################################
#%% Formulate what it means to come up with a function and figureing out paramterrs that give us the best fit between x and y

# equation we are trying to predict

# y = sigma(w*x)

# saying we have some input x and output y and have equation the we are using toe apprximate the value, multiply x times some values W and get the dot product

# scalar product and send through function sigma- sigmoid function
# sigma(a) can be written as : 1/(1+e^-a) 

# sigmoid interesting ,because if we draw out what it can represent, value of a gotten, as a increases, can control how sloped the value becomes

# if you were to multiple a by some factor, could control slope

# curve fitting problem where we have to map the values such that we get the best values that map x and y together

# y could b : y = 0.1, 0.2, 0.9 ...all the way to 1
#  could be n values
# x [0.1,0.3] want to map this to 0.1 of y, all the way to n examples to map to this
# do this by finding w vector with unknown pair of parameters, need to figure out what first parameter is and what second parameter is

# y = (1/e^(-1*x))

# have all the way to cap n instances

# Y ^ 1 = 1/ (1+e)^-w*x(i)

# some up with equation in python for doing this

#%%

# set of matrix multiplications that we can feed to minimization equation in the problem

# let's define objective function such that we know that the values are close to eachother

# y_hat = sigma(w*x^(i)) -> would like y_hat to be as close to real value of y as possible

# objective = sum(y^ii - y_hat^ii) 2 - want to minimize this
# in order to minimize, must take the derivataive of this function with respect to w1 and w2, once this is done, it gives optimization algorithm ability to minimize

# thisisnt that bad to take deriviative

#partial deriviative d: d/dwj of objective function = sum(d/dwj ( y^i - y_hat^i)^2 - only thing needed to take the derivative is y_hat

# derivative of something squared is just 2 times itself
# sum(2*(y^i-Y_hat^i) d/dwi ..lost me at 11:00

# derivative of sigmoid function is phe*1-phe

#%%
############################################################    
#%% Python Unit 4: 4.2.2 optimization with Scipy/Numpy Part III 
############################################################
#%%
# from jupyter notebook file 04 optimize

# focus on what we want to do nnumericallly with numoy values

# length of w determined by the number of columns in the originl x, we will need to perform the opertion for each value of j

# can code up in python no problem

# define the gradient of hte objective function without vectorized programming

def obj_gradA (w,x,y):
    grad = []
    yh = yhat(x,w) # yh is like the y hat vector
    # a not so great implementation of the derivative, lots of for loops
    for j in range(len(w)):
        tmp = 0
        for i in range (len(x)):
            tmp = tmp+yh[i]*(y[i]-yh[i])*(1-yh[i])*x[i,j] # drawing out hte equation ith instance of x and the jth elements multiplied
            
        grad.append(-2*tmp) # append to the gradient which is the derivatiave which is the same size as w, tells which direction to move w to get better objective function
    
    return np.array(grad)
    
# add some vectorization, because repeating alot of operations multiple times in the loop
# can make temp become one single vector taking out that single line step

#%%
def obj_gradB(w,x,y):
    grad = []
    yh = yhat(x,w)
    
    # a better implementation of hte derivative
    tmp = yh*(y-yh)*(1-yh) # exactly the equation that we talked about with the element-wise multiplication; define temp
    for j in range(len(w)):  # for each temp vector, do this
        grad.append(-2*np.sum(tmp*x[:,j])) # grabbing all elements of the jth column; you slice this and do point by point multiplication of x
        return np.array(grad) # converting to vectors and doing the multplication
    
# define the gradient in terms of numpy only operations, vectorized

# repeating even more calculations, no reason why have to saw x*j multiplied by the temp vector, can do dot product with x and autmotaically go culumn by column in x matrix

#%%
def obj_gradC(w,x,y):
    yh = yhat(x,w)
    return -2*np.dot(yh*(y-yh)*(1-yh),x) # entire objective function boiled down to one calculation, under the hood, C++ doing all heavy lifting of for loop and calc of derivitive is very quick
    

#%% now tell scipy what the value of the gradient is

w_start = np.random.rand(*w_exact.shape)

% time w_found = minimize (obj, w_start, method = 'Nelder-Mead', args = (x_rand,y))
% time w_foundA = minimize (obj, w_start, method = 'BFGS', args = (x_rand,y), jac = obj_gradA)
% time w_foundB = minimize (obj, w_start, method = 'BFGS', args = (x_rand,y), jac = obj_gradB)
% time w_foundC = minimize (obj, w_start, method = 'BFGS', args = (x_rand,y), jac = obj_gradC)
# using the magics functions to determine how long it takes to run the lines of code

# calling the min function without hte gradient
# then use it to tell that gradient is here
# use the gradient with different implemnetations of B and C
# print out the values it found and how many loops to minimize


print('exact values: ' , w_exact)
print(w_found.x, w_found.nfev)
print(w_foundA.x, w_foundA.nfev)
print(w_foundB.x, w_foundB.nfev)
print(w_foundC.x, w_foundC.nfev)

# print out hte x values and how many evaluations did it take to get hte object function
# when evaluated the gradient, had to evaluate 95 times and the others were 14 times
# so by letting C++ do the work , it 

#%% ok, so now we have this sigmoid solution and we can make this interactive and calculate these things on the fly

# what should the slope of the sigmoid be?

# go to his example: fairly complex in the jupyter notebook

#%% can add user interface pieces to ipython notebooks and get the noise power that we want


# and have interactive gui with the setup - he uses drag bars

#%% Bonus: numba, allows to compile C++ code, just in time compiler

from numba import jit
from scipy.optimize import minimize

# redefine ex variables

x_rand= (np.random.rand(100, 2) - 0.5)*2 # n rows by n cols

y= yhat(x_rand, w_exact) # generate a function

y = y+np.random.randn(*y.shape)*0.015

# define gradient without vectoried programming

@jit

def obj_gradA(w, x, y):
    grad = np.seros(w.shape)
    yh = yhat(x,w)
    # a not so great impl of the derivatie
    for j in range(len(x)):
        tmp = 0
        for i in range (len(x)):
            tmp = tmp+yh[i]*(y[i]-yh[i])*(1-yh[i])*x[i,j]
        grad[j] = -2*tmp
    return grad

#%timeit obj_gradA(w_exact,x_rand, y)

    #%%
###########################################
########### Unit 5 ########################
###########################################
#%%

# pull everything together with python and jupyter notebooks
# we will pull images from pages and compare to see how similar they are to one ntoher

 #%%
############################################################    
#%% Python Unit 5: 5.1 putting it all together part I
############################################################
#%% # analyzing data from nyt api - downloaded in json.

import warnings
warnings.filterwarnings('ignore')

import requests # this library allows us to call the .get and use a URL
from contextlib import closing
import json # deserialize data into libraries

# get the most recent activity from github... (changes all the time)

with closing(requests.get('https://api.github.com/events')) as r: # save response into variable r > a request object
    payload = json.loads(r.content.decode('utf-8')) # make the content into json
    print (payload[0]['payload']) # print out some interesting stuff
# can see the most recent even on github

# closing takes whatever object and transfers out to use in with statement - makes sure for certain that the connection is closed
# accessing r.content is a string of everything that came back
# payload is a list that it sends back to us
# payload at the 0th element- oth element is actually a dictionary
# oth event, payload printed and this payload is actually another dictionary with keys and values

# wont spend much time, interested in nyt.

#%% Now NYT request

import requests
import json
from contextlib import closing

# get api key saved on hardrive

with open ('../NYTimesAPI.txt') as f: # reading the api key in: free
    apr.key = f.read() # read in his private key

# make the base url and dictionary to get requested key/values
url  = 'https://api.nytimes.com/svc/search/v2/articlesearch/json' # access this file in the article search .json
payload = {'api-key': api_key, 'q':'Olympics'} # key/values for get request (look up in the api) # parameters, key equals your key and the query (q) is equal to the olympics


# perform the actual request

with closing(requests.get(url,params= payload)) as r:
    json_payload = json.loads(r.content.decode ('utf-8')) # this is a dictionary, status:ok means everything is alright
    print(json_payload)
# key called response, which is another dictionary, with a docs key, which is a list - really interested in this
# response varliable is a dictinary with key value pairs
# can access 0th article by accessing the docs

some_article = json_payload['response']['docs'][0] # the first article in the docs, very common way to transform get requests into fata

# can change the 0 to anything else in the articles

print(some_article['lead_paragraph'])

#%% there is a huge amount of information avaialable in these articles

# images that are embedded are able ot be grabbed

from Ipython.display import Image
img_url = 'http://www.nytimes.com/' + some_article['multipedia'][0]['url']  # adding in the multimedia for the article - this is a magic

Image(img_url)

# the way that this is setup, allows us to get snippets of text from the article and build a codebase so that it is easy to get
# this information from the data

# would rather api class structure to display

 #%%
############################################################    
#%% Python Unit 5: 5.1.1 putting it all together part II
############################################################

# wrapping articles in a custom class for functionality

# now that we know what hte overall article metadata looks like, let's create a custom class for getting access to the data

# want to include summary of the article

class NYTarticle(object):
    def __init__(self,article_data): # should be a dictionary, docs was a list of all of hte articles, we will wrap each one in nyt class
        self.data = article_data # should already be decoded json directory when passed in; save all of the data put into this class structure
        self.keys = article_data.keys() # saving hte srticle data keys; what are the associated keys
        # want to hand off the data of type NY article 
        # start by creating this class with data

# define a very simple 'getter' param is the key that we want to access        
    def get(self, param = 'type of material'): # generic getter for any part of the article
        if param in self.keys: # prevent any errors; if parameter in here, return self.data at hte parameter, else return nothing
            return self.data[param]
        else:
            return None
            
# test the bar bones implementation

jsondocs = json_payload['response']['docs'] # list of all of hte documents created
article = NYArticle(json_docs[0]) # at the 0th doc, name article and wrap in NY article
print (article.get('lead_paragraph')) # in the list, we had the lead paragraph, and some text that has to do with the article

# what if wanted other information?  headline ( a dictionary)

print(article.get('headline'))
# keys: abstract - with some text, 

# let's put together a summary with a new class

#%%

class NYTarticle(object):
    def __init__(self,article_data): 
        self.data = article_data 
        self.keys = article_data.keys()
   
    def get(self, param = 'type of material'): 
        if param in self.keys and self.data[param]!=None: # prevent the key errors 
            return self.data[param]
        else:
            return '' # slightly changed the getter, also say is that parameter not equal to none, if not, then return none
            # we are now returning a blank instead
    def summary(self): # agglomerate some info on the article
        summary_inclusion = ['snippet','lead_paragraph','abstract'] # interested in these features
        vals = [self.get(x) for x in summary_inclusion] # for each key, will call self.get and grab each out of the article, and create a list for all of these values that are a part of this dictionary
        return '\n'.join(vals) # going to add a snippe
        
json_docs = json_payload['response']['docs']
article = NYArticle(json_docs[0])
print(article.summary())

#%% want to define a recursion so that we can access all of the diffferent items of hte article

class NYTarticle(object):
    def __init__(self,article_data): 
        self.data = article_data 
        self.keys = article_data.keys()
   
    def get(self, param = 'type of material'): 
        if param in self.keys and self.data[param]!=None: # prevent the key errors 
            return self.data[param]
        else:
            return 'None'
    def get_recurse(self,params = ['type_of_material']):
        def recursion (data, params):
            if isinstance(data, dict) and len(params)>0 and params[0] in data.keys(): 
                return recursion (dta[params[0]], params[1:])
            elif data ==None:
                return ''
            elif isinstance(data, str):
                return data
            else:
                return ''
        return recursion(self.data,params)
        
        
            
    



        
        











            





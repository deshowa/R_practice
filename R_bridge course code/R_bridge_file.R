# Bridge coding course : RBasic R Syntax : 3.2


# very similar to python so we can sort of blow through the syntax
x = 10 # this is assignment
class(x) # what is the type of x, typis equivalent in python
# numeric is type that gets coded exaclty

# comments are the same

# explicitly define the type of a variable
y = as.integer(10) # python integer910)

# complex number support 

z = 10+0i # interprets i as immaginary part of complex number
class(z)

# try to define this right of fthe bat, it will not know what to do

j = sqrt(as.complex(-1))

j

# logicals in r
# use TRUE and FALSE

u = TRUE
v = FALSE

u&v

u|v

!v

# can use strings in R as well

fname = 'Eric'
lname = 'Larson'
paste(fname, lname)

# concatenate 2 strings is paste versus python where it is &

# very basic data types


##### Let's look at vectors in R, work similarly to lists

vec = c(10, 5 ,7)
vec
class(vec)
length(vec)

# difference between python and R, it wasnt sall of the data to be the same type
# all values in vector need to be the same variable type just like in C or C++

str_vec = c('a','b','c')
num_vec= c( 1, 2, 3)

# now if you want to concat, R see these and thinks it needs them to be the same data type

comb_vec = c(str_vec, num_vec)
comb_vec

class(comb_vec)
# changes to character vector

# to index into them, use square brackets

comb_vec[1]
# r uses a 1 index versus python with a 0 index list, [most programming language]

comb_vec[0]

# not accessing any elements, only the type of combined vector

# cannot access the second to last element with - sign, remember this is the syntax for removal

comb_vec[-2]
comb_vec
# see removes second value

# can do some things in R that cant do right out of box in python

# giving names to something your have


series = c(1.0, 5.6, 3600)
names(series) = c('day','temp','sec')
series
# gives nnames to each element in the series.  In python, may want to do this and it will be harder


# conditionals and loops - very similar to python

# logical indexing

if(1==0){
  print(1)
  
} else{
  print(2)
}

# scoping done with the curly braces

# if looping through things, just like python

x = 1:10 # range function in python
z = c() 3 #empyt vector

for (i in seq(x)) {# for each value in x, enumerate()
  if (x[i] < 5) {
    z = c(z, x[i] -1)
  } else {
    z = c(z, x[i]/2)
  }
} 

# didnt have to define as seq(x) count have said 1:10 and given exact same vector z

# very similar syntax


## functions in R easy to define use function rather than def

myfct = function(x1, x2 =5){
  z1 = x1/x1
  z2 = x2*x2
  myvec = c(z1,z2)
  return(myvec)
  
}

myfct

myfct(x1= 2, x2 = 5)
# dont need the names, can flip the orders if you are explicitly naming hte objects

# define optional arguments  - not really in python

myfunct2 = function(x1 = 5, opt_arg){
  if(missing(opt_arg)) {#missing?}
    z1 = 1:10
  } else {
  z1 = opt_arg

  } 
  cat('my function returns', '\n')
  return(z1/x1)
}

######################################
##### Basic R syntax Part II: 3.2.1###
######################################

# installing packages, different from conda

x = 5
x = x*5
x

# easy place to manage and install packages

install.packages('magic')

library(magic)

# goes back to calculator example III-3

# for basic R syntax 3.2.1 the video uses the calculator example




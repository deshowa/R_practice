# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 20:31:36 2016

@author: Alex
"""

"""
Data Mining 1- Unit 1 code

"""

# first, let's read in a .csv file and print the first 5 rows

with open('C:\\SMU Data science\\Data Mining I\\DataMiningNotebooks\\data\\heart_disease.csv') as fid:
    for idx, row in enumerate(fid):
        print row,
        if idx >=4:
            break
        
# want to see what enumerate does : https://docs.python.org/2.3/whatsnew/section-enumerate.html

import numpy as np
sample = np.random.randn(100)
sample_2 = enumerate(sample)

# creates a counter and an element for each value that the data is applied to.  So, the index is the counter and the row is the data

# this makes more sense now that we understand what the process is doing

#%%
import pandas as pd

df = pd.read_csv('C:\\SMU Data science\\Data Mining I\\DataMiningNotebooks\\data\\heart_disease.csv') # read in the csv file

df.head()


df.info()


#%%

# read data from sql lite database

import sqlite3 as sql

con = sql.connect('C:\\SMU Data science\\Data Mining I\\DataMiningNotebooks\\data\\heart_disease_sql') # create connection variable

df = pd.read_sql('select * From heart_disease',con) # the table name is heart disease

df.head()

df.info() # data types are now all objects

#%%

# indexing the dataframe can be done in several ways 

print df.age

print df['age'] # access using strings

print df.age.head()

print df['age'].head()


#%%

print df.chest_pain.min(), df.chest_pain.max(), df.chest_pain.median()

print type(df.chest_pain)

# %% 

# get rid of a variable

print df.info()

if 'site' in df:
    del df['site']

print df.info()

# removed the site variable

#%% replace null or string value or change the data type

import numpy as np

df.dtypes # list the data types, similar to info()

# replace ? with -1, we can deal with missing values later
df = df.replace (to_replace ='?', value = -1) # this actually has to be done in order to do the conversions below, which makes sense

# change the numerics to float

continuous_features = ['rest_blood_press','cholesterol','max_heart_rate','ST_depression']

ordinal_features = ['age','major_vessels','chest_pain',
                    'rest_ecg','Peak_ST_seg','thal','has_heart_disease']

categ_features = ['is_male','high_blood_sugar', 'exer_angina']

df[continuous_features] = df[continuous_features].astype(np.float64)
df[ordinal_features] = df[ordinal_features].astype(np.int64)

df.info()
df.head()

df.describe() # gets summary of continuous or the nominal values

# notice that there are missing values as evidenced by the -1 values

#%%

# how many values have the -1 which we set for the missings in the dataset

import numpy as np

# let's set those values to nan so pandas can see that they are missing

df = df.replace(to_replace = -1, value = np.nan) # replace with NaN - not a number
print df.info()

df.describe() # scroll to see the values


# some stats on the data

df.median()

# before, we were using hte columns, now, we run the code that calculated the value for every column

# we can now fill the nan with the median if we want

#%%

# imputation

# can do the entire set if chosen

df_imputed = df.fillna(df.median())

df_imputed.info()
df_imputed.describe()


# we may not want the median across the board, it may depend on the distributions of hte data


    # we may want the median for hte continuous and the mean for the discrete
    
series_mean = df[continuous_features].mean()

series_median = df[ordinal_features + categ_features].median()

cat_series = pd.concat((series_median,series_mean))

print cat_series # look at what we created
print type(cat_series)

df_imputed = df.fillna(value = cat_series)

df_imputed.info()

df_imputed.describe()

#%% indexing logically into dfs

# can just look at the values you want

df_imputed[df_imputed.has_heart_disease ==0].describe()

# returns 411 values, because those are the 411 observations wth heart disease of 0.  Notice that heart disease variable is 0

#%% The groupby function

df_imputed.groupby(by = 'has_heart_disease').median()

# can also use operators

df_imputed.groupby(by=df_imputed.major_vessels>2).mean()
# outputs true/false grouping for such filters

#%% One hot coding for categorical variables

# allows the creation of a new attribute for each value of a discrete variable

one_hot_df = pd.concat([pd.get_dummies(df_imputed[col],prefix = col) for col in categ_features], axis = 1)

one_hot_df.head()


# can also do for just one column

tmpdf = pd.get_dummies(df_imputed['chest_pain'], prefix = 'chest')

tmpdf.head()

#%% see notes on R-coding in python - will need alternate solution to use Rpy2

#############################################################################
#%% Feature Manipulation in python-pandas ###################################
#############################################################################

#%%
import pandas as pd
import numpy as np

df= pd.read_csv('C:\\SMU Data science\\Data Mining I\\DataMiningNotebooks\\data\\titanic.csv')
df.head()
df.info()
df.dtypes() # see the datatypes of the df

#%% Calculate the percentage of people who died/survived on the titanic

df.head()

############# This is my step through way of doing it
survived = df.Survived.sum()
print survived

total_pax = df.Survived.count()
print total_pax

pct_survived = survived * 1.00 / total_pax # just like SQL, we dont have to cast or change the data type

print pct_survived

# so it can be simplified by:
other_pct_survived = df.Survived.sum() * 1.00 / df.Survived.count()

print other_pct_survived


# so to get the pct of people who died:
pct_died_1 = ( (df.Survived.count()- df.Survived.sum()) * 1.00 ) / df.Survived.count()
print pct_died_1

# the way it was done in class:
    
pct_died_2 = float(len(df[df.Survived ==0]))/len(df)*100
print pct_died_2

# we get the same answer

#%% Group by survival


df_grouped = df.groupby(by = 'Pclass')

print df_grouped

df_grouped.head()
len(df_grouped)
df_grouped.describe() # using describe allows us to see what the groupby did and do aggregation by the grouped data.  very informative

# now can use the df_grouped for simpler operations

print 'The total number of people who survived was: ',df_grouped.Survived.sum()
print '=========================='
print 'The total passengers were: ', df_grouped.Survived.count()
print '=========================='
print 'The percentage of people who survived was: ', df_grouped.Survived.sum()/df_grouped.Survived.count()

##### simply way to do it: 
    
df.groupby(by ='Pclass').Survived.sum()/df.groupby(by ='Pclass').Survived.count()

# python allows the nesting

#%%

# to select a certain row in the dartaframe

df[878:879]
#%% feature discretization

# we can discretize using the cut function in pandas

df['age_range'] = pd.cut(df.Age,[0,16,65,1e6],3,labels = ['child','adult','senior'])
# 1e6 is the upper range that everything must fall into for the pandas cut function, so this is more a formality

df.age_range.describe() # gives a good summary of what was just created, see that there aare 714 records, 606 as the freq with 3 categories


# now let's use the new variable in groups


df_grouped = df.groupby(by = ['Pclass','age_range'])

print 'percentage of survivors in each group'
print df_grouped.Survived.sum() / df_grouped.Survived.count() *100

#%% need to clean up the dataset before we move forward: imputation

# remove the attributed we dont care about

##### Alex's way of doing it

    # clone the df so that we dont mess anything up

       # test_df = df
        
       # useless_attributes = ['PassengerId','Name','Cabin','Ticket']
        
        #test_df = del df[useless_attributes]
        ##### This approach didnt work
# try again

test_df = df
useless_attributes = ['PassengerId','Name','Cabin','Ticket']

for col in useless_attributes:
    if col in test_df:
        del test_df[col]

# so this worked!

# the class way:
    
for col in ['PassengerId','Name','Cabin','Ticket']:
    if col in df:
        del df[col]

# impute missing values

df_grouped = df.groupby(by = ['Pclass','SibSp'])
print (df_grouped.describe())

# looks like we have missing values for age


# use the grouping to fill in the data set in each group, then transform back

df_imputed = df_grouped.transform(lambda grp: grp.fillna(grp.median()))

df_imputed[['Pclass','SibSp']]= df[['Pclass','SibSp']]

print (df_imputed.info())

# redo the age cut value

df_imputed['age_range'] = pd.cut(df_imputed.Age, [0,16,65,1e6],3,labels = ['child','adult','senior'])

df_imputed.dropna(inplace = True)

df_imputed.info() # now we have 884 rows for all variables!  Nie work


# Always ask, did imputation change the variables and their distributions?

df_grouped = df_imputed.groupby(by  = ['Pclass','age_range'])
print ('Pct survived in each group with imputation: ')
print (df_grouped.Survived.sum()/df_grouped.Survived.count() *100)

# not much of a change at all

#%% Normalization in the panadas dataframe

# subtract off the min and divide by the max

df_sub = df_imputed[['Survived','Age','Pclass','Fare']]
df_normalized = (df_sub - df_sub.min()) / (df_sub.max() - df_sub.min())

df_normalized.describe(include = all) # all values between 0 and 1 now
# can divide by standard dev to normalize further



# alternative approach
from sklearn.preprocessing import StandardScaler

df_matrix = df_imputed[['Survived','Age','Pclass','Fare']].values

s_obj = StandardScaler() # this returns an object for us to manipulate

df_matrix_norm = s_obj.fit_transform(df_matrix)  # this normalizes the entire matrix

print (np.std(df_matrix_norm,axis = 0)) # unit standardized
print (np.mean(df_matrix_norm,axis = 0)) # zero mean

#%% On hot coding for indicator variables


#tmpdf = pd.get_dummies(df_imputed['Sex'], prefix = 'gender')
#tmpdf.head()

tmpdf = pd.get_dummies(df_imputed['Pclass'], prefix = 'class')
tmpdf.head()

#%% plotting imputed values

import matplotlib.pyplot as plt
import warnings
warnings.simplefilter('ignore',DeprecationWarning)

%matplotlib inline

df_grouped = df_imputed.groupby(by = ['Pclass','age_range'])
survival_rate = df_grouped.Survived.sum()/ df_grouped.Survived.count()

ax = survival_rate.plot(kind = 'barh', color = 'green')

#%%
##############################################
##### Optional reading assignment for Unit 1##
##############################################

###########################
#%% pandas library overview
###########################

#%% site :
https://vimeo.com/59324550
http://pandas.pydata.org/pandas-docs/version/0.15.2/tutorials.htmlUnit

#%%

# dont have his data ,but can sopy some cool things

## Time series operations

appl_bar.dt # shows the timestamps as strings

# remove and convert to timeseries format and use as index

appl_bars.index - pd.to_datetime(aapl_bars.pop('dt'))

appl_bars.head()


def load_bars(ticker):
    bars = pd.read_csv(temp % ticker)
    bars.index = pd.to_datetime(bars.pop('dt'))
    return bars

aapl_bars.at_time(time(15,0)).head(10) # this gives everything at the 15th hour of the dataset for the first 10 records

# aggreagting values to the month level

mth_mean = appl_bars.cloe_price.resample('M', how = ['mean','median','std'])


mth_mean.plot()
# moving window calculations


close = appl_bars.close_price

close / close.shift(1)-1

minute_returns = aapl_bars.close_price.pct_change()
std_10day = pd.rolling_std(minute_returns,390, *10)
std_10day.resample('B').plot()


#%% data alignment

# can add 2 time series together and pd will fill in the blanks

ts1 = pd.Series(np.random.randn(10),
                index = pd.date_range('1/1/2000', periods = 10))

ts1

ts2 = ts1 [[0, 2, 4, 5, 6, 7, 8]]

ts2

ts1 + ts2

df = pd.DataFrame({'A':ts1,'B':ts2})
df

# can make them 2 columns in the dataframe with imputed Nans


#%%
# Missing data handling

df

df.count() # can see that it omits the count values that are null

df.sum() #  excludes the missing values

df.mean(1) # mean of the rows nas excluded


df.dropna(how = 'all') # this will drop only rows that are completely NA all the way across

df.dropna() # will drop any row that contains an NA

df.fillna(0) # will fill nas with 0

df.fillna(method = 'ffill') # interpolation called full forward

df.asfreq('4h') # changes to 4 hourly

# %% 

keys = ['industries, ccy]
zscore = lambda x: (x-x.mean())/x.std()
# research lambda
normed = df.groupby(keys).apply(zscore)


df.groupby(keys).agg(['mean','std']) # good way to perform multiple operations

# pulling ranked values

highest_rated = data.groupby('title').rating.mean()[freq_titles].order()[-20:] # pulls the top 20 ranked titles


# %% filtering the data

filtered = data[data.title.isin(highest_rated.index)]
filtered.title = filtered.title.str[:25] # truncated the title to the top 25
filtered.groupby(['title','gender']).rating.mean().unstack() # get the votings my ratings, can chagne mean to count

                 
# %% pandas pivot tables

mean_ratings = data.pivot_table('rating', rows = 'title',
                                cols = 'gender', aggfunc = 'mean')

mean_ratings.tail(20)

# look at unstack


























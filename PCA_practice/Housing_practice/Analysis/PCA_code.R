#### Practicing PCA in R with Boston dataset from the UCI machine learning lab ###

# good guide: https://www.analyticsvidhya.com/blog/2016/03/practical-guide-principal-component-analysis-python/
 

# load the libraries

libraries <- c ('ggplot2','Hmisc','factoextra')
sapply(libraries, library, character.only = TRUE)


# first, we will read in the file that we downloaded from: https://archive.ics.uci.edu/ml/datasets/Housing 
crime <- read.csv('Analysis/Data/crime data.csv')

# print a summary of the data
summary(crime)

# first, let's make sure that the datatypes all make sense in the file

sapply(crime, class )

str(crime) # does some of the same things as class, but more data

  # the classes all look pretty nice here to me.   Idont think we will have to do any data type conversion

# one of hte assumptions of PCA is that my features( attributes) are highly correlated, let's see what we can find:

corr_matrix <- rcorr(as.matrix(crime))
print(corr_matrix)
  
  # it looks like we have some very highly correlated values in the dataset.  This meets the main assumption and hence considers that we may have reduncancy in the data

# it is always a goo idea to look at the distributions of the data in the dataset.
# since we have no categorical values, this can be helpful in creating categories


hist(crime, col = 'green' )

# taking all in one view is a little tedious, let's set the view a little differently and add each variable 

# set the matrix

par(mfrow = c(3,2)) # plot 6 at a time

hist(crime$crime, col = 'dark green') # looks like a highly positively skewed variable, take a log to see , the data is kind of sparse, but low crime is prevalent

hist(crime$zn, col= 'dark green') # to no surprise, this is skewed highly in thise case
#hist(log(crime$crime), col = 'dark green')
hist(crime$chas, col = 'dark green') # an indicator variable that must be removed from the dataset.
hist(crime$nox, col = 'dark green')
hist(crime$rm, col = 'dark green') # dwelling sizes are very normally distributed
hist(crime$dis, col = 'dark green')
# panel 2
par(mfrow = c(3,2))
hist(crime$rad, col = 'dark green')
hist(crime$tax, col = 'dark green')
hist(crime$ptratio, col = 'dark green')
hist(crime$b, col = 'dark green')
hist(crime$lstat, col = 'dark green')
hist(crime$medv, col = 'dark green')


# so, we know that the explanatory variable is highly-positively skewed, let's look at a qqplot

par(mfrow = c(1,1))
qqnorm(crime$crime)
# obviously, just what we expected
qqnorm(crime$crime**2)
qqnorm(1/crime$crime)
qqnorm(log(crime$crime))
abline(0,1) # adds the 45 degree line
# a log transform seems to perform the best, but not amazing with this data.  However, we have quite a few observations so, we will continue

# now we create a dataset of x variables to plug into the PCA 

x_vars<- subset(crime, select = -c(crime, chas)) # removed the y variable and the indicator variable from the dataset
names(x_vars) # check to ensure we removed the columns

# drop the categorical 

####################################
##### Let's run the PCA ############
####################################


# remember that since the ranges on the variables
prin_comp <- prcomp(x_vars, scale. = T)

names(prin_comp)
# these are the available values in the PCA

# let's first look at the scree: http://www.sthda.com/english/wiki/principal-component-analysis-in-r-prcomp-vs-princomp-r-software-and-data-mining
fviz_screeplot(prin_comp) 

# it looks like 4pcs can explain 80% of the variation in the dataset

# let's look at the 
prin_comp$rotation[,1:4] # look at only the 4 pcs we are interested in


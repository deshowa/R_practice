# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 18:00:23 2017

@author: Alex
"""

"""

Date Mining Unit II code

"""
#%%
# first, we will start off with creating the dataset that last week ended off of.  We might be able to run execfile(), but easy enough to create

import pandas as pd


df = pd.read_csv('C:\\SMU Data science\\Data Mining I\\DataMiningNotebooks\\data\\titanic.csv')


df['AgeRange'] = pd.cut(df['Age'], [0,16,65,1e6],3, labels = ['child','adult','senior'])

df_grouped = df.groupby(by = ['Pclass','AgeRange'])

# removed the attributes not needed

for col in ['PassengerId','Name','Cabin','Ticket']:
    if col in df:
        del df[col]

df_grouped = df.groupby(by = ['SibSp','Pclass'])

print (df_grouped.describe())

#%% impute the median

df_imputed = df_grouped.transform(lambda grp:grp.fillna(grp.median()))

df_imputed[['Pclass','SibSp','Sex','Embarked']] = df[['Pclass','SibSp','Sex','Embarked']]

df_imputed['age_range'] = pd.cut(df_imputed.Age,[0,16,65,1e6],3,labels=['child','adult','senior'])

print (df_imputed.info())

df_imputed.dropna(inplace=True)

# 5. Rearrange the columns
df_imputed = df_imputed[['Survived','Age','age_range','Sex','Parch','SibSp','Pclass','Fare','Embarked']]



#df_imputed[['Pclass','SibSp']]= df[['Pclass','SibSp']]

#df_imputed['age_range'] = pd.cut(df_imputed.Age, [0,16,65,1e6],3,labels = ['child','adult','senior'])

#df_imputed.dropna(inplace = True)

df_imputed.info() #

# alright this fixes it so that we have the correct dataset for the rest of teh analysis

# %% 
###### START UNIT II COURSE WORK ##########
#%%

############################################
#%% Data Visualization in Python 
############################################

import matplotlib.pyplot as plt
import warnings
warnings.simplefilter('ignore', DeprecationWarning)

%matplotlib inline

# pandas has plenty of plotting abilities built into the system

plt.style.use('ggplot')


df_grouped = df_imputed.groupby(by = ['Pclass','age_range'])

# to get column names df.list()

survival_rate = df_grouped.Survived.sum()/df_grouped.Survived.count()

ax = survival_rate.plot(kind = 'barh', color = 'blue')

#%% make a crosstab - allows you to easily getthe numbers

survival = pd.crosstab([df_imputed['Pclass'], df_imputed['age_range']], df_imputed.Survived.astype(bool)) # bool is how we wanted it crosstabed

print (survival)

#%% make a stacked bar
# can make the crosstab into a chart

survival_rate = survival.div(survival.sum(1).astype(float), axis = 0)
# survival.div is telling us we want the variables divided
# sum(1) sums across the row as a floar
# axis = 0 tells us to divide the row essentially, the format is (0,1) we want to divide on the row, so we pick 0

survival_rate.plot(kind ='barh' , stacked = True, color = ['black','gold'])

print (survival_rate)

#%%
# plot rates by sex and class and plain bar graph

survival_counts = pd.crosstab([df_imputed['Pclass'],df_imputed['Sex']], df_imputed.Survived.astype(bool))

survival_counts.plot(kind = 'bar',stacked = True, color = ['black','gold'])

# %% may want a boxplot

ax = df_imputed.boxplot()

#%% may want to breakdown the fare by class

df_imputed.boxplot(column = 'Fare', by = 'Pclass')


#%% looking at boxplots separately

vars_to_plot_separate = [['Survived','SibSp','Pclass'],
                         ['Parch'],
                         ['Age'],
                         ['Fare'] ]
plt.figure(figsize=(10, 6))

for index, plot_vars in enumerate(vars_to_plot_separate):
    plt.subplot(len(vars_to_plot_separate)/2, 
                2, 
                index+1)
    ax = df_imputed.boxplot(column=plot_vars)
plt.show()

#%% look at the figures separately
# dont need subplot

vars_to_plot_separate = [['SibSp'], ['Pclass'],['Parch'],['Age'],['Fare']]

for index, plot_vars in enumerate (vars_to_plot_separate):
    plt.figure(figsize = (4,4))
    ax= df_imputed.boxplot(column = plot_vars, by  = 'Survived')
plt.show()

#%% scatterplot matrix

from pandas.tools.plotting import scatter_matrix
ax = scatter_matrix(df_imputed,figsize = (15,10)) # having the figsize in really helps blow the picture up a bit

#%%
from pandas.tools.plotting import parallel_coordinates
# good tool for visualizing more than 2 dimensions on the same plot

df_sub = df_imputed[['Survived','Age','Pclass','Sex']] # essentially created new df with just these variables

df_sub.Sex = df_sub.Sex =='male' # creating a vector of true and false values

# create normalized variables

df_normalized = (df_sub - df_sub.mean())/df_sub.std()

df_normalized.Survived = df_sub.Survived # putting back the original value to the column survived

# add some jutter to Pclass and sex variables

df_normalized.Pclass = df_normalized.Pclass + np.random.rand(*df_normalized.Pclass.shape)/2


df_normalized.Sex = df_normalized.Sex +np.random.rand(*df_normalized.Sex.shape)/2

parallel_coordinates(df_normalized,'Survived')

plt.figure()

parallel_coordinates(df_normalized[df_sub.Pclass>1],'Survived')


#%% using seaborn


# built on pandas and matplotlib


import seaborn as sns

cmap = sns.diverging_palette(220,10, as_cmap = True) # one of hte many color mappings

# now try plotting come of hte previous plots to see how much more visually appealing they are

# appears that must set a palette to start

#%% correlation matrix

sns.set(style = 'darkgrid') # one of the many styles to plot using seaborn

f, ax = plt.subplots(figsize = (9,9)) # f is figure pass into seaborn, ax is axes

sns.linearmodels.corrplot(df_imputed,
             annot = True, # plot numeric annotations?
             sig_stars = True, # plot significance?
             diag_names = True, # plot the names of the variables on the diagonal
             cmap  = cmap,
             ax = ax
             )
f.tight_layout() # automatically adjusts subplot parameters to fit within the figure area -- experimental

# *** is 95% confidence
#%% violin plot



pal = sns.cubehelix_palette(start=2.8, rot=.1)

sns.violinplot(df_imputed[['Age','Fare','SibSp','Parch']],
               color = pal,
               groupby = df_imputed.Survived.astype(bool))
# get some sort of weird error, because of the palette

#%% factorplot - basically a grouped boxplot

sns.factorplot('age_range','Fare','Survived', df_imputed,
               kind = 'box',
               palette = 'PRGn')

#%% Paired grid - sophisticated way to combine many plots


# create a plot grid
g = sns.PairGrid(df_imputed[['Fare','Survived','SibSp']], diag_sharey=False)
g.map_lower(sns.kdeplot, cmap="Blues_d") # use joint kde on the lower triangle
g.map_upper(plt.scatter) # scatter on the upper
g.map_diag(sns.kdeplot, lw=3) # kde histogram on the diagonal


# pretty cool


#%% Using MLD3 


# use a seaborn example and integrate with mld3
import mpld3

sns.set(style = 'darkgrid') # one of hte many styles to plot using

g = sns.FacetGrid(df_imputed, col = 'age_range',row = 'Sex', margin_titles = True)
g.map(plt.hist, 'Survived', color = 'steelblue', lw = 0)

mpld.display() # add d3 vector graphics support
# go to the corner of the image to enable zooming ,etc.

#%% PCA and LDA using scikit learn

from sklearn import datasets as ds
iris = ds.load_iris()
print (iris['DESCR']) # description of the dataset
print (iris.data())

#%% convert to a datafrome and visualize

import pandas as pd
import numpy as np

df = pd.DataFrame(iris.data, columns = iris.feature_names)

print (df.info())

# add in the class targets and names
df['target'] = iris.target.astype(np.int)

print (df.info())
print (df.head())

# %% visualize with seaborn

%matplotlib inline

from matplotlib import pyplot as plt

import seaborn as sns

sns.set()

sns.pairplot(df, hue = 'target', size = 2)

#%%

# now let's use PCA, and LDA to find the two "best" dimensions of this data
# these are linear transforms to help project the features into something more understandable

from sklearn.decomposition import PCA
from sklearn.lda import LDA

x = iris.data

y = iris.target

target_names = iris.target_names

pca = PCA(n_components = 2)

x_pca = pca.fit(x).transform(x) # fit the data and then transform it

lda = LDA(n_components = 2)

x_lda = lda.fit(x, y).transform(x) # fit the data and then transform

print ('pca: ', pca.components_)

print ( 'lda: ', lda.scalings_.T)

#%% format the wrights into readable strings here
# can skip this step if wanted

def get_feature_names_from_weights(weights, names):
    tmp_array = []
    for comp in weights:
        tmp_string = ''
        for fidx,f in enumerate(names):
            if fidx>0 and comp[fidx]>=0:
                tmp_string+='+'
            tmp_string += '%.2f*%s ' % (comp[fidx],f[:-5])
        tmp_array.append(tmp_string)
    return tmp_array
 #%%   Analytics
 
 pca_weight_strings = get_feature_names_from_weights(pca.components_,iris.feature_names)
 lda_weight_strings = get_feature_names_from_weights(lda.scalings_.T, iris.feature_names)
 
 # createsome pandas datafraomce from the transformed outputs
 
 df_pca = pd.DataFrame(x_pca, columns = [pca_weight_strings])
 df_lda = pd.DataFrame(x_lda, columns = [lda_weight_strings])
 
 from pandas.tools.plotting import scatter_plot
 
 # scatterplot the output from the nsames ceeated from the weights
 
 
 ax = scatter_plot(df_pca, pca_weight_strings[0], pca_weight_strings[1], c = y, s = (y+2) *10)
 
 newfig = plt.figure()
 
 ax = scatter_plot(df_lda, lda_weight_strings[0], lda_weight_strings[1], c = y, s = (y+2)*10)
 
 plt.show()
 
 # %% A more complex dataset and problem
 
 # fetch the images for the dataset
# this will take a long time the first run because it needs to download
# after the first time, the dataset will be save to your disk (in sklearn package somewhere) 
# if this does not run, you may need additional libraries installed on your system (install at your own risk!!)

from sklearn.datasets import fetch_lfw_people



lfw_people = fetch_lfw_people(min_faces_per_person=70, resize=0.4)
 
 
 #%%
 
 # get some of the specifics of the dataset
X = lfw_people.data
y = lfw_people.target
names = lfw_people.target_names

n_samples, n_features = X.shape
_, h, w = lfw_people.images.shape
n_classes = len(names)

print("n_samples: {}".format(n_samples))
print("n_features: {}".format(n_features))
print("n_classes: {}".format(n_classes))
print("Original Image Sizes {}by{}".format(h,w))
print 50*37 # the size of the images are the size of the feature vectors

#%%

# a helper plotting function
def plot_gallery(images, titles, h, w, n_row=3, n_col=6):
    """Helper function to plot a gallery of portraits"""
    plt.figure(figsize=(1.7 * n_col, 2.3 * n_row))
    plt.subplots_adjust(bottom=0, left=.01, right=.99, top=.90, hspace=.35)
    for i in range(n_row * n_col):
        plt.subplot(n_row, n_col, i + 1)
        plt.imshow(images[i].reshape((h, w)), cmap=plt.cm.gray)
        plt.title(titles[i], size=12)
        plt.xticks(())
        plt.yticks(())

plot_gallery(X, names[y], h, w) # defaults to showing a 3 by 6 subset of the faces


# %% reconstruct using full pca

from sklearn.decomposition import PCA

n_components = 300
print "Extracting the top %d eigenfaces from %d faces" % (
    n_components, X.shape[0])

pca = PCA(n_components=n_components)
%time pca.fit(X)
eigenfaces = pca.components_.reshape((n_components, h, w))

#%%

eigenface_titles = ["eigenface %d" % i for i in range(eigenfaces.shape[0])]
plot_gallery(eigenfaces, eigenface_titles, h, w)

#%% reconstruct the image

def reconstruct_image(trans_obj,org_features,faces):
    low_rep = trans_obj.transform(org_features)[0]
    rec_image = np.zeros(faces[0].shape)

    for idx,weight in enumerate(low_rep):
        rec_image += weight*faces[idx]
    return low_rep, rec_image
    
idx_to_reconstruct = 4    
low_dimensional_representation, reconstructed_image = reconstruct_image(pca,X[idx_to_reconstruct],eigenfaces)

#%%
plt.subplot(1,2,1)
plt.imshow(X[idx_to_reconstruct].reshape((h, w)), cmap=plt.cm.gray)
plt.title('Original')
plt.subplot(1,2,2)
plt.imshow(reconstructed_image, cmap=plt.cm.gray)
plt.title('Reconstructed from Full PCA')

#%% using randmized PCA

# lets do some PCA of the features and go from 1850 features to 300 features
from sklearn.decomposition import RandomizedPCA

n_components = 300
print "Extracting the top %d eigenfaces from %d faces" % (
    n_components, X.shape[0])

pca = RandomizedPCA(n_components=n_components)
%time pca.fit(X)
eigenfaces = pca.components_.reshape((n_components, h, w))


#%% # show components

eigenface_titles = ["eigenface %d" % i for i in range(eigenfaces.shape[0])]
plot_gallery(eigenfaces, eigenface_titles, h, w)


#%%

# okay, so lets choose an image and reconstruct it using the eigenfaces
from random import random as rd
from ipywidgets import widgets  # make this interactive!

def plt_reconstruct(idx_to_reconstruct):
    idx_to_reconstruct = np.round(idx_to_reconstruct)
    low_dimensional_representation, reconstructed_image = reconstruct_image(pca,X[idx_to_reconstruct],eigenfaces)

    plt.subplot(1,2,1)
    plt.imshow(X[idx_to_reconstruct].reshape((h, w)), cmap=plt.cm.gray)
    plt.title('Original')
    plt.subplot(1,2,2)
    plt.imshow(reconstructed_image, cmap=plt.cm.gray)
    plt.title('Reconstructed')
    
widgets.interact(plt_reconstruct,idx_to_reconstruct=(1,100,1))




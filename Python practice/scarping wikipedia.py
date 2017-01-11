# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 07:00:02 2016

@author: Alex
"""

# tutorial here: https://www.analyticsvidhya.com/blog/2015/10/beginner-guide-web-scraping-beautiful-soup-python/

# This is a simple program for scraping the web and downloading the results into a file

import urllib2 as url

# import the beautiful soup functions

from bs4 import BeautifulSoup as bs

# import pandas for datadframes
import pandas as pd

# this gives a file-like handle to the remote data
#response = url.urlopen('http://localhost:8080/')


# specify the scrape URL
wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

# query the website and return the html to the variable 'page'

page = url.urlopen(wiki)


# parse the intiial html in the page variable and store it in beautiful soup format

soup = bs(page)

print soup.prettify()

# work with the html tags

soup.tag

# return the content between opening and closting tag including the tag

# return the strng with a given tag


soup.title.string

# find all the links within a page's <a> tag; the a tag is for links in the file

soup.a

# since we only got one link returned, we will do a find all
# the not to show only links, we will iterate over the a and return the link using attribute href with get
all_links = soup.find_all("a")

for link in all_links:
    print link.get("href")
    
# since we want to extract tables, we must search the text for any tables instead 
    
all_tables = soup.find_all('table')

soup.find_all('table', class_= 'wikitable sortable plainrowheaders')

right_table = soup.find('table', {'class' : 'wikitable sortable plainrowheaders'})

# now to generate lists, we will run the below

A = []
B = []
C = []
D = []
E = []
F = []
G = [] 

for row in right_table.findAll('tr'):
    cells = row.findAll('td')
    states = row.findAll('th') # to store second column data
    if len(cells)==6: # only extract table body not heading '/wiki/' = 6
        A.append(cells[0].find(text = True))
        B.append(states[0].find(text = True))
        C.append(cells[1].find(text = True))
        D.append(cells[2].find(text = True))
        E.append(cells[3].find(text = True))
        F.append(cells[4].find(text = True))
        G.append(cells[5].find(text = True))
        


df = pd.DataFrame(A, columns = ['Number'])
df['State/UT'] = B
df['Admin_Capital'] = C
df['Legislative_Capital'] = D
df['Judiciary_Capital'] = E
df['Year_Capital'] = F
df['Former_Capital'] = G
df

df.to_csv('C:/SMU Data science/Python practice/wikipedia_scrape_results.csv', encoding = 'utf-8', na_rep = "", index = False )














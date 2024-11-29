#Project Name:   Image detection of Online Market Korean photocards for Collectibles
#Project Details: A “ Card randomizer” Python program was used to select the precise cell within each load for extraction and categorization for kpop photocards
#it identifies prices, title and waste material for  the percentages of storing materials that collectors such as plastic sleeves 
#(for storing cards) photocards to educate them on the waste impact


#using python is get way to manipulate data and analyze it python 
#First imported the data:
import pandas as pd
import csv
import numpy as np


#(a) prompt user
#(b) input scanner 
#3. group by category

#print function method 

#note: figure out how to take a specific percentage of a paper/glass/
#declare a catergory called mainWasteCat
#insert new columm using in a dataframe
#with open("data.csv", 'r') as csvfile:
#1.read file
df = pd.read_csv('data1.csv')
#2.add catergory called waste catag
#df.insert(3, "wasteCATAG", np.nan)
df.head()
print(df.head)

#need another catalog before we can group because we need the catalog to group them by catalog
#group by to group the materials
#find the catalog there are missing (NA filled to know what catalog belong too) prompt the user with that 
#add catalog data to missing values 
#take that input put it back into the catalog
#group by category 





#(a) prompt user using printf
#print("what category does:" + df['Materials'] + "belong to？")

#prompt the user for missing values in WASTECATAG (comeback)
#access the index based , range the column

#figure out the range and the sum
for i, value in enumerate(df['wasteCATAG']):
   #if condition for parsing materials into segments
    if ( 1 <= i <= 18):
         new_value = input(f"What CAT is this {df.loc[i, 'Materials']}: ")
         df.loc[i, 'wasteCATAG'] = str(new_value) 

#key error
print(df['Materials'])
#print(wasteCATAG)

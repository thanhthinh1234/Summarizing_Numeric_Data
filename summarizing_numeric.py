"""
Author: Thinh Mai
Date: 11/8/2019
Purpose: Summarizing Numeric Data

"""
#load modules
import os
import pandas as pd

#load data
titanic = pd.read_csv('titanic3.csv', sep=',', header=0)

#dat: numerical (pandas) Series
#group: categorical (pandas) Series -- same length as dat
def generateNumericSummary(dat,group):
    #capture column names from user input, then use to create an output dictionary
    dat_col = dat.name
    group_col = group.name

    #a summary of counts of null values across columns
    null = (titanic.isnull().sum(axis=0))
    # #number of values of dat that are missing
    num_missing = null[dat_col]

    #subset 2 input columns
    new = titanic[[dat_col,group_col]]

    #calculate mean and standard deviation
    means = new.groupby([group_col]).mean()
    std = new.groupby([group_col]).std()
    #create output dictionary
    s = {'std':std[dat_col],'numMissing':num_missing,'mean':means[dat_col]}
    return s

print(generateNumericSummary(titanic['age'],titanic['pclass']))

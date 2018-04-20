__author__ = 'chuqiao'

import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("full.csv")

df =data[['#ID(s) interactor A','ID(s) interactor B','Creation date']]

# drop rows of Pandas DataFrame whose value in certain columns is NaN
df = df.dropna()


# get only year values
df['Creation date'] = df['Creation date'].map(lambda x: str(x).split('/')[0])


# series
interacotorA = df.groupby('Creation date')['#ID(s) interactor A'].apply(list)

interacotorB = df.groupby('Creation date')['ID(s) interactor B'].apply(list)

# create dictionary
dicA = interacotorA.to_dict()

dicB = interacotorB.to_dict()

# concatenate two dic into one
interacotor = {key: value + dicB[key] for key, value in dicA.items()}


# remove duplicate values from dict
Results = {k: list(set(v)) for k, v in interacotor.items()}

# get length of list as a value in dictionary
new = {key:len(value) for key,value in Results.items()}


# sort a dictionary by key
class SortedDisplayDict(dict):
    def __str__(self):
        return "{" + ", ".join("%r: %r" % (key, self[key]) for key in sorted(self)) + "}"

# call SortedDisplayDict
onew = SortedDisplayDict(new)


# convert dict to dataframe and set key as index
newdf = pd.DataFrame.from_dict(onew, orient = "index")
# add columns name New
newdf.columns =["New"]

# sort by index
newdf =newdf.sort_index()


# create current column
current = []
length = 0

# for row in newdf['New'][1:]:
for row in newdf['New']:
    length += row
    current.append(length)

# insert 0 and remove the last one
current = [0] + current
current = current[:-1]

# add courrent columns to newdf
seriesCurrent = pd.Series(current)

newdf['Current'] = seriesCurrent.values


newdf.rename(columns={'Current':'Current UniProt accession numbers'}, inplace=True)
# newdf.columns = newdf.columns.str.replace('Current', 'Current UniProt accession numbers')

# set index name to Year
newdf.index.name = 'Year'


# plot a figure
# custom color
my_colors = ['#999CFC', '#FD9A9B']

newdf[['New','Current UniProt accession numbers']].plot(kind='bar', width=1.0, stacked=True, color=my_colors, edgecolor = "none", title = "Current and New UniProt accession numbers")

# datacursor(hover=True)


plt.show()

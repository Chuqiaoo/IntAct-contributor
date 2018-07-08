# intact-contributor

# Aim
 A gigurevto show the major contributors of new data in the IntAct database over time.
# Background
IntAct (http://www.ebi.ac.uk/intact) is a database of protein interactions. In computational terms one interaction is an edge between two nodes in a graph. Each node is a protein, each edge is a report of this protein interaction. The data in IntAct comes from the scientific literature. One paper might contribute a single interaction, or tens of thousands to the database.


# Minimum requirements
It should be possible to run the script on almost any computers where python 3 is installed. it also needs python dependencies,

**pandas**, [installation documentation](https://pandas.pydata.org/pandas-docs/stable/install.html), if you have pip installed, please run pip3 install pandas\
**matplotlib**, [installation documentation](https://matplotlib.org/users/installing.html).\


# Usage
Unzip the folder


**convert.py** - to convert a huge file from txt format to csv format\
**mycsv.csv** - a csv file as a result from convert.py\
**IntAct.py** - a python file which is implementing all functions to visualization data\



# Test

Run the script with provided mycsv file a figture will pop up to your screen.

![alt text](https://github.com/Chuqiaoo/intact-contributor/blob/master/result.png)


# Contributors
Aim and Backgroud are edited by Henning Hermjakob.

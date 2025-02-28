# -*- coding: utf-8 -*-
"""
Created on Mon Jun 08 19:03:27 2015

@author: Corinne
"""

# Magic commands!
# use the % sign
%ls
    # will list files in working directory
%pwd
    # print working directory
%cd data
    # move into data directory

"""
For loops and List review
"""

mylist = range(1,6)

for x in mylist:
    print x
    # iterating through something
    # x becomes each of the elements

[x*2 for x in mylist]
    # same as above except it put it in a list
    # expression OR function goes before the "for"
    # list comprehension must output a list

[len(str(x)) for x in mylist]
    # function that goes before for loop

# strings are just list containers
for x in 'hello'
    print x
    # h-e-l-l-o....

# make it a list comprehension
[x.upper() for x in 'hello']

# another way to do it...

newlist = []
for x in 'hello':
    newlist.append(x.upper())

f=open('airlines.csv', 'rU')
    # opens the file
    # second argument rU = read mode, Universal mode
        # diff OS have diff characters at the end of lines
        # rU converts all line endings to one universal thing
    # creates a file connection
    # if it can't find the file it will create an error
    # everything is case sensitive
    # have NOT read in the file, just created a pointer to the file

data = f.read()
    # really long string
f.close()
    # always close the connection

"""
a reminder about list splicing...
"""

# list slicing [start:end:stride]
    # start is INCLUSIVE
    # end is EXCLUSIVE

# another way to open the file
with open('airlines.csv', 'rU') as f:
    data = f.read()
    # context manager
    # automatically closes the file for you, so a bit nicer than using
        # the three lines of code to open, read, close

"""
Data File --> String --> List of Lists
"""

with open('airlines.csv', 'rU') as f:
    data = []
    for row in f:
        data.append(row)
        # when you iterate through a file connection, you are iterating
            # through rows (or lines)
        # each row is stored as a string in the list 'data'
        
# making a list comprehension
with open('airlines.csv', 'rU') as f:
    data = [row for row in f]

# splitting strings
'hello corinne'.split()
'hello,corinne'.split(',')
    # splits on commas tada
    # default is spaces

with open('airlines.csv', 'rU') as f:
    data = [row.split(',') for row in f]
    # TADA

# now do everything but more elegant
# will be mostly the same
# USE THIS ONE!!!!!!!!!!!!
import csv
with open('airlines.csv', 'rU') as f:
    data = [row for row in csv.reader(f)]
    # csv reader takes care of the splitting
    # drops new line characters

# want to separate data into two lists
# move header to another list

header = data[0]
data = data[1:]
    # slices the list and overwrites the original list


"""
EXERCISES:

1. Create a list containing the average number of incidents per year for each airline.
Example for Aer Lingus: (2 + 0)/30 = 0.07
Expected output: [0.07, 2.73, 0.23, ...]

2. Create a list of airline names (without the star).
Expected output: ['Aer Lingus', 'Aeroflot', 'Aerolineas Argentinas', ...]

3. Create a list (of the same length) that contains 1 if there's a star and 0 if not.
Expected output: [0, 1, 0, ...]

4. BONUS: Create a dictionary in which the key is the airline name (without the star)
   and the value is the average number of incidents.
Expected output: {'Aer Lingus': 0.07, 'Aeroflot': 2.73, ...}
"""

# be aware...
# if you have for x in data
# each x is a LIST TYPE
    # so doing data[x] will not work
# if you have for x in range(0,len(data))
# each x is an int
    # so doing data[x] will work

# Exercise 1

for x in range(0,len(header)):
    print str(x) + " - " + header[x]

incident = []
for row in data:
    incident.append(round((int(row[2])+int(row[5]))/float(30),2))

# using list comprehension
incident2 = [round((int(row[2])+int(row[5]))/float(30),2) for row in data]

# Exercise 2
# look up strip function

new_name =[]
for row in data:
    if row[0][-1]=="*":
        new_name.append(row[0].strip("*"))
    else:
        new_name.append(row[0])
    
# using list comprehension bc I forgot how strip worked
new_name2 = [row[0].strip("*") for row in data]

# Exercise 3

star = []

for row in data:
    if row[0][-1]=="*":
        star.append(1)
    else:
        star.append(0)

# Exercise 4

airline_incidents = dict(zip(new_name2, incident2))

        
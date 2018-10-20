#import csv library
import csv

#prompt user for file
electionfile = input("What file do you want? ")

#Open the chosen CSV
with open(electionfile) as csv.file:
    csvreader = csv.reader(csv.file, delimiter=",")

    #skip the header
    next(csvreader)

    #get total vote count and create a set of mayors
    total = 0
    mayor = set()
    for row in csvreader:
        total += 1
        mayor.add(row[2])

    #convert set to list to support indexing
    mayorlist = list(mayor)

    #create a list of votes by candidate
    mvotes = []

    #create vote count by candidate
    mtotal = 0

    #create an index counter for mayor list
    x = 0

    #iterate over entire list of candidates to get respective vote counts
    while x < len(mayorlist):
        # reset the file
        csv.file.seek(0)
        for row in csvreader:
            if row[2]==mayorlist[x]:
                mtotal += 1
        mvotes.append(mtotal)
        mtotal = 0
        x += 1

#turn the two lists into a dictionary

# mayordict = {}
# for i in range(len(mayorlist)):
#     mayordict[mayorlist[i]] = mvotes[i]

#print out the text and total votes
print("Election Results")
print("---------------------")
print("Total votes: " + str(total))
print("---------------------")

#print out the votes by candidate using while loop for mayorlist and mvotes lists
#I PROBABLY SHOULD HAVE USED DICTIONARIES!  HOPEFULLY MY 2 LISTS ARE ALL ORDERED PROPERLY.  I THINK THEY ARE...
y = 0
while y < len(mayorlist):
    print(str(mayorlist[y]) + ": " + "{:.1%}".format(float(float(mvotes[y])/float(total))) + " " +str(mvotes[y]))
    y += 1

#locate the index of the max value in mvotes
v = mvotes.index(max(mvotes))
#use the above index location in mvotes to correlate to mayorlist index
#AGAIN, I THINK I SHOULD HAVE USED DICTIONARIES!  HOPEFULLY MY 2 LISTS ARE ALL ORDERED PROPERLY.  I THINK THEY ARE...
print("---------------------")
print("Winner: " + str(mayorlist[v]))
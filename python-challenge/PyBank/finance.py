import csv
import numpy as np

finance_file = input("What file do you want? ")

with open(finance_file) as csv.file:
    csvreader = csv.reader(csv.file, delimiter=',')

    next(csvreader)

    months = 0
    revenue = 0
    change = []
    max = 0
    min = 0
    for row in csvreader:
        months += 1
        revenue += int(row[1])
        if int(row[1]) > int(max):
            maxmonth = row[0]
            maxrevenue = row[1]
            max = row[1]
        if int(row[1]) < int(min):
            minmonth = row[0]
            minrevenue = row[1]
            min = row[1]
        change.append(row[1])

change2 = []
for i in range(len(change)-1):
    difference = [int(change[i + 1]) - int(change[i])]
    change2.append(difference)

change3 = [np.abs(x) for x in change2]



print('Financial Analysis')
print('--------------------------')
print('Total Months: : ' + str(months))
print('Total Revenue: ' + str(revenue))
print('Average Revenue Change: ' + str(np.average(change3)))
print('Greatest Increase in Revenue: ' + str(maxmonth) + " " + str(maxrevenue))
print('Greatest Increase in Revenue: ' + str(minmonth) + " " + str(minrevenue))

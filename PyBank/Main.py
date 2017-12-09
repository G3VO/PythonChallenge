import csv
import os

csv_path = os.path.join('Downloads', 'budget_data_1.csv') 
with open(csv_path , 'r') as budget1_csv:
    budget1_csv_reader = list(csv.reader(budget1_csv))

 months = []
 revenue = []
 change_rev = []
    for row in budget1_csv_reader:
        months.append (row[0])
        revenue.append ((row[1]))
#budget_data1.csv.close()    
print(budget1_csv_reader)
print("\n")
print(revenue)

print('Total Months:',len(months) -1)

revenue_1 = int(revenue[1])
print('$',revenue_1)

revenue_ints = (revenue[1:])
print(revenue_ints)

rev_num = []
for i in range(len(revenue_ints)):
    #print(i)
    rev_num.append(int(revenue_ints[i]))
    
    
#checking integer values in the revenue list    
print(rev_num)    
    
#calcutating the change of revenue
diff_rev = 0
start_change = 0
rev_change = []

for i in range(len(rev_num)):
    diff_rev = rev_num[i] - start_change
    rev_change.append(diff_rev)
    
print(rev_change)    

#to find the average change find the sum of rev_change/len(rev_change)
average_revenue_change = sum(rev_change)/len(rev_change)
print('Average Revenue Change: $',round(average_revenue_change, 2))

#to find max apply sorted(rev_change)
greatest_increase = rev_change[-1]
print('Greatest Increase in Revenue:',greatest_increase)

greatest_decrease = rev_change[0]
print('Greatest Decrease in Revenue:',greatest_decrease)

______________________________________________________

import csv
import os

csv_path = os.path.join('Downloads', 'budget_data_2.csv') 
with open(csv_path , 'r') as budget2_csv:
    budget2_csv_reader = list(csv.reader(budget2_csv))

    months2 = []
    revenue2 = []
    change_rev2 = []
    for row in budget2_csv_reader:
        months2.append (row[0])
        revenue2.append ((row[1]))
#budget_data1.csv.close()    
print(budget2_csv_reader)
print("\n")
print(revenue2)
    
print('Total Months:',len(months2) -1)

#making a new list without the 1st element from the revenue list 
revenue2_ints = (revenue2[1:])
print(revenue2_ints)

#change revenue string values to integers
rev2_num = []
for i in range(len(revenue2_ints)):
    rev2_num.append(int(revenue2_ints[i]))
#checking integer values in the revenue list    
print(rev2_num)  

import numpy 
diff_rev2 = 0
start_change = 0
rev2_change = []

for i in range(len(rev2_num)):
 #diff_rev2 = numpy.diff(rev2_num)
    change = rev2_num[i] - start_change
    rev2_change.append(change)
    start_change = rev2_num[i]    
print('list of revenue 2 change:',rev2_change)
print('\n')
print('There are ',len(rev2_change), 'elements')
max_rev2_change = max(rev2_change)
print('max',max_rev2_change)
print('min',min(rev2_change))

#print(numpy.sum(rev2_change))
print('The len is =',len(rev2_change))
print('The sum of all change in revenue =',sum(rev2_change))

#to find the average change find the sum of rev_change/len(rev_change)

#import numpy 
average_revenue2_change = sum(rev2_change)/len(rev2_change)
print('Average Revenue Change: $',round((average_revenue2_change), 2))

higher_rev2_change = max(rev2_change)
index_high2 = rev2_change.index(higher_rev2_change)
high_month = months[index_high2]
print(high_month)

#to find max, min revenue
greatest_decrease2 = rev2_change[0]
print('Greatest Decrease in Revenue:',greatest_decrease2)

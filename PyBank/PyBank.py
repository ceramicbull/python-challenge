#!/usr/bin/env python
# coding: utf-8

#import OS and CSV modules
import os
import csv

#locate and name csv data
bank_csv = os.path.join("Resources", "budget_data.csv")

#establish variables
month_list=[]
profit_list=[]
change_list=[]
prev_profit=False
best_change=0
best_month=0
worst_change=0
worst_month=0

#open and sort results from csv with for loop
with open(bank_csv) as csv_file:
    csv_reader=csv.reader(csv_file, delimiter=",")
    #header row
    csv_header=next(csv_file)
    prev_profit 
    #loop to collect info in lists
    for row in csv_reader:
        #set previous profit on first iteration
        if prev_profit==False:
            prev_profit=int(row[1])
        #collect month
        month_list.append(row[0])
        #collect profit
        profit_list.append(int(row[1]))
    #determine change in profit
    for value in profit_list:
        if int(value)!=prev_profit:
            change_list.append(int(value)-prev_profit)
            prev_profit=int(value)
        
#Determine Results
#Total Quantity of Months
total_months=len(month_list)
#Total Profits
net_profit=sum(profit_list)
#Total Changes
net_change=sum(change_list)
#Average Change
avg_change=net_change/len(change_list)

#determine max and min change
for change in change_list:
    if best_change<int(change):
        best_month=change_list.index(change)
        best_change=int(change)
    elif worst_change>int(change):
        worst_month=change_list.index(change)
        worst_change=int(change)

#determine best and worst months
#remove first month from list of months for determining change
month_list.pop(0)
#best month now matches the index from the change list
best_month_str=month_list[best_month]
#ditto for worst month
worst_month_str=month_list[worst_month]

#Simultaneously Print/Write Results
#new line in f-string workaround via https://towardsdatascience.com/how-to-add-new-line-in-python-f-strings-7b4ccc605f4a
new_line = '\n'
with open('analysis/results.txt','w') as r:
    print(f'Financial Analysis{new_line}----------------------------{new_line}Total Months: {total_months}{new_line}Total: ${net_profit}{new_line}Average Change: ${round(avg_change,2)}{new_line}Greatest Increase in Profits: {best_month_str} (${best_change}){new_line}Greatest Decrease in Profits: {worst_month_str} ({worst_change})')
    r.write(f'Financial Analysis{new_line}----------------------------{new_line}Total Months: {total_months}{new_line}Total: ${net_profit}{new_line}Average Change: ${round(avg_change,2)}{new_line}Greatest Increase in Profits: {best_month_str} (${best_change}){new_line}Greatest Decrease in Profits: {worst_month_str} ({worst_change})')
#!/usr/bin/env python
# coding: utf-8

#import modules
import os
import csv

#locate and name csv data
election_csv = os.path.join("Resources", "election_data.csv")

#establish variables
candidate_list=[]
vote_list=[]
total_votes=0
most_votes=0
winner=0

#open and tabulate votes from csv with for loop
with open(election_csv) as csv_file:
    csv_reader=csv.reader(csv_file, delimiter=",")
    #header row
    csv_header=next(csv_file)
    
    for row in csv_reader:
        if row[2] in candidate_list:
            vote_list.append(row[2])
        else:
            candidate_list.append(row[2])
            vote_list.append(row[2])

#print results
#define total votes
total_votes=len(vote_list)
#new line in f-string workaround via https://towardsdatascience.com/how-to-add-new-line-in-python-f-strings-7b4ccc605f4a
new_line = '\n'
#simultaneously print to consule and write to text file
with open('analysis/results.txt','w') as r:
    #print/write total votes and lines
    print(f'Election Results:{new_line}-------------------------')
    r.write(f'Election Results:{new_line}-------------------------{new_line}')
    print(f'Total Votes: {total_votes}{new_line}-------------------------')
    r.write(f'Total Votes: {total_votes}{new_line}-------------------------')
    #for loop to print/write candidate results and percentages, and store in dictionary
    for candidate in candidate_list:
        cand_total=vote_list.count(candidate)
        cand_percent=float(cand_total/total_votes)*100
        if cand_total>most_votes:
            winner=candidate
            most_votes=cand_total
        print(f'{candidate}: {round(cand_percent,3)}% ({cand_total})')
        r.write(f'{new_line}{candidate}: {round(cand_percent,3)}% ({cand_total})')
    #print/write line, determine and print winner and final line
    print(f'-------------------------{new_line}Winner: {winner}{new_line}-------------------------')
    r.write(f'{new_line}-------------------------{new_line}Winner: {winner}{new_line}-------------------------')
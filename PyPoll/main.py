#!/usr/bin/env python
# coding: utf-8

# In[7]:


import os
import csv


csvpath=os.path.join('Resources','election_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    
#Variable

    votes = []
    county = []
    candidates = []
    khan = []
    correy = []
    li = []
    otooley = []


    for row in csvreader:
        votes.append(int(row[0]))
        county.append(row[1])
        candidates.append(row[2])

    
    total_votes = (len(votes))
    

#Vote_name

    for candidate in candidates:
        if candidate == "Khan":
            khan.append(candidates)
            khan_votes = len(khan)
        elif candidate == "Correy":
            correy.append(candidates)
            correy_votes = len(correy)
        elif candidate == "Li":
            li.append(candidates)
            li_votes = len(li)
        else:
            otooley.append(candidates)
            otooley_votes = len(otooley)
    
    
    
#Percentages
    khan_percent = round(((khan_votes / total_votes) * 100), 2)
    correy_percent = round(((correy_votes / total_votes) * 100), 2)
    li_percent = round(((li_votes / total_votes) * 100), 2)
    otooley_percent = round(((otooley_votes / total_votes) * 100), 2)
   
    
#Winner 
    if khan_percent > max(correy_percent, li_percent, otooley_percent):
        winner = "Khan"
    elif correy_percent > max(khan_percent, li_percent, otooley_percent):
        winner = "Correy"  
    elif li_percent > max(correy_percent, khan_percent, otooley_percent):
        winner = "Li"
    else:
        winner = "O'Tooley"

        
print(f'Financial Analysis'+'\n')
print(f'----------------------------')
print(f"Total Votes: $" +str(total_votes))
print(f'----------------------------'+'\n')
print(f"Khan: {khan_percent}% ({khan_votes})")
print(f"Correy: {correy_percent}% ({correy_votes})")
print(f"Li: {li_percent}% ({li_votes})")
print(f"O'Tooley: {otooley_percent}% ({otooley_votes})")
print(f'----------------------------')
print(f"Winner: {winner}")
print(f'----------------------------')


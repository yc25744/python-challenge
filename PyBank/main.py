#!/usr/bin/env python
# coding: utf-8

# In[19]:


import os
import csv 


csvpath=os.path.join('Resources','budget_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)
    
    month = []
    revenue = []
    revenue_diff = []
    monthly_change = []
    
#Months       
    for row in csvreader:
        month.append(row[0])
        revenue.append(row[1])
    
    
 #Revenue 
    revenue_int = map(int,revenue)
    total_revenue = (sum(revenue_int))
    

 #Avg Change
    i = 0
    for i in range(len(revenue) - 1):
        profit_loss = int(revenue[i+1]) - int(revenue[i])
        
 # append profit_loss
        revenue_diff.append(profit_loss)
    Total = sum(revenue_diff)
    
#print(revenue_change)
    monthly_change = Total / len(revenue_diff)
    
    
    
#Greatest Increase
    profit_increase = max(revenue_diff)
    k = revenue_change.index(profit_increase)
    month_increase = month[k+1]
    
#Greatest Decrease
    profit_decrease = min(revenue_diff)
    j = revenue_change.index(profit_decrease)
    month_decrease = month[j+1]


#Print Statements

print(f'Financial Analysis'+'\n')
print(f'----------------------------'+'\n')


print("Total months: " + str(len(month)))

print("Total Revenue: $ " + str(total_revenue))
      
print("Average change  : $" + str(monthly_change))

print(f"Greatest Increase in Profits: {month_increase} (${profit_increase})")

print(f"Greatest Decrease in Profits: {month_decrease} (${profit_decrease})")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





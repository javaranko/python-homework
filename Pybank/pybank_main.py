#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Import pathlib and set the file path
from pathlib import Path
import csv
csv_data = Path('./budget_data.csv')


# In[2]:


# Initialize list of records
records = []


# In[3]:


# Open the csv file as an object
with open(csv_data, 'r') as csvfile:
    # Pass in the csv file to the csv.reader() function
    #(with ',' as the delimiter/separator) and return the csvreader object
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the heder row first
    csv_header = next(csvreader)
    # Print the header
    #print(csv_header)
    
    #Append the column 'Average' to the header
    csv_header.append("Average")
    
    # Append the header to teh list of record
    records.append(csv_header)
    #print(csv_header)
    
    # Read each row of data after the header
    # for row in csvreader:
        
    net_profit = 0
    greatest_increase = 0
    date_greatincrease = str
    greatest_decrease = 0
    date_greatdecrease = str
    
    first_row = next(csvreader)
    month_count = 1
    net_profit = net_profit + int(first_row[1])
    previous_net = int(first_row[1])
    net_change_list = []
    
    #initialize greatest increase and decrease
    greatest_increase = int(first_row[1])
    date_greatincrease = str(first_row[0])
    greatest_decrease = int(first_row[1])
    date_greatdecrease = str(first_row[0])
    
    for row in csvreader:
        net_profit += int(row[1])
        month_count += 1
        net_change = int(row[1]) - previous_net
        previous_net = int(row[1])
                                         
        # Recording the change
        net_change_list = net_change_list + [net_change]
        month_change = month_count - 1
        
        #identififying the greatest increase and decrease
        if net_change > greatest_increase:
            greatest_increase = net_change
            date_greatincrease = str(row[0]) 
        elif net_change < greatest_decrease:
            greatest_decrease = net_change
            date_greatdecrease = str(row[0])
                         
        # print(net_change)
average_month_change = round(sum(net_change_list) / month_change,2)
# printing results
print()
print("Financial Analysis")
print("-------------------------------")
print("Total Months: ", month_count)
print("Total: $",net_profit)
print("Average Change: $",average_month_change)
print("Greatest Increase in Profits: ", date_greatincrease, " ($",greatest_increase,")")
print("Greatest Decrease in Profits: ", date_greatdecrease, " ($",greatest_decrease,")")

# Export the results to text file

from pathlib import Path
import csv
pybank_analysis = Path('./pybank_analysis.txt')

with open(pybank_analysis, 'w') as txt_file:
    txt_file.write(f"Financial Analysis\n")
    txt_file.write(f"------------------------------\n")
    txt_file.write(f"Total Months: {month_count}\n")
    txt_file.write(f"Total: $ {net_profit}\n")
    txt_file.write(f"Average Change: $ {average_month_change}\n")
    txt_file.write(f"Greatest Increase in Profits:  {date_greatincrease} ($ {greatest_increase})\n")
    txt_file.write(f"Greatest Decrease in Profits:  {date_greatdecrease} ($ {greatest_decrease})\n")
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# python-challenge
import os
import csv
from pathlib import Path

#file location
input_file = Path("python-challenge", "PyBank", "budget_data.csv")

#create list
total_months = []
total_profits = []
monthly_profit_change = []

#open csv in default reade mode
with open(input_file,newline="", encoding= utf-8") as budget:

    #store content in csvreader
    csvreader = csv.reader(budget,delimiter=",")
    
    #skip header
    header = next(csvreader)

    for row in csvreader:

        total_months.append(row[0])
        total_profit.append(int9row[1]))

    for i in range(len(total_profits)-1):

monthly_profit_change.append(total_profits[i+1]-total_profit[i])

#Obtain max and min of the montly profit change list
max_increase_value = max(montly_profit_change)
max_decrease_value - min(monthly_profit_change)

max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1

#print results

print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

output_file = Path("python-Challenge", "PyBank", "Financial_Analysis_summary.txt")

with open(output_file, "w") as file:

# Write methods to print to Financial_Analysis_Summary 
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

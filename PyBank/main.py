import os
import csv
file_path = "Resources/budget_data.csv"

with open(file_path, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    #skip the header row
    header = next(csvreader)
    
    #month names list (not an actual count)
    month_count = []
    #profit/loss amount
    monthly_profit = []
    #difference/month
    change_by_month = []
    
    #add to the month_count and monthly_profit lists by going through the csv sheet
    for row in csvreader:
        #add months
        month_count.append(row[0])
        #add Profit/Loss values
        monthly_profit.append(int(row[1]))
    #add the changes of each month to the change_by_month list
    for i in range(len(monthly_profit)-1):
        change_by_month.append(monthly_profit[i+1]-monthly_profit[i])
        
#calculate the greatest increase and decrease in profit      
greatest_increase = max(change_by_month)
greatest_decrease = min(change_by_month)

#Associate the greatest profit & loss with the month name & assign variable name for print use 
greatest_increase_month = change_by_month.index(max(change_by_month))+1
greatest_decrease_month = change_by_month.index(min(change_by_month))+1

#calculate and print results with an f-string
print(f"Months Considered:{len(month_count)}")
print(f"Net Profit of Period in ($): {sum(monthly_profit)}")
print(f"Average Monthly Variation in ($): {round(sum(change_by_month)/len(change_by_month))}")
print(f"Greatest Increase in ($): {month_count[greatest_increase_month]} - {(int(greatest_increase))}")
print(f"Greatest Decrease in ($): {month_count[greatest_decrease_month]} - {(int(greatest_decrease))}")

with open("Bank_Summary.", "w") as txt
    txt.write(f"Months Considered:{len(month_count)}")
    txt.write(f"Net Profit of Period in ($): {sum(monthly_profit)}")
    txt.writef"Average Monthly Variation in ($): {round(sum(change_by_month)/len(change_by_month))}")
    txt.write(f"Greatest Increase in ($): {month_count[greatest_increase_month]} - {(int(greatest_increase))}")
    txt.write(f"Greatest Decrease in ($): {month_count[greatest_decrease_month]} - {(int(greatest_decrease))}")
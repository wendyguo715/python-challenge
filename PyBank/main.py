import os
import csv

#Pull csv file
csvpath = os.path.join('Resources', 'budget_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
 
    month = 0
    net_amount = 0
    profit_losses_list = []
    date_list = []
    for row in csvreader:
        month = month + 1
        net_amount += int(row[1]) 
        profit_losses_list.append(int(row[1]))
        date_list.append(row[0])

ave_change = (profit_losses_list[-1] - profit_losses_list[0])/(month - 1)
max_value = max(profit_losses_list)
min_value = min(profit_losses_list)

max_index = profit_losses_list.index(max_value)
min_index = profit_losses_list.index(min_value)

print("Financial Analysis")
print(f"Total Months: {month}")
print(f"Total: ${net_amount}")
print(f'Average Change: ${ave_change}')
print(f'Greatest Increase in Profits: {date_list[max_index]} (${max_value})')
print(f'Greatest Decrease in Profits: {date_list[min_index]} (${min_value})')

output_path = os.path.join("output.csv")
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow("Financial Analysis")
    csvwriter.writerow(["Total Months: ",month])
    csvwriter.writerow(["Total: ",net_amount])
    csvwriter.writerow(["Average Change: ",ave_change])
    csvwriter.writerow(["Greatest Increase in Profits ",date_list[max_index],max_value])
    csvwriter.writerow(["Greatest Decrease in Profits ",date_list[min_index],min_value])
    


import os
import csv

# Define variables
total_months = 0
net_total_amount = 0
monthly_change = []
month_count = []
greatest_increase_month = 0
greatest_increase = 0
greatest_decrease_month = 0
greatest_decrease = 0

# CSV location
csvpath = os.path.join('Resources', 'budget_data.csv')

# Read csv file and specify read format
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
# Read the header and skip first row
    csv_header = next(csvreader)
    row = next(csvreader)
    
    # List of calcs, start from row 1 due to row 0 being header
    previous_row = int(row[1])
    total_months = total_months + 1
    net_total_amount = net_total_amount + int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]
    
    # Loop through csv for calcs, starting at row 1
    for row in csvreader:

        #Total number of months
        total_months = total_months + 1
    
         #Net amount profit/losses
        net_total_amount = net_total_amount + int(row[1])

        # Difference between current and previous month
        profit_loss_change = int(row[1]) - previous_row
        monthly_change.append(profit_loss_change)
        previous_row = int(row[1])
        month_count.append(row[0])
        
        # Greatest Increase
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]
            
        # Greatest Decrease
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]  
        
        # Calculate The Average & The Date
        average_change = sum(monthly_change)/ len(monthly_change)
    
    highest = max(monthly_change)
    lowest = min(monthly_change)

# Print Results
print(f"Financial Analysis")
print(f"---------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total_amount}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})")
print(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})")

# Location of txt file to write to
output_file = os.path.join('Analysis', 'Results.text')

# Open write file
with open(output_file, 'w',) as txtfile:

# Write to txt file
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_total_amount}\n")
    txtfile.write(f"Average Change: ${average_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})\n")
    txtfile.write(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})\n")
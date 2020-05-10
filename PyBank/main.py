# modules
import os
import csv

# Set path for file
csvpath = os.path.join('Resources', 'budget_data.csv')

# Define variables
total_months = 0
revenue = []
change = []
dates = []

# Read CSV file
with open(csvpath, newline="") as pybank:
    csv_reader = csv.reader(pybank, delimiter=',')
    csv_header = next(csv_reader)

    # Set first value
    value = 867884

    for row in csv_reader:
        revenue.append(int(row[1]))

        difference = int(row[1])-value
        change.append(difference)
        value = int(row[1])

        # Total Months
        dates.append(row[0])
        total_months += 1
    
    # Remove First Change because null
    change.pop(0)

    # Total Profit
    net_total_profit = sum(revenue)

    # Average Change
    average_change = sum(change) / len(change)
    average_change = round(average_change, 2)

    # Greatest Increase
    greatest_increase = max(change)
    
    # Greatest Decrease
    greatest_decrease = min(change)
    
    # Month References
    decrease_ref = change.index(greatest_decrease) + 1
    increase_ref = change.index(greatest_increase) + 1

    # Print Statements
    print("Financial Analysis")
    print("-------------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${net_total_profit}")
    print(f"Average Change: ${average_change}")
    print("Greatest Increase in Profits: " + dates[increase_ref] + f" ${greatest_increase}")
    print("Greatest Decrease in Profits: " + dates[decrease_ref] + f" ${greatest_decrease}")

    # Output
    output = open("pybank_output.txt", "w")

    line1 = "Financial Analysis"
    line2 = "-------------------------------"
    line3 = str(f"Total Months: {total_months}")
    line4 = str(f"Total: ${net_total_profit}")
    line5 = str(f"Average Change: ${average_change}")
    line6 = str("Greatest Increase in Profits: " + dates[increase_ref] + f" ${greatest_increase}")
    line7 = str("Greatest Decrease in Profits: " + dates[decrease_ref] + f" ${greatest_decrease}")
    output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))
        



    
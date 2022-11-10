#Import os
import os
import csv

# Set relative path for csv file
csvpath = os.path.join("Resources", "budget_data.csv")

# Define variables starting points
total_months = 0
total_profits = 0
sum_of_change = 0
total_of_change = 0

dates = []
profits = []

# Read csv file
with open(csvpath, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read header row
    csv_header = next(csvreader)
    
    # Go to the first row
    first_row = next(csvreader)

    # Total month counter
    total_months += 1

    # Total profit and loss counter
    total_profits += int(first_row[1])
    sum_of_change = int(first_row[1])

    
    # Read the rows after the header row
    for row in csvreader:

        # Get the date
        dates.append(row[0])

        # Keep the the records of changes in rows
        total_of_change = int(row[1])-sum_of_change
        profits.append(total_of_change)
        sum_of_change = int(row[1])
           

        # Total number of months
        total_months += 1

        # Total of Profits/Losses
        total_profits= total_profits + int(row[1])

        # Average of change of "Profit/Losses"
        average_change = sum(profits)/len(profits)

  # The greatest increase in profits
    greatest_increase = max(profits)
    greatest_increase_output = profits.index(greatest_increase)
    greatest_increase_date = dates[greatest_increase_output]

    # The greatest decrease in profits
    greatest_decrease = min(profits)
    greatest_decrease_output = profits.index(greatest_decrease)
    greatest_decrease_date = dates[greatest_decrease_output]

#Make text file
file_to_save = os.path.join("analysis", "Financial_analysis.txt")
with open(file_to_save, "w") as txt_file:
    output = (
        f"Financial Analysis\n"
        f"----------------------------\n"
        f"Total Months: {str(total_months)}\n"
        f"Total: ${str(total_profits)}\n"
        f"Average Change: ${str(round(average_change,2))}\n"
        f"Greatest Increase in Profits: {greatest_increase_date} (${str(greatest_increase)})\n"
        f"Greatest Decrease in Profits: {greatest_decrease_date} (${str(greatest_decrease)})\n")
    print(output)
    txt_file.write(output)
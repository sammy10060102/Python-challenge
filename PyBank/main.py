import os
import csv

count = 0
nettotal = 0
monthA = 0
monthly_changes = []
total_monthly_changes = 0
dates = []

budget_data_csv = os.path.join("Resources", "budget_data.csv")

#open and read csv
with open(budget_data_csv) as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_reader)
    first_row = next(csv_reader)
    count = count + 1
    nettotal = int(first_row[1])
    monthA = int(first_row[1])

    for row in csv_reader:
        count = count + 1 
        nettotal= nettotal + int(row[1])
        monthB = int(row[1])
        monthlychange = monthB - monthA
        monthly_changes.append(monthlychange)
        dates.append(row[0])
        monthA = monthB

    for monthly_change in monthly_changes:
        total_monthly_changes = total_monthly_changes + monthly_change

    average_monthly_change = total_monthly_changes / len(monthly_changes)

    highest_monthly_change = max(monthly_changes)
    highest_change_index = monthly_changes.index(highest_monthly_change)
    highest_date = dates[highest_change_index]

    greatest_increase_losses = min(monthly_changes)
    greatest_decrease_index = monthly_changes.index(greatest_increase_losses)
    worst_date_losses = dates[greatest_decrease_index]

    line1 = "FINANCIAL ANALYSIS"
    line2 = "------------------------------------------------------------------------------------------"
    line3 = str(f"Total number of months:   {str(count)}")
    line4 = str(f"Total net Profit/Loss ${str(nettotal)}")
    line5 = str(f"Average monthly change  ${str(round(average_monthly_change,2))}")
    line6 = str(f"Greatest increase profit {highest_date} ${str(highest_monthly_change)}")
    line7 = str(f"Greatest increase Loss {worst_date_losses} ${str(greatest_increase_losses)}")

    print(line1)
    print(line2)
    print(line3)
    print(line4)
    print(line5) 
    print(line6)
    print(line7)

    # open a text file to write to 
    result = open("analysis/result.txt", "w")

    result.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))

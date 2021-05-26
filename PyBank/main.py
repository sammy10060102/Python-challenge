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

    average_monthly_change = total_monthly_changes / count

    highest_monthly_change = max(monthly_changes)
    highest_change_index = monthly_changes.index(highest_monthly_change)
    highest_date = dates[highest_change_index]

    greatest_increase_losses = min(monthly_changes)
    greatest_decrease_index = monthly_changes.index(greatest_increase_losses)
    worst_date_losses = dates[greatest_decrease_index]


    print("Financial Analysis")
    print("-------------------------")
    print("Total number of months: " + str(count))
    print("Total net Profit/Loss $" + str(nettotal))
    print("Average monthly change " + str(round(average_monthly_change,2))) 
    print(f"Greatest increase profit {highest_date} ${str(highest_monthly_change)}")
    print(f"Greatest increase Loss {worst_date_losses} ${str(greatest_increase_losses)}")
import os
import csv

budget_data_csv = os.path.join("Resources", "budget_data.csv")

#open and read csv
with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader, None)
    
    counter = 0

    for row in csv_reader:
        print(f"{row}")
        counter = counter + 1 
    
    print("total number of months: " + str(counter))
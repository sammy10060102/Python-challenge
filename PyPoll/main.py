import os
import csv

election_data = os.path.join("Resources", "election_data.csv")

#open and read csv
with open(election_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    for row in csv_reader:
        print("csv file display " + str(row))
import os
import csv

election_data = os.path.join("Resources", "election_data.csv")

#open and read csv
with open(election_data) as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_reader)

    count_votes = 0

#count total votes
    for row in csv_reader:
        count_votes += 1

    print ("Election Results")
    print ("---------------------------------")
    print ("Total Votes:  "  + str(count_votes))
    
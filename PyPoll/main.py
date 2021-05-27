import os
import csv

election_data = os.path.join("Resources", "election_data.csv")

#open and read csv
with open(election_data) as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_reader)

    total_votes = 0

    percentage = 0
    votes_per_candidate = []
    percentage_of_votes_per_candidate = []
    candidates_list = []
    
    

    #count total votes
    for row in csv_reader:

        total_votes += 1

        candidate = row[2]
        
        if not candidates_list.__contains__(candidate):
            # add new candidate to candidate list
            candidates_list.append(candidate)
            # add new index to array of votes per candidate
            votes_per_candidate.append(1)
        else:
            #get index of candidate
            candidate_index = candidates_list.index(candidate)
            #add vote to candidate 
            votes_per_candidate[candidate_index] += 1

    for votes in votes_per_candidate:
        #calculate the percentage of votes per candidate
        percentage = (votes / total_votes) * 100
        percentage_of_votes_per_candidate.append(percentage)

    #check highest vote
    highestCheck = votes_per_candidate[0]
    winning_candidate = ""
    winner = max(votes_per_candidate)
    #get index of highest vote
    index = 0
    index = votes_per_candidate.index(winner)
    #allocate winning candidate
    winning_candidate = candidates_list[index]

    line1 = "Election Results"
    line2 = "---------------------------------"
    line3 = "Total Votes:  "  + str(total_votes)
    line4 = "---------------------------------"
    line5 = "---------------------------------"
    line6 = "Winner: " + str(winning_candidate)
    line7 = "---------------------------------"

    print(line1)
    print(line2)
    print(line3)
    print(line4)
    for index in range(len(candidates_list)):
        print(f"{candidates_list[index]}: {round(percentage_of_votes_per_candidate[index], 3)}% ({votes_per_candidate[index]})")
    print(line5) 
    print(line6)
    print(line7)

    # open a text file to write to 
    result = open("analysis/result.txt", "w")

    result.write('{}\n{}\n{}\n{}'.format(line1,line2,line3,line4))
    for index in range(len(candidates_list)):
        result.write('\n{}'.format(f"{candidates_list[index]}: {round(percentage_of_votes_per_candidate[index], 3)}% ({votes_per_candidate[index]})"))
    result.write('\n{}\n{}\n{}'.format(line5,line6, line7))
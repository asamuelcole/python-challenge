# modules
import os
import csv

# Set path for file
csvpath = os.path.join('Resources', 'election_data.csv')

# Define variables
total_votes = 0
candidates_list = []
khan_list = []
correy_list = []
li_list = []
otooley_list = []

# Read File
with open(csvpath) as pypoll:
    csv_reader = csv.reader(pypoll, delimiter=',')
    csv_header = next(csv_reader)

    for row in csv_reader:
        # Total Votes
        total_votes += 1

        candidates_list.append(row[2])

    # Gather votes by candidate
    for candidate in candidates_list:
        if candidate == "Khan":
            khan_list.append(candidate)
        elif candidate == "Correy":
            correy_list.append(candidate)
        elif candidate == "Li":
            li_list.append(candidate)
        else:
            otooley_list.append(candidate)


        # Total votes by candidate
        votes_for_khan = len(khan_list)
        votes_for_correy = len(correy_list)
        votes_for_li = len(li_list)
        votes_for_otooley = len(otooley_list)

    # Percentages by candidates
    khan_percent = (votes_for_khan / total_votes) * 100
    khan_percent = round(khan_percent, 2)
    correy_percent = (votes_for_correy / total_votes) * 100
    correy_percent = round(correy_percent, 2)
    li_percent = (votes_for_li / total_votes) * 100
    li_percent = round(li_percent, 2)
    otooley_percent = (votes_for_otooley / total_votes) * 100
    otooley_percent = round(otooley_percent, 2)

    # Determine Winner
    if khan_percent > max(correy_percent, li_percent, otooley_percent):
        winner = "Khan"
    elif correy_percent > max(khan_percent, li_percent, otooley_percent):
        winner = "Correy"  
    elif li_percent > max(correy_percent, khan_percent, otooley_percent):
        winner = "Li"
    else:
        winner = "O'Tooley"

    # Print Statements
    print("Election Results")
    print("--------------------------")
    print(f"Total Votes: {total_votes}")
    print("--------------------------")
    print(f"Khan {khan_percent}% ({votes_for_khan})")
    print(f"Correy {correy_percent}% ({votes_for_correy})")
    print(f"Li {li_percent}% ({votes_for_li})")
    print(f"O'Tooley {otooley_percent}% ({votes_for_otooley})")
    print("--------------------------")
    print("Winner: " + winner)
    print("--------------------------")

    # Output
    output = open("pypoll_output.txt", "w")

    line1 = "Election Results"
    line2 = "--------------------------"
    line3 = str(f"Total Votes: {total_votes}")
    line4 = "--------------------------"
    line5 = str(f"Khan {khan_percent}% ({votes_for_khan})")
    line6 = str(f"Correy {correy_percent}% ({votes_for_correy})")
    line7 = str(f"Li {li_percent}% ({votes_for_li})")
    line8 = str(f"O'Tooley {otooley_percent}% ({votes_for_otooley})")
    line9 = "--------------------------"
    line10 = ("Winner: " + winner)
    line11 = "--------------------------"
    output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11))
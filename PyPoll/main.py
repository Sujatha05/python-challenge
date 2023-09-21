
# Import Libraries
import os
import csv

# Set File Path for Input and Output

csvpath = os.path.join('..','Resources', 'election_data.csv')
file_to_output = "Election_results.txt"


# Declaring the Variables 
total_votes = 0
candidates = []
candidate_votes = {}
winner_count = 0
winner = ""


# Open the File
with open('election_data.csv') as csvfile:
    csvreader = csv.DictReader(csvfile)
 
    #loop through to find the total votes
    #This loop will get the list of unique candidates and the dictionary with the candidate 
    # names and the corresponding votes
    for row in csvreader:

        # Find the total vote count
        total_votes += 1

        candidate = row["Candidate"]
        
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 0
        
        candidate_votes[candidate] = candidate_votes[candidate] + 1


#The below code will create the output

with open(file_to_output, 'w') as txt_file:
    #create header
    election_header = (
        f"Election Results\n\n"
        f"---------------------------\n")
    txt_file.write(election_header)
    print(election_header)
     #Total Votes
     
    Votes=(f"Total Votes : {total_votes}\n\n"
           f"---------------------------\n\n")
    print(Votes)
    txt_file.write(Votes) 

    
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = float(votes)/float(total_votes)*100
        if (votes > winner_count):
            winner_count = votes
            winner = candidate
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n\n"
        display=(f"---------------------------\n")
        print(voter_output)
        txt_file.write(voter_output)
        
        
    winning_summary = (
        f"Winner: {winner}\n"
    )
    print(display)
    txt_file.write(display)
    print(winning_summary)
    print(display)
    txt_file.write(winning_summary)
    txt_file.write(display)
    
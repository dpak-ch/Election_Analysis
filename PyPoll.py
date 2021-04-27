# Python practice reading csv files
# Election results analysis

import csv
import os

# Assign variable to open the file from a path
file_to_load = os.path.join('Resources','election_results.csv')

# Assign variable to save the file to a path
file_to_save = os.path.join('Analysis', 'election_analysis.txt')

# Variable for vote count
total_votes = 0

# Candidate list
candidate_options = []

# Candidate votes
candidates_votes = {}

# Using the with statement open the file as a text file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    print(headers)

    # Print each row in the CSV file.
    for row in file_reader:
        total_votes +=1

        candidate_name = row[2]
        
        if candidate_name not in candidate_options:
            # Add candidate name to list
            candidate_options.append(candidate_name)
            # initialize candidate vote count
            candidates_votes[candidate_name] = 0

        # Count candidate votes
        candidates_votes[candidate_name] += 1

winning_count = 0
winning_pct = 0
winning_candidate = ""
candidate_results = ""
winning_candidate_summary = ""

# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidates_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidates_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    
    vote_percentage = float(votes) / float(total_votes) * 100
    
    if (vote_percentage>winning_pct):
        winning_pct = vote_percentage
        winning_candidate = candidate_name
        winning_count = votes
            
    # 4. Print the candidate name and percentage of votes.
    print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
    candidate_results = (f"{candidate_results}\n{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
print(f"{winning_candidate} is the winner. She got {winning_count} votes which is ~{winning_pct:.1f}% of total votes")
winning_candidate_summary = (f"\nCandidate Name: {winning_candidate}\n\n% Votes: {winning_pct:.1f}\n")

election_results = (
    f"\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"-------------------------\n")
print(election_results,end="")
separator = "-------------------------\n"

with open(file_to_save,"w") as txt_file:
    txt_file.write(election_results)
    txt_file.write(candidate_results)
    txt_file.write(separator)
    txt_file.write(winning_candidate_summary)
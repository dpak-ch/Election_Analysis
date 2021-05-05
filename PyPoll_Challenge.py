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
candidate_options_list = []

# Candidate votes
candidate_votes_dict = {}

# Voter turnout
voter_count_dict = {}

# Using the with statement open the file as a text file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Skip past header row
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        total_votes +=1

        candidate_name = row[2]
        county = row[1]

        # Initialize dictionary with county and voter count 
        if county not in voter_count_dict:
            voter_count_dict[county] = 0
        
        # Populate candidate options list
        if candidate_name not in candidate_options_list:
            # Add candidate name to list
            candidate_options_list.append(candidate_name)
            # initialize candidate vote count
            candidate_votes_dict[candidate_name] = 0

        # Count candidate votes
        candidate_votes_dict[candidate_name] += 1

        # Count votes by county
        voter_count_dict[county] +=1


# Print Overall election results
separator = "-------------------------"
print("Election Results")
print(f"{separator}")
print(f"Total votes: {total_votes:,}")
print(f"{separator}\n")

# ------------------------------------------------------------
# County calculations and print
#-------------------------------------------------------------

county_votes_int = 0
county_votepct_float = 0.0
largest_turnout_int = 0
largest_county = ""
county_results = ""

print('County Votes: ')

# Determine stats by county
for county in voter_count_dict:
    county_votes_int = voter_count_dict[county]
    county_votepct_float = county_votes_int / total_votes * 100
    if (county_votes_int > largest_turnout_int):
        largest_turnout_int = county_votes_int
        largest_county = county
    print(f"{county}: {county_votepct_float:.1f}% ({county_votes_int:,})")
    county_results = (f"{county_results}\n{county}: {county_votepct_float:.1f}% ({county_votes_int:,})\n")
print(f"\n{separator}")
print(f"Largest County Turnout: {largest_county}")
print(f"{separator}\n")

# ------------------------------------------------------------
# Candidate calculations
#-------------------------------------------------------------

winning_count = 0
winning_pct = 0
winning_candidate = ""
candidate_results = ""
winning_candidate_summary = ""


# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes_dict:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes_dict[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    
    if (vote_percentage>winning_pct):
        winning_pct = vote_percentage
        winning_candidate = candidate_name
        winning_count = votes

    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    candidate_results = (f"{candidate_results}\n{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

print(f"\n{separator}")
print(f"Winner: {winning_candidate}")
print(f"Winning Vote Count: {winning_count:,}")
print(f"Winning Percentage: {winning_pct:.1f}%")
print(f"{separator}")
winning_candidate_summary = (f"Winner: {winning_candidate}\n\nWinning Vote Count: {winning_count:,}\n\nWinning Percentage: {winning_pct:.1f}%")

with open(file_to_save,"w") as txt_file:
    txt_file.write("Election Results")
    txt_file.write(f"\n{separator}")
    txt_file.write(f"\nTotal votes: {total_votes:,}")
    txt_file.write(f"\n{separator}")
    txt_file.write("\nCounty Results:\n")
    txt_file.write(county_results)
    txt_file.write(f"\n{separator}")
    txt_file.write(f"\nLargest County Turnout: {largest_county}")
    txt_file.write(f"\n{separator}\n")
    txt_file.write("Candidate Results:\n")
    txt_file.write( candidate_results)
    txt_file.write(f"{separator}\n")
    txt_file.write("Winning Candidate Summary:\n")
    txt_file.write(f"{separator}\n")
    txt_file.write(winning_candidate_summary)
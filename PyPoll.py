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
            candidate_options.append(candidate_name)

print(candidate_options)
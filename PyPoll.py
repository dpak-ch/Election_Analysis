# Python practice reading csv files
# Election results analysis

import csv
import os

# Assign variable to open the file from a path
file_to_load = os.path.join('Resources','election_results.csv')

# Assign variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_load, "r") as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    print(headers)

    # # Print each row in the CSV file.
    # for row in file_reader:
    #     print(row)

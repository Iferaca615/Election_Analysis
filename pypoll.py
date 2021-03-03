# The data we need to retrieve
# 1. total num of votes cast
# 2. Complete list of candidates who recived votes
# 3. the percentage of votes each candidate won
# 4. the total num of votes each candidate won
# 5. the winner of the election based on popular vote


import csv
import os
# Assign a var. for the file to load and the path.
file_to_load = os.path.join('Resources', 'election_results.csv')
# Open the election results and read the file.
with open(file_to_load) as election_data:
# to-do preform analysis 
# Read the file pbject with the reader function
    file_reader = csv.reader(election_data)

    # Read and Print the Header row.
    headers = next(file_reader)
    print(headers)


# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")
# # Using the open() function with the "w" mode will write data to the file.
# open(file_to_save, 'w')

# # Using the with statement open the file as a text file
# with open(file_to_save,'w') as txt_file:
#     # Write some data to the file.
#     txt_file.write("Counties in the Election\n-------------\nArapahoe\nDenver\nJefferson")





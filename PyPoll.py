

'''
Data needed to be retrieved:
1. total # of votes cast
2. list of candidates who received votes
3. percentage of votes each candidate won
4. total # of votes each candidate won
5. winner of election based on popular vote
'''

import csv # needed to pull from data file
import os # needed for directory path

# input data file path 
data_file_path = os.path.join('Resources', 'election_results.csv')

# output analysis file path
analysis_file_path = os.path.join('analysis', 'election_analysis.txt')


# open data file for read
with open(data_file_path) as election_data:

	# read the file 
	file_reader = csv.reader(election_data)
	
	headers = next(file_reader)

	
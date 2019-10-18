

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

# initialize total votes counter
total_votes = 0

# candidates and votes
candidate_options = []
candidate_votes = {}

# winning candidate and count tracker
winning_candidate = ''
winning_count = 0
winning_percentage = 0

# open data file for read
with open(data_file_path) as election_data:
	# create reader object
	file_reader = csv.reader(election_data)
	
	# read header row
	headers = next(file_reader)

	for row in file_reader:
		total_votes += 1 # increment total votes
		candidate_name = row[2]
		if candidate_name not in candidate_options: 
			# if it's a new candidate, add to list
			candidate_options.append(candidate_name)
			# begin tracking votes for candidate
			candidate_votes[candidate_name] = 0

		# increment this candidates # of votes
		candidate_votes[candidate_name] += 1

# open output file for write
with open(analysis_file_path, 'w') as output_file:
	election_results = (
		f'\nElection Results\n'
		f'--------------------\n'
		f'Total Votes: {total_votes:,}\n'
		f'--------------------\n')
	# save final vote count
	output_file.write(election_results)

	# go through candidates
	for candidate in candidate_votes:
		# retrieve vote count
		votes = candidate_votes[candidate]
		# calculate percentage
		vote_percentage = int(votes) / int(total_votes) * 100
		candidate_results = (
			f'{candidate}: {vote_percentage:.1f}% ({votes:,})\n')
		#save candidate's results
		output_file.write(candidate_results)


		# update winner trackers
		if (votes > winning_count) and (vote_percentage > winning_percentage):
			winning_count = votes
			winning_percentage = vote_percentage
			winning_candidate = candidate


	winning_candidate_summary = (
		f'-----------------------\n'
		f'Winner: {winning_candidate}\n'
		f'Winning Vote Count: {winning_count:,}\n'
		f'Winning Percentage: {winning_percentage:.1f}%\n'
		f'-----------------------\n')
	# save winning candidate's results
	output_file.write(winning_candidate_summary)





















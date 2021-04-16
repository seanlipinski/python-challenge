import os
import csv

votes = 0
winner_votes = 0
total_candidates = 0
greatest_votes = ["", 0]
candidate_options = []
candidate_votes = []

khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# set path for file
Election_data = os.path.join("Election_data.csv")

#Open the file using "write" mode. Specifically the variable to hold the contents
with open(Election_data, 'r') as csvfile:
	# Initialize csv.writer
	csvreader = csv.reader(csvfile, delimiter=',')

	for row in csvreader:
		votes = votes + 1
		
	#There are four candidates if the name is found, count the times it appears and store in a list
	if row[2] == "Khan":
		khan_votes += 1
	elif row[2] == "Correy":
		correy_votes += 1
	elif row[2] == "Li":
		li_votes += 1
	elif row[2] == "O'Tooley":
		otooley_votes += 1

 # To find the winner we want to make a dictionary out of the two lists we previously created 
candidates = ["Khan", "Correy", "Li","O'Tooley"]
votes = [khan_votes, correy_votes,li_votes,otooley_votes]

# We zip them together the list of candidate(key) and the total votes(value)
# Return the winner using a max function of the dictionary 
dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

# Print a the summary of the analysis
khan_percent = (khan_votes/votes) *100
correy_percent = (correy_votes/votes) * 100
li_percent = (li_votes/votes)* 100
otooley_percent = (otooley_votes/votes) * 100

# Print the summary table
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Khan: {khan_percent:.3f}% ({khan_votes})")
print(f"Correy: {correy_percent:.3f}% ({correy_votes})")
print(f"Li: {li_percent:.3f}% ({li_votes})")
print(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")

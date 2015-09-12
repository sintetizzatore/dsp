#The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.


import csv

def read_data(data):
	with open(data) as f:
		return [row for row in csv.DictReader(f)]

  def get_min_score_difference(self, parsed_data):
    # COMPLETE THIS FUNCTION

  def get_team(self, index_value, parsed_data):
    # COMPLETE THIS FUNCTION
    
    
# This is a different route using mapreduce

import csv

def read_data(data):
	with open(data) as f:
		return [row for row in csv.DictReader(f)]
		
def get_min_score_difference(self, mapreduce, extractor):
	row = mapreduce(self)
	return extractor(row)
	
def get_team(data, fdiff1, fdiff2, goal):
	self = read_data(data)
	return get_min_score_difference(self, lambda array: min(array, key=lambda x: abs(int(x[fdiff1]) - int(x[fdiff2]))), lambda row: row[goal])
	
if __name__ == '__main__':
	print(get_team('football.csv', 'Goals', 'Goals Allowed', 'Team'))
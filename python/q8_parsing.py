#The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.


import csv

  def read_data(data):
   # COMPLETE THIS FUNCTION

  def get_min_score_difference(self, parsed_data):
    # COMPLETE THIS FUNCTION

  def get_team(self, index_value, parsed_data):
    # COMPLETE THIS FUNCTION
    
    
# This doesn't complete functions above, but does answer the challenge:

import csv

def read_all(fname):
	with open(fname) as f:
		return [row for row in csv.DictReader(f)]

def mapreduceextract(data, mapreduce, extractor):
	row = mapreduce(data)
	return extractor(row)

def thisextract(fname, fdiff1, fdiff2, freport):
	data = read_all(fname)
	return mapreduceextract(data, lambda array: min(array, key=lambda x: abs(int(x[fdiff1]) - int(x[fdiff2]))), lambda row: row[freport])
        
if __name__ == '__main__':
	print(thisextract('football.csv', 'Goals', 'Goals Allowed', 'Team'))
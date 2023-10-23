#------------------------------------------------------------------------------------
#   This source code analyzes data to help a small, rural town modernize
#   its vote-counting process. It works with a datset called "election_data.csv" 
#   which is comprised of three columns:
#       Voter ID
#       County
#       Candidate
#
#   The values of interest include:
#       The total mumber of votes cast
#       A complete list of candidates who received votes
#       The percentage of votes each candidate won
#       The total number of votes each candidate won
#       The winner of the election based on popular vote
#
#   The results of this analysis will be printed to the screen as well as 
#   written to a text file called "polling_results.txt"
#
#   This code exercises reading in a csv file, writing to a text file and
#   the use of lists and dictionaries in Python
#--------------------------------------------------------------------------------------

import os
import csv

voting_csv = os.path.join("Resources", "election_data.csv")

# define a dictionary for a candidate list and correspong votes list
polling_dict = {}

# open voting_csv as csvfile:
with open(voting_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # recognize header row and skip
    next(csvreader, None)
    

    #---------------------------------------------------------------
    #  find unique candidate names and create the keys in dictionary
    #  while counting the number of votes (values) for each candidate 
    #---------------------------------------------------------------
    for row in (csvreader):
        this_candidate = row[2]
        if this_candidate in polling_dict:
            polling_dict[this_candidate] += 1               
        else:
            polling_dict.update({this_candidate:1})     

    # identify the list of keys and the list of values for easy analysis
    candidate_list = list(polling_dict.keys())
    votes_list = list(polling_dict.values())

    # determine the winning candidate by finding the maximum sum of votes
    maxvotes = max(polling_dict.values())
    max_index = votes_list.index(maxvotes)
    winning_candidate = candidate_list[max_index]
    
    # determine overall number of votes (this is also the number of rows minus the header)
    total_votes = sum(polling_dict.values())

    #----------------------------------------------------------------
    # create print lists for easy reference
    #----------------------------------------------------------------
    print_list_top = ["Election Results",
                    "----------------------------------",
                    "Total Votes:  " + str(total_votes),
                    "----------------------------------",]
    print_list_bottom = ["----------------------------------",
                        "Winner:  " + winning_candidate,
                        "----------------------------------"]
                          
    #--------------------------------------------------------------
    # loop through the print list - top and bottom - and print to screen
    #--------------------------------------------------------------
    for i in print_list_top:
        print(i)

    # loop through dictionary to figure individual data and print
    for key in polling_dict:
        votes = polling_dict.get(key)
        percentage_of_votes = round((votes / total_votes * 100), 3)
        
        print(key + ":  " + str(percentage_of_votes) + "%  (" + str(votes) + ")")

    for i in print_list_bottom:
        print(i)


#------------------------------------------------------------------
# create polling_results as a text file to write results
# this file will reside in the same folder as the source code
#------------------------------------------------------------------ 
output_file = os.path.join('analysis', 'polling_results.txt')
with open(output_file, "w", newline='') as polling_output:


#with open('analysis', 'polling_results.txt', 'w') as polling_output:
   
    #--------------------------------------------------------------
    # loop through the print list - top and bottom - and write results to text file
    #--------------------------------------------------------------
    for i in print_list_top:
        polling_output.write(i)
        polling_output.write("\n")
    
    # loop through dictionary to figure individual data and print
    for key in polling_dict:
        votes = polling_dict.get(key)
        percentage_of_votes = round((votes / total_votes * 100), 3)
        
        polling_output.write(key + ":  " + str(percentage_of_votes) + "%  (" + str(votes) + ")")
        polling_output.write("\n") 
    
    for i in print_list_bottom:
        polling_output.write(i)
        polling_output.write("\n")

   
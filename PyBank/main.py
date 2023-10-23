#---------------------------------------------------------------------------------
#   This source code analyzes the financial records of a company.
#   It works with a dataset called "budget_data.csv" which is composed
#   of two columns:
#           Date
#           Profit/Losses
#
#   The values of interest are the following:
#           The total number of months included in the dataset
#           The net total amount of "Profit/Losses" over the entire period
#           The changes in "Profit/Losses" over the entire period, and the average of those
#           The greatest increase in profits, both date and time, over the entire period
#           The greatest decrease in profits, both date and time, over the entire period
#
#   The results will be printed to the screen as well as written to a text file called
#   "financial_results.txt"
#
#   This code exercises reading in csv files, writing to text files, and the use
#   of lists in Python
#-----------------------------------------------------------------------------------

import os
import csv

# find budget_data.csv as the source code file file
financial_csv = os.path.join("Resources", "budget_data.csv")

# create a list for profit/loss and a list for the date
# these will serve for easily indexed data
profit_loss_list = []
date_list = []

# with open(udemy_csv, encoding='utf-8') as csvfile:
with open(financial_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # identify and skip the header row
    next(csvreader, None)

    #--------------------------------------------------------
    # set up variables and loop through the source data to fill
    # the list of profit/loss and associated date
    #--------------------------------------------------------
    total_movement = 0
    previous_profit_loss = 0
    for row in csvreader:
        total_movement = total_movement + int(row[1])
 
        profit_loss_list.append(int(row[1]))
        date_list.append(row[0])

    total_months = len(profit_loss_list)

    #--------------------------------------------------------
    # create a list that holds the CHANGE, or DELTA, from the previous entry
    #--------------------------------------------------------
    delta = []
    previous_profit_loss = 0
    for x in profit_loss_list:
        delta.append(x - previous_profit_loss)        
        previous_profit_loss = x

    # determine the greatest increase and decrease from the delta list
    greatest_increase = (max(delta))
    greatest_decrease = (min(delta))
    # determine the date of the greatest increase
    greatest_increase_index = delta.index(greatest_increase)
    greatest_increase_date = date_list[greatest_increase_index]
    # determine the date of the greatest decrease
    greatest_decrease_index = delta.index(greatest_decrease)
    greatest_decrease_date = date_list[greatest_decrease_index]
    
    # remember the first entry of the delta list doe not count toward the total change
    total_change = sum(delta) - delta[0]
    # find the average change in profit'loss
    average_change = (round(total_change / (len(delta) -1),2))

     #----------------------------------------------------------------
    # create print lists for easy, multiple reference
    #----------------------------------------------------------------
    print_list = ["Finanacial Ananlysis",
                    "-------------------------------",
                    "Total Months:  " + str(total_months),
                    "Total:  $" + str(total_movement),
                    "Average Change:  $" + str(average_change),
                    "Greatest Increase in Profits:  " + str(greatest_increase_date) + "  ($" + str(greatest_increase) + ")",
                    "Greatest Decrease in Profits:  " + str(greatest_decrease_date) + "  ($" + str(greatest_decrease) + ")"]

    #--------------------------------------------------------------
    # loop through the print list to print to screen
    #--------------------------------------------------------------
    for i in print_list:
        print(i)                
    
    # open financial_results.txt to write results to a file
    output_file = os.path.join('analysis', 'financial_results.txt')
    with open(output_file, "w", newline='') as financial_output:
    #with open('financial_results.txt', 'w') as financial_output:
       
        #--------------------------------------------------------------
        # loop through the print list to write to the results file
        #--------------------------------------------------------------
        for line in print_list:
            financial_output.write(line)
            financial_output.write("\n")

    
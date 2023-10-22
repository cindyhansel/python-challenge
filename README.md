# python-challenge
Module 3 challenge

This repository contains all files and folders for the Python challenge in Module 3

Two main source files are used for this challenge.
  One is contained in a folder called PyBank and 
  another is contained in a folder called PyPoll

Each main source will use a csv source file from a "Resources" folder
contained in it's repective folders, PyBank and PyPoll.

When each main runs, the results output will be printed to the screen
as well as written to a text file. These text files will be located in a folder
called "analysis" under the same folder as the "Resources" and source code folder.

The PyBank main source code will analyze the financial records of a company. 
The dataset is composed of two columns: "Date" and "Profit/Losses."

  This main will find the following values:
    The total number of months included in the dataset
    The net total amount of "Profit/Losses" over the entire period
    The changes in "Profit/Losses over the entire period, then the average of those changes
    The greatest increase in porfits, both the date and amount, over the entire period
    The greatest decrease in profits, both the date and amount, over the entire period

The PyPoll main source code will analyze a set of poll data in order to modernize a small,
rural vote-counting process. The dataset is composed of three columns which are the "Voter ID",
"County" and "Candidate."

  This main will calculate and report the following values:
    The total number of votes cast
    A complete list of candidates who received votes
    The percentage of votes each candidate won
    The total number of votes each candidate won
    The winner of the election based on popular vote

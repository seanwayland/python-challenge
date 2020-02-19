import os
import csv


#The total number of votes cast

totalVotes = 0.0

#A complete list of candidates who received votes

candidatesDictionary = {}

currentCandidate = ""
currentVotes = 0.0

#The percentage of votes each candidate won

#The total number of votes each candidate won

#lsThe winner of the election based on popular vote.

with open('election_data.csv', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        currentCandidate = row[0]
        currentVotes = float(row[2])

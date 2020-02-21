import os
import csv
from collections import Counter


#The total number of votes cast

totalVotes = 0.0

#A complete list of candidates who recls
# eived votes

candidatesArray = []

currentCandidate = ""
currentVotes = 0.0

firstBool = True

#The percentage of votes each candidate won

#The total number of votes each candidate won

#lsThe winner of the election based on popular vote.

with open('election_data.csv', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:

        if (firstBool == True):
            firstBool = False
        else:
            currentCandidate = row[2]
            candidatesArray.append(currentCandidate)
#candidatesDict = Counter(candidatesArray)
candidatesDict = {}
for i in candidatesArray:
  candidatesDict[i] = candidatesDict.get(i, 0) + 1
  

for j in candidatesDict:
    totalVotes += candidatesDict[j]

print(f'total votes recieved: {totalVotes} ')

winnerVal = 0
winner = ""
print("candidates list: ")
for key,val in candidatesDict.items():
    print(key)

print("")
for key,val in candidatesDict.items(): 
   

    print(f' {key}  : recieved {val*100/totalVotes}  percent and total votes {val}')
    if ((val/totalVotes) > winnerVal):
        winnerVal = val/totalVotes
       # print(winnerVal)
        winner = key

print(f'winner = {winner} ')



            



import os
import csv


# Lists to store data

#The total number of months included in the dataset
totalMonths = 0.0

#The net total amount of "Profit/Losses" over the entire period
profit = 0.0
#The average of the changes in "Profit/Losses" over the entire period
monthlyProfitChange = 0.0
monthlyProfitAverage = 0.0
#The greatest increase in profits (date and amount) over the entire period
greatestIncrease = 0.0
#The greatest decrease in losses (date and amount) over the entire period
greatestDecrease = 0.0 
totalMonthlyChange = []
storeProfit = 0.0
firstBool = True
increaseIndex = ""
decreaseIndex = ""
valOne = ""


# with open(udemy_csv, newline="", encoding='utf-8') as csvfile:
with open('budget_data.csv', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:

        # skip first row 
        if (firstBool == True) :
            firstBool = False 
            
        else :

            val = float(row[1])
        
            totalMonths += 1  
            profit += val # add profit to total 
            if totalMonths > 1: 
                monthlyProfitChange = val - storeProfit
                totalMonthlyChange.append(monthlyProfitChange)
            #print(f"mpc {monthlyProfitChange} tmc {totalMonthlyChange}")
            
            ## check if value is greatest or lowest increase 
            if (monthlyProfitChange > greatestIncrease) : 
                greatestIncrease = monthlyProfitChange
                increaseIndex = row[0]
            if (monthlyProfitChange < greatestDecrease) :
                greatestDecrease = monthlyProfitChange  
                decreaseIndex = row[0]
            storeProfit = val      

    
    #calculate average change 
monthlyProfitAverage = round(sum(totalMonthlyChange)/(totalMonths-1),2)

## print output to terminal

print(f"Total Months: {totalMonths} Total: ${profit} Average Change: ${monthlyProfitAverage}  Greatest Increase in Profits: {increaseIndex} : ${greatestIncrease} Greatest Decrease in Profits: {decreaseIndex} :${greatestDecrease}")


# print out put to file 
f = open("myResults.txt","w") 
f.write("\nTotal Months: ")
f.write(str(totalMonths))
f.write("\nTotal Profit: ")
f.write(str(profit))
f.write("\nAverage Change: ")
f.write(str(monthlyProfitAverage))
f.write("\nGreatest Increase month : ")
f.write(str(increaseIndex))
f.write("\nGreatest Increase : ")
f.write(str(greatestIncrease))
f.write("\nGreatest Decrease month : ")
f.write(str(decreaseIndex))
f.write("\nGreatest Decrease  : ")
f.write(str(greatestDecrease))
f.close()
import os
import csv

#Creating a path for the CSV file (I ha to use my entire file path)
csv_location = os.path.join("C:\\Users\\ayoat001\\Documents\\USC Data Analytics Bootcamp\\Module 2 - Python\\Homework","budget_data.csv")

#Creating starting variables
totalMonths = 0
totalPL = 0
prevPL = 0
PLChange = 0
maxInc = ['', 0]
maxDec = ['', 0]
PLChangeHold = []

# Using a with statement to open the budget file
with open(csv_location, newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=",")
 

    for row in csv_reader:
#Total months calculation
        totalMonths = totalMonths + 1
        # print(f'total months = {totalMonths}')
    #Total PL calculation. must transform values into integers
        totalPL = totalPL + int(row['Profit/Losses'])
        # print(f'Total : ${totalPL}')
    #PL Change calculation. must transform values into integers
        PLChange = int(row['Profit/Losses']) - prevPL
        prevPL = int(row['Profit/Losses'])
        # print(f'{PLChange}')

    #Adding PLChange calculations to the empty list created above 
        PLChangeHold.append(PLChange)

    
        if (PLChange > maxInc[1]):
            maxInc[1] = PLChange
            maxInc[0] = row['Date']   
        # print(f'Greatest Increase in Profits: {maxInc}')

        if (PLChange < maxDec[1]):
            maxDec[1] = PLChange
            maxDec[0] = row['Date'] 
    # print(f'Greatest Decrease in Profits: {maxDec}')

#calculating average PL and rounding to 2 decimal points
    avgPL = round((sum(PLChangeHold) - PLChangeHold[0]) / (len(PLChangeHold) - 1), 2)
    # print(f'Average Change : ${avgPL}')

    
    Summary = f"Financial Analysis\n\
    ------------------------------\n\
    Total Months: {totalMonths}\n\
    Total: ${totalPL}\n\
    Average Change: ${avgPL}\n\
    Greatest Increase in Profit: {maxInc}\n\
    Greatest Decrease in Profit: {maxDec})\n"

    print(Summary)
  
output_path = os.path.join('C:\\Users\\ayoat001\\Documents\\USC Data Analytics Bootcamp\\Module 2 - Python\\Homework', 'PyBank_Analysis.txt')

with open(output_path, 'w', newline='') as datafile:
    
    datafile.write(Summary)
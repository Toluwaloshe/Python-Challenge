import os
import csv

#Creating a path for the CSV file (I had to use my entire file path)
csv_location = os.path.join("C:\\Users\\ayoat001\\Documents\\USC Data Analytics Bootcamp\\Module 2 - Python\\Homework","election_data3.csv")

# Using a with statement to open the election file
with open(csv_location) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)

#Creating a list of lists, listing out each row in the CSV
    csv_data = [row for row in csv_reader]
    # print(f'This is the data {csv_data}')

#Taking count of the total votes
    totalVotes = len(csv_data)-1
    # print(f'Total Votes = {totalVotes}')

#Defining a function so that I dont have to rewrite several lines of code for each candidate
    def votes_per_candidate(candidate):
        a = 0
        for c in csv_data:
            if c[2] == candidate:
                a = a + 1
#This exits the function and starts from the beginning
        return a

 #Calculating total votes for each candidate   
    khanVotes = votes_per_candidate("Khan")
    # print(f'Votes for Khan : {khanVotes}')

    correyVotes = votes_per_candidate("Correy")
    # print(f'Votes for Correy : {correyVotes}')

    liVotes = votes_per_candidate("Li")
    # print(f'Votes for Li : {liVotes}') 

    otooleyVotes = votes_per_candidate("O'Tooley")
    # print(f"Votes for O'Tooley : {otooleyVotes}")   

#Calculating percentage of votes per candidate
    khanPercentage = 100*(round((khanVotes / totalVotes) , 2))
    # print(khanPercentage)

    correyPercentage = 100*(round((correyVotes / totalVotes) , 2))
    # print(correyPercentage)

    liPercentage = 100*(round((liVotes / totalVotes) , 2))
    # print(liPercentage)

    otooleyPercentage = 100*(round((otooleyVotes / totalVotes) , 2))
    # print(otooleyPercentage)

#Summary

    Summary = f"Election Results\n\
    ------------------------------\n\
    Total Votes: {totalVotes}\n\
    -------------------------------\n\
    Khan: {khanPercentage}%  ({khanVotes})\n\
    Correy: {correyPercentage}% ({correyVotes})\n\
    Li: {liPercentage}% ({liVotes})\n\
    O'Tooley: {otooleyPercentage}% ({otooleyVotes})\n\
    -------------------------------\n\
    Winner: Khan\n"

print(Summary)

output_path = os.path.join('C:\\Users\\ayoat001\\Documents\\USC Data Analytics Bootcamp\\Module 2 - Python\\Homework', 'PyPoll_Analysis.txt')

with open(output_path, 'w', newline='') as datafile:
    
    datafile.write(Summary)
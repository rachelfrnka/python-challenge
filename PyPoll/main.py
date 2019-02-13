import os
import csv

file_path = "Resources/election_data.csv"

#set the vote count for each equal to 0
Khan = 0
Li = 0
Correy = 0
OTooley = 0
total_votes = 0

with open(file_path ,"r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    #skip the header row
    header = next(csvreader) 
    #set up if statements to add to the vote counts if the conditions are met
    for row in csvreader:
        total_votes += 1
        if row[2] == "Khan":
            Khan += 1
        elif row[2] == "Correy":
            Correy +=1
        elif row[2] == "O'Tooley":
            OTooley +=1
        elif row[2] == "Li":
            Li +=1
    
 
#calculate the percentage for each candidate
percent_correy = (Correy/total_votes)*100
percent_tooley = (OTooley/total_votes)*100
percent_khan = (Khan/total_votes)*100
percent_li = (Li/total_votes)*100


#Print results
print("Election Results")
print(f"Total Votes: {total_votes}")
print(f"Khan: {percent_khan:f}% ({Khan})")
print(f"Correy: {percent_correy:f}% ({Correy})")
print(f"Li: {percent_li:f}% ({Li})")
print(f"O'Tooley: {percent_tooley:f}% ({OTooley})")


with open("Election_Results_Summary.txt", "w") as txt
    txt.write("Election Results")
    txt.write(f"Total Votes: {total_votes}")
    txt.write(f"Khan: {percent_khan:f}% ({Khan})")
    txt.write(f"Correy: {percent_correy:f}% ({Correy})")
    txt.write(f"Li: {percent_li:f}% ({Li})")
    txt.write(f"O'Tooley: {percent_tooley:f}% ({OTooley})")
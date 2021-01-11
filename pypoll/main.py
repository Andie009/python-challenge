import os
import csv

#Note column headers  
#voter_id = row 0
#country = row1
#candidate = row2

#Create empty dictionary to hold candidate info
candidates = {}

#Open and read in csv file
csvpath = os.path.join('Resources','election_data.csv')
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:

        #Loop through values from row 2, add one to skip header, if it is one, ignore
        if row[2] in candidates.keys():
            candidates[row[2]] = candidates[row[2]] + 1
        else:
            candidates[row[2]] = 1

        #Total votes
        total = candidates.values()
        total_votes = sum(total)

         #List candidate names   
        list_candidates = candidates.keys()

         #Votes for each candidate   
        votes_per = [f'{(x/total_votes)*100:.1f}%' for x in candidates.values()]
            
        #Winning candidate
        winner = list(candidates.keys())[list(candidates.values()).index(max(candidates.values()))]
        winner
        

# Print results
print("Election results")
print("--------------------------------")
print(f" Total votes: {int(total_votes)}")
print("---------------------------------")
i = 0
for candidate, vote in candidates.items():
    print(f'{candidate}, {vote} , {votes_per[i]}') 
    i+=1
print("------------------------------")
print(f" Winner: {winner}")
print("------------------------------")

# Location of txt file to write to
output_file = os.path.join('Analysis', 'Results.text')

# Open write file
with open(output_file, 'w',) as txtfile:

# Write results to txt file
    txtfile.write(f"Election Results\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write(f"---------------------------\n")
    i = 0
    for candidate, vote in candidates.items():
        txtfile.write(f"{candidate}, {vote} , {votes_per[i]}\n") 
        i+=1
    txtfile.write(f"---------------------------\n")
    txtfile.write(f" Winner: {winner}\n")
    txtfile.write(f"---------------------------\n")

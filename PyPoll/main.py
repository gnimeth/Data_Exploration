#Import os
import os
import csv

# Set relative path for csv file
csvpath = os.path.join("Resources", "election_data.csv")

#Define values
votes = {}
total_votes = 0

most_candidate_count = 0
most_candidate_name = ""

with open(csvpath, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read header row
    csv_header = next(csvreader)

    # Loop through the data
    for row in csvreader:

      number_of_votes = row[2]

      total_votes = total_votes + 1

      if number_of_votes in votes:
        votes[number_of_votes] = votes[number_of_votes] + 1
      else:
        votes[number_of_votes] = 1


#for winner
for key, value in votes.items():

  if value > most_candidate_count:
      most_candidate_name = key
      most_candidate_count = value

#Make text file
file_to_save = os.path.join("analysis", "election_analysis.txt")
with open(file_to_save, "w") as txt_file:
    output = "Election Results\n-------------------------\n"
    print(output)
    txt_file.write(output)

    output = f"Total Votes: {total_votes}\n-------------------------\n"
    print(output)
    txt_file.write(output)
    
    for key, value in votes.items():
        if value > most_candidate_count:
          most_candidate_name = key
          most_candidate_count = value
        
        output = f"{key} {round((value / total_votes)*100,3)}% ({value})"
        print(output)
        txt_file.write(output + '\n')
  

    print(f'-------------------------\nWinner: {most_candidate_name}\n-------------------------')
    txt_file.write(f'-------------------------\nWinner: {most_candidate_name}\n-------------------------')
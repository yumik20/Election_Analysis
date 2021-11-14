import csv
import os
#Assign a variable for the file to load and the path. 
file_to_load = os.path.join("Resources","election_results.csv")
#Open the election results and read the file. 
with open(file_to_load, "r") as election_data: 
    #to do: perform analysis.
    print(election_data)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
#using the open() function with the"w" mode we will write data to the file. 
with open(file_to_save, "w") as txt_file:
    #write some data to the file 
    txt_file.write("Counties in the Election\n--------------------------")
    #write tree counties to the file. 
    txt_file.write("\nArapahoe\nDenver\nJefferson")

#Open the election results and read the file. 
with open(file_to_load) as election_data:

    #to do: read and analyze the data here. 
    #read the file object with the reader function. 
    file_reader =csv.reader(election_data)
   
    #print the haeder row. 
    headers =next(file_reader)
   
    #print each row in the csv file.
    for row in file_reader:
      print(row)
    #read the file object with the reader function. 
    file_reader =csv.reader(election_data, delimiter=",")

#Add our dependencies 
import csv
import os 
#Assign a variable to load a file from a path 
file_to_load =os.path.join("Resources","election_results.csv")
#Assign a variable to save the file to a path.
file_to_save =os.path.join("analysis","election_analysis.txt")

#1 Initialize a total vote counter.
total_votes = 0 


#Candidate Options 
candidate_options= []

#1.Declare the empty dictionary. 
candidate_votes = {}

#Winning Candidate and Winning Count Tracker 
winning_candidate = " "
winning_count =0 
winning_percentage = 0 



#Open the election results and read the file 
with open(file_to_load, "r") as election_data:
    file_reader = csv.reader(election_data)

    #Read the header row. 
    headers = next (file_reader)

#Print each row in the CSV file. 
    for row in file_reader:
    #2. Add to the total vote count 
        total_votes += 1

    #Print the candidate name from each row. 
        candidate_name = row[2]
        #if the candidate does not match any existing candidate... 
        if candidate_name not in candidate_options:
            #Add candidate name to the candidate list. 
            candidate_options.append(candidate_name)

            #2. Begin tracking that candidate's vote count. 
            candidate_votes[candidate_name] = 0

        #Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1 

        

#Print the candidate vote dictionary.
print(candidate_votes)
print()

#print the candidate list
print(candidate_options)
print()


#3. Print the total votes.
print(total_votes)
print()

with open(file_to_save, "w") as txt_file:
#determin the percentage of votes for each candidate by looking through the counts. 
#1. interate through the candidate liost. 


# Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
# Save the final vote count to the text file.
    txt_file.write(election_results)
    for candidate_name in candidate_votes:
        
        #2. Retrieve vote count of a candidate. 
        votes = candidate_votes[candidate_name]
        #3. Calculate the percentage of the votes. 
        vote_percentage = float(votes) / float(total_votes) * 100

        candidate_results =(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Save the results to our text file.



        
        print(candidate_results)

        txt_file.write(candidate_results)
    txt_file.write (f"-------------------------\n")




#To do: print out each candidate's name, vote count, and percentage of #votes to the terminal.

# Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
             winning_count = votes
             winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
             winning_candidate = candidate_name

     
    #print out each candidate's name, vote count, and percentage of
# votes to the terminal 
             print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)

         
    


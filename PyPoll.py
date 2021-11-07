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
    print(headers)

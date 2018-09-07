import os
import csv
import pandas as pd
   
csvpath = os.path.join("Election_Data.csv")

with open(csvpath, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    data = pd.read_csv(csvfile) 
    
    Total = int(data.index.size)
    print("Election Results")
    print("-----------------------------------")
    print("Total Votes : ", str(Total))
    print("-----------------------------------")

    candi_name = data["Candidate"].unique()
    candi_count = data.groupby("Candidate")
    candidate_count = candi_count.agg({'Voter ID':"count"})["Voter ID"].tolist()

    percentage = []
    for i in range(len(candidate_count)):
        percentage.append((candidate_count[i]/Total))
    lst = []
    for i in range(len(candidate_count)):
        x= candi_name[i] + ": " + str("{:.2%}".format(percentage[i])) + " (" + str(candidate_count[i]) + ")"
        print(x)
        lst.append(x)

    candidate_winner = candi_count.agg({'Voter ID':"count"}).sort_values(by = "Voter ID", ascending=False )

    print("-------------------------------------")
    print("Winner : ", candidate_winner.index[1])

    f = open("Election_Results.txt" , "w")
    f.write("Election Results"+ "\n")
    f.write("Total Votes : "+ str(Total) + "\n")
    f.write("-------------------------------------"+ "\n")
    f.write(lst[0] + "\n")
    f.write(lst[1] + "\n")
    f.write(lst[2] + "\n")
    f.write(lst[3] + "\n")
    f.write("-------------------------------------" + "\n")
    f.write("Winner : "+ candidate_winner.index[1] + "\n")
    f.write("-------------------------------------" + "\n")
    f.close()

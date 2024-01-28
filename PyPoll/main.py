import os
import csv
csvpath = os.path.join("Resources","election_data.csv")
print("Election Results \n-------------------------")
with open(csvpath, encoding='UTF-8') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')
     next(csvreader)
     votes = 0
     totalvotes1 = 0
     totalvotes2 = 0
     totalvotes3 = 0
     winner = ''
     for row in csvreader:
         votes += 1
         if row[2] == "Charles Casper Stockham":
             totalvotes1 += 1
             charles = row[2]
             percentByCharles = totalvotes1 / votes * 100
         if row[2] == "Diana DeGette":
             totalvotes2 += 1
             diana = row[2]
             percentByDiana = totalvotes2 / votes * 100
         if row[2] == "Raymon Anthony Doane":
             totalvotes3 += 1
             raymon = row[2]
             percentByRaymon = totalvotes3 / votes * 100
         if totalvotes1 > totalvotes2 and totalvotes3:
             winner = 'Charles Casper Stockham'
         if totalvotes2 > totalvotes1 and totalvotes3:
             winner = 'Diana DeGette'
         if totalvotes3 > totalvotes1 and totalvotes2:
             winner = 'Raymon Anthony Doane'
    print(f"Total Votes: {votes}")
    print(f"-------------------------")
    print(f"{charles}: %{percentByCharles:.3f} ({totalvotes1})")
    print(f"{diana}: %{percentByDiana:.3f} ({totalvotes2})")
    print(f"{raymon}: %{percentByRaymon:.3f} ({totalvotes3})")
    print(f"-------------------------")
    print(f"Winner: {winner}")
    print(f"-------------------------")
beginningRows()
getAnalysis()

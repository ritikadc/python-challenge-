import os
import csv


csvpath = os.path.join("Resources","election_data.csv")
writtencsvpath = os.path.join("analysis", "results.csv")


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
     
line0 = ("Election Results")
line1 = ("-------------------------")
line8 = (f"Total Votes: {votes}")
line9 = ("-------------------------")
line2 = (f"{charles}: %{percentByCharles:.3f} ({totalvotes1})")
line3 = (f"{diana}: %{percentByDiana:.3f} ({totalvotes2})")
line4 = (f"{raymon}: %{percentByRaymon:.3f} ({totalvotes3})")
line5 = ("-------------------------")
line6 = (f"Winner: {winner}")
line7 = ("-------------------------")


print(f"Total Votes: {votes}")
print("-------------------------")
print(f"{charles}: %{percentByCharles:.3f} ({totalvotes1})")
print(f"{diana}: %{percentByDiana:.3f} ({totalvotes2})")
print(f"{raymon}: %{percentByRaymon:.3f} ({totalvotes3})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

with open(writtencsvpath, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")
    csvwriter.writerow([f"{line0} \n{line1} \n{line8} \n{line9} \n{line2} \n{line3} \n{line4} \n{line5} \n{line6} \n{line7}"])

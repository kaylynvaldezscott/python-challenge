import os
import csv

#declare and initialize variables
totVotes = 0
Candidate = []
Candidate_Votes1 = 0
Candidate_Votes2 = 0
Candidate_Votes3 = 0
oldCandidate = ""
newCandidate = ""
WINNER = ""

with open("election_data.csv") as fin:
  headerline = next(fin)
  for row in csv.reader(fin):
      #current row data
      tempCANDIDATE = str(row[2])

      if tempCANDIDATE == "Charles Casper Stockham":
         Candidate_Votes1 += 1
      elif tempCANDIDATE == "Diana DeGette":
         Candidate_Votes2 += 1
      else:
         Candidate_Votes3 += 1

      totVotes += 1
      
print("Election Results")
print("---------------------------")
print(f"Total Votes: {totVotes}")
print("---------------------------")
Can1 = str("Charles Casper Stockham: ")
Can2 = str("Diana DeGetti: ")
Can3 = str("Raymon Anthony Doane: ")
Perc1 = Candidate_Votes1 * 100 / totVotes
Perc2 = Candidate_Votes2 * 100 / totVotes
Perc3 = Candidate_Votes3 * 100 / totVotes
print(Can1 + '%.3f' % Perc1 + f'% ({Candidate_Votes1})')
print(Can2 + '%.3f' % Perc2 + f'% ({Candidate_Votes2})')
print(Can3 + '%.3f' % Perc3 + f'% ({Candidate_Votes3})')

#determine winner
if (Perc1 > Perc2) and (Perc1 > Perc3):
   WINNER = Can1
if (Perc2 > Perc1) and (Perc2 > Perc3):
   WINNER = Can2
if (Perc3 > Perc2) and (Perc3 > Perc1):
   WINNER = Can3

print(f'Winner is: {WINNER}')  
# for x in listNames
#   print the name, location, percentage
#Export to text file
txtOUT = open("pyPoll.txt","w")

txtOUT.write("Election Results")
txtOUT.write("\n")
txtOUT.write("----------------------------")
txtOUT.write("\n")
txtOUT.write(f"Total Votes:   {totVotes}")
txtOUT.write("\n")
txtOUT.write(Can1 + '%.3f' % Perc1 + f'% ({Candidate_Votes1})')
txtOUT.write("\n")
txtOUT.write(Can2 + '%.3f' % Perc2 + f'% ({Candidate_Votes2})')
txtOUT.write("\n")
txtOUT.write(Can3 + '%.3f' % Perc3 + f'% ({Candidate_Votes3})')
txtOUT.write("\n")
txtOUT.write(f"Winner is: {WINNER}")
txtOUT.write("\n")

txtOUT.write("** end of output **")

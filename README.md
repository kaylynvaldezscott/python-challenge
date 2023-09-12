# python-challenge

Submitted by Kaylyn Valdez-Scott
Date: 11-SEP-2023
Project Title: Python Challenge

PyBank Description:

The purpose of this code is to analyze the records to calculate each of the following values:
- total number of months included in the dataset
- net total amount of "Profit/Losses" over the entire period
- the changes in "Profit/Losses" over the entire period, and then the average of those changes
- greatest increase in profits (date and amount) over the entire period
- greatest decrease in profits (date and amount) over the entire period

Enter script in to VSC:
import os
import csv

#define variables and initialize
pos_increase = 0; pos_date = str("")
neg_decrease = 0; neg_date = str("")
total_PL = 0; total_Months = 0

with open("budget_data.csv") as fin:
  headerline = next(fin)
  for row in csv.reader(fin):
      #current row data
      tempDATE = str(row[0]); tempPL   = int(row[1])
      total_PL += tempPL

      if tempPL > pos_increase:
         pos_increase = tempPL
         pos_date = tempDATE

      if tempPL < neg_decrease:
         neg_decrease = tempPL
         neg_date = tempDATE

      total_Months += 1

average_chg = total_PL / total_Months

print("Financial Analysis")
print("----------------------------")
print(f"Total Months:   {total_Months}")
print(f" Total:  ${total_PL}")

print(' Average Change: %.2f' % average_chg)
print(f" Greatest Increase in Profits: {pos_date} (${pos_increase})")
print(f" Greatest Decrease in Profits: {neg_date} (${neg_decrease})")
print("")
print("** end of output **")
#Export solution to text file
txtOUT = open("pyBank.txt","w")

txtOUT.write("Financial Analysis")
txtOUT.write("\n")
txtOUT.write("----------------------------")
txtOUT.write("\n")
txtOUT.write(f"Total Months:   {total_Months}")
txtOUT.write("\n")
txtOUT.write(f" Total:  ${total_PL}")
txtOUT.write("\n")
txtOUT.write(' Average Change: %.2f' % average_chg)
txtOUT.write("\n")
txtOUT.write(f" Greatest Increase in Profits: {pos_date} (${pos_increase})")
txtOUT.write("\n")
txtOUT.write(f" Greatest Decrease in Profits: {neg_date} (${neg_decrease})")
txtOUT.write("\n")
txtOUT.write("\n")
txtOUT.write("** end of output **")

End result will give you a txt file called pyBank.txt, which will give you a Financial Analysis of information read. 

PyPoll Description:

The purpose of this code is to analyze the records to calculate each of the following values:
- the total number of votes cast
- a complete list of candidates who received votes
- percentage of votes each candidate won
- total number of votes each candidate won
- winner of the election based on popular vote

Enter script in to VSC:
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

End result will give you a txt file called pyPoll.txt, which will give you a Financial Analysis of information read.

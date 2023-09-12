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

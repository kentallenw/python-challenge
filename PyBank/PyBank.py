import os
import csv

# Track various financial parameters
month_count = 0
change_month = []
net_change_list = []
largest_dec = ["",100000000000000000]
largest_inc = ["", 0]
total_net = 0

# Read CSV file
csvpath = os.path.join("downloads","budget_data.csv")

with open(csvpath, newline="") as csvfile:

# Specify delimiter and variable that hold contents
    csvreader = csv.reader(csvfile,delimiter=",")
    header = next(csvreader)    

# sum total dollars across all time periods
    print("Financial Analysis")
    print("--------------------------")

    total = 0
    aggregate = 0
    net_change = 0
    for row in csvreader:
        aggregate += int(row[1])
        total = total + 1
    print("Total Months: " + str(total))
    print("Total: $" + str(aggregate))

   

# >> append to two lists: both month and change from prior month
# starting row (0)
# reset calculation in current to prior and repeat
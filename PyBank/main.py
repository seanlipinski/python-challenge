# Import the os module
import os
#Module for reading csv file
import csv



#initialize variable to hold total months
Total_Months = []

#initialize variable to total Profit/losses
Total_Net_Amount = []

monthly_profit_change = []

prev_revenue = 0
revenue_change = 0 
greatest_increase = []
greatest_decrease = []

revenue_changes = []

#Path to collect data from the csv excel file
PyBank_csv = os.path.join('PyBank.csv')

#read in the csv file
with open(PyBank_csv, 'r') as csvfile:

	#Split the data on commas
	csvreader = csv.reader(csvfile, delimiter=',')

	header = next(csvreader)

	# loop through all the rows in PyBank.csv
	for row in csvreader:
		#incremtent Total months counter
		Total_Months.append(row[0])
		Total_Net_Amount.append(int(row[1]))
	
	# Iterate through the profits in order to get the monthly change in profits
	for i in range(len(Total_Net_Amount)-1):
	
		# Take the difference between two months and append to monthly profit change
		monthly_profit_change.append(Total_Net_Amount[i+1]-Total_Net_Amount[i])
	
	# Obtain the max and min of the the montly profit change list
	max_increase_value = max(monthly_profit_change)
	max_decrease_value = min(monthly_profit_change)


	# Correlate max and min to the proper month using month list and index from max and min
	#We use the plus 1 at the end since month associated with change is the + 1 month or next month
	max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
	max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 


	print()
	print()
	print()
	print("financial Analysis")
	print("------------------------------------------")
	print(f"Total_Months: {len(Total_Months)}")
	print(f"Total Revenue: ${sum(Total_Net_Amount)}")
	print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
	print(f"Greatest Increase in Profits: {Total_Months[max_increase_month]} (${(str(max_increase_value))})")
	print(f"Greatest Decrease in Profits: {Total_Months[max_decrease_month]} (${(str(max_decrease_value))})")

	# write results to csv
	
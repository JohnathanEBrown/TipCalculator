print('Welcome to the tip calculator.')

total_bill = float(input('What was the total bill? $')) 
#Store the value of bill

tip_percentage = int(input('What percentage tip would you like to give? 10, 12, or 15?'))
#record tip amount

dinner_group = int(input('How many people split the bill?'))
#record number of people splitting the bill

bill_with_tip = tip_percentage / 100 * total_bill + total_bill

bill_per_person = bill_with_tip / dinner_group

final_amount = '{:.2f}'.format(bill_per_person)


print(f'Each person should pay: ${final_amount}')

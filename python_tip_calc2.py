total_bill_amt = float(input ('What is total bill amount? '))
service = input ('How was your service? ')
split_bill = int (input ('How many ways split bill? '))
if service == 'good':
    tip_amt = (total_bill_amt * .2)
elif service == 'fair':
    tip_amt = (total_bill_amt * .15)
elif service == 'bad':
    tip_amt = (total_bill_amt * .10)
print(tip_amt)
tip_total = (total_bill_amt + tip_amt)
print(tip_total)
print(tip_total / split_bill)
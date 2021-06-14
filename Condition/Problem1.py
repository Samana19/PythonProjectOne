'''Price of a house is $1M.
If buyer has good credit,
they need to put down 10%
otherwise
they need to put down 20%.
Print the down payment.'''
PriceOfHouse=1000000
good_credit=True
if good_credit:
    DownPayment=0.1*PriceOfHouse
else:
    DownPayment=0.2*PriceOfHouse
print(f"The  down payment is ${DownPayment}")
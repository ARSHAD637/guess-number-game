amount = int(input("enter the amount:"))
if amount >10000:
    discount = amount*0.3
elif amount >5000:
    discount = amount*0.2
elif  amount > 1000:
    discount = amount*0.1
else:
    discount = 0 

final_amount = ( amount - discount)
print(f'Amount ={amount}')
print(f'Discount = {discount}')
print(f'Final price = {final_amount}')
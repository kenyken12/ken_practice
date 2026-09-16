print("**********BREW&BYTE*************\n")

#input from customer
name = input("hello!, can i get your name?:  ").title().strip()
order = input("what can I get for you?:  ").strip()

#taxes, tips allat
total = 5
tax = total * 0.0625
tip = total * 0.18
newTotal = total + tax + tip 

#item code 
itemCode = f"{order[:3]}-{len(order)}"

print(f"CUSTOMER: {name}\nORDER: {order}\nITEM CODE: {itemCode}\nTOTAL - {round(newTotal, 2)}\n")

print("**********GOODBYE*************")






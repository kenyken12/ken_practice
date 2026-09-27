
inventory = {
    "laptops": 5,
    "mouses": 12,
    "keyboards": 7,
    "headphones": 10
}

item = input("what do you want to buy?: ")


      
if item == "laptops":

       quantity = int(input(f"how many do you want? ({inventory[item]} left:) "))
       if quantity > inventory[item]:
              print("we dont have enough sorry!")
       
       else:
              print(f"purchased {quantity} {item}!")
              inventory["laptops"] -= quantity                     

elif item == "mouses":
       quantity = int(input(f"how many do you want? ({inventory[item]} left:) "))
       if quantity > inventory[item]:
              print("we dont have enough sorry!")
       
       else:
              print(f"purchased {quantity} {item}!")
              inventory["mouses"] -= quantity

elif item == "keyboards":
       quantity = int(input(f"how many do you want? ({inventory[item]} left:) "))
       if quantity > inventory[item]:
              print("we dont have enough sorry!")
       else:
              print(f"purchased {quantity} {item}!")
              inventory["keyboards"] -= quantity

elif item == "headphones":
       quantity = int(input(f"how many do you want? ({inventory[item]} left:) "))
       if quantity > inventory[item]:
              print("we dont have enough sorry!")
              
       else:
              print(f"purchased {quantity} {item}!")
              inventory["headphones"] -= quantity

else:
       print("we do not have that...")


print(inventory)

for i in inventory:
      if inventory[i] < 5:
            print(f"{i} are low on stock!")



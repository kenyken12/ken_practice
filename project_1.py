
inventory = {
    "laptops": 5,
    "mouses": 12,
    "keyboards": 7,
    "headphones": 10
}

item = input("what do you want to buy?: ")

if item == "laptops":
    quantity = int(input("how many do you want?: "))
    if quantity > inventory["laptops"]:
           print("we dont have enough sorry!")
    else:
            inventory["laptops"] -= quantity

elif item == "mouses":
    quantity = int(input("how many do you want?: "))
    if quantity > inventory["mouses"]:
           print("we dont have enough sorry!")
    else:
            inventory["mouses"] -= quantity

elif item == "keyboards":
    quantity = int(input("how many do you want?: "))
    if quantity > inventory["keyboards"]:
           print("we dont have enough sorry!")
    else:
            inventory["keyboards"] -= quantity

elif item == "headphones":
    quantity = int(input("how many do you want?: "))
    if quantity > inventory["headphones"]:
           print("we dont have enough sorry!")
    else:
            inventory["headphones"] -= quantity

else:
      print("wtf u talm bout")

print(inventory)

for i in inventory:
      if inventory[i] < 5:
            print(f"{i} are low on stock!")



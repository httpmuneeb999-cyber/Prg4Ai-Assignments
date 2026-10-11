                     

 
names = {1: "Bubble", 2: "macroni", 3: "loaded fries", 4: "champagne"}
prices = {1: 500, 2: 800, 3: 250, 4: 1500}

print("Menu")
for number in names:
    print(number, names[number], "Rs", prices[number])

def calculate_price(price, quantity):
    return price * quantity

file = open("orders.txt", "w")
file.write("Orders:\n")
file.write("Item\tQuantity\tPrice\n")

final_bill = 0
choice = input("Select an item number (0 to finish) : ")

while choice != "0":
    number = int(choice)
    if number in names:
        quantity = int(input("Enter the quantity : "))
        item_price = calculate_price(prices[number], quantity)
        final_bill += item_price
        print("Item:", names[number], "Quantity:", quantity, "Price:", item_price)
        file.write(names[number] + "\t" + str(quantity) + "\t" + str(item_price) + "\n")
    else:
        print("invalid choice")
    choice = input("Select an item numbe from menu and press 0 to end this program: ")

print("finalbill", final_bill)
file.write("finalbill " + str(final_bill) + "\n")

file.close()


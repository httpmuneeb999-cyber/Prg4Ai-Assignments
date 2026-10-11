products = []
for i in range(5):
    product = {
        "name": input("enter the product name : "),
        "price": int(input("enter the price : ")),
        "quantity": int(input("enter the quantity : "))
    }
    products.append(product)

def calculate_bill(products):
    bill = 0
    for product in products:
        bill += product["price"] * product["quantity"]
    discount = 0
    if bill > 10000:
        discount = bill * 10 / 100
    final_bill = bill - discount
    return bill, discount, final_bill

bill, discount, final_bill = calculate_bill(products)

most_expensive = products[0]
for product in products:
    if product["price"] > most_expensive["price"]:
        most_expensive = product

file = open("bill.txt", "w")
file.write("Shopping Bill:\n")
file.write("Name\tPrice\tQuantity\tTotal\n")

for product in products:
    total_price = product["price"] * product["quantity"]
    print("Name:", product["name"], "Price:", product["price"],
          "Quantity:", product["quantity"], "Total:", total_price)
    file.write(product["name"] + "\t" + str(product["price"]) + "\t"
               + str(product["quantity"]) + "\t" + str(total_price) + "\n")

print("Bill:", bill)
print("Discount:", discount)
print("Final bill:", final_bill)
print("Most expensive product:", most_expensive["name"])

file.write(
    "Bill: " + str(bill) + "\n" +
    "Discount: " + str(discount) + "\n" +
    "Final bill: " + str(final_bill) + "\n" +
    "Most expensive product: " + most_expensive["name"] + "\n"
)
file.close()
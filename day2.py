# Problem: 
# Design a solution for a grocery store where the transactions are stored as list of string.
# Each string contains a Item name and an amount (positive for a sale, negative for a return).
# Write a Python function to create a dictionary that summarizes the total sales and returns for each product.
# Input List :
# transactions = [
# "Milk 100",
# "Curd -30",
# "Curd 100",
# "Soap 140",
# "Milk 140",
# "Soap -130",
# "Tomato 40"
# ]
# Expected Output :
# {
# "Milk ": {"total_sales": 240, "total_returns": 0},
# "Curd ": {"total_sales": 100, "total_returns": 30},
# "Soap ": {"total_sales": 140, "total_returns": 130},
# "Tomato ": {"total_sales": 40, "total_returns": 0},
# }


def grocery_details(grocery):
    grocery_dict={}

    # splitting the item and price from grocery list and storing it to variables
    for i in transactions:
        item,price=i.split()
        price=int(price)

        # Initialize item in gro_dict if not already present
        if item not in grocery_dict:
            grocery_dict[item] = {"total_sales": 0, "total_returns": 0}

        # Update total_sales or total_returns based on the price
        if price>0:
            grocery_dict[item]["total_sales"]+=price
        else:
            grocery_dict[item]["total_returns"]+=abs(price)
    print(grocery_dict)

transactions = [
"Milk 100",
"Curd -30",
"Curd 100",
"Soap 140",
"Milk 140",
"Soap -130",
"Tomato 40"
]

grocery_details(transactions)
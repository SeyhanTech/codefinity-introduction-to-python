# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100
print("Processing started.")
for item, stock in inventory.items():
    print(f"Processing {item}")
    while stock[0] < stock[1]:
        stock[0] += stock[2]
        if stock[1] > 100:
            stock[3] = True   
print("Processing completed")



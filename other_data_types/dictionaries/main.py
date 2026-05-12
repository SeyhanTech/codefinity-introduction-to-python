grocery_inventory = {"Milk": (113, "Diary"), "Eggs": (116,"Dairy"), "Bread": (117, "Bakery"), "Apples": (141, "Produce")}
bread_details = grocery_inventory["Bread"]
grocery_inventory["Cookies"] = (143, "Bakery")


print("Details of Bread:", bread_details)
print("Inventory after adding Cookies:", grocery_inventory)

grocery_inventory.pop("Eggs")
print("Inventory after removing Eggs:", grocery_inventory)
# 1. Real-World Python Dictionary Applications
# Task 1: Restaurant Menu Update
restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}
print(restaurant_menu)
restaurant_menu["Beverages"] = {"Coke": "3.99", "Fanta": "3.99"}
print(restaurant_menu)
restaurant_menu["Main Course"] = {"Steak" : 17.99}
print(restaurant_menu)
del restaurant_menu["Starters"]["Steak"]
print(restaurant_menu)


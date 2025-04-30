
inventory = {
    "apple": 10,
    "banana": 15,
    "orange": 20,
    "grape": 12
}


print("Current Inventory:")
for item, qty in inventory.items():
    print(f"{item.capitalize()}: {qty}")

item_name = input("\nEnter the item name to sell: ").lower()
sell_qty = int(input("Enter the quantity to sell: "))

if item_name in inventory:
    if inventory[item_name] >= sell_qty:
        inventory[item_name] -= sell_qty
        print(f"\nSold {sell_qty} {item_name}(s). Remaining stock: {inventory[item_name]}")
    else:
        print(f"\nNot enough {item_name}s in stock. Available: {inventory[item_name]}")
else:
    print(f"\nItem '{item_name}' not found in inventory.")

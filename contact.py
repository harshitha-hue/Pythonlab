
contacts = {
    "Alice": "123-456-7890",
    "Bob": "987-654-3210"
}
print("Current Contacts:")
for name, number in contacts.items():
    print(f"{name}: {number}")
name = input("\nEnter contact name: ").strip()
phone = input("Enter phone number: ").strip()
if name in contacts:
    print(f"\nUpdating {name}'s phone number from {contacts[name]} to {phone}.")
else:
    print(f"\nAdding new contact: {name}")

contacts[name] = phone
print("\nUpdated Contacts:")
for name, number in contacts.items():
    print(f"{name}: {number}")

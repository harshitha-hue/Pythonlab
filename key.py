
data = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "profession": "Engineer"
}
print("Available keys:", list(data.keys()))

key = input("Enter a key to look up its value: ")
try:
    value = data[key]
    print(f"The value for key '{key}' is: {value}")
except KeyError:
    print(f"KeyError: The key '{key}' does not exist in the dictionary.")

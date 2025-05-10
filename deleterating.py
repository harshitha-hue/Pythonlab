import pandas as pd
data = {
    'Order_ID': [101, 102, 103, 104, 105],
    'Customer_Name': ['Alice Johnson', 'Bob Smith', 'Charlie Brown', 'David Wilson', 'Eva Adams'],
    'Product': ['Laptop', 'Headphones', 'Smartphone', 'Tablet', 'Smartwatch'],
    'Category': ['Electronics', 'Accessories', 'Electronics', 'Electronics', 'Wearables'],
    'Price': [800, 50, 600, 300, 150],
    'Quantity': [1, 2, 1, 1, 1]
}
df = pd.DataFrame(data)
payment_methods = ['Credit Card', 'PayPal', 'Debit Card', 'Net Banking', 'UPI']
df.insert(2, 'Payment_Method', payment_methods)
df['Review_Rating'] = [4.5, 4.0, 3.8, 4.2, 4.7]
df.drop('Review_Rating', axis=1, inplace=True)
print(df)

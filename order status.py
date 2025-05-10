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
df['Order_Status'] = ['Shipped', 'Delivered', 'Pending', 'Shipped', 'Delivered']
print(df)

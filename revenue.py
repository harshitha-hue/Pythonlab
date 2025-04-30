import pandas as pd
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
          'September', 'October', 'November', 'December']

revenue = [5000, 5200, 4800, 5400, 5600, 5800, 6100, 5900, 6200, 6500, 7000, 6900]
revenue_series = pd.Series(revenue, index=months)
print("Monthly Advertising Revenue (USD):")
print(revenue_series)
print("\nTotal Annual Revenue:", revenue_series.sum(), "USD")
print("Average Monthly Revenue:", revenue_series.mean(), "USD")
print("Month with Highest Revenue:", revenue_series.idxmax())

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Generate random sales data
np.random.seed(0)  # For reproducibility
months = pd.date_range('2023-01-01', periods=12, freq='M')
sales = np.random.randint(1000, 5000, size=12)

# Create DataFrame
data = pd.DataFrame({'Month': months, 'Sales': sales})

# Step 2: Plot time-series data
plt.figure(figsize=(10, 6))
sns.lineplot(x='Month', y='Sales', data=data, marker='o', label='Sales')

# Step 3: Highlight maximum sales month
max_sales_month = data.loc[data['Sales'].idxmax()]
plt.annotate('Max Sales', xy=(max_sales_month['Month'], max_sales_month['Sales']),
             xytext=(max_sales_month['Month'], max_sales_month['Sales'] + 500),
             arrowprops=dict(facecolor='red', shrink=0.05))

# Step 4: Customize plot
plt.title('Monthly Sales Data')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)
plt.show()

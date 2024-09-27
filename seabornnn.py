import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Load the tips dataset
tips = sns.load_dataset('tips')

# Step 2: Create a bar chart showing average total bill per day
plt.figure(figsize=(8, 5))
sns.barplot(x='day', y='total_bill', data=tips, palette='coolwarm')

# Step 3: Customize the plot
plt.title('Average Total Bill Amount by Day')
plt.xlabel('Day of the Week')
plt.ylabel('Average Total Bill')
plt.grid(True)

plt.show()

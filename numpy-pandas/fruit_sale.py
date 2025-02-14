import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fruit_sale = np.random.randint(0, 100, (8, 3))

fruit_df = pd.DataFrame(
    fruit_sale,
    columns=["Apple", "Bananas", "Cherries"]
)

# Let's also label the rows as Day 1, Day 2, etc.
fruit_df.index = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7", "Day 8"]
print("\nFruit sales DataFrame:\n", fruit_df)

total_per_fruit = fruit_df.sum(axis=0)
print("\nTotal sales per fruit:\n", total_per_fruit)

total_per_day = fruit_df.sum(axis=1)
print("\nTotal sales per day:\n", total_per_day)

# Find the day with maximum total
best_day = total_per_day.idxmax()
print("\nDay with highest total sales:", best_day)

average_per_fruit = fruit_df.mean(axis=0)
print("\nAverage sales per fruit:\n", average_per_fruit)

# Create a new column "Total Sales" by summing across each row
fruit_df["Total Sales"] = fruit_df.sum(axis=1)
print(fruit_df)

# Plot the bar chart
total_per_fruit.plot(kind="bar")

plt.title("Total fruit sales")
plt.xlabel("Fruit Type")
plt.ylabel("Total Sales")
plt.show()




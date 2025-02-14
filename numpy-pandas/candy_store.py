import numpy as np


# 1. Let's simulate daily sales for 3 types of candies over 7 days
# We'll create a 2D array of random integers between 0 and 50
candy_sales = np.random.randint(0, 50, (7, 3))
print("Candy sales array (7 rows for days, 3 columns for candy types):\n", candy_sales)

# 2. Let's label them for our understanding (not in code, just conceptually):
# Columns: [Chocolate, Gummy Bears, Lollipops]

# 3. Sum up total sales for each candy type
# axis=0 means we sum down the rows
total_each_candy = candy_sales.sum(axis=0)
print("\nTotal sales for each candy type:\n", total_each_candy)

# 4. Sum up total sales per day
# axis=1 means we sum across each row
sales_per_day = candy_sales.sum(axis=1)
print("\nTotal sales per day:\n", sales_per_day)





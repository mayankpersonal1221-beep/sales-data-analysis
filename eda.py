import pandas as pd 
#Load the csv file
df = pd.read_csv("data/sales.csv")
print("original data:")
print(df)
# create total sales column 
df["TotalSales"] = df["Quantity"] * df["Price"]
# show updated data
print("\nData with TotalSales:")
print(df)
# cateogry wise sales calculation 
category_sales=df.groupby("Category")["TotalSales"].sum()
print("\nCateogry-wise Total sales:")
print(category_sales)
# now we plot a graph 
import matplotlib.pyplot as plt
category_sales.plot(kind="bar", title="Total sales by category")
plt.xlabel("category")
plt.ylabel("TotalSales")
plt.show()
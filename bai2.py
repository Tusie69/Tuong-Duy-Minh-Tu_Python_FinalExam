import pandas as pd

products = {
    "id": [1, 2, 3, 4, 5],
    "name": ["Laptop", "Mouse", "Keyboard", "Monitor", "USB"],
    "price": [800, 20, 150, 250, 15],
    "quantity": [5, 20, 10, 8, 30]
}

df = pd.DataFrame(products)

df.to_csv("products.csv", index=False)
print("Data saved to products.csv")

df = pd.read_csv("products.csv")

print("\n=== PRODUCT LIST ===")
print(df)

print("\n=== PRODUCTS WITH PRICE > 100 ===")
print(df[df["price"] > 100])

df["total"] = df["price"] * df["quantity"]

print("\n=== PRODUCT LIST AND TOTAL VALUE ===")
print(df)

total_inventory = df["total"].sum()

print(f"\nTotal Inventory Value: {total_inventory}")

df.to_csv("products.csv", index=False)

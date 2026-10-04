import csv
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 420,
    "GOOGL": 175,
    "AMZN": 190
}

portfolio = {}
total_investment = 0

while True:
    stock_name = input("Enter stock symbol (or 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))

        investment = stock_prices[stock_name] * quantity

        portfolio[stock_name] = quantity
        total_investment += investment

        print(f"{stock_name} added successfully!")
        print(f"Investment: ₹{investment}")
    else:
        print("Stock not available. Please try again.")

print("\n----- Portfolio Summary -----")

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity

    print(f"{stock}: {quantity} shares × ₹{price} = ₹{investment}")

print(f"\nTotal Investment: ₹{total_investment}")
with open("portfolio.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Stock", "Quantity", "Price", "Investment"])

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        investment = price * quantity

        writer.writerow([stock, quantity, price, investment])

    writer.writerow([])
    writer.writerow(["Total Investment", total_investment])

print("\nPortfolio saved to portfolio.csv")
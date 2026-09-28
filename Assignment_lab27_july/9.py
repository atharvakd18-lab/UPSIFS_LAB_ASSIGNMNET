# write a program to calculate profit or loss percentage based on cost price and selling price.
cost_price = float(input("Enter the cost price: "))
selling_price = float(input("Enter the selling price: "))

if selling_price > cost_price:
    profit = selling_price - cost_price
    profit_percentage = (profit / cost_price) * 100
    print("Profit percentage:", profit_percentage, "%")
elif selling_price < cost_price:
    loss = cost_price - selling_price
    loss_percentage = (loss / cost_price) * 100
    print("Loss percentage:", loss_percentage, "%")
else:
    print("No profit, no loss.")
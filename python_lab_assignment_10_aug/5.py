# Write a Python function generate_bill(*args, **kwargs) where *args contains item prices and **kwargs contains item names with their quantities. Calculate the total bill, total quantity, average price, apply a 10% discount if the bill exceeds ₹5,000, and display the final payable amount.
def generate_bill(*args, **kwargs):
    # Calculate total bill
    total_bill = sum(price * quantity for price, quantity in zip(args, kwargs.values()))
    
    # Calculate total quantity
    total_quantity = sum(kwargs.values())
    
    # Calculate average price
    average_price = total_bill / total_quantity if total_quantity else 0
    
    # Apply discount if bill exceeds ₹5,000
    if total_bill > 5000:
        discount = 0.1 * total_bill
        final_payable = total_bill - discount
    else:
        final_payable = total_bill
    
    # Display results
    print("Total Bill:", total_bill)
    print("Total Quantity:", total_quantity)
    print("Average Price:", average_price)
    print("Final Payable Amount:", final_payable)
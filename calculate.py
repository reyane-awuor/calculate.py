def calculate_discount(price, discount_percent):
    """Calculate the final price after applying a discount if applicable."""
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    else:
        return price


original_price = float(input("Enter the original price of the item: "))
discount = float(input("Enter the discount percentage: "))


final_price = calculate_discount(original_price, discount)
print(f"The final price after discount is: ${final_price:.2f}")
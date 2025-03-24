def calculate_discount(price, discount_percent):
    # Apply discount only if it's 20% or more
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price  # No discount applied

# Get user input
price = float(input("Enter the original price of the item in Ksh: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(price, discount_percent)

# Print results in Ksh
if discount_percent >= 20:
    print(f"Discount applied! Final price: Ksh {final_price:.2f}")
else:
    print(f"No discount applied. Original price: Ksh {price:.2f}")

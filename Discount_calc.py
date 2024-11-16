def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    return price

def get_valid_input(prompt, input_type=float, min_value=0):
    while True:
        try:
            user_input = input_type(input(prompt))
            if user_input < min_value:
                print(f"Please enter a value greater than or equal to {min_value}.")
            else:
                return user_input
        except ValueError:
            print(f"Invalid input. Please enter a valid {input_type.__name__}.")

# Prompt the user for input with validation
price = get_valid_input("Enter the original price of the item: $", float, min_value=0)
discount_percent = get_valid_input("Enter the discount percentage: ", float, min_value=0)

# Calculate the final price
final_price = calculate_discount(price, discount_percent)

# Display the result with formatted output
if final_price != price:
    print(f"\nDiscount Applied: {discount_percent}%")
    print(f"Original Price: ${price:.2f}")
    print(f"Final Price after {discount_percent}% discount: ${final_price:.2f}")
else:
    print(f"\nNo discount applied. The price remains: ${price:.2f}")

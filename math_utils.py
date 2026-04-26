def calculate_discount(price, discount_percentage):
    # BUG: Subtracting the percentage directly instead of calculating the fraction
    return price - discount_percentage

def process_payment(amount, fee_string):
    # BUG: Fails to cast fee_string to float before adding
    total = amount + float(fee_string)
    return total

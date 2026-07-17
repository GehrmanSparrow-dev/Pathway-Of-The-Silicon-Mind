def calculate_bill(item_prices, tax_rate=0.05, **kwargs):
    subtotal=sum(item_prices)

    # Apply each discount one after another
    # kwargs stores discounts as key-value pairs
    for discount_name, discount_rate in kwargs.items():
        subtotal -= subtotal * discount_rate
    total = subtotal + (subtotal * tax_rate)
    return f"Total amount: ${total:.2f}"
bill1 = calculate_bill([10.99, 5.50, 3.25])
bill2 = calculate_bill([20.00, 15.00], tax_rate=0.08, seasonal=0.10)
bill3 = calculate_bill([50.00, 25.00], loyalty=0.05, coupon=0.10)
print(bill1)
print(bill2)
print(bill3)

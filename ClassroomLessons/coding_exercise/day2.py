# day2.py
price_text = "49.99"
price = float(price_text)
tax = price * 0.12
total = price + tax

print("Price:", price)
print("Tax:", tax)
print("Total:", total)
print(type(price), type(tax), type(total))
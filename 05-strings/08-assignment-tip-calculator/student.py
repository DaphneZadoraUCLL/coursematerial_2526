def tip_calculator():
    price = int(input("Enter total price:"))
    tip = input("Enter tip percentage (default=20)")

    if tip == '':
        tip = 20
    else:
        tip = int(tip)

    total = round(price + (price / 100 * tip))
    print(f"You have to pay {total}")


tip_calculator()

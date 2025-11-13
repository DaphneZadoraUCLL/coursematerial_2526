def total_cost(amount):
    if amount < 100:
        return amount + 10
    if amount >= 200:
        return amount * 0.95
    if amount >= 100 and amount < 200:
        return amount


print(total_cost(50))
print(total_cost(150))
print(total_cost(500))

def coins(amount):
    coin_5 = amount // 5
    amount -= 5 * coin_5
    coin_2 = amount // 2
    amount -= 2 * coin_2
    coin_1 = amount
    return coin_5 + coin_2 + coin_1

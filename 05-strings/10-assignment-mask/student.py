def mask(password):
    length = len(password)
    return f'{'*'*length}'


print(mask('test'))

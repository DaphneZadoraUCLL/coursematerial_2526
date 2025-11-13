from math import ceil


def movie_ticket(duration, imax, student, ticket_count):
    if duration < 90:
        price = 10
    elif duration < 120:
        price = 11
    elif duration < 150:
        price = 12
    else:
        price = 15

    if imax is True:
        price = ceil(price * 1.2)
    if student is True:
        price -= 3

    return price * ticket_count


print(movie_ticket(70, False, False, 1))
print(movie_ticket(70, False, True, 1))
print(movie_ticket(70, False, True, 3))
print(movie_ticket(180, True, False, 2))

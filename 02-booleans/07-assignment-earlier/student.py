def earlier(h1, m1, h2, m2):
    time_1 = (h1 * 60) + m1
    time_2 = (h2 * 60) + m2
    return time_1 < time_2

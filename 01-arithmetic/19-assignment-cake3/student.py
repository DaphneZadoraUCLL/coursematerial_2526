def cake3(eggs, flour, butter, sugar):
    cakes_eggs = eggs // 5
    cakes_flour = flour // 250
    cakes_butter = butter // 200
    cakes_sugar = sugar // 250
    return min(cakes_eggs, cakes_flour, cakes_butter, cakes_sugar)

lijst = [1, 2, 53, -10, 2, 6, 3, 6, 8, 2, 5, 10]

def kwadraten_som(grond_getallen):
    res = 0
    for getal in grond_getallen:
        if getal > 0:
            res = res + getal ** 2
    return res


print(kwadraten_som(lijst))
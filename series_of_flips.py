from random import choice

def coin_flip():
    flip = ['H','T']
    return choice(flip)

def series_of_flips(n):
    flips = []
    for i in range(n):
        flips.append(coin_flip())
    return flips

print(series_of_flips(10))

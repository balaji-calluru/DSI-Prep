from random import choice

def coin_flip():
    flip = ['H','T']
    return choice(flip)

def series_of_flips(n):
    flips = []
    for i in range(n):
        flips.append(coin_flip())
    return flips

def four_flip_sample_space():
    flip = ['H','T']
    flips = []
    for f1 in flip:
        for f2 in flip:
            for f3 in flip:
                for f4 in flip:
                    flips.append([f1,f2,f3,f4])
    return flips

#print(series_of_flips(10))

for flip in four_flip_sample_space():
    print(flip)
sample_space = ["cat","dog","fish","rat"]

# List all outcomes for four pets randomly selected from SS, with replacement

outcome = []

for i1 in sample_space:
    for i2 in sample_space:
        for i3 in sample_space:
            for i4 in sample_space:
                outcome.append([i1, i2, i3, i4])

#for i in outcome:
#    print(i)

## what is the probability that a person will select 2 or more cats when randomly choosing 4 pets (with replaceement)?

two_or_more_cats = []
for pets in outcome:
    if pets.count('cat') >= 2:
        two_or_more_cats.append(pets)

print(len(two_or_more_cats) / len(outcome))
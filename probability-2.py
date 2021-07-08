'''
Consider invitations sent for a party.
20 invitations are sent out
Each guest can possibly bring up to ten guests
(with equal probability of between not going and 10 guests)
No matter what, at least one person (you) will be at the party
'''

from random import choice

## Synthesize outcomes
def num_attendees():
    num_peeps = 1
    for _ in range(20):
        num_peeps += choice(range(0, 11+1))
    return num_peeps

print(num_attendees())

#evaluate distribuion of sampling
#run sampling multiple times and get the average to get the better distribution
outcomes = dict()
for _ in range(100000):
    attending = num_attendees()
    if attending not in outcomes:
        outcomes[attending] = 0
    outcomes[attending] += 1

#for k, v in sorted(outcomes.items()):
#    print(f'{k}: {v}')

'''
Given a sample of outcomes, provide code to deliver an estimated probability
that between 80 and 90 people will attend the party.
Round the result to 3 decimal places
'''

hits = dict()
min_range = 80
max_range = 90

eighty_to_ninety = 0
total = sum(outcomes.values())

for k, v in outcomes.items():
    if k >= min_range and k <= max_range:
        hits[k] = v
        eighty_to_ninety += v

for k, v in sorted(hits.items()):
    print(f'{k}: {v}')

print(f'proba: {round(eighty_to_ninety / total, 3)}')

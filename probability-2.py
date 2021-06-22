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

#print distribuion of sampling
outcomes = dict()
for _ in range(100000):
    attending = num_attendees()
    if attending not in outcomes:
        outcomes[attending] = 0
    outcomes[attending] += 1

for k, v in sorted(outcomes.items()):
    print(f'{k}: {v}')

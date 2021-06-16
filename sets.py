a = ['bat', 'cat', 'dog', 'porpoise', 'whale', 'ant', 'bear']
b = ['bat', 'cat', 'dog', 'eagle', 'porpoise', 'shark', 'anteater', 'gull']
c = ['porpoise', 'platypus', 'crane', 'hermit crab', 'shark', 'anteater', 'gull']

def union(s1, s2):
    si = s1.copy()
    for i in s2:
        if i not in s1:
            si.append(i)
    return si

def union_mult_sets(*mult_sets):
    set_union = []
    for lst in mult_sets:
        for item in lst:
            if item not in set_union:
                set_union.append(item)
    return set_union

def intersect( s1, s2):
    si = []
    for i in s1:
        if i in s2:
            si.append(i)
    return si

def intersection_mult(*mult_sets):
    set_intersect = []
    if len(mult_sets) > 1 and len(mult_sets[0]) > 0:
        for item in mult_sets[0]:
            is_member = True
            for set_ in mult_sets[1:]:
                if item not in set_:
                    is_member = False
                    break
            if is_member:
                set_intersect.append(item)
    return set_intersect

def set_diff(s1, s2):
    sd = []
    for i in s1:
        if i not in s2:
            sd.append(i)
    return sd

def is_subset(ms, ss):
    sub = True
    for i in ss:
        if i not in ms:
            sub = False
            break
    return sub

#print(a)
#print(union(a,b))
#print(union_mult_sets(a, b, c))
#print(intersect(a,b))
#print(intersection_mult(a,b,c))
#print(set_diff(a,b))
#print(set_diff(b,a))
#print(set_diff(union(a,b), a))
#print(is_subset(union_mult_sets(a, b, c), a))

four_sided_die = [1,2,3,4]
coin_toss = ['H', 'T']

sample_space = []
for roll in four_sided_die:
    for flip1 in coin_toss:
        for flip2 in coin_toss:
            sample_space.append([roll, flip1, flip2])

print(sample_space)
print()

## first roll is 1
A = []
for outcome in sample_space:
    if outcome[0] == 1:
        A.append(outcome)
print(A)
print()

## at least one heads
B = []
for outcome in sample_space:
    if outcome.count('H') > 0:
        B.append(outcome)
print(B)
print()

print(union(A,B))

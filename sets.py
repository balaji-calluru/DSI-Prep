a = ['bat', 'cat', 'dog', 'porpoise', 'whale', 'ant', 'bear']
b = ['bat', 'cat', 'dog', 'eagle', 'shark', 'anteater', 'gull']
c = ['porpoise', 'platypus', 'crane', 'hermit crab', 'shark', 'anteater', 'gull']
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

print(union_mult_sets(a, b, c))
print(intersect(a,b))
print(any(a))

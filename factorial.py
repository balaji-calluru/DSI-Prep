def factorial(n):
    if n == 1:
        return n
    else:
        return n*factorial(n-1)

# print(factorial(5))
# print()

def permutations(n,k):
    return(int(factorial(n) / factorial(n-k)))

# print(permutations(10, 4))
# print()

def permutations2(n, k):
    perm = 1
    for i in range(n, n-k, -1):
        perm *= i
    return perm

# print(permutations2(10, 4))
# print()

base_5 = ['ant', 'bat', 'cat', 'dog', 'egg']
outputs = []
for an1 in base_5:
    for an2 in base_5:
        for an3 in base_5:
            for an4 in base_5:
                for an5 in base_5:
                    outputs.append([an1, an2, an3, an4, an5])

uniq_perms = []
for an_list in outputs:
    perm = True
    for an in an_list:
        if an_list.count(an) > 1:
            perm = False
            break
    if perm:
        uniq_perms.append(an_list)

# for an_list in uniq_perms:
#     print(an_list)
# print(len(uniq_perms))

def swap(lst, idx_1, idx_2):
    lst_ = lst.copy()
    temp = lst_[idx_2]
    lst_[idx_2] = lst_[idx_1]
    lst_[idx_1] = temp
    return lst_

temp = [1,2,3,4,5]
#print(swap(temp, 2, 4))
#print([0] * 5)

def heaps_non_recursive(lst, k):
    # avoid modifying lst
    lst_copy = lst.copy()
    # holds stack state
    c = [0] * len(lst) # -> [0, 0, 0 ...]
    # collect perms, collect initial perm
    perms = [lst_copy[:k]]
    i = 0 # acts like a stack pointer
    while i < len(lst_copy):
        if c[i] < i:
            if i % 2 == 0:
               lst_copy = swap(lst_copy, 0, i)
            else:
                lst_copy = swap(lst_copy, c[i], i)
            if lst_copy[:k] not in perms:
                perms.append(lst_copy[:k])
            # incr the counter
            c[i] += 1
            # reset i
            i = 0
        else:
            # reset state of count state at i
            c[i] = 0
            i += 1
    return perms

base_5 = ['ant', 'bat', 'crawdad', 'eagle', 'falcon']
five_perms = heaps_non_recursive(base_5, 5)
#for five in five_perms:
#    print(five)
#print(len(five_perms))
#print(permutations2(5, 5))

def combinations(n, k):
    return(factorial(n) // (factorial(n-k) * factorial(k)))

def combinations2(n, k):
    perm = 1
    for i in range(n, n-k, -1):
        perm *= i
    return int(perm / factorial(k))

# print(combinations(5,3))
# print(combinations2(5,3))

# print(list(range(5,1,-1)))

# an expensive counting approach
'''
Out of 11 basketball players, we can have teams
of 5. How many teams of 5 are possible?
'''

num_comb = combinations2(11, 5)

def combinations3():
    eleven_nums = range(1, 11+1)
    possible_five = []

    for i in eleven_nums:
        for j in eleven_nums:
            for k in eleven_nums:
                for l in eleven_nums:
                    for m in eleven_nums:
                        possible_five.append([i,j,k,l,m])
    
    perms = []
    for five in possible_five:
        if len(list(set(five))) == 5:
            perms.append(five)

#    for five in perms:
#        print(five)

# combinations3()

# an expensive sampling approach
from random import choice

def basketball_combs_samp(team_size=11, num_players=5):
    comb_count = combinations(team_size, num_players)
    comb_index = 0
    combs = []
    player_range = range(1, team_size+1)
    while len(combs) < combinations(team_size, num_players):
        player_comb = []
        while len(player_comb) < num_players:
            player_num = choice(player_range)
            if player_num not in player_comb:
                player_comb.append(player_num)
        player_comb = sorted(player_comb)
        if player_comb not in combs:
            comb_index += 1
            print(comb_index, comb_count, player_comb)
            combs.append(player_comb)
    return combs
team_size = 21
num_players = 5
#print(len(basketball_combs_samp(team_size , num_players)))
#print()

def combs_from_itertools(lst, k):
    # get a frozen version of the input
    lst_frozen = tuple(lst)
    n = len(lst_frozen)
    combs = []
    if k > n: return
    indices = list(range(k))
    yield tuple(lst_frozen[i] for i in indices)
    while True:
        for i in reversed(range(k)):
            if indices[i] != i + n - k:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, k):
            indices[j] = indices[j-1] + 1
        yield tuple(lst_frozen[i] for i in indices)
bask_nums = list(range(1, 21+1))
counter = 0
#for team in combs_from_itertools(bask_nums, 5):
#    print(team)
#    counter += 1
#print(counter)
#print(combinations(21, 5))

print(list(reversed(list(range(10)))))
print(list(range(9,-1,-1)))

lst = [1,1,2,2,3,3,4,4,5,5]
st = set(lst)
print(st)
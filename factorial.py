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
print(combinations(5,3))


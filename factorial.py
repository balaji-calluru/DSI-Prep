def factorial(n):
    if n == 1:
        return n
    else:
        return n*factorial(n-1)

print(factorial(5))

def permutations(n,k):
    return(int(factorial(n) / factorial(n-k)))

print(permutations(3,2))

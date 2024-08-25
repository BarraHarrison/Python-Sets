# Sets: unordered, mutable, no duplicates
my_set = set()
my_set.add(1)
my_set.add(2)
my_set.add(3)

for i in my_set:
    print(i)
if i in my_set:
    print("yes")


odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u)

i = odds.intersection(primes)
print(i)

e = evens.intersection(primes)
print(e)

set_a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set_b = {1, 2, 3, 10, 11, 12}

diff = set_a.difference(set_b)
print(diff)
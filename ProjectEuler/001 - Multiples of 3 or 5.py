# https://projecteuler.net/problem=1

multiples = [i for i in range(1000) if i % 3 == 0 or i % 5 == 0]
print(sum(multiples))

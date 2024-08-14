import random
from timeit import default_timer as timer
from collections import Counter

items = [1, 2, 3, 4]
rolls = 0
maxOnes = 0

start = timer()

while rolls < 1000000:
    numbers = Counter(random.choices(items, k=231))
    rolls += 1

    ones_count = numbers[1]
    if ones_count > maxOnes:
        maxOnes = ones_count

    if ones_count >= 177:
        break

end = timer()
print("Time Elasped:", end - start)
print("Highest Ones Roll:", maxOnes)
print("Number of Roll Sessions: ", rolls)

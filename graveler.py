import random
from multiprocessing import Pool, cpu_count
from timeit import default_timer as timer
from collections import Counter

items = [1, 2, 3, 4]

def simulate_rolls(rolls_per_worker):
    maxOnes = 0
    for _ in range(rolls_per_worker):
        numbers = Counter(random.choices(items, k=231))
        ones_count = numbers[1]
        if ones_count > maxOnes:
            maxOnes = ones_count
        
        if ones_count >= 177:
            break
    return maxOnes

if __name__ == "__main__":
    start = timer()

    total_rolls = int(1e9)
    num_workers = cpu_count()
    print(num_workers)
    rolls_per_worker = total_rolls // num_workers

    with Pool(num_workers) as pool:
        results = pool.map(simulate_rolls, [rolls_per_worker] * num_workers)
        print(results)
    
    max_ones = max(results)
    print("Highest Ones Roll:", max_ones)

    end = timer()
    print("Time Elapsed:", end - start)
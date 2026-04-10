import time
import random
from naive import find_positive_pairs as naive_find
from optimized import find_positive_pairs as optimized_find

print("Generating batch label data...")
# Simulating a batch of 5,000 items with 50 possible classes
labels = [random.randint(0, 50) for _ in range(5000)]

print("Running Naive Approach...")
start = time.perf_counter()
naive_res = naive_find(labels)
naive_time = time.perf_counter() - start
print(f"Naive Time: {naive_time:.4f}s")

print("Running Optimized Approach...")
start = time.perf_counter()
opt_res = optimized_find(labels)
opt_time = time.perf_counter() - start
print(f"Optimized Time: {opt_time:.4f}s")

speedup = naive_time / opt_time if opt_time > 0 else 0
print(f"\nPair counts match: {len(naive_res) == len(opt_res)}")
print(f"Optimized code is {speedup:.2f}x faster.")

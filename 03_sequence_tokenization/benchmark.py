import time
import random
import string
from naive import tokenize_sequences as naive_tok
from optimized import tokenize_sequences as optimized_tok

print("Generating sequence data...")
vocab = list(string.ascii_uppercase + "()=[]")
dataset = ["".join(random.choices(vocab, k=50)) for _ in range(50000)]

print("Running Naive Approach...")
start = time.perf_counter()
naive_res = naive_tok(dataset)
naive_time = time.perf_counter() - start
print(f"Naive Time: {naive_time:.4f}s")

print("Running Optimized Approach...")
start = time.perf_counter()
opt_res = optimized_tok(dataset)
opt_time = time.perf_counter() - start
print(f"Optimized Time: {opt_time:.4f}s")

speedup = naive_time / opt_time if opt_time > 0 else 0
print(f"\nOutputs match: {naive_res == opt_res}")
print(f"Optimized code is {speedup:.2f}x faster.")

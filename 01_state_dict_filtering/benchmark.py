import time
from naive import clean_state_dict as naive_clean
from optimized import clean_state_dict as optimized_clean

print("Generating dummy state_dict data...")
dummy_dict = {f"module.layer_{i}.weight": [0.1] * 10 for i in range(10000)}
expected = [f"layer_{i}.weight" for i in range(10500)] # 500 missing keys

print("Running Naive Approach...")
start = time.perf_counter()
naive_res = naive_clean(dummy_dict, expected)
naive_time = time.perf_counter() - start
print(f"Naive Time: {naive_time:.4f}s")

print("Running Optimized Approach...")
start = time.perf_counter()
opt_res = optimized_clean(dummy_dict, expected)
opt_time = time.perf_counter() - start
print(f"Optimized Time: {opt_time:.4f}s")

speedup = naive_time / opt_time if opt_time > 0 else 0
print(f"\nOutputs match: {naive_res[1] == opt_res[1]}")
print(f"Optimized code is {speedup:.2f}x faster.")

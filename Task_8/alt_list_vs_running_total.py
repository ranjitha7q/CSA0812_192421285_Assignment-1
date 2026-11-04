"""Task 8 - Alternative: store every payment in a list and add at the end
vs keep a running total. Compare time and space; say when storing is needed."""
import time
import tracemalloc
import random

random.seed(2)
N = 150_000
amounts = [round(random.uniform(100, 900), 2) for _ in range(N)]

def running_total(values):
    total = 0.0
    for v in values:
        total += v
    return total

def store_then_sum(values):
    stored = []
    for v in values:
        stored.append(v)
    return sum(stored)

for name, fn in [("running total", running_total), ("list then sum", store_then_sum)]:
    tracemalloc.start()
    t0 = time.perf_counter()
    r = fn(amounts)
    dt = time.perf_counter() - t0
    peak = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    print(f"{name:14}: {dt * 1000:7.2f} ms  peak extra memory {peak / 1024:9.1f} KiB  total={r:,.2f}")

print("Both are O(n) time. Running total is O(1) extra space; storing is O(n) space.")
print("Storing is needed only when entries must be printed again, audited, sorted,")
print("or corrected individually after the total was calculated.")

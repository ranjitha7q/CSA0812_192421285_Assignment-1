"""Task 6 - Alternative concept: one long script / lambdas vs functions.
Compares repeated code and function-call overhead for n entries."""
import time
import random

random.seed(1)
N = 200_000
entries = [(round(random.uniform(1, 30), 1), round(random.uniform(3.0, 5.0), 1),
            round(random.uniform(8.0, 9.2), 1)) for _ in range(N)]

# (a) functions
def rate_per_litre(fat, snf):
    return round(30.0 + round((fat - 3.5) / 0.1) * 0.40 + round((snf - 8.5) / 0.1) * 0.30, 2)

def payment(l, f, s):
    return round(l * rate_per_litre(f, s), 2)

t0 = time.perf_counter()
total_f = 0.0
for l, f, s in entries:
    total_f += payment(l, f, s)
t_func = time.perf_counter() - t0

# (b) one long script: formula pasted inline (the same formula would be
#     pasted again for every report, e.g. daily slip, ten-day slip, audit)
t0 = time.perf_counter()
total_i = 0.0
for l, f, s in entries:
    total_i += round(l * round(30.0 + round((f - 3.5) / 0.1) * 0.40 + round((s - 8.5) / 0.1) * 0.30, 2), 2)
t_inline = time.perf_counter() - t0

# (c) lambda
pay_lambda = lambda l, f, s: round(l * round(30.0 + round((f - 3.5) / 0.1) * 0.40 + round((s - 8.5) / 0.1) * 0.30, 2), 2)
t0 = time.perf_counter()
total_l = 0.0
for l, f, s in entries:
    total_l += pay_lambda(l, f, s)
t_lambda = time.perf_counter() - t0

print(f"n = {N:,} entries")
print(f"functions : {t_func:.3f} s  total={total_f:,.2f}")
print(f"inline    : {t_inline:.3f} s  total={total_i:,.2f}")
print(f"lambda    : {t_lambda:.3f} s  total={total_l:,.2f}")
print(f"Function-call overhead vs inline: {(t_func - t_inline) / N * 1e9:.0f} ns per entry")
print("Time is O(n) for all three; space is O(1) extra. The difference is a constant")
print("factor, while repeated inline code means every rate revision must be edited")
print("in every pasted copy.")

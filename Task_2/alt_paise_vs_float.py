"""Task 2 - Alternative concept: integer paise, or floats rounded after
every addition. Compare time, memory (sys.getsizeof) and correctness."""
import sys
import time
from decimal import Decimal

payments = ["33.40"] * 1000 + ["0.10"] * 3
N = 2000  # repeat count for timing


def total_paise(items):
    total = 0
    for s in items:
        rupees, paise = s.split(".")
        total += int(rupees) * 100 + int(paise.ljust(2, "0")[:2])
    return total                      # integer paise


def total_float_rounded(items):
    total = 0.0
    for s in items:
        total = round(total + float(s), 2)   # round after every addition
    return total


def total_float(items):
    t = 0.0
    for s in items:
        t += float(s)
    return t


def total_decimal(items):
    t = Decimal("0")
    for s in items:
        t += Decimal(s)
    return t


def timeit(fn):
    t0 = time.perf_counter()
    for _ in range(N):
        r = fn(payments)
    return r, (time.perf_counter() - t0) / N * 1e6


print(f"{'method':24}{'result':>22}{'correct?':>10}{'us/run':>10}")
for name, fn in [("plain float", total_float),
                 ("float, round each add", total_float_rounded),
                 ("integer paise", total_paise),
                 ("Decimal", total_decimal)]:
    r, us = timeit(fn)
    shown = r / 100 if fn is total_paise else r
    ok = Decimal(str(shown)) == Decimal("33400.30") if fn is not total_decimal else r == Decimal("33400.30")
    print(f"{name:24}{str(shown):>22}{str(ok):>10}{us:>10.1f}")

print("\nMemory of ONE stored value (sys.getsizeof, bytes):")
print("  float   33.40          :", sys.getsizeof(33.40))
print("  int     3340 (paise)   :", sys.getsizeof(3340))
print("  Decimal('33.40')       :", sys.getsizeof(Decimal("33.40")))
print("  str     '33.40'        :", sys.getsizeof("33.40"))

"""Task 4 - Alternative concept: floor()/int() instead of round() for steps."""
import math
import time

BASE, FS, SS = 30.00, 0.40, 0.30


def rate_round(fat, snf):
    return round(BASE + round((fat - 3.5) / 0.1) * FS + round((snf - 8.5) / 0.1) * SS, 2)

def rate_floor(fat, snf):
    return round(BASE + math.floor((fat - 3.5) / 0.1) * FS + math.floor((snf - 8.5) / 0.1) * SS, 2)

def rate_int(fat, snf):
    return round(BASE + int((fat - 3.5) / 0.1) * FS + int((snf - 8.5) / 0.1) * SS, 2)


for fat, snf in [(4.2, 8.6), (4.2, 3.6), (3.8, 8.9), (3.1, 8.2)]:
    print(f"fat={fat}, snf={snf}: round={rate_round(fat, snf):6}  floor={rate_floor(fat, snf):6}  int={rate_int(fat, snf):6}")

print("\nWhy: (3.8-3.5)/0.1 =", (3.8 - 3.5) / 0.1, "-> floor gives", math.floor((3.8 - 3.5) / 0.1), "(should be 3)")
print("     (3.1-3.5)/0.1 =", (3.1 - 3.5) / 0.1, "-> floor gives", math.floor((3.1 - 3.5) / 0.1),
      "and int gives", int((3.1 - 3.5) / 0.1))

N = 200_000
for name, fn in [("round", rate_round), ("floor", rate_floor), ("int", rate_int)]:
    t0 = time.perf_counter()
    for _ in range(N):
        fn(4.2, 8.7)
    print(f"{name:6}: {(time.perf_counter() - t0) / N * 1e6:.3f} us per call (O(1) time, O(1) space)")

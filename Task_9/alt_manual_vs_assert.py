"""Task 9 - Alternative: testing by typing inputs by hand vs an assert test function.
Compares time to rerun all tests after a rate change."""
import time
import milk_calc
from decimal import Decimal as D

CASES = [("10", "3.5", "8.5", "300.00"), ("8.5", "4.2", "8.7", "283.90"),
         ("12", "3.1", "8.2", "330.00"), ("20", "3.8", "8.5", "624.00"),
         ("15.5", "3.2", "8.9", "465.00")]


def run_asserts():
    for l, f, s, exp in CASES:
        assert milk_calc.payment(l, f, s) == D(exp)


t0 = time.perf_counter()
run_asserts()
auto = time.perf_counter() - t0
print(f"automated: {len(CASES)} cases re-checked in {auto * 1000:.3f} ms")

TYPING_SECONDS_PER_CASE = 20   # assumption: ~20 s to type 3 values, run and compare by eye
manual = len(CASES) * TYPING_SECONDS_PER_CASE
print(f"manual   : about {manual} s for the same {len(CASES)} cases (assumed {TYPING_SECONDS_PER_CASE} s each)")

# After a rate change (fat step 0.40 -> 0.45) the assert test reports exactly which expectations changed.
milk_calc.FAT_STEP_VALUE = D("0.45")
for l, f, s, exp in CASES:
    got = milk_calc.payment(l, f, s)
    print(f"  after rate change: {l} L fat {f}: expected(old)={exp} actual={got} {'ok' if got == D(exp) else 'CHANGED'}")

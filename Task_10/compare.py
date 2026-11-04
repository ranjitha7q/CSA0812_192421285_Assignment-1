"""Task 10 - compare expectations with execution.

Truth ('bank amount') = each payment rounded to paise (half-up, Decimal), then summed exactly.
Compared against float arithmetic, with rounding of each payment or only of the total.
"""
import random
import sys
import time
from decimal import Decimal, ROUND_HALF_UP

sys.path.insert(0, "../task09_testing")
import milk_calc as mc   # noqa: E402


def make_entries(n, seed):
    rnd = random.Random(seed)
    out = []
    for _ in range(n):
        litres = f"{rnd.uniform(1, 40):.2f}"          # two decimals, like a digital scale
        fat = f"{rnd.randint(25, 60) / 10:.1f}"       # 2.5 .. 6.0
        snf = f"{rnd.randint(78, 92) / 10:.1f}"       # 7.8 .. 9.2
        out.append((litres, fat, snf))
    return out


def float_payment_unrounded(litres, fat, snf):
    rate = round(30.0 + round((fat - 3.5) / 0.1) * 0.40 + round((snf - 8.5) / 0.1) * 0.30, 2)
    return litres * rate


for n in (5_000, 150_000):
    entries = make_entries(n, seed=n)
    print(f"\n=== {n:,} payments ===")

    # Decimal, round each payment (the reference)
    t0 = time.perf_counter()
    bank = Decimal("0")
    bank_each = []
    for l, f, s in entries:
        p = mc.payment(l, f, s)
        bank_each.append(p)
        bank += p
    t_dec = time.perf_counter() - t0

    # Decimal, round only the total
    t0 = time.perf_counter()
    raw = Decimal("0")
    for l, f, s in entries:
        raw += Decimal(l) * mc.rate_per_litre(f, s)
    dec_total_only = mc.money(raw)
    t_dec2 = time.perf_counter() - t0

    # float, round each payment
    fl = [(float(l), float(f), float(s)) for l, f, s in entries]
    t0 = time.perf_counter()
    float_each = 0.0
    mismatches = 0
    for (l, f, s), exact in zip(fl, bank_each):
        p = round(float_payment_unrounded(l, f, s), 2)
        float_each += p
        if Decimal(str(p)) != exact:
            mismatches += 1
    t_fl = time.perf_counter() - t0

    # float, round only the total
    t0 = time.perf_counter()
    float_raw = 0.0
    for l, f, s in fl:
        float_raw += float_payment_unrounded(l, f, s)
    float_total_only = round(float_raw, 2)
    t_fl2 = time.perf_counter() - t0

    print(f"Decimal, round each payment (bank amount) : {bank:>16}   {t_dec:6.3f} s")
    print(f"Decimal, round only the total             : {dec_total_only:>16}   {t_dec2:6.3f} s   diff vs bank {dec_total_only - bank}")
    print(f"float,   round each payment               : {float_each:>16.10f}   {t_fl:6.3f} s   diff vs bank {Decimal(float_each) - bank:.6f}")
    print(f"float,   round only the total             : {float_total_only:>16.2f}   {t_fl2:6.3f} s   diff vs bank {Decimal(str(float_total_only)) - bank}")
    print(f"float payments that differ from the Decimal paise value: {mismatches} of {n:,}")
    print(f"float printed total to 2 dp: {float_each:.2f}  vs bank {bank}")

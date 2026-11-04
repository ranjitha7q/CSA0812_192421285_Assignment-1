"""Task 12 D - evidence: tests for both seasons and the bonus. Run: python test_v2.py"""
from datetime import date
from decimal import Decimal as D
from milkrate_v2 import rate_per_litre, payment, bonus, ten_day_statement, season_for

fails = 0
def check(label, got, exp):
    global fails
    ok = got == exp
    fails += not ok
    print(f"{label:<58}{str(exp):>12}{str(got):>12}  {'PASS' if ok else 'FAIL'}")

print(f"{'TEST':<58}{'EXPECTED':>12}{'ACTUAL':>12}  RESULT")
print("-" * 92)
# seasons
check("season_for 31 Mar", season_for(date(2026, 3, 31)), "standard")
check("season_for 1 Apr",  season_for(date(2026, 4, 1)), "summer")
check("season_for 30 Jun", season_for(date(2026, 6, 30)), "summer")
check("season_for 1 Jul",  season_for(date(2026, 7, 1)), "standard")
# rates, two-decimal readings
check("standard 3.50/8.50", rate_per_litre("3.50", "8.50", "standard"), D("30.00"))
check("standard 4.25/8.63 (7.5 + 1.3 steps)", rate_per_litre("4.25", "8.63", "standard"), D("33.39"))
check("standard 3.15/8.37 (-3.5 + -1.3 steps)", rate_per_litre("3.15", "8.37", "standard"), D("28.21"))
check("summer 3.50/8.50", rate_per_litre("3.50", "8.50", "summer"), D("32.00"))
check("summer 4.25/8.63 (35.765 -> half up)", rate_per_litre("4.25", "8.63", "summer"), D("35.77"))
check("summer 3.15/8.37 (30.035 -> half up)", rate_per_litre("3.15", "8.37", "summer"), D("30.04"))
# payments
check("payment 20 L standard 4.25/8.63", payment("20", "4.25", "8.63", "standard"), D("667.80"))
check("payment 20 L summer 4.25/8.63", payment("20", "4.25", "8.63", "summer"), D("715.40"))
# bonus boundary
check("bonus 499.99 L", bonus("499.99"), D("0.00"))
check("bonus exactly 500 L", bonus("500"), D("0.00"))
check("bonus 500.01 L (on ALL litres)", bonus("500.01"), D("250.01"))
check("bonus 510 L", bonus("510"), D("255.00"))
# full ten-day statements
st = ten_day_statement([(date(2026, 5, 10), "500", "3.5", "8.5")])
check("summer, 500 L exactly: total (no bonus)", st["total"], D("16000.00"))
st = ten_day_statement([(date(2026, 5, 10), "510", "3.5", "8.5")])
check("summer, 510 L: milk 16320.00 + bonus 255.00", st["total"], D("16575.00"))
st = ten_day_statement([(date(2026, 11, 3), "510", "3.5", "8.5")])
check("standard, 510 L: milk 15300.00 + bonus 255.00", st["total"], D("15555.00"))
st = ten_day_statement([(date(2026, 11, 1), "170", "3.5", "8.5")] * 3)
check("standard, 3 x 170 L = 510 L (bonus uses period total)", st["bonus"], D("255.00"))
st = ten_day_statement([(date(2026, 3, 31), "300", "3.5", "8.5"), (date(2026, 4, 2), "300", "3.5", "8.5")])
check("period straddling 1 Apr: 9000 + 9600 + bonus 300", st["total"], D("18900.00"))
# validation still works
for label, args in [("fat 7.01 rejected", ("10", "7.01", "8.5")), ("litres 0 rejected", ("0", "3.5", "8.5"))]:
    try:
        payment(*args); got = "accepted"
    except ValueError:
        got = "rejected"
    check(label, got, "rejected")
print("-" * 92)
print("ALL TESTS PASSED" if not fails else f"{fails} FAILED")
assert not fails

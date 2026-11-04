"""Task 9 - automated tests with assert. Run:  python test_calculator.py
Prints a test table (expected vs actual) and stops with an error on any failure."""
from decimal import Decimal as D
from milk_calc import payment, rate_per_litre, ten_day_total

rate_cases = [
    # description,                     fat,   snf,   expected rate
    ("standard milk",                  "3.5", "8.5", D("30.00")),
    ("fat above standard",             "4.2", "8.5", D("32.80")),
    ("fat below standard",             "3.1", "8.5", D("28.40")),
    ("snf above standard",             "3.5", "8.9", D("31.20")),
    ("snf below standard",             "3.5", "8.2", D("29.10")),
    ("both above",                     "4.2", "8.7", D("33.40")),
    ("both below",                     "3.1", "8.2", D("27.50")),
    ("boundary fat 2.0",               "2.0", "8.5", D("24.00")),
    ("boundary fat 7.0",               "7.0", "8.5", D("44.00")),
    ("boundary snf 6.0",               "3.5", "6.0", D("22.50")),
    ("boundary snf 10.0",              "3.5", "10.0", D("34.50")),
]
pay_cases = [
    ("10 L standard",                  "10",   "3.5", "8.5", D("300.00")),
    ("8.5 L fat 4.2 snf 8.7",          "8.5",  "4.2", "8.7", D("283.90")),
    ("12 L fat 3.1 snf 8.2",           "12",   "3.1", "8.2", D("330.00")),
    ("paise rounding 3.765 -> 3.77",   "0.1255", "3.5", "8.5", D("3.77")),
    ("fraction of a litre",            "0.125", "3.5", "8.5", D("3.75")),
]
invalid_cases = [
    ("text litres",         "abc", "3.5", "8.5"),
    ("negative litres",     "-5",  "3.5", "8.5"),
    ("zero litres",         "0",   "3.5", "8.5"),
    ("empty litres",        "",    "3.5", "8.5"),
    ("fat below 2.0",       "10",  "1.9", "8.5"),
    ("fat above 7.0",       "10",  "7.1", "8.5"),
    ("snf below 6.0",       "10",  "3.5", "5.9"),
    ("snf above 10.0",      "10",  "3.5", "10.1"),
    ("text fat",            "10",  "high", "8.5"),
    ("scientific notation", "1e3", "3.5", "8.5"),
    ("nan",                 "10",  "nan", "8.5"),
]
five = [("10", "3.5", "8.5"), ("8.5", "4.2", "8.7"), ("12", "3.1", "8.2"),
        ("20", "3.8", "8.5"), ("15.5", "3.2", "8.9")]
# hand calculation: 300.00 + 283.90 + 330.00 + 624.00 + 465.00 = 2002.90

failures = 0
print(f"{'TEST':<34}{'EXPECTED':>12}{'ACTUAL':>12}  RESULT")
print("-" * 68)
for desc, fat, snf, exp in rate_cases:
    got = rate_per_litre(fat, snf)
    ok = got == exp; failures += not ok
    print(f"rate: {desc:<28}{str(exp):>12}{str(got):>12}  {'PASS' if ok else 'FAIL'}")
for desc, litres, fat, snf, exp in pay_cases:
    got = payment(litres, fat, snf)
    ok = got == exp; failures += not ok
    print(f"pay : {desc:<28}{str(exp):>12}{str(got):>12}  {'PASS' if ok else 'FAIL'}")
for desc, litres, fat, snf in invalid_cases:
    try:
        payment(litres, fat, snf); got = "accepted"
    except (ValueError, TypeError):
        got = "rejected"
    ok = got == "rejected"; failures += not ok
    print(f"bad : {desc:<28}{'rejected':>12}{got:>12}  {'PASS' if ok else 'FAIL'}")
got = ten_day_total(five)
ok = got == D("2002.90"); failures += not ok
print(f"sum : {'5 entries (hand total)':<28}{'2002.90':>12}{str(got):>12}  {'PASS' if ok else 'FAIL'}")
print("-" * 68)
print("ALL TESTS PASSED" if failures == 0 else f"{failures} TEST(S) FAILED")
assert failures == 0

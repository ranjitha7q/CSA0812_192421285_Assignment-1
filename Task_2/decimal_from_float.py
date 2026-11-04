"""Variant asked in Task 2: Decimal(amount) -> Decimal(float(amount))."""
from decimal import Decimal

payments = ["33.40"] * 1000 + ["0.10"] * 3


def total_decimal_from_float(items):
    total = Decimal("0")
    for amount in items:
        total += Decimal(float(amount))   # float is converted FIRST
    return total


print("Decimal(float(amount)) total :", total_decimal_from_float(payments))
print("Decimal(float('33.40'))      :", Decimal(float("33.40")))
print("Decimal('33.40')             :", Decimal("33.40"))
# Explanation: float('33.40') is already the nearest binary fraction, which
# is slightly different from 33.40. Decimal(float) copies that binary error
# exactly, so the 'exact' Decimal total is exact for the WRONG numbers.

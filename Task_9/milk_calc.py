"""Milk co-operative payment calculator (final design for tasks 9-11).

* Money and percentages are Decimal, created from STRINGS (never from floats).
* Every payment is rounded to paise with ROUND_HALF_UP.
* All rates/limits are named constants in one place.

Usage:  python milk_calc.py            (interactive)
        python milk_calc.py file.csv   (lines: id,litres,fat,snf)
"""
import re
import sys
from decimal import Decimal, ROUND_HALF_UP

# ---- Rate card -------------------------------------------------------------
BASE_RATE = Decimal("30.00")       # Rs/litre at 3.5 % fat and 8.5 % SNF
STD_FAT = Decimal("3.5")
STD_SNF = Decimal("8.5")
STEP = Decimal("0.1")              # one step = 0.1 %
FAT_STEP_VALUE = Decimal("0.40")   # Rs/litre per fat step
SNF_STEP_VALUE = Decimal("0.30")   # Rs/litre per SNF step

# ---- Validation limits -----------------------------------------------------
FAT_MIN, FAT_MAX = Decimal("2.0"), Decimal("7.0")
SNF_MIN, SNF_MAX = Decimal("6.0"), Decimal("10.0")   # assumption: not given in brief

PAISE = Decimal("0.01")
_NUMBER = re.compile(r"^\d+(\.\d+)?$")   # digits with optional fraction: no sign, no 'nan', no '1e3'


def to_decimal(value, name="value"):
    """Convert a string/int/Decimal to Decimal; reject floats, text and non-finite input."""
    if isinstance(value, float):
        raise TypeError(f"{name}: pass a string such as '8.5', not a float")
    text = str(value).strip()
    if not _NUMBER.match(text):
        raise ValueError(f"{name} '{text}' is not a valid non-negative number")
    return Decimal(text)


def money(x):
    """Round a Decimal to whole paise (half-up)."""
    return x.quantize(PAISE, rounding=ROUND_HALF_UP)


def whole_steps(reading, standard):
    """Number of whole 0.1 % steps between reading and standard (half-up, symmetric)."""
    return ((reading - standard) / STEP).quantize(Decimal("1"), rounding=ROUND_HALF_UP)


def validate(litres, fat, snf):
    """Return (litres, fat, snf) as Decimals or raise ValueError."""
    litres = to_decimal(litres, "litres")
    fat = to_decimal(fat, "fat")
    snf = to_decimal(snf, "snf")
    if litres <= 0:
        raise ValueError("litres must be greater than 0")
    if not FAT_MIN <= fat <= FAT_MAX:
        raise ValueError(f"fat {fat} outside {FAT_MIN}-{FAT_MAX}")
    if not SNF_MIN <= snf <= SNF_MAX:
        raise ValueError(f"snf {snf} outside {SNF_MIN}-{SNF_MAX}")
    return litres, fat, snf


def rate_per_litre(fat, snf):
    """Price per litre in Rs, rounded to paise."""
    fat, snf = to_decimal(fat, "fat"), to_decimal(snf, "snf")
    rate = (BASE_RATE
            + whole_steps(fat, STD_FAT) * FAT_STEP_VALUE
            + whole_steps(snf, STD_SNF) * SNF_STEP_VALUE)
    return money(rate)


def payment(litres, fat, snf):
    """Amount payable for one delivery in Rs, rounded to paise. Validates first."""
    litres, fat, snf = validate(litres, fat, snf)
    return money(litres * rate_per_litre(fat, snf))


def ten_day_total(entries):
    """Sum of per-entry payments for (litres, fat, snf) tuples of strings."""
    total = Decimal("0")
    for litres, fat, snf in entries:
        total += payment(litres, fat, snf)
    return total


def run(lines):
    print(f"{'ID':<6}{'Litres':>9}{'Fat%':>7}{'SNF%':>7}{'Rate':>9}{'Amount':>12}")
    print("-" * 50)
    total = Decimal("0")
    for line in lines:
        line = line.strip()
        if not line:
            continue
        parts = [p.strip() for p in line.split(",")]
        try:
            if len(parts) != 4:
                raise ValueError("need 4 fields: id,litres,fat,snf")
            fid, litres, fat, snf = parts
            amt = payment(litres, fat, snf)
            rate = rate_per_litre(fat, snf)
        except (ValueError, TypeError) as err:
            print(f"INVALID '{line}': {err}")
            continue
        total += amt
        print(f"{fid:<6}{litres:>9}{fat:>7}{snf:>7}{rate:>9}{amt:>12}")
    print("-" * 50)
    print(f"{'TOTAL':<38}{total:>12}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as fh:
            run(fh.readlines())
    else:
        print("Enter id,litres,fat,snf per line; blank line to finish")
        rows = []
        while (s := input("> ")).strip():
            rows.append(s)
        run(rows)

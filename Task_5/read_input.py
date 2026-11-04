"""Task 5 - reading the clerk's entries and converting types.

Usage:
    python read_input.py                 # interactive: type entries
    python read_input.py sample_input.txt   # batch: one entry per line
Entry format:  farmer_id,litres,fat,snf
"""
import sys

FAT_MIN, FAT_MAX = 2.0, 7.0
SNF_MIN, SNF_MAX = 6.0, 10.0


def is_number(text):
    """String-method check: optional spaces, digits, at most one dot."""
    t = text.strip()
    if t.count(".") > 1 or t == "" or t == ".":
        return False
    return t.replace(".", "", 1).isdigit()


def read_entry(line):
    """Return (farmer_id, litres, fat, snf) as (str, float, float, float)
    or raise ValueError with a clear message."""
    parts = [p.strip() for p in line.split(",")]
    if len(parts) != 4:
        raise ValueError("need 4 fields: id,litres,fat,snf")
    farmer_id, litres_t, fat_t, snf_t = parts
    for name, t in (("litres", litres_t), ("fat", fat_t), ("snf", snf_t)):
        if not is_number(t):
            raise ValueError(f"{name} '{t}' is not a valid non-negative number")
    litres, fat, snf = float(litres_t), float(fat_t), float(snf_t)
    if litres <= 0:
        raise ValueError("litres must be greater than 0")
    if not FAT_MIN <= fat <= FAT_MAX:
        raise ValueError(f"fat {fat} outside {FAT_MIN}-{FAT_MAX}")
    if not SNF_MIN <= snf <= SNF_MAX:
        raise ValueError(f"snf {snf} outside {SNF_MIN}-{SNF_MAX}")
    return farmer_id, litres, fat, snf


def rate_per_litre(fat, snf):
    return round(30.00 + round((fat - 3.5) / 0.1) * 0.40 + round((snf - 8.5) / 0.1) * 0.30, 2)


def main(lines):
    print(f"{'ID':<6}{'Litres':>8}{'Fat%':>7}{'SNF%':>7}{'Rate':>9}{'Amount':>11}")
    print("-" * 48)
    total = 0.0
    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            fid, litres, fat, snf = read_entry(line)
        except ValueError as err:
            print(f"INVALID  '{line}': {err}")
            continue
        rate = rate_per_litre(fat, snf)
        amt = round(litres * rate, 2)
        total += amt
        print(f"{fid:<6}{litres:>8.1f}{fat:>7.1f}{snf:>7.1f}{rate:>9.2f}{amt:>11.2f}")
    print("-" * 48)
    print(f"{'TOTAL':<37}{total:>11.2f}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            main(f.readlines())
    else:
        print("Enter entries as id,litres,fat,snf (blank line to finish)")
        typed = []
        while True:
            s = input("> ")
            if s.strip() == "":
                break
            typed.append(s)
        main(typed)

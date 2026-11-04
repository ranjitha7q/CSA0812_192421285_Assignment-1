"""Task 6 - logic organised into functions (float version, one-decimal readings)."""

BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30
STD_FAT, STD_SNF, STEP = 3.5, 8.5, 0.1


def rate_per_litre(fat, snf):
    """Return the price per litre (Rs) for the given fat % and SNF %, rounded to 2 decimals."""
    fat_steps = round((fat - STD_FAT) / STEP)
    snf_steps = round((snf - STD_SNF) / STEP)
    return round(BASE_RATE + fat_steps * FAT_STEP_VALUE + snf_steps * SNF_STEP_VALUE, 2)


def payment(litres, fat, snf):
    """Return the amount payable (Rs) for one delivery, rounded to 2 decimals."""
    return round(litres * rate_per_litre(fat, snf), 2)


def ten_day_total(entries):
    """Return the sum of payments for a list of (litres, fat, snf) tuples."""
    total = 0.0
    for litres, fat, snf in entries:
        total += payment(litres, fat, snf)
    return round(total, 2)


def scope_demo():
    """Constants may be READ inside a function but not reassigned."""
    print("reading BASE_RATE inside function:", BASE_RATE)
    try:
        exec("def bad():\n    BASE_RATE = BASE_RATE + 1\n    return BASE_RATE\nbad()", globals())
    except UnboundLocalError as e:
        print("assigning to it inside a function ->", type(e).__name__, ":", e)
    local_rate = rate_per_litre(4.2, 8.7)      # local name, dies when function ends
    return local_rate


def print_vs_return():
    """print() shows a value but gives back None; return hands the value to the caller."""
    def shows(l, f, s):
        print("  (inside shows) payment =", payment(l, f, s))
    def gives(l, f, s):
        return payment(l, f, s)
    a = shows(8.5, 4.2, 8.7)
    b = gives(8.5, 4.2, 8.7)
    print("shows() returned:", a, "| gives() returned:", b, "| usable in maths: ", b * 2)


if __name__ == "__main__":
    entries = [(10, 3.5, 8.5), (8.5, 4.2, 8.7), (12, 3.1, 8.2)]
    for e in entries:
        print(e, "-> rate", rate_per_litre(e[1], e[2]), "pay", payment(*e))
    print("ten_day_total =", ten_day_total(entries))
    scope_demo()
    print_vs_return()

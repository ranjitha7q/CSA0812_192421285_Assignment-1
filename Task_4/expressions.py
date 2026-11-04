"""Task 4 - correct expressions (float version, one-decimal readings)."""
import math

BASE_RATE = 30.00
FAT_STEP_VALUE, SNF_STEP_VALUE = 0.40, 0.30
STD_FAT, STD_SNF, STEP = 3.5, 8.5, 0.1


def fat_steps(fat):
    return round((fat - STD_FAT) / STEP)

def snf_steps(snf):
    return round((snf - STD_SNF) / STEP)

def rate(fat, snf):
    return round(BASE_RATE + fat_steps(fat) * FAT_STEP_VALUE
                 + snf_steps(snf) * SNF_STEP_VALUE, 2)

def amount(litres, fat, snf):
    return round(litres * rate(fat, snf), 2)


print("fat_steps(4.2)  =", fat_steps(4.2), "| snf_steps(8.7) =", snf_steps(8.7))
print("rate(4.2, 8.7)  =", rate(4.2, 8.7), "| amount(8.5, 4.2, 8.7) =", amount(8.5, 4.2, 8.7))

print("\n--- Precedence and associativity ---")
print("2 + 3 * 4        =", 2 + 3 * 4, "  (* before +)")
print("-2 ** 2          =", -2 ** 2, " (** binds tighter than unary minus)")
print("(-2) ** 2        =", (-2) ** 2)
print("2 ** 3 ** 2      =", 2 ** 3 ** 2, " (** is right-associative: 2**(3**2))")
print("100 - 30 - 20    =", 100 - 30 - 20, " (- is left-associative)")
print("-7 // 2          =", -7 // 2, " (floors toward minus infinity)")

print("\n--- Surprising result 1: step counts from float subtraction ---")
for reading in (4.2, 3.8):
    x = (reading - 3.5) / 0.1
    print(f"({reading} - 3.5) / 0.1 = {x!r:22} round -> {round(x)}  floor -> {math.floor(x)}  int -> {int(x)}")
print("3.8 should be exactly 3 steps: floor/int lose a step (2), only round() is safe.")

print("\n--- Surprising result 2: round() on .5 uses banker's rounding ---")
print("round(0.5), round(1.5), round(2.5) =", round(0.5), round(1.5), round(2.5))
print("round(2.675, 2) =", round(2.675, 2), " (binary 2.675 is slightly below 2.675)")

print("\n--- Surprising result 3: money as float ---")
print("int(19.99 * 100) =", int(19.99 * 100), " (expected 1999)")
print("0.1 * 3          =", 0.1 * 3)
print("0.1 * 3 == 0.3   =", 0.1 * 3 == 0.3)

print("\n--- round() vs floor() for negatives ---")
for v in (-2.5, -2.4, -2.6):
    print(f"v={v:5}  round={round(v):3}  floor={math.floor(v):3}  int={int(v):3}")

print("\n--- Comparison chaining and Boolean operators ---")
fat = 4.2
print("2.0 <= fat <= 7.0               =", 2.0 <= fat <= 7.0)
print("2.0 <= fat and fat <= 7.0       =", 2.0 <= fat and fat <= 7.0)
fat = 7.5
print("fat=7.5: 2.0 <= fat <= 7.0      =", 2.0 <= fat <= 7.0)
print("fat=7.5: not (2.0 <= fat <= 7.0) =", not (2.0 <= fat <= 7.0))

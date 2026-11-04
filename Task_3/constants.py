"""Task 3 - rates and limits as named constants (one place to revise)."""
from decimal import Decimal

# Rate card (UPPER_CASE = convention for constants)
BASE_RATE = Decimal("30.00")      # Rs/litre for 3.5 % fat and 8.5 % SNF
STD_FAT = Decimal("3.5")          # standard fat %
STD_SNF = Decimal("8.5")          # standard SNF %
STEP = Decimal("0.1")             # one step = 0.1 %
FAT_STEP_VALUE = Decimal("0.40")  # Rs/litre per fat step
SNF_STEP_VALUE = Decimal("0.30")  # Rs/litre per SNF step

# Validation limits
FAT_MIN, FAT_MAX = Decimal("2.0"), Decimal("7.0")
SNF_MIN, SNF_MAX = Decimal("6.0"), Decimal("10.0")   # assumption
PAYMENT_DAYS = 10                 # farmers are paid every ten days

print("BASE_RATE =", BASE_RATE, "| FAT_STEP_VALUE =", FAT_STEP_VALUE)

# --- Python has no true constants: this is allowed (but wrong by convention)
BASE_RATE = Decimal("99.00")
print("Reassigned BASE_RATE (allowed!) :", BASE_RATE)
BASE_RATE = Decimal("30.00")      # restore

# --- Dynamic typing: same name, different types
x = 10
print("x =", x, type(x).__name__)
x = "ten"
print("x =", x, type(x).__name__)

# --- Multiple assignment and swapping
a, b = 3.5, 8.5
print("before swap:", a, b)
a, b = b, a
print("after  swap:", a, b)
fat = snf = 0
print("chained assignment fat, snf :", fat, snf)

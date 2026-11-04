"""Task 12 A/B - impact of two-decimal readings on the ORIGINAL design (Task 7 float
module and Task 9 Decimal calculator) compared with the modified design."""
import sys
from decimal import Decimal as D
sys.path.insert(0, "../task07_module")
sys.path.insert(0, "../task09_testing")
import milkrate                     # original float module
import milk_calc                    # original Decimal calculator (whole steps)
import milkrate_v2                  # modified design

print("Original float module: steps from two-decimal readings")
for fat in ("4.25", "4.15", "4.05", "3.95"):
    raw = (float(fat) - 3.5) / 0.1
    print(f"  fat {fat}: (fat-3.5)/0.1 = {raw!r:22} round() -> {round(raw)}")

print("\nRate per litre (standard season) for two-decimal readings")
print(f"{'fat':>6}{'snf':>6}{'orig float':>12}{'orig Decimal':>14}{'modified':>10}{'difference/L':>14}")
for fat, snf in [("4.25", "8.63"), ("4.15", "8.55"), ("4.05", "8.50"), ("4.21", "8.50"), ("4.29", "8.50"), ("3.15", "8.37")]:
    a = milkrate.rate_per_litre(float(fat), float(snf))
    b = milk_calc.rate_per_litre(fat, snf)
    c = milkrate_v2.rate_per_litre(fat, snf, "standard")
    print(f"{fat:>6}{snf:>6}{a:>12.2f}{str(b):>14}{str(c):>10}{str(c - b):>14}")

print("\nObservation: fat 4.21 and fat 4.29 get the SAME original rate (whole-step rounding throws")
print("away the analyser's precision) while the modified design pays 0.01 % = 0.1 step pro rata.")
print("Float module vs Decimal calculator disagree on exact half-steps (fat 4.05: float sees 5.4999.. -> 5 steps, Decimal 5.5 -> 6): float noise.")

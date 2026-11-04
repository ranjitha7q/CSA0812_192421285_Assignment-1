"""Task 11 - Alternative: read the rate card from a JSON file at start-up
instead of constants in a module. Compare start-up cost and editing cost."""
import json
import sys
import time
from decimal import Decimal

sys.path.insert(0, "../task09_testing")

t0 = time.perf_counter()
import milk_calc                               # constants live in the module
t_module = time.perf_counter() - t0

t0 = time.perf_counter()
with open("ratecard.json") as fh:
    card = {k: Decimal(v) for k, v in json.load(fh).items()}
t_json = time.perf_counter() - t0

print(f"module import (constants)       : {t_module * 1e3:7.3f} ms (once per run)")
print(f"JSON read + Decimal conversion  : {t_json * 1e3:7.3f} ms (once per run)")
print("Space: 6 values either way -> O(1)")
print("Rate card from JSON :", card)

# Applying the JSON card to the calculator without editing any .py file
milk_calc.BASE_RATE = card["base_rate"]
milk_calc.FAT_STEP_VALUE = card["fat_step_value"]
milk_calc.SNF_STEP_VALUE = card["snf_step_value"]
print("payment 8.5 L, 4.2/8.7 with JSON card:", milk_calc.payment("8.5", "4.2", "8.7"))
print("\nEditing cost: JSON -> clerk edits one text file, no code redistribution,")
print("but a typo ('0,40') is only caught at run time, so the loader must validate.")

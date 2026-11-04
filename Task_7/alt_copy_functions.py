"""Task 7 - Alternative concept: copying the functions into every script vs importing.
Measures the one-time import cost and shows the caching in sys.modules."""
import importlib
import sys
import time

t0 = time.perf_counter()
import milkrate                       # first import: file is read and compiled/cached
t_first = time.perf_counter() - t0

t0 = time.perf_counter()
importlib.import_module("milkrate")   # second import: found in sys.modules
t_second = time.perf_counter() - t0

print(f"first import  : {t_first * 1e6:8.1f} us (one-time cost per program run)")
print(f"second import : {t_second * 1e6:8.1f} us (cached in sys.modules)")
print("same object   :", sys.modules["milkrate"] is milkrate)

# Copy-paste approach: if the rate card is pasted into N scripts, a rate
# revision means N edits and N chances to miss one (the original bug).
scripts = ["daily_slip.py", "ten_day_slip.py", "bank_file.py", "audit.py"]
print(f"\nRate revision with copied functions: {len(scripts)} files to edit")
print("Rate revision with one module       : 1 file to edit (milkrate.py)")

"""Implements pseudocode B and prints the same trace table as the hand trace."""
import math

def payment_steps(litres, fat, snf):
    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)
    rate = round(30.00 + fat_steps * 0.40 + snf_steps * 0.30, 2)
    return fat_steps, snf_steps, rate, round(litres * rate, 2)

entries = [(10, 3.5, 8.5), (8.5, 4.2, 8.7), (12, 3.1, 8.2)]
total = 0.0
print(f"{'litres':>6}{'fat':>6}{'snf':>6}{'f_steps':>8}{'s_steps':>8}{'rate':>8}{'payment':>10}{'total':>10}")
for litres, fat, snf in entries:
    fs, ss, rate, pay = payment_steps(litres, fat, snf)
    total += pay
    print(f"{litres:>6}{fat:>6}{snf:>6}{fs:>8}{ss:>8}{rate:>8.2f}{pay:>10.2f}{total:>10.2f}")
print("Final total:", f"{total:.2f}")

"""Task 1 - Alternative concept: separate variables per farmer vs one list of tuples.

Shows what the 'three separate variables' style looks like and why it
does not scale to 300 farmers (900 names) or 150,000 farmers.
"""

# --- Alternative: separate variables (only 3 farmers shown) ---
farmer1_litres, farmer1_fat, farmer1_snf = 10, 3.5, 8.5
farmer2_litres, farmer2_fat, farmer2_snf = 8.5, 4.2, 8.7
farmer3_litres, farmer3_fat, farmer3_snf = 12, 3.1, 8.2
# For 300 farmers this needs 300 x 3 = 900 variable names, and the
# payment expression would have to be copy-pasted 300 times.
print("Variables needed for 300 farmers :", 300 * 3)
print("Variables needed for 150,000     :", 150_000 * 3)

# --- Chosen design: one list of tuples (farmer_id, litres, fat, snf) ---
entries = [
    ("F001", 10, 3.5, 8.5),
    ("F002", 8.5, 4.2, 8.7),
    ("F003", 12, 3.1, 8.2),
]
total_litres = 0
for farmer_id, litres, fat, snf in entries:   # one loop works for any n
    total_litres += litres
print("Total litres (loop over list)    :", total_litres)
print("Names needed for any n farmers   : 1 (the list)")

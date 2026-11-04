"""Task 3 - Alternative concept: magic numbers vs RATE_CARD dictionary.
Counts how many places must change when the fat step goes 0.40 -> 0.45."""

# (a) Magic numbers typed inside expressions (the volunteer's style)
def rate_magic(fat, snf):
    r = 30.00 + round((fat - 3.5) / 0.1) * 0.40 + round((snf - 8.5) / 0.1) * 0.30
    return round(r, 2)

def amount_magic(litres, fat, snf):
    return round(litres * (30.00 + round((fat - 3.5) / 0.1) * 0.40
                           + round((snf - 8.5) / 0.1) * 0.30), 2)

def report_magic(fat, snf):
    return "fat step Rs 0.40, snf step Rs 0.30 -> " + str(rate_magic(fat, snf))

# (b) Dictionary rate card
RATE_CARD = {"base": 30.00, "fat": 0.40, "snf": 0.30, "std_fat": 3.5, "std_snf": 8.5}

def rate_card(fat, snf, card=RATE_CARD):
    r = (card["base"]
         + round((fat - card["std_fat"]) / 0.1) * card["fat"]
         + round((snf - card["std_snf"]) / 0.1) * card["snf"])
    return round(r, 2)

import inspect
src_magic = inspect.getsource(rate_magic) + inspect.getsource(amount_magic) + inspect.getsource(report_magic)
print("Places where 0.40 is typed (magic numbers):", src_magic.count("0.40"))
print("Places where 0.40 is typed (RATE_CARD)    : 1 (the dictionary value)")
print("rate_magic(4.2, 8.7) =", rate_magic(4.2, 8.7), "| rate_card(4.2, 8.7) =", rate_card(4.2, 8.7))
print("Dictionary also lets one function serve many seasons:",
      rate_card(4.2, 8.7, dict(RATE_CARD, base=32.00)))

"""Milk co-operative rate card v2 - DESIGN DECISION: MODIFY (not redesign).

Changes from the original design
* analyser readings have two decimals -> steps are counted exactly (fractions of a step)
  instead of being rounded to a whole 0.1 % step
* seasonal rate cards (April-June vs rest of year); season is a PARAMETER
* a separate bonus function for ten-day periods above 500 litres

ASSUMPTIONS (edit RATE_CARDS in ONE place if the union's circular says otherwise):
* summer fat step value is Rs 0.45 and SNF step Rs 0.30 - the brief was unclear on this
* fraction of a step is paid pro rata (0.01 % fat = 0.1 step)
* bonus = Rs 0.50 x ALL litres of the ten-day period if litres > 500 (exactly 500 -> no bonus)
"""
from datetime import date
from decimal import Decimal, ROUND_HALF_UP
from typing import NamedTuple

PAISE = Decimal("0.01")
STD_FAT, STD_SNF, STEP = Decimal("3.5"), Decimal("8.5"), Decimal("0.1")


class RateCard(NamedTuple):
    base: Decimal
    fat_step: Decimal
    snf_step: Decimal


RATE_CARDS = {
    "standard": RateCard(Decimal("30.00"), Decimal("0.40"), Decimal("0.30")),
    "summer":   RateCard(Decimal("32.00"), Decimal("0.45"), Decimal("0.30")),  # April-June
}
SUMMER_MONTHS = (4, 5, 6)
BONUS_THRESHOLD = Decimal("500")      # litres in a ten-day period (strictly more than)
BONUS_PER_LITRE = Decimal("0.50")     # Rs per litre on ALL litres of the period

FAT_MIN, FAT_MAX = Decimal("2.00"), Decimal("7.00")
SNF_MIN, SNF_MAX = Decimal("6.00"), Decimal("10.00")


def money(x):
    return x.quantize(PAISE, rounding=ROUND_HALF_UP)


def season_for(day):
    """Return the rate-card name for a datetime.date."""
    return "summer" if day.month in SUMMER_MONTHS else "standard"


def rate_per_litre(fat, snf, season="standard"):
    """Rate in Rs/litre, rounded to paise. fat/snf are strings or Decimals (2 decimals ok)."""
    fat, snf = Decimal(str(fat)), Decimal(str(snf))
    if not (FAT_MIN <= fat <= FAT_MAX and SNF_MIN <= snf <= SNF_MAX):
        raise ValueError("fat or snf outside allowed range")
    card = RATE_CARDS[season]
    fat_steps = (fat - STD_FAT) / STEP      # exact fractional steps, e.g. 7.5
    snf_steps = (snf - STD_SNF) / STEP
    return money(card.base + fat_steps * card.fat_step + snf_steps * card.snf_step)


def payment(litres, fat, snf, season="standard"):
    """Milk amount for one delivery (no bonus)."""
    litres = Decimal(str(litres))
    if litres <= 0:
        raise ValueError("litres must be greater than 0")
    return money(litres * rate_per_litre(fat, snf, season))


def bonus(total_litres):
    """Ten-day volume bonus: Rs 0.50 on ALL litres when strictly more than 500 L."""
    total_litres = Decimal(str(total_litres))
    return money(total_litres * BONUS_PER_LITRE) if total_litres > BONUS_THRESHOLD else Decimal("0.00")


def ten_day_statement(entries):
    """entries: list of (date, litres, fat, snf). Season is chosen per entry from its date."""
    milk = Decimal("0.00")
    litres_sum = Decimal("0")
    for day, litres, fat, snf in entries:
        milk += payment(litres, fat, snf, season_for(day))
        litres_sum += Decimal(str(litres))
    b = bonus(litres_sum)
    return {"litres": litres_sum, "milk": milk, "bonus": b, "total": milk + b}


if __name__ == "__main__":
    print("rate 4.25/8.63 standard:", rate_per_litre("4.25", "8.63", "standard"))
    print("rate 4.25/8.63 summer  :", rate_per_litre("4.25", "8.63", "summer"))
    print(ten_day_statement([(date(2026, 5, 10), "510", "3.5", "8.5")]))

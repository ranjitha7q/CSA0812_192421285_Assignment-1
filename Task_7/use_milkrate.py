"""Second script: imports milkrate in three different ways."""
import milkrate
from milkrate import payment
import milkrate as mr
import sys
import math
from decimal import Decimal

print("milkrate.rate_per_litre(4.2, 8.7) =", milkrate.rate_per_litre(4.2, 8.7))
print("payment(8.5, 4.2, 8.7)            =", payment(8.5, 4.2, 8.7))
print("mr.BASE_RATE                       =", mr.BASE_RATE)
print("milkrate.__name__                  =", milkrate.__name__, "(not '__main__', so the test block did not run)")
print("this script's __name__             =", __name__)
print("module cached in sys.modules       =", "milkrate" in sys.modules)
print("math.floor(2.7) =", math.floor(2.7), "| Decimal('0.1')+Decimal('0.2') =", Decimal("0.1") + Decimal("0.2"))
print("first 2 module search paths        =", sys.path[:2])

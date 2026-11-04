"""Task 5 - Alternative concept: try/except float() vs string-method checks."""
import time


def check_str(text):
    t = text.strip()
    if t.count(".") > 1 or t in ("", "."):
        return False
    return t.replace(".", "", 1).isdigit()


def check_try(text):
    try:
        float(text)
        return True
    except ValueError:
        return False


samples = ["8.5", " 8.5 ", "eight", "8.5.1", "", "-3", "1e3", "nan", "inf", "8,5"]
print(f"{'input':10}{'str-method':>12}{'try/float':>12}")
for s in samples:
    print(f"{s!r:10}{str(check_str(s)):>12}{str(check_try(s)):>12}")

print("\nNote: try/float accepts 'nan', 'inf', '1e3' and negatives -> these need")
print("extra checks (math.isfinite, range checks) before they are safe for money.")

N = 300_000
for name, fn in [("str-method", check_str), ("try/float", check_try)]:
    for label, value in [("valid ' 8.5 '", " 8.5 "), ("invalid 'eight'", "eight")]:
        t0 = time.perf_counter()
        for _ in range(N):
            fn(value)
        print(f"{name:11} {label:16}: {(time.perf_counter() - t0) / N * 1e9:8.0f} ns/entry")

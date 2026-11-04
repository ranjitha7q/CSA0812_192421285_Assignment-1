# Task 8 - Pseudocode (written before the Python code)

## A. Payment for one entry

```
START
INPUT litres, fat, snf
SET fat_steps TO round((fat - 3.5) / 0.1)
SET snf_steps TO round((snf - 8.5) / 0.1)
SET rate TO 30.00 + fat_steps * 0.40 + snf_steps * 0.30
SET rate TO rate rounded to 2 decimals
SET payment TO litres * rate
SET payment TO payment rounded to 2 decimals
OUTPUT payment
END
```

## B. Ten-day total for one farmer (running total)

```
START
SET total TO 0
FOR EACH entry IN entries
    IF entry is valid THEN
        SET total TO total + payment(entry)
    ELSE
        OUTPUT "invalid entry"
    ENDIF
ENDFOR
OUTPUT total
END
```

## C. Validation of one entry (flowchart in flowchart_validation.png)

```
START
INPUT litres, fat, snf
IF litres, fat or snf is not a number THEN
    OUTPUT "invalid: not a number"
ELSE
    IF litres <= 0 THEN
        OUTPUT "invalid: litres"
    ELSE
        IF fat < 2.0 OR fat > 7.0 THEN
            OUTPUT "invalid: fat"
        ELSE
            IF snf < 6.0 OR snf > 10.0 THEN
                OUTPUT "invalid: snf"
            ELSE
                OUTPUT "valid"
            ENDIF
        ENDIF
    ENDIF
ENDIF
END
```

## D. Hand trace (3 entries)

| Entry | litres | fat | snf | fat_steps | snf_steps | rate | payment | running total |
|---|---|---|---|---|---|---|---|---|
| start | | | | | | | | 0.00 |
| 1 | 10   | 3.5 | 8.5 | 0  | 0  | 30.00 | 300.00 | 300.00 |
| 2 | 8.5  | 4.2 | 8.7 | 7  | 2  | 30 + 2.80 + 0.60 = 33.40 | 283.90 | 583.90 |
| 3 | 12   | 3.1 | 8.2 | -4 | -3 | 30 - 1.60 - 0.90 = 27.50 | 330.00 | 913.90 |

Final OUTPUT total = 913.90 (matches `trace_check.py`).

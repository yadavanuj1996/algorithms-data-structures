Here's everything we covered on bit manipulation, in one place:

## Core operators

| Operator | What it does | Example |
|---|---|---|
| `n & 1` | Grabs the **last bit** (1 = odd, 0 = even) | `13 & 1` → `1101 & 0001` = 1 |
| `n >> 1` | Right shift — drops last bit, halves the number | `13 >> 1` → `1101` becomes `110` (6) |
| `n << 1` | Left shift — doubles, adds a 0 at the end | `3 << 1` → `11` becomes `110` (6) |
| `result \| bit` | OR — sets/places a bit | `110 \| 1` = `111` |
| `a ^ a = 0` | XOR — identical numbers cancel out | `5 ^ 5` = 0, `5 ^ 0` = 5 |
| `n & (n-1)` | Removes the **lowest set bit** | `1100 & 1011` = `1000` |
| `n >>= 1` | Shorthand for `n = n >> 1` (assigns back!) | `n >> 1` alone changes nothing |

## The three problem patterns

**1. Missing Number → XOR trick**
XOR all indices with all values — pairs cancel, the missing number survives.
`[3,0,1]`: `0^1^2^3 ^ 3^0^1` = `2` ✅

**2. Counting 1-bits → check & shift**
Loop: `count += n & 1`, then `n >>= 1`, until `n` is 0. Use `while n:` — bit-width doesn't matter here.
Faster alternative: `n = n & (n-1)` loops once per set bit only (Brian Kernighan).

**3. Reverse Bits → shift-then-OR reconstruction**
```python
res = 0
for _ in range(32):
    res = (res << 1) | (n & 1)
    n >>= 1
```
- **Shift `res` BEFORE placing the bit** — shift-after pushes your last bit one position too far
- **`range(32)`, not `while n:`** — fixed bit-width means leading zeros matter (they become trailing zeros in the result). `while n:` stops early and loses them
- The 32 = the problem's stated bit-width, nothing to do with the input's value. 16-bit problem → `range(16)`

## Key distinctions we clarified

- **Reverse ≠ Flip.** Reverse reorders positions (read the bits backwards); flip inverts values (0↔1, positions unchanged). `1000` reversed = `0001`, flipped = `0111`.

## When to use what

- Fixed-width problems (reverse, "32-bit integer" stated) → `for _ in range(width)`
- Counting/extracting until done → `while n:`
- Finding the lone unpaired number → XOR
- Fast set-bit counting → `n & (n-1)`

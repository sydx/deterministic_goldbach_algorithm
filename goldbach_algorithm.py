from sympy import isprime, primerange
from fractions import Fraction

# Define OEIS A026741
def a026741(n):
    return n if n % 2 == 1 else n // 2

# Construct the imbalance trail as per the updated definition
def imbalance_trail(p):
    return [
        Fraction(a026741(k), a026741(2 * p - k))
        for k in range(1, p)
        if a026741(2 * p - k) != 0
    ]

# Constructive Goldbach algorithm using updated imbalance
# trail definition
def goldbach_via_updated_imbalance(max_even=100):
    results = []
    for n in range(4, max_even + 1, 2):
        t = 2 * n - 1
        found = False
        for p in primerange(2, 2 * n):
            trail = imbalance_trail(p)
            denominators = [frac.denominator for frac in trail]
            if t in denominators:
                q = 2 * n - p
                if isprime(q):
                    results.append((2 * n, tuple(sorted((p, q)))))
                    found = True
                    break
        if not found:
            results.append((2 * n, None))
    return results

results = goldbach_via_updated_imbalance(150)

import pandas as pd

df = pd.DataFrame(results,
    columns=["Even Number",
             "Goldbach Pair (via Updated Imbalance Trail)"])
print(df)

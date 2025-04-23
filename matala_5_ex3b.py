import random
import time
import matplotlib.pyplot as plt
from typing import List

def egalitarian_min_value(valuations: List[List[int]]) -> float:
    """
    State-space search for egalitarian allocation; returns the maximum
    achievable minimum player value, using the same pruning rules from part (a).
    """
    n = len(valuations)
    m = len(valuations[0]) if n else 0

    # Precompute per-item upper bounds
    max_vals = [max(valuations[p][j] for p in range(n)) for j in range(m)]
    suffix_max = [0] * (m + 1)
    for j in range(m - 1, -1, -1):
        suffix_max[j] = suffix_max[j + 1] + max_vals[j]

    best_min = -float('inf')
    player_vals = [0] * n

    def dfs(idx: int):
        nonlocal best_min
        if idx == m:
            # all items assigned
            best_min = max(best_min, min(player_vals))
            return
        # prune if even giving all remaining to worst can't beat best_min
        if min(player_vals) + suffix_max[idx] <= best_min:
            return
        seen = set()
        for p in range(n):
            v = valuations[p][idx]
            if v in seen:
                continue
            seen.add(v)
            player_vals[p] += v
            dfs(idx + 1)
            player_vals[p] -= v

    dfs(0)
    return best_min

# --- Part 3(b) performance test ---

players_list = [2, 3, 4]
item_counts  = list(range(2, 9))   # number of items from 2 to 8
trials       = 5                   # average over 5 random trials

runtimes = {p: [] for p in players_list}

for p in players_list:
    for m in item_counts:
        elapsed = 0.0
        for _ in range(trials):
            # random valuations between 1 and 2^32
            vals = [
                [random.randint(1, 2**32) for _ in range(m)]
                for _ in range(p)
            ]
            start = time.perf_counter()
            _ = egalitarian_min_value(vals)
            elapsed += time.perf_counter() - start
        runtimes[p].append(elapsed / trials)

# Plot the results
plt.figure()
for p in players_list:
    plt.plot(item_counts, runtimes[p], marker='o', label=f"{p} players")
plt.xlabel("Number of items")
plt.ylabel("Average runtime (seconds)")
plt.title("Egalitarian Allocation Search Runtime")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

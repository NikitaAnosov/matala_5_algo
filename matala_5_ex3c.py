import random
import time
import matplotlib.pyplot as plt
from typing import List

def improved_egalitarian_min_value(valuations: List[List[int]]) -> float:
    """
    Exact egalitarian allocation with two extra heuristics:
      1. Sort items by descending maximum valuation.
      2. Initialize the best‐min value via a greedy assignment.
    Returns the maximum achievable minimum player value.
    """
    n = len(valuations)
    m = len(valuations[0]) if n else 0

    # 1) Compute each item's max valuation and sort items descendingly
    max_vals = [max(valuations[p][j] for p in range(n)) for j in range(m)]
    order = sorted(range(m), key=lambda j: -max_vals[j])
    # Reorder the valuation matrix
    reordered = [[valuations[p][j] for j in order] for p in range(n)]

    # 2) Build suffix_max on sorted items
    sorted_max = [max(reordered[p][k] for p in range(n)) for k in range(m)]
    suffix_max = [0]*(m+1)
    for k in range(m-1, -1, -1):
        suffix_max[k] = suffix_max[k+1] + sorted_max[k]

    # 3) Greedy initial bound: always give each item to the currently worst-off player
    player_vals = [0]*n
    for k in range(m):
        p_min = min(range(n), key=lambda p: player_vals[p])
        player_vals[p_min] += reordered[p_min][k]
    best_min = min(player_vals)

    # 4) Exact DFS with bounding & symmetry-breaking on the sorted items
    player_vals = [0]*n
    def dfs(idx: int):
        nonlocal best_min
        if idx == m:
            best_min = max(best_min, min(player_vals))
            return
        # bound: even if the worst-off gets all remaining, can't exceed best_min ⇒ prune
        if min(player_vals) + suffix_max[idx] <= best_min:
            return
        seen = set()
        for p in range(n):
            v = reordered[p][idx]
            if v in seen:           # symmetry-breaking
                continue
            seen.add(v)
            player_vals[p] += v
            dfs(idx+1)
            player_vals[p] -= v

    dfs(0)
    return best_min

if __name__ == "__main__":
    # --- Part 3(c) Performance Test ---
    players_list = [2, 3, 4]
    item_counts  = list(range(2, 9))   # test from 2 to 8 items
    trials       = 5
    runtimes     = {p: [] for p in players_list}

    for p in players_list:
        for m in item_counts:
            total_time = 0.0
            for _ in range(trials):
                # random valuations in [1, 2^32]
                vals = [
                    [random.randint(1, 2**32) for _ in range(m)]
                    for _ in range(p)
                ]
                start = time.perf_counter()
                _ = improved_egalitarian_min_value(vals)
                total_time += (time.perf_counter() - start)
            runtimes[p].append(total_time / trials)

    # Plot the results
    plt.figure()
    for p in players_list:
        plt.plot(item_counts, runtimes[p], marker='o', label=f"{p} players")
    plt.xlabel("Number of items")
    plt.ylabel("Average runtime (seconds)")
    plt.title("Improved Egalitarian Allocation Runtime\n(values ∈ [1, 2^32])")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

from typing import List
import copy
import random
import time
import matplotlib.pyplot as plt
from typing import List

def egalitarian_allocation(valuations: List[List[float]]) -> None:
    """
    Finds and prints an egalitarian allocation (maximizing the minimum player value)
    by exhaustive search with two pruning rules:
      1) Bound: if even the best-case addition of all remaining items to the current
         worst-off player cannot exceed the current best min-value, prune.
      2) Symmetry-breaking: for each item, only assign it to the first player seen
         for each distinct valuation, skipping duplicates.
    """
    n = len(valuations)
    m = len(valuations[0]) if n > 0 else 0

    # Precompute, for each item j, the max value any player assigns to it
    max_vals = [max(valuations[p][j] for p in range(n)) for j in range(m)]
    # suffix_max[j] = sum of max_vals[j..m-1]
    suffix_max = [0] * (m + 1)
    for j in range(m - 1, -1, -1):
        suffix_max[j] = suffix_max[j + 1] + max_vals[j]

    best_min_value = -float('inf')
    best_alloc = None

    # current partial allocation: list of item‐lists per player,
    # and the current total values per player
    current_alloc = [[] for _ in range(n)]
    player_values = [0] * n

    def dfs(item_idx: int):
        nonlocal best_min_value, best_alloc

        # If all items assigned, check and possibly update best solution
        if item_idx == m:
            curr_min = min(player_values)
            if curr_min > best_min_value:
                best_min_value = curr_min
                best_alloc = copy.deepcopy(current_alloc)
            return

        # Prune by bounding
        worst_now = min(player_values)
        if worst_now + suffix_max[item_idx] <= best_min_value:
            return

        seen_vals = set()
        for p in range(n):
            v = valuations[p][item_idx]
            if v in seen_vals:
                continue
            seen_vals.add(v)

            # assign item to player p
            current_alloc[p].append(item_idx)
            player_values[p] += v

            dfs(item_idx + 1)

            # undo
            player_values[p] -= v
            current_alloc[p].pop()

    dfs(0)

    # Print the best allocation found
    for p in range(n):
        items = best_alloc[p]
        total = sum(valuations[p][j] for j in items)
        item_list = ", ".join(map(str, items))
        print(f"Player {p} gets items {item_list} with value {total}")



# Example usage:
if __name__ == "__main__":
    egalitarian_allocation([[4, 5, 6, 7, 8],
                            [8, 7, 6, 5, 4]])



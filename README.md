# Egalitarian Allocation (Question 3)

This repository contains a Python implementation of the **egalitarian allocation** algorithm for fair division of discrete items among players.

- **(a)** A full state-space search (`egalitarian_allocation`) with two pruning rules:
  1. **Bounding rule**: prune branches where even optimal remaining assignment cannot improve the current best minimum value.
  2. **Symmetry-breaking rule**: skip duplicate valuation assignments to avoid equivalent subtrees.

- **(b)** A performance test script (`matala_5_ex3b.py`) that:
  - Generates random valuation matrices (values in \[1, 2<sup>32</sup>\]).
  - Measures average runtime of the search for 2, 3, and 4 players as a function of the number of items.
  - Plots the resulting runtime-vs-items graph.

- **(c)** An improved search script (`matala_5_ex3c.py`) with two additional heuristics:
  1. **Item sorting**: by descending maximum valuation to front-load high-value items.
  2. **Greedy initial bound**: by computing an initial allocation giving each item to the current worst-off player.
  - Plots the resulting runtime-vs-items graph.

---

## File Structure

- `matala_5_ex3a.py`  
  Contains the `egalitarian_allocation(valuations: List[List[float]])` function and code for part (a).

- `matala_5_ex3b.py`  
  Implements the performance test for part (b) and produces a matplotlib plot.

  - `matala_5_ex3c.py`  
  Implements the improved search with sorting and greedy bound for part (c), plus its performance test and plot.

- `README.md`  
  This documentation file.

---

## Requirements

- Python 3.7+
- `matplotlib` (for plotting in part (b))

You can install Matplotlib via pip:

```bash
pip install matplotlib

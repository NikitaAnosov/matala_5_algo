# Egalitarian Allocation (Question 3)

This repository contains a Python implementation of the **egalitarian allocation** algorithm for fair division of discrete items among players.

- **(a)** A full state-space search (`egalitarian_allocation`) with two pruning rules:
  1. **Bounding rule**: prune branches where even optimal remaining assignment cannot improve the current best minimum value.
  2. **Symmetry-breaking rule**: skip duplicate valuation assignments to avoid equivalent subtrees.

- **(b)** A performance test script (`test_egalitarian_runtime.py`) that:
  - Generates random valuation matrices (values in \[1, 2<sup>32</sup>\]).
  - Measures average runtime of the search for 2, 3, and 4 players as a function of the number of items.
  - Plots the resulting runtime-vs-items graph.

---

## File Structure

- `matala_5_ex3a.py`  
  Contains the `egalitarian_allocation(valuations: List[List[float]])` function and supporting code for part (a).

- `matala_5_ex3b.py`  
  Implements the performance test for part (b) and produces a matplotlib plot.

- `README.md`  
  This documentation file.

---

## Requirements

- Python 3.7+
- `matplotlib` (for plotting in part (b))

You can install Matplotlib via pip:

```bash
pip install matplotlib

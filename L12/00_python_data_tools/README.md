# Python Data Tools — tutorial

> **Tour of the pandas / numpy / scipy / matplotlib / sklearn functions used in the L11 + L12 starter notebooks.** Read this if anything in a starter notebook looks unfamiliar.

## What's in here

- [`python_data_tools_starter.ipynb`](python_data_tools_starter.ipynb) — ~30 cells, ~30 minutes if you read it carefully.

Five sections:

1. **pandas** — DataFrames, `read_csv`, column/row selection, `apply`, `value_counts`, building from a list of dicts.
2. **numpy** — element-wise math, `diff`, `arange`, `argmax`, `polyfit`.
3. **scipy.signal** — `find_peaks`, `correlate` (with the cross-correlation explained).
4. **matplotlib** — `subplots` / `ax.plot` / `ax.scatter` / `ax.hist` / annotation lines.
5. **sklearn refresher** — the L11 train/fit/score recipe in one self-contained cell.

Closes with a one-page reference card mapping each function to *which project notebook uses it* — useful for `Ctrl+F` lookups while you work.

## Why this exists separately

The project starters jump straight into "load a CSV, slide a window, fit a classifier" because they need to fit in 90 minutes of lecture. If you're new to pandas/numpy, those starters skim past the libraries fast. This tutorial is the runway: every function gets a tiny standalone example with made-up data so you can change a value and see what happens, without the noise of a real recording or a full ML pipeline.

## Order of operations (recommended)

1. Skim this notebook (~30 min). Run every cell. Change values. Re-run.
2. Open the project starter you signed up for. The functions should now feel familiar.
3. When something *still* looks new, search this notebook (`Ctrl+F` / `Cmd+F`) — every function used by the starters appears here at least once.

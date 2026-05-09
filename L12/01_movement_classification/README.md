# Project 1 — Movement classification

> **Recognize basic dance moves (jump, spin, hold, step) from wrist-mounted accelerometer data.**

> **New to pandas / numpy / sklearn?** Skim [`../00_python_data_tools/python_data_tools_starter.ipynb`](../00_python_data_tools/python_data_tools_starter.ipynb) first — it's a 30-minute tour of every function the L11 + L12 starters use, with tiny standalone examples.

## Reference implementation

You already built this in **L11**. There's no separate L12 starter — the L11 notebook *is* the reference.

- Notebook: [`../../L11/L11_starter.ipynb`](../../L11/L11_starter.ipynb)
- Sample data: [`../../data/sample-still-walk-jump.csv`](../../data/sample-still-walk-jump.csv)
- Wearable program: [`../../L11/wearable_datalogger.py`](../../L11/wearable_datalogger.py)

If you pick this project for L13–L15, you are making the L11 work *better and bigger*, not starting from scratch.

## What the L11 starter gives you

- Wearable datalogger program for the micro:bit (records X/Y/Z to onboard flash).
- A notebook that loads the CSV, plots magnitude, labels segments, computes 6 features per 1-second window, and trains a depth-3 decision tree.
- A confusion matrix you can read.
- A digit-recognition bonus to show the same recipe scales to other data.

## What to build next (pick one as your L13 starting goal)

1. **Add a movement class.** Record `spin`, `wave`, or `squat` and add it to the labels. How does the confusion matrix change?
2. **Try a different model.** Swap `DecisionTreeClassifier` for `KNeighborsClassifier` or `RandomForestClassifier`. Does accuracy change? Does *interpretability* change?
3. **Cut features.** Train on only 2–3 features instead of 6. Find the smallest feature set that still works — fewer features = less code on-device.
4. **Multi-dancer test.** Record two students doing the same moves. Train on student A, test on student B. (Spoiler: it usually doesn't transfer well — that's the lesson.)
5. **Live deployment.** Run the trained tree *on the micro:bit* so it cues lanterns in real time. This is essentially **Project 6** — see that folder for the export-to-`if/elif` recipe.

## What you need

- 1× micro:bit v2 + battery pack + armband (per recording session).
- A laptop with Colab access.
- *(For multi-dancer or live deployment)* a second micro:bit.

## What to read before L13

Re-run the L11 notebook end-to-end on the bundled sample CSV. Then re-run it on **your** L11 homework recording. If anything breaks, fix it first — your L13 work will build on top.

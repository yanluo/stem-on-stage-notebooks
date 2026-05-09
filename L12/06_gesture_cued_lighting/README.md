# Project 6 — Gesture-cued lighting

> **Train a tiny gesture classifier in Colab, deploy it onto a wearable micro:bit, and have the dancer's gestures cue lantern colors over radio.**

## What's in here

- [`gesture_lighting_starter.ipynb`](gesture_lighting_starter.ipynb) — trains a depth-3 decision tree on the L11 still/walk/jump dataset, then **exports the tree as plain Python `if/elif`** that you paste into the device program.
- [`wearable_gesture.py`](wearable_gesture.py) — MakeCode Python program that reads accelerometer data, computes the same 6 features the model was trained on, runs the pasted-in `predict(...)`, and broadcasts `radio.send_string("color:<label>")` whenever the predicted label changes.

## Why this is the ambitious project

It stitches together everything from the course:

- **L4** — radio messaging.
- **L7** — the lantern controller that picks up `color:` cues.
- **L9** — accelerometer reads.
- **L11** — feature engineering and decision-tree classification.

The new piece is **deployment**: getting the trained model out of Colab and onto a battery-powered board. The trick is "tree → `if/elif`": a depth-3 decision tree is six lines of Python, no dependencies, no model file to load.

## What you need

- 1× micro:bit v2 + battery + wrist strap.
- A laptop with Colab access (for training).
- Optional second micro:bit running the L7 lantern controller — to actually see the cues land somewhere visible.

## End-to-end workflow

1. Open the notebook → train → see the printed `predict(...)` function.
2. Copy that function. Open `wearable_gesture.py`. Paste between the `# ----- PASTE FROM NOTEBOOK -----` markers (replacing the bundled placeholder predict, which is trained on the L11 sample).
3. Open [https://makecode.microbit.org/](https://makecode.microbit.org/), switch to Python view, paste the *whole file*, click Download to flash a battery-powered board.
4. Strap to a dancer's wrist. The board's LED shows the predicted move (square / stick figure / diamond). Each label change sends a radio cue on group 7.
5. Wire the radio messages into your L7 lantern controller — when it sees `color:walk`, it picks the walk pattern.

## What to build next (pick one as your L13 goal)

1. **Train on *your* gestures.** Capture a recording with `arms-up`, `clap`, `twirl` (or whatever maps to lantern moods you want). Re-run the notebook on it. Re-paste the new `predict()`. The wearable file doesn't change.
2. **Hysteresis.** Only fire a cue if the same label is predicted for 3 windows in a row, otherwise the lanterns will flicker between classes during transitions.
3. **Richer cue.** Each label drives both a NeoPixel color *and* a pattern (e.g., `twirl` → chase pattern, `clap` → flash).
4. **Compare against L10.** L10 used a hand-tuned threshold (`if mag > 2200: jump`). Run that detector and the trained tree side by side on the same recording. Which is more reliable on stage?
5. **Confidence gating.** Replace the tree with a `RandomForestClassifier` and only fire a cue if 7 of 10 trees agree. Quieter, but more reliable.

## Pitfalls and gotchas

- **Feature consistency is critical.** The notebook computes features on a 1-second window at 20 Hz. The wearable does the same, in the same order, with the same formulas. If you change one side, change both.
- **`std_mag` definition.** Pandas' `chunk["mag"].std()` uses the *sample* standard deviation (divide by N–1) by default. The wearable uses the *population* version (divide by N). For 20 samples this difference is small but visible. If your tree retrains and the device misclassifies, this is one place to check — match `ddof=0` in the notebook or change the device math.
- **MakeCode Python list ops.** `list.pop(0)` is O(n). At 20 Hz with a 20-element buffer this is fine; if you push the sample rate to 50+ Hz, switch to a ring buffer.
- **Radio group must match.** The wearable uses `radio.set_group(7)`. The lantern controller must be on the same group, or your cues vanish into the ether.

# Project 4 — Beat tracker

> **Estimate the dancer's tempo (BPM) from accelerometer data, so the lanterns can pulse with the dance.**

## What's in here

- [`beat_starter.ipynb`](beat_starter.ipynb) — load 30 s of synthetic motion → peak counting → autocorrelation → BPM-over-time plot.
- [`wearable_beat.py`](wearable_beat.py) — MakeCode Python that detects beats live, blinks the LED, and broadcasts `radio.send_value("beat", n)` on group 7 (the L4–L7 lantern group).
- [`../../data/sample-beat.csv`](../../data/sample-beat.csv) — 30 s synthetic recording at 50 Hz, tempo steps from 120 BPM down to 100 BPM at t=20 s.

## Why this project is worth it

Every other project is *analysis* — you collect data, run code on a laptop, look at a plot. This one closes the loop: motion goes in, light comes out, in real time. It's the most visually satisfying live demo of the six.

## What you need

- 1× micro:bit v2 + battery + arm/wrist strap.
- The L4–L7 lantern stack (or just one micro:bit running the lantern controller for testing).
- A laptop with Colab access (for the analysis side).

## Two methods, when to use which

| Method            | Strength                                | Weakness                              |
|-------------------|-----------------------------------------|---------------------------------------|
| Peak counting     | Simple, runs on-device, gives per-beat events for the radio | Sensitive to threshold; misses beats with shallow peaks |
| Autocorrelation   | Robust to noise; doesn't need a threshold | Gives a period, not a beat — no per-beat event for blinking |

The on-device wearable uses peak counting (autocorrelation is too heavy for MicroPython). On the laptop, autocorrelation is the better second opinion.

## What to build next (pick one as your L13 goal)

1. **Lantern integration.** Wire the `"beat"` radio messages into the L7 controller so the NeoPixels pulse on every beat.
2. **Compare to ground truth.** Look up the song's BPM on Spotify, run the dancer with that song, report the error.
3. **Bandpass filter** the magnitude before `find_peaks` (1–4 Hz, since dance tempos live there). Kills high-frequency jitter.
4. **Phase-aware color.** Track every 4th beat as the downbeat → brighter color on the downbeat.
5. **Drop-out recovery.** When the dancer freezes for 2 s, the detector finds no beats. Decide what the lanterns do — hold last good tempo, fade out, lock to a fallback?

## Tuning the wearable

`THRESHOLD_OFFSET = 250` mg is tuned for moderately energetic motion. For a slow dance you'll want lower (~150 mg); for high-impact choreography, higher. Watch the LED — if it blinks faster than your foot taps, raise it; if it misses obvious beats, lower it.

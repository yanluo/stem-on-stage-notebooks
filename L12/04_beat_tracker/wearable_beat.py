# Wearable beat tracker for micro:bit v2 (MakeCode Python).
# Paste into https://makecode.microbit.org/ -> Python view, then flash.
#
# - Reads acceleration magnitude at 50 Hz.
# - Detects a beat when |a| crosses a threshold above its short-term average,
#   with a 300 ms cooldown between beats (caps detectable BPM at 200).
# - Blinks the LED on each detected beat.
# - Broadcasts radio.send_value("beat", n) so the L7 lantern controller can pulse.

radio.set_group(7)                  # match the lantern group from L4-L7

THRESHOLD_OFFSET = 250              # mg above moving baseline
COOLDOWN_MS      = 300

baseline_mg = 1000                  # starts at gravity, will adapt
beat_count  = 0
last_beat_t = -10000


def update_baseline(mag):
    # Slow exponential moving average; ~1 second time-constant at 50 Hz
    global baseline_mg
    baseline_mg = baseline_mg + (mag - baseline_mg) * 0.02


def on_forever():
    global beat_count, last_beat_t
    mag = input.acceleration(Dimension.STRENGTH)
    now = input.running_time()
    update_baseline(mag)
    if mag > baseline_mg + THRESHOLD_OFFSET and (now - last_beat_t) > COOLDOWN_MS:
        beat_count  += 1
        last_beat_t = now
        basic.show_icon(IconNames.SMALL_DIAMOND)
        radio.send_value("beat", beat_count)
    basic.pause(20)                 # 50 Hz

basic.forever(on_forever)

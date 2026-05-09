# Wearable gesture-cued lighting controller for micro:bit v2 (MakeCode Python).
# Paste into https://makecode.microbit.org/ -> Python view, then flash.
#
# How it works:
#   1) Reads accelerometer at 20 Hz into a 1-second sliding buffer (20 samples).
#   2) Once the buffer is full, computes 6 features matching the L11 notebook:
#        mean_mag, std_mag, max_mag, range_x, range_y, range_z
#   3) Runs predict() — a decision tree exported from the L12 starter notebook.
#   4) When the predicted label changes, sends radio.send_string("color:<label>")
#      so the L7 lantern controller can pick up the cue.
#
# To retrain on YOUR gestures:
#   - run gesture_lighting_starter.ipynb on your captured CSV
#   - copy the printed predict(...) block
#   - paste it between the markers below

import math

radio.set_group(7)             # match the lantern group from L4-L7

WINDOW_SIZE = 20               # 1 s at 20 Hz

buf_x = []
buf_y = []
buf_z = []
buf_mag = []
last_label = ""


# ----- PASTE FROM NOTEBOOK -----
def predict(mean_mag, std_mag, max_mag, range_x, range_y, range_z):
    if std_mag <= 185.28:
        return "still"
    else:
        if mean_mag <= 1187.62:
            return "walk"
        else:
            return "jump"
# ----- END PASTE ---------------


def show_label(label):
    if label == "still":
        basic.show_icon(IconNames.SQUARE)
    elif label == "walk":
        basic.show_icon(IconNames.STICK_FIGURE)
    elif label == "jump":
        basic.show_icon(IconNames.DIAMOND)
    else:
        basic.show_icon(IconNames.QUESTION)


def on_forever():
    global last_label
    x = input.acceleration(Dimension.X)
    y = input.acceleration(Dimension.Y)
    z = input.acceleration(Dimension.Z)
    mag = math.sqrt(x * x + y * y + z * z)

    buf_x.append(x)
    buf_y.append(y)
    buf_z.append(z)
    buf_mag.append(mag)

    if len(buf_mag) > WINDOW_SIZE:
        buf_x.pop(0)
        buf_y.pop(0)
        buf_z.pop(0)
        buf_mag.pop(0)

    if len(buf_mag) == WINDOW_SIZE:
        # Pass 1: sums and extrema
        total = 0
        max_mag = buf_mag[0]
        min_x = buf_x[0]; max_x = buf_x[0]
        min_y = buf_y[0]; max_y = buf_y[0]
        min_z = buf_z[0]; max_z = buf_z[0]
        for i in range(WINDOW_SIZE):
            total += buf_mag[i]
            if buf_mag[i] > max_mag: max_mag = buf_mag[i]
            if buf_x[i] < min_x: min_x = buf_x[i]
            if buf_x[i] > max_x: max_x = buf_x[i]
            if buf_y[i] < min_y: min_y = buf_y[i]
            if buf_y[i] > max_y: max_y = buf_y[i]
            if buf_z[i] < min_z: min_z = buf_z[i]
            if buf_z[i] > max_z: max_z = buf_z[i]

        mean_mag = total / WINDOW_SIZE

        # Pass 2: variance for std
        var_total = 0
        for i in range(WINDOW_SIZE):
            d = buf_mag[i] - mean_mag
            var_total += d * d
        std_mag = math.sqrt(var_total / WINDOW_SIZE)

        range_x = max_x - min_x
        range_y = max_y - min_y
        range_z = max_z - min_z

        label = predict(mean_mag, std_mag, max_mag, range_x, range_y, range_z)

        if label != last_label:
            last_label = label
            show_label(label)
            radio.send_string("color:" + label)

    basic.pause(50)            # 20 Hz sampling

basic.forever(on_forever)

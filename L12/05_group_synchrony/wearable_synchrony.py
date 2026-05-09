# Judge board for L12/05 group synchrony (MakeCode Python, micro:bit v2).
# Paste into https://makecode.microbit.org/ -> Python view, then flash.
#
# This is the third board in the synchrony rig. It listens to BOTH dancer
# wearables (wearable_dancer.py with ROLE="A" and ROLE="B"), buffers each
# stream into a 1-second sliding window, computes a windowed Pearson
# correlation every second, and broadcasts a color cue to the lanterns.
#
# Architecture:
#
#   [dancer A wearable] --radio "magA" 20 Hz-->
#                                                [judge board, this file]
#   [dancer B wearable] --radio "magB" 20 Hz-->          |
#                                                  computes r every 1 s
#                                                  broadcasts "color:..."
#                                                          |
#                                                          v
#                                                    [lanterns on group 7]
#
# All four boards share radio group 7. The lantern controller from L4-L7
# picks up the "color:" string messages; it ignores the dancers' value
# messages so there's no cross-talk.
#
# Why this works without numpy: Pearson correlation has a closed-form
# expression (see correlation() below) that's just five running sums and
# one square root -- all in MakeCode's math library.

import math

radio.set_group(7)
basic.show_string("J")        # "J" = judge

WINDOW = 20                   # samples per buffer (1 s at 20 Hz)
THRESHOLD_GREEN  = 0.7
THRESHOLD_YELLOW = 0.3

bufA = []
bufB = []
last_color = ""
last_score_ms = 0


def on_received(name, value):
    if name == "magA":
        bufA.append(value)
        if len(bufA) > WINDOW:
            bufA.pop(0)
    elif name == "magB":
        bufB.append(value)
        if len(bufB) > WINDOW:
            bufB.pop(0)

radio.on_received_value(on_received)


def correlation():
    """Pearson r over the last n paired samples. Returns None if not enough
    data or if either signal is constant (variance = 0)."""
    n = min(len(bufA), len(bufB))
    if n < 5:
        return None

    # Run through the last n samples of each buffer, accumulating the
    # five sums needed for the closed-form Pearson formula.
    sumA = 0
    sumB = 0
    sumAA = 0
    sumBB = 0
    sumAB = 0
    for i in range(n):
        a = bufA[len(bufA) - n + i]
        b = bufB[len(bufB) - n + i]
        sumA  += a
        sumB  += b
        sumAA += a * a
        sumBB += b * b
        sumAB += a * b

    num = n * sumAB - sumA * sumB
    varA = n * sumAA - sumA * sumA
    varB = n * sumBB - sumB * sumB
    if varA <= 0 or varB <= 0:
        return None
    return num / math.sqrt(varA * varB)


def color_for(r):
    if r is None:
        return "unknown"
    if r > THRESHOLD_GREEN:
        return "green"
    if r > THRESHOLD_YELLOW:
        return "yellow"
    return "red"


def show(color):
    if color == "green":
        basic.show_icon(IconNames.YES)
    elif color == "yellow":
        basic.show_icon(IconNames.QUESTION)
    elif color == "red":
        basic.show_icon(IconNames.NO)
    else:
        basic.show_icon(IconNames.SMALL_DIAMOND)


def on_forever():
    global last_color, last_score_ms
    now = input.running_time()
    if now - last_score_ms < 1000:        # one score per second
        basic.pause(50)
        return
    last_score_ms = now

    r = correlation()
    color = color_for(r)
    if color != last_color:
        last_color = color
        show(color)
        if color != "unknown":
            radio.send_string("color:" + color)

basic.forever(on_forever)

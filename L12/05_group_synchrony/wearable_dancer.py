# Dancer broadcaster for L12/05 group synchrony (MakeCode Python, micro:bit v2).
# Paste into https://makecode.microbit.org/ -> Python view, then flash.
#
# Flash this onto BOTH dancers' boards. Set ROLE to "A" on one and "B" on the
# other before each flash. Strap to the wrist as in L11/Project 2 (LED matrix
# up, logo forward). At runtime the board shows "A" or "B" briefly so you can
# tell at a glance which one is which.
#
# What it does:
#   - reads accelerometer at 20 Hz, computes magnitude
#   - broadcasts radio.send_value("magA" or "magB", mag) on group 7
#
# Pairs with wearable_synchrony.py (the "judge" board) which receives both
# streams, computes a windowed Pearson correlation, and broadcasts a color
# cue to the lanterns.

import math

ROLE = "A"                    # <-- CHANGE TO "B" FOR THE SECOND DANCER

radio.set_group(7)            # match the lantern group from L4-L7
basic.show_string(ROLE)       # so you can see which role this board has

KEY = "mag" + ROLE            # "magA" or "magB"


def on_forever():
    x = input.acceleration(Dimension.X)
    y = input.acceleration(Dimension.Y)
    z = input.acceleration(Dimension.Z)
    mag = int(math.sqrt(x * x + y * y + z * z))
    radio.send_value(KEY, mag)
    basic.pause(50)           # 20 Hz

basic.forever(on_forever)

# Wearable pose recognizer for micro:bit v2 (MakeCode Python).
# Paste into https://makecode.microbit.org/ -> Python view, then flash.
#
# Reads pitch + roll (degrees) and shows a different LED icon per posture.
#
# Mounting: lay the board flat on top of your wrist with the LED matrix
# facing the ceiling and the logo pointing forward (away from your body).
# Hold the arm out, palm down. From this neutral pose:
#   - tip the hand fingers-down  -> "bending"  (pitch goes negative)
#   - twist the wrist thumb-up   -> "lying"    (roll grows past +/-40)
#   - everything else            -> "tilted"
#
# Thresholds below are tuned from real wrist-mount measurements; if your
# values look different on the console, retune the numbers in classify().

current = ""

def classify(pitch, roll):
    if abs(pitch) < 15 and abs(roll) < 15:
        return "upright"
    if pitch < -25:
        return "bending"
    if abs(roll) > 40:
        return "lying"
    return "tilted"


def show(pose):
    if pose == "upright":
        basic.show_icon(IconNames.HAPPY)
    elif pose == "bending":
        basic.show_icon(IconNames.SAD)
    elif pose == "lying":
        basic.show_icon(IconNames.ASLEEP)
    else:
        basic.show_icon(IconNames.CONFUSED)


def on_forever():
    global current
    pitch = input.rotation(Rotation.PITCH)
    roll  = input.rotation(Rotation.ROLL)
    pose  = classify(pitch, roll)
    serial.write_value("pitch", pitch)
    serial.write_value("roll",  roll)
    if pose != current:                # only redraw on a change
        current = pose
        show(pose)
        serial.write_line("pose=" + pose)
    basic.pause(200)                   # 5 Hz is plenty for posture

basic.forever(on_forever)

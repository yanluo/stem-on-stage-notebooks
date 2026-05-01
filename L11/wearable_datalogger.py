# Wearable datalogger for micro:bit v2 (MakeCode Python).
# Paste into https://python.microbit.org/ or MakeCode's Python view, then flash.
#
# Buttons:
#   A -> clear flash log and start recording (check icon)
#   B -> stop recording (X icon)
#
# After recording: plug the board into a laptop, open MICROBIT/MY_DATA.HTM,
# click Download to save as microbit-log-<name>.csv.

log.set_columns(["t", "x", "y", "z"])

recording = False
t0 = 0


def on_button_pressed_a():
    global recording, t0
    log.delete(full=True)               # clear previous run
    t0 = input.running_time()
    recording = True
    basic.show_icon(IconNames.YES)      # check = recording

input.on_button_pressed(Button.A, on_button_pressed_a)


def on_button_pressed_b():
    global recording
    recording = False
    basic.show_icon(IconNames.NO)       # X = stopped

input.on_button_pressed(Button.B, on_button_pressed_b)


def on_forever():
    if recording:
        log.log({
            "t": (input.running_time() - t0) / 1000,    # seconds since A pressed
            "x": input.acceleration(Dimension.X),
            "y": input.acceleration(Dimension.Y),
            "z": input.acceleration(Dimension.Z),
        })
    basic.pause(50)                     # ~20 Hz

basic.forever(on_forever)

def on_button_pressed_a():
    pass
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_tilt_left():
    radio.send_number(2)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_received_string(receivedString):
    basic.show_string(receivedString)
    basic.pause(1000)
radio.on_received_string(on_received_string)

def on_gesture_shake():
    radio.send_number(1)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_gesture_tilt_right():
    radio.send_number(3)
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

radio.set_group(24)
radio.set_transmit_power(7)
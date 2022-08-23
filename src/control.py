import pyfirmata

led_pin = 7
button_pin = 8

board = pyfirmata.Arduino("/dev/ttyACM0")

while True:
    if board.digital[button_pin].read(1):
        board.digital[led_pin].write(1)
    else:
        board.digital[led_pin].write(0)

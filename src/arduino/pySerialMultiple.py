#!/usr/bin/env python3
"""Control an Arduino over the USB port."""

# Imports
import serial
# Functions

USB_PORT = "COM3"  # Arduino windows
# USB_PORT = "/dev/ttyUSB0"  # Arduino Uno R3 Compatible
# USB_PORT = "/dev/ttyAMA0"  # Arduino Uno WiFi Rev2

usb = serial.Serial(USB_PORT, 9600, timeout=2)

def print_commands():
   """Prints available commands."""
   print("Available commands:")
   print("  a - Read Arduino value")
   print("  b - Send servo command")
   print("  x - Exit program")

def test_connection():
    # Main
    # Connect to USB serial port at 9600 baud
    # try:
    # except:
    #    print("ERROR - Could not open USB serial port.  Please check your port name and permissions.")
    #    print("Exiting program.")
    #    exit()
    # Send commands to Arduino
    print("Enter a command from the keyboard to send to the Arduino.")
    print_commands()
    while True:
        command = input("Enter command: ")
        if command == "a":  # read Arduino A0 pin value
            #   usb.write(b'<HelloWorld, 12, 24.7>')  # send command to Arduino
            line = usb.readline()  # read input from Arduino
            line = line.decode()  # convert type from bytes to string
            line = line.strip()  # strip extra whitespace characters
            print("Arduino: '" + line + "'")

            while line:
                line = usb.readline()  # read input from Arduino
                line = line.decode()  # convert type from bytes to string
                line = line.strip()  # strip extra whitespace characters
                print("Arduino: '" + line + "'")

        elif command == "b":  # send value
            direction = str(input("Enter move direction: "))
            msg = '<Servo, ' + direction +'>'
            usb.write(str.encode(msg))
            print("command sent: " + msg)
        elif command == "d":  # send value
            seconds = str(input("Enter delay millisecond: "))
            msg = '<ServoDelay, ' + seconds +'>'
            usb.write(str.encode(msg))
            print("command sent: " + msg)
        elif command == "x":  # exit program
            print("Exiting program.")
            exit()
        else:  # unknown command
            print("Unknown command '" + command + "'.")
            print_commands()


def sendCommand(command1, command2, command3, command4, command5, command6):
    direction = "%s, %s, %s, %s, %s, %s" % (command1, command2, command3, command4, command5, command6)
    msg = '<Servo, ' + direction +'>'
    usb.write(str.encode(msg))


if __name__ == '__main__':
    test_connection()

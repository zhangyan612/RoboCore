direction = str(input("Enter move direction: "))
msg = '<Servo, ' + direction +'>'
print("command sent: " + str(msg))


direction = "%s, %s, %s, %s, %s, %s" % (10, 3, 2, 3, 4, 2)
msg = '<Servo, ' + direction +'>'
print("command sent: " + str(msg))

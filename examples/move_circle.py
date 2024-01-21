import picar_4wd as fc
import time

def move25():
    speed4 = speed(25)
    speed4.start()
    time.sleep(2)
    fc.backward(100)
    x = 0
    for i in range(1):
        time.sleep(0.1)
        speed = speed4()
        x += speed*0.1
        print("%smm/s"%speed)
    print("%smm/s"%x)
    speed4.deinit()
    fc.stop()
        




# Constants
#MOVEMENT_DISTANCE_CM = 2.5  # Distance to move in centimeters
#WHEEL_DIAMETER_CM = 6.5   # Diameter of the wheels in centimeters

# Calculate the number of revolutions needed to cover the distance
#revolutions = MOVEMENT_DISTANCE_CM / (WHEEL_DIAMETER_CM * 3.14159)

# Set the speed of the car (adjust as needed)
#set_speed(20)

# Move backward by the calculated distance
#backward(revolutions)

# Allow time for the movement to complete
#time.sleep(2)

# Stop the car
#stop()

#try:
#    while True:
#        fc.forward(50)
#        time.sleep(1)
#finally:
#    fc.stop()
#    time.sleep(0.2)

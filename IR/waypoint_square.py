# Misc
import rclpy
def check_result(result, err_msg):
    if result is False:
        swimmer.set_autopilot_mode("off")
        swimmer.set_mode("safemode")
        swimmer.shutdown()
        raise Exception(err_msg)
        
import time

# Swimmer
from aqua2_navigation.swimmer import SwimmerAPI

# Creates an instance of the Swimmer API
swimmer = SwimmerAPI()
swimmer.start_spin()

# Calibrates the Robot. Important to do as part of the pre-operation process
result = swimmer.calibrate()
check_result(result, "Calibration Failed! Shutting down user script!")

time.sleep(2)
# Sets the Robot to Swimmode. Must be calibrated first.
result =  swimmer.set_mode("swimmode")
check_result(result, "Setting Swimmode Failed! Shutting down user script!")

time.sleep(2)

swimmer.set_pose()
# Square:
result = swimmer.set_autopilot_mode("depth")
check_result(result, "Setting Depth Failed! Shutting down user script!")

#swimmer.zero_heading()
# DOESNT WORK swimmer.zero_local_pose()

while(True):
    swimmer.swim_to_wp(speed=1.0, depth=2.0, x = 0.0, y = 0.0)
    swimmer.swim_to_wp(speed=0.4, depth=2.0, x = 0.0, y = 5.0)
    swimmer.swim_to_wp(speed=0.4, depth=2.0, x = 5.0, y = 5.0)
    swimmer.swim_to_wp(speed=0.4, depth=2.0, x = 5.0, y = 0.0)
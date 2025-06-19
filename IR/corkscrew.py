
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

swimmer.zero_local_pose()
# Calibrates the Robot. Important to do as part of the pre-operation process
result = swimmer.calibrate()
#check_result(result, "Calibration Failed! Shutting down user script!")

time.sleep(2)
# Sets the Robot to Swimmode. Must be calibrated first.
result =  swimmer.set_mode("swimmode")
#check_result(result, "Setting Swimmode Failed! Shutting down user script!")

time.sleep(2)
# Square:
result = swimmer.set_autopilot_mode("angles")
#check_result(result, "Setting Depth Failed! Shutting down user script!")

#swimmer.zero_heading()
_depth = 5.0
_roll = 20.0
while(True):
    _roll += 20.0
    if(_roll > 360.0):
        _roll = 0.0
    swimmer.timed_swim(speed=0.4, heave=0.0, yaw=0.0, pitch= 0.0, roll = _roll, duration = 1.0, depth = _depth)
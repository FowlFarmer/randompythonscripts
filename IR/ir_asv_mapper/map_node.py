import rclpy
from rclpy.node import Node
from map_asv import mapper
import cv2

# Copyright 2023 WATonomous
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node, Timer

# msg imports
from geometry_msgs.msg import Pose
from sensor_msgs.msg import CompressedImage

class Anomaly(Node):

    def __init__(self):
        super().__init__('sensor_map_visualizer')
        # Declare and get the parameter
        # self.declare_parameter('version', 1)
        # self.declare_parameter('compression_method', 0)
        self.declare_parameter('max_pose_to_sensor_interval', 2) # Max timestamp difference between the pose and sensor data to consider the sensor data valid

        # Initialize ROS2 Constructs
        self.map_publisher = self.create_publisher(CompressedImage, '/image_sub_placeholder', 10)
        self.pose_subscription = self.create_subscription(
            Pose, '/pose_placeholder', self.pose_callback, 10)
        # self.subscription = self.create_subscription(
        #     Temperature, '/temp_placeholder', self.unfiltered_callback, 10)
        self.dissolved_oxygen_subscription = self.create_subscription(
            DissolvedOxygen, '/dissolved_oxygen_placeholder', self.dissolved_oxygen_callblack, 10
        )
        self.timer = self.create_timer(0.1, self.timer_callback) # 10fps map update rate

        self.dissolved_oxygen, self.temperature, self.pose = None, None, None
        self.map = mapper(map_image=None)


    def pose_callback(self, msg):
        self.pose = msg
    
    def dissolved_oxygen_callblack(self, msg):
        self.dissolved_oxygen = msg
        if(self.pose.header.stamp.sec - self.dissolved_oxygen.header.stamp.sec > self.get_parameter('max_pose_to_sensor_interval').value):
            self.get_logger().warn("Pose and sensor data are too far apart, ignoring sensor data")
            return
        map.update_dissolved_oxygen_layer(
            ((self.pose.position.x, self.pose.position.y), self.dissolved_oxygen.data), radius=3)

    def timer_callback(self):
        if self.dissolved_oxygen is None or self.pose is None:
            self.get_logger().warn("Pose or sensor data not received yet, skipping map update")
            return
        
        # Update the map with sensor data
        updated_map = self.map.update_map()

        # Publish the updated map
        msg = CompressedImage()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.format = 'jpeg'
        msg.data = cv2.imencode('.jpg', updated_map)[1].tobytes()
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)

    python_anomaly = Anomaly()

    rclpy.spin(python_anomaly)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    python_anomaly.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

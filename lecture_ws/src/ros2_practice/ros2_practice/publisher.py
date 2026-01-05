#!/usr/bin/env python3
import random
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class VehicleSpeedPublisher(Node):
    def __init__(self):
        super().__init__('vehicle_speed_publisher')
        self.pub = self.create_publisher(Float32, '/vehicle/speed_mps', 10)
        self.timer = self.create_timer(0.05, self.on_timer)
        self._v = 0.0
    def on_timer(self):
        self._v += random.uniform(-0.08, 0.1)
        self._v = max(0.0, min(self._v, 16.7))
        msg = Float32(data=self._v)
        self.pub.publish(msg)
def main():
    rclpy.init()
    node = VehicleSpeedPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()
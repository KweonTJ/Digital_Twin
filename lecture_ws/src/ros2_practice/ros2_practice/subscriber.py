#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

MPS_TO_KMPH = 3.6

class CarSpeedSubscriber(Node):
    def __init__(self):
        super().__init__('vehicle_speed_subscriber')
        self.sub = self.create_subscription(Float32, '/vehicle/speed_mps',
self.on_msg, 10)
    
    def on_msg(self, msg: Float32):
        kmh = msg.data * MPS_TO_KMPH
        print(f'Current Vehicle Speed: {kmh:.1f} km/h')
def main():
    rclpy.init()
    node = CarSpeedSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
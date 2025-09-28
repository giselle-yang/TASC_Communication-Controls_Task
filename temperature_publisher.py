#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class TemperaturePublisher(Node):
    def __init__(self):
        super().__init__('temperature_publisher')
        self.publisher_ = self.create_publisher(Float32, 'temperature', 10)
        self.timer = self.create_timer(1.0, self.publish_temperature)  # 1 Hz
        self.get_logger().info('Temperature Publisher Node Started')

    def publish_temperature(self):
        temp = random.uniform(-100, 100.0)  # Generate fake temperature
        msg = Float32()
        msg.data = temp
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published temperature: {temp:.2f}°C')
        

def main(args=None):
    rclpy.init(args=args)
    node = TemperaturePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

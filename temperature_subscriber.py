#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class TemperatureSubscriber(Node):
    def __init__(self):
        super().__init__('temperature_subscriber')
        self.subscription = self.create_subscription(
            Float32,
            'temperature',
            self.listener_callback,
            10)
        self.get_logger().info('Temperature Subscriber Node Started')

    def listener_callback(self, msg):
        temp = msg.data
        if temp > 80.0:
            self.get_logger().warn(f"Temperature: {temp:.2f}°C -> Robot is overheating!")
        if temp<-20.0:
            self.get_logger().warn(f"Temperature: {temp:.2f}°C -> Robot is too cold!")
        else:
            self.get_logger().info(f'Temperature: {temp:.2f}°C')

def main(args=None):
    rclpy.init(args=args)
    node = TemperatureSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

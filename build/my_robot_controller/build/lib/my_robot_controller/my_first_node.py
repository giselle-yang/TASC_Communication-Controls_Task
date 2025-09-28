#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
#object oriented to create ros2 node

#this class inherits node class from rclpy
class myNode(Node):
    #constructor
    def __init__(self):
        super().__init__("first_node")
        self.get_logger().info("Hello from ROS2")

def main(args=None):
    rclpy.init(args=args)

    #creating a node
    node = myNode()
    #spin means continue to run until ctrl c
    rclpy.spin(node)
    #shuts down all ros2 comms
    rclpy.shutdown()

if __name__== '__main__':
    main()
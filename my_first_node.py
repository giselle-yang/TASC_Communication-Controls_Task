#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
#object oriented to create ros2 node

#this class inherits node class from rclpy
class myNode(Node):
    #constructor
    def __init__(self):
        super().__init__("first_node")
        self.counter=0
        #self.get_logger().info("ROS2")
        
        self.create_timer(1.0, self.timer_callback) 
    def timer_callback(self):
        self.get_logger().info("Hello"+str(self.counter))
        self.counter+=1

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
#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose

class myNode(Node):
    #constructor
    def __init__(self):
        super().__init__("pose_subscriber")

        #subscriber - msg, topic name, callback,queue size
        self.pose_subscriber=self.create_subscription(Pose, "/turtle1/pose",self.pose_callback,10)
    def pose_callback(self,msg: Pose):
        self.get_logger().info("X:"+str(msg.x)+"Y:"+str(msg.y))
        #can access the attributes by using msg.x or msg.y


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
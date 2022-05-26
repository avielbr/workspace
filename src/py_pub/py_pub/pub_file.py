#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
 
class RobotNewsStation(Node):
    def __init__(self):
        super().__init__("robot_news_station")
        self.publisher_ = self.create_publisher(Bool, "robot_news", 15)
        self.timer_ = self.create_timer(1, self.publish_news)
        self.get_logger().info("-> Robot News Station tuning in!")
        self.counter_ = 0
        self.data = True

    def publish_news(self):
        msg = Bool()
        msg.data = self.data
        self.publisher_.publish(msg)
        self.data = not self.data
        self.counter_ += 1

 
def main(args=None):
    rclpy.init(args=args)
    node = RobotNewsStation()
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()

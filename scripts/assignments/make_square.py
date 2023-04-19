#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

def pose_callback(pose):
    global x, y, theta
    x = pose.x
    y = pose.y
    theta = pose.theta

rospy.init_node('make_square')
rospy.Subscriber('/turtle2/pose', Pose, pose_callback)
pub = rospy.Publisher('/turtle2/cmd_vel', Twist, queue_size=10)
rate = rospy.Rate(10)

while not rospy.is_shutdown():
    # move forward
    twist = Twist()
    twist.linear.x = 1
    pub.publish(twist)
    rospy.sleep(1)
    
    # stop and turn
    twist = Twist()
    twist.angular.z = 1.57  # 90 degrees in radians
    pub.publish(twist)
    rospy.sleep(1)
    
    # repeat 3 more times to complete square
    rate.sleep()

#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

def pose_callback(pose):
    global x, y, theta
    x = pose.x
    y = pose.y
    theta = pose.theta

rospy.init_node('make_tringle')
rospy.Subscriber('/turtle3/pose', Pose, pose_callback)
pub = rospy.Publisher('/turtle3/cmd_vel', Twist, queue_size=10)
rate = rospy.Rate(10)

# move forward
twist = Twist()
twist.linear.x = 2
pub.publish(twist)
rospy.sleep(2)

# turn 120 degrees (in radians) to the right
twist = Twist()
twist.angular.z = -2.0944
pub.publish(twist)
rospy.sleep(2)

# move forward
twist = Twist()
twist.linear.x = 2
pub.publish(twist)
rospy.sleep(2)

# turn 120 degrees (in radians) to the right
twist = Twist()
twist.angular.z = -2.0944
pub.publish(twist)
rospy.sleep(2)

# move forward
twist = Twist()
twist.linear.x = 2
pub.publish(twist)
rospy.sleep(2)

# turn 120 degrees (in radians) to the right
twist = Twist()
twist.angular.z = -2.0944
pub.publish(twist)
rospy.sleep(2)

# move forward
twist = Twist()
twist.linear.x = 2
pub.publish(twist)
rospy.sleep(2)

# stop
twist = Twist()
pub.publish(twist)

rospy.spin()

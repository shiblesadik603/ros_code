#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from math import pi
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose



current_pose = Pose()

def pose_callback(pose):
    global current_pose
    current_pose = pose


def rotate(angle, clockwise):
    global current_pose

    # Initialize the node and publisher/subscriber

    cmd_vel_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    pose_sub = rospy.Subscriber('/turtle1/pose', Pose, pose_callback)

    # Create a Twist message
    twist_msg = Twist()

    # Convert the angle to radians and normalize it to (-pi, pi] range
    angle = angle * pi / 180.0
    if angle > pi:
        angle -= 2 * pi
    elif angle <= -pi:
        angle += 2 * pi

    # Set the angular velocity and direction based on the shortest rotation path and clockwise parameter
    if clockwise:
        if angle > 0:
            twist_msg.angular.z = -0.5  # radians per second
        else:
            twist_msg.angular.z = 0.5   # radians per second
    else:
        if angle > 0:
            twist_msg.angular.z = 0.5   # radians per second
        else:
            twist_msg.angular.z = -0.5  # radians per second

    # Set the start angle and current angle
    start_angle = current_pose.theta
    current_angle = current_pose.theta

    # Rotate until the desired angle is reached
    while abs(current_angle - start_angle) < abs(angle):
        cmd_vel_pub.publish(twist_msg)
        current_angle = current_pose.theta

    # Stop the rotation by sending a zero velocity Twist message
    twist_msg.angular.z = 0.0
    cmd_vel_pub.publish(twist_msg)


 
# draw s with turtlesim

def move(speed,distance,is_forward):
    velocity_msg = Twist()
    if is_forward:
        velocity_msg.linear.x = abs(speed)
    else:
        velocity_msg.linear.x = -abs(speed)
    distance_moved = 0.0
    t0 = rospy.Time.now().to_sec()
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    while True:
        rospy.loginfo("Turtlesim moves forward")
        velocity_publisher.publish(velocity_msg)
        t1 = rospy.Time.now().to_sec()
        distance_moved = (t1-t0)*speed
        if distance_moved > distance:
            rospy.loginfo("reached")
            break
    velocity_msg.linear.x = 0
    velocity_publisher.publish(velocity_msg)



if __name__=='__main__':
    rospy.init_node("draw_s",anonymous=True)

    
    move(2,2,False)
    rotate(90,True)
    move(2,2,True)
    rotate(90,False)
    move(2,2,True)
    rotate(90,True)
    move(2,2,True)
    rotate(90,True)
    move(2, 2, True)
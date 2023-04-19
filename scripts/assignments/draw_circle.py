#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

if __name__=='__main__':
    rospy.init_node("draw_circle")
    rospy.loginfo("Node has been started.")
    pub=rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)

    rate=rospy.Rate(2)

    while not rospy.is_shutdown():
        msg=Twist()
        msg.linear.x= 1.0
        msg.angular.z= 1.0
        pub.publish(msg)
        rate.sleep()

# akhon code e kono change korle just
# git add .
# git commit -m "ki change korsi sei relaeted msg (Ex: fixed issue)"
# git push

# ei 3 ta command dilei hobe, next time kono change kora hoile segula upload korar jonno
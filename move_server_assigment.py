#!/usr/bin/env python

import rospy
from ros_coc.srv import *
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import time
x=0
y=0
yaw=0


def poseCallback(pose_message):
    global x
    global y, yaw
    x= ___.x
    y= ___.y
    yaw = pose_message.theta


def handle_move(req):
    	#declare a Twist message to send velocity commands
        velocity_message = Twist()
        #get current location 
        global x, y
        x0=x
        y0=y
	distance = ___
	speed = ___
	is_forward= ___
        if (is_forward):
            ___.linear.x =abs(speed)
        else:
        	___.linear.x =-abs(speed)

        distance_moved = 0.0
        loop_rate = rospy.Rate(10) # we publish the velocity at 10 Hz (10 times a second)    
        cmd_vel_topic='___'
        velocity_publisher = rospy.Publisher(cmd_vel_topic, ___, queue_size=10)

        while True :
                rospy.loginfo("Turtlesim moves forwards")
                velocity_publisher.publish(___)

                loop_rate.sleep()
                
                               
                distance_moved = abs(0.5 * math.sqrt(((x-x0) ** 2) + ((y-y0) ** 2)))
                print  distance_moved               
                if  not (distance_moved<distance):
                    rospy.loginfo("reached")
                    break
        
        #finally, stop the robot when the distance is moved
        velocity_message.linear.___ = ___
        velocity_publisher.publish(___)
    

def move_server():
	rospy.init_node('move_server')
	s = rospy.Service( '___', ___, ___ )
	rospy.spin()

if __name__ == "__main__":
        position_topic = "___"
        pose_subscriber = rospy.Subscriber(position_topic, ___, ___) 
	___()


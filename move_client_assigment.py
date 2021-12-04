#!/usr/bin/env python

import rospy
from ros_coc.srv import ___

def move_client():
    rospy.wait_for_service('move')
    try:
        distance = ___(input("Enter distance : "))
        speed = ___(input("Enter speed : "))
	flag = ___(input("Enter if 'is forward'(True or False) : "))
        move = rospy.ServiceProxy('xxx', xxxx)
        move(___,___,___)
        
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

if __name__ == "__main__":
    print "Turtlesim Moves"
    ___()

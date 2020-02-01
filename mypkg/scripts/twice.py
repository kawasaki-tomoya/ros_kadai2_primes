#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

num = 0

def cb(message):
	num = message.data
	y = []
	for i in range(1,num):
		if num % i == 0:
			y.append(i)
			
	rospy.loginfo(message.data)
	rospy.loginfo(y)
	if len(y) == 1:
		print num, 'is SOSUU.'
	
if __name__ == '__main__':
	rospy.init_node('twice')
	sub = rospy.Subscriber('count_up', Int32, cb)
	rospy.spin()

#!/usr/bin/env python
from time import sleep
from math import isnan
import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped
from tf.transformations import quaternion_from_euler
from nav_msgs.msg import Odometry
import urllib2


#####  ThingSpeak Channel Settings #####
# The ThingSpeak Channel ID
# The Write API Key for the channel
# Replace this with your Write API key
apiKey = "xxxxxxxxxxxxxxxxx"

# Create the topic string
data1 = 0
data2 = 0
data3 = 0
data4 = 0
data5 = 0
data6 = 0
data7 = 0

###### Start of functions ######
def callback(msg):				#define a function called 'callback' that receives a parameter named 'msg'
	#print msg.pose.pose
	
	global px, py, pz, ox, oy, oz, ow
	px = msg.pose.pose.position.x
	py = msg.pose.pose.position.y
	pz = msg.pose.pose.position.z

	ox = msg.pose.pose.orientation.x
	oy = msg.pose.pose.orientation.y
	oz = msg.pose.pose.orientation.z
	ow = msg.pose.pose.orientation.w

    # assigning values to global variables
	global data1, data2, data3, data4, data5, data6, data7
	data1 = px
	data2 = py
	data3 = pz
	data4 = ox
	data5 = oy
	data6 = oz
	data7 = ow

rospy.init_node('init_pos')

while not rospy.is_shutdown():
	
	odom_sub = rospy.Subscriber("/odom", Odometry, callback)

	##### Send laserdata to ThingSpeak #####
	# https://api.thingspeak.com/update?api_key=<key>&field1=0

	# build the payload string
	tPayload = "field1=" + str(data1) + "&field2=" + str(data2) + "&field3=" + str(data3) + "&field4=" + str(data4) + "&field5=" + str(data5) + "&field6=" + str(data6) + "&field7=" + str(data7)

	# attempt to publish this data to the topic 
	
	#https://api.thingspeak.com/update?api_key=xxxxxxxxxxxxxxxxx&field1=10&field2=5
	req="https://api.thingspeak.com/update?api_key="+apiKey+"&"+tPayload
	response=urllib2.urlopen(req)

	print(response)
	#response=request.urlopen(req)
	#print(response)
	###################################
	

rospy.spin()



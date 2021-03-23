#!/usr/bin/env python
import rospy
from my_pkg.msg import two_ints

c = None
d = None

def callback(data):
    global c , d
    c = data.a
    d = data.b
    publisher()

def ops():
    e = c + d
    f = e * 20
    return e , f

def publisher():
    pub = rospy.Publisher('tl',two_ints,queue_size=1)
    x,y = ops()
    r = rospy.Rate(1)
    msg = two_ints()
    while not rospy.is_shutdown():
        msg.a = x
        msg.b = y
        pub.publish(msg)
        r.sleep()

def listener():
    rospy.init_node('c_l')
    rospy.Subscriber('two_ints',two_ints,callback)
    rospy.spin()

if __name__ == '__main__':
    listener()


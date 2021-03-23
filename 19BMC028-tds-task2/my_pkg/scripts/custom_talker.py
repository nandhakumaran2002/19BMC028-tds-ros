#!/usr/bin/env python
import rospy
from my_pkg.msg import two_ints

def talker():
    rospy.init_node('c_t')
    pub = rospy.Publisher('two_ints',two_ints,queue_size=1)
    r = rospy.Rate(1)
    msg = two_ints()
    while not rospy.is_shutdown():
        msg.a = 3
        msg.b = 4
        pub.publish(msg)
        r.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

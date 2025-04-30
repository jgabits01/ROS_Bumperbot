import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/joel/vsC/Self-Driving-and-ROS-2-Learn-by-Doing-Plan-Navigation/Section3_Introduction_to_ROS_2/bumperbot_ws/install/bumperbot_py_examples'

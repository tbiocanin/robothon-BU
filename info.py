import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi,sqrt
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_tutorial',
                anonymous=True)

robot = moveit_commander.RobotCommander()

scene = moveit_commander.PlanningSceneInterface()

# print(robot.get_current_state())

group_name = "panda_arm"
group = moveit_commander.MoveGroupCommander(group_name)
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                               moveit_msgs.msg.DisplayTrajectory,
                                               queue_size=20)
pose_goal = geometry_msgs.msg.Pose()

print(group.get_current_pose().pose)
# pose_goal = group.get_current_pose().pose

# pose_goal.position.x = 0.4
# pose_goal.position.y = 0.1
# pose_goal.position.z = 0.4
# group.set_pose_target(pose_goal)
# plan = group.go(wait=True)
# group.stop()
# group.clear_pose_targets()

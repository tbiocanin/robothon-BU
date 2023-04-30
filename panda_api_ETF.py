import franka_gripper.msg
import rospy
import sys
from koordinate import *

# Brings in the SimpleActionClient
import actionlib

import copy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi,sqrt
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list
from tf.transformations import quaternion_from_euler
from geometry_msgs.msg import Quaternion
import time

''' 
Project: Robothon manipulation competition API
Authors: Ruzic Nikola, Rodic Filip, Biocanin Teodor
Date: April, 2023
File: proba_objekat.py
Contains:
    robot_dealerNODE 
Description:
    Implementation of basic robot functions with direct communication to
    the Franka Emika Panda robot
'''


class robot_dealerNODE():

    def __init__(self):
        rospy.init_node('grasp_client_py')
        moveit_commander.roscpp_initialize(sys.argv)
        # Info command
        # starting_pose = group.get_current_pose().pose  

        self.robot = moveit_commander.RobotCommander()

        self.scene = moveit_commander.PlanningSceneInterface()

        self.group_name = "panda_arm"
        self.group = moveit_commander.MoveGroupCommander(self.group_name)
        self.display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                                    moveit_msgs.msg.DisplayTrajectory,
                                                    queue_size=20)

        self.client = actionlib.SimpleActionClient('/franka_gripper/grasp', franka_gripper.msg.GraspAction)
        self.client_variable = actionlib.SimpleActionClient('/franka_gripper/move', franka_gripper.msg.MoveAction)

        self.group.set_max_velocity_scaling_factor(0.2) 
        self.group.set_max_acceleration_scaling_factor(0.2)	

        starting_pose = geometry_msgs.msg.Pose()
        quat_tf = quaternion_from_euler(-3.1204858987484454 , -0.03254517022215577, -0.7864853124233606)

        quat_msg = Quaternion(quat_tf[0], quat_tf[1], quat_tf[2], quat_tf[3])

        starting_pose.position.x = 0.343529876052
        starting_pose.position.y = 0.027006783481
        starting_pose.position.z = 0.418143675693

        starting_pose.orientation = quat_msg
        self.set_joints(0.331871547138, -0.659965603918, -0.240024021077, -2.71483051872, -0.184904711679, 2.0982702793, 1.01525540689)

        # self.group.set_pose_target(starting_pose)
        # plan = self.group.go(wait=True)
        # self.group.stop()
        # self.group.clear_pose_targets()

        # [0.331871547138, -0.659965603918, -0.240024021077, -2.71483051872, -0.184904711679, 2.0982702793, 1.01525540689]
        # self.set_joints(0.331871547138, -0.659965603918, -0.240024021077, -2.71483051872, -0.184904711679, 2.0982702793, 1.01525540689)

        self.positions = []



    def grasp_client(self,width,epsInner,epsOuter,speed,force):
        # Creates the SimpleActionClient, passing the type of the action
        # (GraspAction) to the constructor.
        

        # Waits until the action server has started up and started
        # listening for goals.

        self.client.wait_for_server()

        # Creates a goal to send to the action server.
        goal = franka_gripper.msg.GraspGoal()
        goal.width = width
        goal.epsilon.inner = epsInner
        goal.epsilon.outer = epsOuter
        goal.speed = speed
        goal.force = force

        # Sends the goal to the action server.
        self.client.send_goal(goal)

        # Waits for the server to finish performing the action.
        self.client.wait_for_result()

        # Prints out the result of executing the action
        print("finished grasping")
        return self.client.get_result()  # A GraspResult

    def grasp_client_variable(self,width,speed):
        # Creates the SimpleActionClient, passing the type of the action
        # (GraspAction) to the constructor.
        

        # Waits until the action server has started up and started
        # listening for goals.

        self.client_variable.wait_for_server()

        # Creates a goal to send to the action server.
        goal = franka_gripper.msg.MoveGoal()
        print(goal)
        goal.width = width
        goal.speed = speed

        # Sends the goal to the action server.
        self.client_variable.send_goal(goal)

        # Waits for the server to finish performing the action.
        self.client_variable.wait_for_result(rospy.Duration.from_sec(5.0))

        # Prints out the result of executing the action
        print("finished grasping")
        return self.client_variable.get_result()  # A GraspResult

    def moveit_grasp():
        gripper_name = panda_arm.get_end_effector_link()


    def move_robot(self,pos,ori,dx=0,dy=0,dz=0,tol = 0.005):
        
        x_global = pos[0] + dx
        y_global = pos[1] + dy
        z_global = pos[2] + dz

        x_or = ori[0] 
        y_or = ori[1]
        z_or = ori[2]

        _pose = geometry_msgs.msg.Pose()
        quat_tf = quaternion_from_euler(x_or , y_or, z_or)

        quat_msg = Quaternion(quat_tf[0], quat_tf[1], quat_tf[2], quat_tf[3])

        _pose.position.x = x_global
        _pose.position.y = y_global
        _pose.position.z = z_global

        _pose.orientation = quat_msg

        self.group.set_pose_target(_pose)
        # self.group.set_path_constraints(tol) 
        # self.group.set_goal_position_tolerance(tol)
        plan = self.group.go(wait=True)
        self.group.stop()
        self.group.clear_pose_targets()

    

    def add_pose(self,pose):
        self.positions.append(pose)

    def make_pose(self,x_global,y_global,z_global, x_or, y_or, z_or):
        _pose = geometry_msgs.msg.Pose()
        quat_tf = quaternion_from_euler(x_or , y_or, z_or)

        quat_msg = Quaternion(quat_tf[0], quat_tf[1], quat_tf[2], quat_tf[3])

        _pose.position.x = x_global
        _pose.position.y = y_global
        _pose.position.z = z_global

        _pose.orientation = quat_msg

        return _pose

    def move_robot_L(self,pos,dx=0,dy=0,dz=0):
        waypoints = []
        pos_node = self.make_pose(pos.position[0]+dx,pos.position[1]+dy,pos.position[2]+dz,pos.rpy[0],pos.rpy[1],pos.rpy[2])
        waypoints.append(copy.deepcopy(pos_node))
        (plan, fraction) = self.group.compute_cartesian_path(
        waypoints, 0.01, 0.0)  

        self.group.execute(plan, wait=True)

    def move_robot_J(self,pos,dx=0,dy=0,dz=0):
        self.move_robot(pos.position,pos.rpy,dx,dy,dz)


    def set_joints(self,j1,j2,j3,j4,j5,j6,j7):
        joint_goal = [j1,j2,j3,j4,j5,j6,j7]
        self.group.go(joint_goal, wait=True)
        self.group.stop()
        

    def move_to_pose(self,pose):
        self.group.set_pose_target(pose)
        plan = self.group.go(wait=True)
        self.group.stop()
        self.group.clear_pose_targets()

    def set_slider_length(self, lenPER):
        self.slider = lenPER

    def calculate_slider_length(pos1,pos2):
        return math.dist(pos1.position, pos2.position)

    def set_vel_acc(self,value):
        self.group.set_max_velocity_scaling_factor(value) 
        self.group.set_max_acceleration_scaling_factor(value)


    

if __name__ == '__main__':
    try:
        pass

    except rospy.ROSInterruptException:
        print("program interrupted before completion")

   
import panda_api_ETF
from panda_api_ETF import *
import time
import math
from board_orientation import *
# from koordinate import *

rN = robot_dealerNODE()

# pos= [0.45, 0, 0.7]
# ori= [math.pi,0, -math.pi/4]
# rN.move_robot(pos,ori)
# rN.set_vel_acc(0.1)
pos= [0.45, 0, 0.7]
ori= [math.pi,0, -math.pi/4]
rN.move_robot(pos,ori)
rN.set_vel_acc(0.1)



board_origin, board_orientation,_ = vision()
print("gledaj vamo")
print(board_origin, board_orientation)

# print(start_button_press.pos_board_cs)

# board_origin = [0.44798833408, 0.0983415023025]
# board_orientation = 0

cable_grab = Coords('''joints = [0.123968671809 0.20600802755 -0.311686978045 -2.46212787739 -0.0175176675807 2.62793402963 0.600727843634]
  panda_link8 pose = [
  header: 
    seq: 0
    stamp: 
      secs: 1682793628
      nsecs:  59730052
    frame_id: "/world"
  pose: 
    position: 
      x: 0.469573183141
      y: -0.0932599124007
      z: 0.215675683591
    orientation: 
      x: 0.926509617253
      y: -0.374266160163
      z: -0.00776256462593
      w: 0.0380067505145 ]
  panda_link8 RPY = [3.0652692282630625, -0.01406146968808864, -0.767290947211288]''', 0,1,1,board_origin, board_orientation)

cable_take_out = Coords('''joints = [0.123968671809 0.20600802755 -0.311686978045 -2.46212787739 -0.0175176675807 2.62793402963 0.600727843634]
  panda_link8 pose = [
  header: 
    seq: 0
    stamp: 
      secs: 1682793628
      nsecs:  59730052
    frame_id: "/world"
  pose: 
    position: 
      x: 0.449573183141
      y: -0.0932599124007
      z: 0.215675683591
    orientation: 
      x: 0.926509617253
      y: -0.374266160163
      z: -0.00776256462593
      w: 0.0380067505145 ]
  panda_link8 RPY = [3.0652692282630625, -0.01406146968808864, -0.767290947211288]''', 0,1,1,board_origin, board_orientation)

cable_plug_in_approach = Coords('''joints = [-0.506314704784 0.0823964123496 0.0489897385019 -2.44676241309 1.68905913737 1.73867231187 1.4637706234]
  panda_link8 pose = [
  header: 
    seq: 0
    stamp: 
      secs: 1682794409
      nsecs: 246963977
    frame_id: "/world"
  pose: 
    position: 
      x: 0.457432822631
      y: -0.124547705664
      z: 0.295299512493
    orientation: 
      x: -0.0238077072511
      y: 0.729641057894
      z: 0.530128038522
      w: 0.431301962068 ]
  panda_link8 RPY = [1.658060172354127, 0.7136902636222886, 2.5484573970883306]''', 0,1,1,board_origin, board_orientation)

cable_plug_in_prepare = Coords('''joints = [1.47359357659 -1.05450236766 -1.95430274833 -2.44789261477 1.50851632273 2.48341113347 0.896817590935]
  panda_link8 pose = [
  header: 
    seq: 0
    stamp: 
      secs: 1682794916
      nsecs: 352931976
    frame_id: "/world"
  pose: 
    position: 
      x: 0.435641016094
      y: -0.104846211967
      z: 0.157192231216
    orientation: 
      x: 0.014801544954
      y: 0.698061064057
      z: 0.493091894778
      w: 0.518991376055 ]
  panda_link8 RPY = [1.5353095402902672, 0.7894675380778109, 2.2842046159658085]''', 0,1,1,board_origin, board_orientation)


# rN.grasp_client_variable(0.03,0.1)
# rN.move_robot_J(hatch_grasped,0,0,0.05)
# rN.move_robot_J(hatch_grasped)
# rN.grasp_client(0.015,0.005,0.005,0.5,5)
# rN.move_robot_J(hatch_lift_15)
# rN.move_robot_J(hatch_lift_30)
# rN.move_robot_J(hatch_lift_60)
# rN.move_robot_J(hatch_lift_75)
# rN.move_robot_J(hatch_lift_90)
# rN.move_robot_J(hatch_lift_100)
# rN.grasp_client(0.015,0.005,0.005,0.5,5)
# rN.move_robot_J(hatch_lift_depart)
# rN.move_robot_J(hatch_lift_depart,0,0,0.1)

###############################

# rN.set_joints(0.331871547138, -0.659965603918, -0.240024021077, -2.71483051872, -0.184904711679, 2.0982702793, 1.01525540689)

# rN.move_robot_J(cable_grab,0,0,0.2)
# rN.move_robot_J(cable_grab,0,0,0.002)
# rN.grasp_client(0.007,0.002,0.002,0.5,5)
# rN.move_robot_J(cable_take_out)
# rN.move_robot_J(cable_take_out,0,0,0.2)
# rN.move_robot_J(cable_plug_in_approach)
# rN.move_robot_J(cable_plug_in_prepare)
# rN.grasp_client_variable(0.009,0.1)

test_port_take_out = Coords('''joints = [0.338127919605 0.130485322574 -0.234318823982 -2.56966125759 -0.0193603740044 2.72324884706 0.906230387083]
  panda_link8 pose = [
  header: 
    seq: 0
    stamp: 
      secs: 1682790961
      nsecs: 242918968
    frame_id: "/world"
  pose: 
    position: 
      x: 0.450169677267
      y: 0.0450743558555
      z: 0.220324328506
    orientation: 
      x: 0.924184562993
      y: -0.381237778094
      z: 0.0208130626314
      w: 0.0103666052437 ]
  panda_link8 RPY = [3.1382905635074017, -0.046385694980998184, -0.7824272147614435]''', 0,1,1,board_origin, board_orientation)

test_port_plug_in = Coords('''joints = [0.333021631203 0.151382270533 -0.234261829935 -2.48506457533 -0.0196069813992 2.66923524194 0.906817508729]
  panda_link8 pose = [
  header: 
    seq: 0
    stamp: 
      secs: 1682791120
      nsecs: 842514038
    frame_id: "/world"
  pose: 
    position: 
      x: 0.472426941746
      y: 0.0466269562202
      z: 0.234755614071
    orientation: 
      x: 0.923091214319
      y: -0.383509347143
      z: 0.0266824238622
      w: 0.0105469880809 ]
  panda_link8 RPY = [-3.1405893997814407, -0.0573866303012271, -0.7875714377198617]''', 0,1,1,board_origin, board_orientation)

rN.move_robot_J(test_port_take_out,0,0,0.05)
rN.grasp_client(0.010,0.005,0.005,0.5,15)
rN.set_vel_acc(0.05)
rN.move_robot_J(test_port_take_out)
rN.grasp_client(0.010,0.005,0.005,0.5,15)
rN.move_robot_J(test_port_take_out,0,0,0.05)

##################################################################
# State4 : Probe plugin
##################################################################
rN.move_robot_J(test_port_plug_in,0,0,0.05)
rN.set_vel_acc(0.05)
rN.move_robot_J(test_port_plug_in)
rN.move_robot_J(test_port_plug_in,0,0,-0.01)
rN.grasp_client(0.010,0.005,0.005,0.5,15)
rN.move_robot_J(test_port_plug_in,0,0,0.05)
rN.grasp_client(0.010,0.005,0.005,0.5,15)
rN.move_robot_L(test_port_plug_in,0,0,-0.007)
rN.set_vel_acc(0.1)
rN.move_robot_J(test_port_plug_in,0,0,0.05)
from panda_api_ETF import *
from board_orientation import *

rG = robot_dealerNODE()
# rG.grasp_client_variable(0.03,0.1)

rG.grasp_client(0.010,0.005,0.005,0.5,15)

dist = np.array([0.2610, 0.4163, 0, 0, 0])
mtx = np.array([[2595.79350037846,	0,	650.746133050557],
[0,	2596.04867348007,	531.462343257144],
[0,	0,	1]])


pos= [0.45, 0, 0.8]
ori= [math.pi,0, -math.pi/4]
rG.move_robot(pos,ori)
rG.set_vel_acc(0.1)

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,960)


ret,frame =cap.read()

cv2.imshow('Original', frame)
newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (1280,960), 0.5, (1280,960)) 


frame2 = cv2.undistort(frame, mtx, dist, None, newcameramtx)
# print(frame2)
cv2.imshow('Und', frame2)
cv2.imwrite('Und.jpg', frame2)

board_origin, board_orientation = vision()

# print(board_origin)
# pos= [board_origin[0], board_origin[1], 0.25]
# ori= [math.pi,0, -math.pi/4]
# rG.move_robot(pos,ori)

# pos= [X_blue, Y_blue, 0.15]
# rG.move_robot(pos,ori)

time.sleep(15)
# cv2.destroyAllWindows()


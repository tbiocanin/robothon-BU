# robothon-BU


# Robothon - autonomous:go Panda control system 

Custom made Panda API and opencv based computer vision package made for
the Robothon - Grand Challenge competition.

## Getting Started

Clone the whole repository and run the catkin_make command.

### Prerequisites

Our test bench is using Ubuntu 16.04. We tested our programs for the franka_ros and frankalib 0.8.0 versions.

The Panda API is based on the moveit framework for planning and robot connection. Moveit needs to be compatable with frankalib and franka_ros versions.

### Equipment

-Franka Emika Panda robot system with factory built-in force and torque sensors.
-Ordinary webcam(logitech webcam C270)

### Instalation 

One importand notice, our project requires the kinetic version of ROS.

Links that were used for the setup of the mentioned packages:
https://frankaemika.github.io/docs/installation_linux.html
https://ros-planning.github.io/moveit_tutorials/doc/getting_started/getting_started.html


## Usage

Panda-PC communication
Move into ws_moveit and run the following command:
roslaunch panda_moveit_config panda_control_moveit_rviz.launch robot_ip:=<the_robot_ip>

## Authors

-Ruzic Nikola and Rodic Filip - Software design, robot training, camera calibration algorithm, coordinate transformations.

-Biocanin Teodor - Software design, computer vision.

### Module descriptions

## Panda API:

---
panda_api_ETF.py 

Built in point to point, cartesian movement with speed and acceleration control. 
Binary and variable grip control. General robot manipulation functionalities and server-client based communication
with the franka interface.

koordinate.py

Holds the trained robot coordinates and calculates relative positions to the defined anchor point.
Calculates the coordinate transformations with the estimated anchor point position and estimated board orientation.
Has aditional parsing functionalities for posistion memorisation.

---

## Calibration and position estimation:

---

board_orientation.py

Initial Calibration was done using the matlab calibration app. Using the obtained calibration matricies, the script unwraps the webcam image. More finite calibration is done actively with one aruco sticker used to find the workspace point because of the unrelaible mounting point of the camera, and the camera angle.

---

## Computer vision

---

board_orientation.py

Based on the board configuration, an approach was defined in which we focused on characteristic object within it. Thus, using openCV we focused on the buttons to locate them at first. It was done in such way that we found them based on colour and contour size that they have. Afterwards, we derived its characteristics and used that information for further board orientation definement. 

slider_detect.py

To define how much the slider should move, a similar approach was used so that data about the desired position is extracted. Based on the slider length, and the length represented on the display, the desired positions are determined. 
---

## Unit testing functionalities

---

-grasp.py
-hatch.py
-info.py
-force.py
-calibration.py

---

## Acknowledgments

We would like to express our heartfelt thanks to the ETF Robotics Research Group for their invaluable assistance in the Robothon competition. We are particularly grateful for the contributions of Assistant Nikola Knezevic, whose expertise and tireless efforts were essential to the success of our team. We would also like to extend our appreciation to Professor Kosta Jovanovic, Assistant Zavisa Gordic, and Assistant Milos Petrovic for their invaluable support and guidance. Their dedication and contributions were instrumental in helping our team overcome challenges in the competition. We are truly fortunate to have had the opportunity to work with such a talented and dedicated group of individuals.

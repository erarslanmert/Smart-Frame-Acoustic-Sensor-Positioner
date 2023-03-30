# Smart-Frame-Acoustic-Sensor-Positioner
The project aims to calculate acoustic sensor positions easily and quickly for different 
configurations and deployments of each four acoustic sensor in a four corner shaped product. When a new 
configuration of deployment is introduced to the system, the mission file should be updated 
in order to provide a correct internal localization to the computer. The calculation and 
measurement of distance and angle between sensors can be difficult for some sensor 
configurations. Therefore, the company uses a solid frame with cross sticks. That helps 
keeping the sensors in a pre-defined position. The heading positions such as 180°, 90° or 270°
are sufficient to integrate and calculate manually by the engineers during a demo or 
integration operation.
 
Figure 1: Currently used solid frame
Figure2: Mission file example which is introduced to the computer
However, when the deployment area is limited or customers want to deploy sensors in a 
different configuration, it becomes very confusing and takes too much time to measure and 
calculate their position with respect to True North created by GPS headings. Also, calculating 
the yaw of sensors is difficult when we have an imaginary axis. Smart Frame comes up with a 
proper solution to that situation. More additional benefits will be explained in the 5th section 
of this document and the company can decide whether those benefits and opportunities will 
be considerable or not.
2- SYSTEM DETAILS
The system is composed of two main parts, these are hardware and software. Main idea 
is to measure distance and the angle of a virtual line which can be drawn in between the
centers of two acoustic sensor posts. Hardware is deployed such that it covers all around the windcap 
of the sensor posts. Platform is deployed as it looks to the heading of sensor post ( that means, 
the system takes the 180 degrees opposite direction of the plugs located on the sensor posts 
as reference in the beginning ). Hardware includes two twin towers. One is deployed to the 
first acoustic sensor post which also has a primer GPS unit. The other is deployed on second, third and 
fourth acoustic sensor in order. It takes almost 5 min. to complete that measurement process. When 
we get the angles and distances between acoustic sensor posts, the software calculates and locates
sensor positions with respect to True North introduced by primer and seconder GPS headings 
and sensor post headings. The mission file can be created directly by only one click in an 
instant.
Figure 3: The measurement principles and parameters of the system. Sensor headings are drawn with black lines, 
angles measured by system according to software reference are drawn with claret red and GPS headings are drawn with 
blue
A) Hardware
System includes some electrical and structural components. They are listed below with 
their mission:
Cameras: Two identical cameras are located in two pair structures. They are used to recognize 
the spherical red bulb object located on the center of the system, and to align centers of 
moving parts on the system. 
Lidar: It is used to measure distance between pair centers. It provides ± 1 cm accuracy in range 
0-3 m.
Continuous Feedback Servo Motors: System includes two pairs of continuous feedback servo 
motors. They are used to align distance sensors and cameras to each other. In order to get a 
healthy measurement, cameras and distance sensors should look at each other when they are 
totally parallel and they must be aligned to their centers. Having a feedback servo motor gives 
the opportunity to get the exact position of the motor shaft as an angle with an accuracy ± 1°.
Red Bulb: Red bulb is used to easily recognize video processing. When it is recognized, a blue 
line is drawn in the center of the bulb in the GUI and motors can be directed to align cameras 
to that line. In order to satisfy center selection, it must be a spherical object to recognize its 
center from all instances before alignment.
Electronics Box: it includes most of the cables, PCB, USB HUB etc.
Solid Parts: They are designed to place the system on the right center of the acoustic sensor posts and 
provide consistent measurement between pair structures.
Figure 4: Some 3D model visuals for the first pair, all components are assembled in drawing program
Figure 5: Real prototypes of two pairs, both are assembled with all components
B) Software (GUI)
A simple user interface is developed with different options, helpful visuals and extra tools 
in order to ease the measurement and calculation process for the users. After two pairs are 
connected to the laptop via USB hubs ( USB 3.0 or higher ports ) the software becomes ready 
to run. It has necessary helpful directions in all tools. It mainly consists of two camera frames, 
motor control buttons, acoustic sensor relation options, saving measurement button, visual 
deployment check window, zoom camera window, video processing on/off buttons, settings 
window, instantaneous data observation consoles and manual calculation tool.
Figure 6: Graphical user interface
Settings window includes usb COM port entries for two servos and lidar. When a 
different laptop is used to perform, it can be arranged according to new port numbers of those 
components. In addition there are video capture number entries. Laptops give 0 or 1 to their 
own webcams to perform video capture functions at the back end. The user can arrange 
cameras which are going to be displayed on the GUIs camera frames. In addition, the settings 
window includes acoustic sensor id number entry parts. They are listed in the mission file when all 
measurements are done. If the save settings button is clicked the window is locked and the 
system starts. When there is no proper data access via the ports the system gives warning. 
The user can unlock the settings window by clicking the blue refresh button.
Figure 7: Settings window
Manual calculation tool is added in order to calculate and visualize the system setup 
configuration by entering angle and distance values by hand without connecting the pairs to 
the laptop. It also has a guidance picture on the right.
Figure 8: Manual calculation tool window
It is also possible to check the measurements or manual entries visually by hovering 
to the right bottom image of the armored vehicle top.
Figure 9 & 10: Two visual check window examples. First is the default one and second one is created after a
mesaruments.
When the measurement process is done it is possible to create a mission file and save 
it to the desired directory. The system can be restarted and be ready for measurement when 
the system settings window is refreshed and the settings are saved.
Figure 11: The mission file can be saved to the desired directory in the computer.
3- PROJECT CHALLENGES 
The project had different problems to be solved. They are solved step by step during the 
design and development process. Those are:
 Determining measurement reference points:
It was very important to get healthy measurements and perform correct calculations. It is 
solved by designing some coverage platform which is fit for acoustic sensor windcape. In addition 
adding spherical bulbs on the top of the pairs ended up a sufficient alignment of the system 
to the acoustic sensor centers.
 Distance measurement:
Distance measurement seems easy by the engineering side. However, in this project it 
really differs when the system has less accuracy than 1 cm. Also spacing and parallel alignment 
is very important to get a correct measurement because of that reason using a lidar was a 
good option.
 Measuring angle:
Angle measurement is also an important parameter for the system. Using an 
accelerometer could be an option however small and cheap sensors are not working properly 
when the system moves back to previous positions. The solution was using a feedback servo.
 Controlling Continuous Servos:
Continuous Feedback servos get PWM signals in order to control only servo speed. It was 
a difficult challenge in that project to control those servos according to their angle positions 
considering cycle and signal parameters etc.
 Providing a proper motion to the necessary parts.
 Drawing 3D models for sensors and designed cases, holder parts for production and 
checking whether each component is fit.
 Designing sensor cages.
 Designing solid parts according to low weight, space and easy deployment purposes
 Arranging component placements considering future repairs and changes.
 Producing solid parts with few revisions and fastening them during the assembly.
 Software development for getting sensor data.
 Software development for correct position calculation w.r.t. True North.
 GUI development.
4- PROJECT BENEFITS
  Minimizing measurement and calculation time.
 Human mistakes are reduced.
 Being able to update sensor positions even if the sensors are configured by dummy 
angles or distances such as 53°, 134°, 321° etc.
 Considerable gain of time in integration and mounting process.
 It can provide an opportunity to change the configuration during a demonstration.
 The currently used solid frame can be eliminated by using this system.
 Even if a solid frame is used, this system can be used for a double check.
 In case of supplying that system with an order of sensor deployment coming from customers, it 
can be a chance for the end user to mount it to a different platform by themselves without 
a necessary call from company engineers. That can supply a profit in the aspect of time, 
employee labor, flight and accommodation costs etc. when an update in the configuration 
is demanded by the end user.
 It can be used in internal developments and upgrades to save time and labor of 
engineers.
 The system components can be repaired or changed easily.
 Low weight and small space requirement.
 System software can always be updated, upgraded or combined with external options.
5- FUTURE OPORTUNITIES
. As all components and software are designed and developed by considering future 
upgrades and updates some future improvements can be predictable.
After some kinematic analysis and designs it can be possible to measure and calculate 
elevation in the Z axis and pitch and roll .
The distance and angle accuracy can be increased by some extra software development or 
using different components.
The solid holder parts can be redesigned and servo control codes can be improved for a better 
and sharper movement. 
It can be possible to complete measurement by adding an extra step with end to end 
measurements between sensor posts even if there are visual obstacles such as RCWS, mast or 
other Payloads on the mounting platform.

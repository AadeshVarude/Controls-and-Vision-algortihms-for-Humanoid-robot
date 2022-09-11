Here in this repository we make three section for the Nimbro Humanoid robot.
- **A) Controls and Trajectory Generation** 
- **B) Edge Detection and Horizon Detection**
- **C) Object Detection using YOLOv4**

**Controls and Trajectory Generation:**


We generate a stabalised trajectory for the COM trajectory and end effector of swing leg trajectory for the multiple step of biped walkig using 3DLIPM.
The mathematical calculations and the code is provided in the controls folder.

![Multistep_3D](https://user-images.githubusercontent.com/50541542/189535476-c4854fa3-9a40-4413-8d60-dbaed86c1c06.gif)


**Edge Detection and Horizon Detection**
We create an HSV trackbar in order to create a customixed mask for better edge detection. Using the customixed mask we use the canny edge detection in order to detect the football edege field.


https://user-images.githubusercontent.com/50541542/189536013-0e3b7759-eb52-46e5-948d-d44f7b0c470b.mp4

Later using the HSV masking method and Canny edge detection we detection the edges and filter the field line by using Hough line transform. Later we choose a band to whcih we want to restrict our horizon.


https://user-images.githubusercontent.com/50541542/189536314-99117499-b2f0-4ced-a9fc-46cb6b04283f.mp4

**Object Detection using YOLOv4**
Now on this horizon deteected video we implement the YOLOv4 model to detect the footaball.



https://user-images.githubusercontent.com/50541542/189536533-3b465d77-683e-44ae-876a-e98503ca361d.mp4



# GO2-LiDAR-Rebuild
This project provides a complete ROS 2 Humble pipeline for running 2D SLAM on the Unitree GO2, using the robot’s built‑in LiDAR odometry (/utlidar/robot_odom) and a retimed LaserScan stream to produce a stable map → odom → base_link TF tree under sim time, with CycloneDDS configured for reliable communication over the GO2’s Ethernet interface; the package includes a TF relay for odometry, a scan retimer aligned to /clock, and a launch file that brings up the entire mapping stack with slam_toolbox for real‑time, drift‑free mapping.


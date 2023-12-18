# Overview

This document is intended to provide summary information on various data sets captured during Flight 1 of the Blue Origin Deorbit, Descent, and Landing Tipping Point (BODDL-TP) Flight 1. 

The flight was completed under NASA contract 80LARC19C0005 in October 2020.

Points of contact:
- Stefan Bieniawski <sbieniawski@blueorigion.com>, Blue Origin
- Kevin Somervill <kevin.m.somervill@nasa.gov>, NASA Langley Research Center


## Sections

- Events: timing of key events during flight
- Data Files: descriptions of data recorded
- Commercial LiDAR Frame Description: description of data frame format
- Camera and IMU Definitions: camera model and IMU coordinate frames
- Images: description of camera and image naming convention 

# Events

Point(s) of contact:
- Stefan Bieniawski <sbieniawski@blueorigion.com>, Blue Origin

## PURPOSE

This sections summarizes the main events and timing for Flight 1 of the Blue Origin Deorbit, Descent, and Landing Tipping Point (BODDL-TP).

All times are in TAI (International Atomic Time) time standard which is currently 37 seconds ahead of UTC. Element timestamps are in nanoseconds since 1970-01-01. The reference T-0 time is 1602596210210000000 nanoseconds which corresponds to 2020-10-13 13:36:13.21 UTC. The T-0 time corresponds to the engine command start and occurs prior to thrust build-up or liftoff.

Event			Elapsed Time(s)		Altitude (m) 
Ignition 		0 			1118 
Liftoff 		7.26 			1118
MECO 			143.49 			56281
Apogee 			246.6 			106744
Deploy brakes 		406.34 			6184
Restart ignition 	425.31 			2201 
Touchdown 		447.83 			1116

# Data Files

Point(s) of contact:
- Stefan Bieniawski <sbieniawski@blueorigion.com>, Blue Origin
- Sam Pedrotty <samuel.m.pedrotty@nasa.gov>, NASA Johnson Space Center


## PURPOSE

This section summarizes information on the data recorded by Blue Origin and the Safe and Precise Landing--Integrated Capability Evolution (SPLICE) Project for Flight 1 of the Blue Origin Deorbit, Descent, and Landing Tipping Point (BODDL-TP).

Three files are provided:
* truth.csv
* dlc.csv
* commercial_lidar.csv

## Time
The first column of each file is the time of validity for the data per the TAI timestamp.  See the section "Events" for additional information on the timing and major events.

## Data

* truth.csv
Contains the truth data of the host vehicle for the vehicle center of navigation. Positions and velocities are [m] in Earth-centered Earth-fixed frame. The quaternions use the Breckenridge definition of the quaternion, 
i^2 = j^2 = k^2 = -1, ijk=1. When represented in vector form, the scalar is last, e.g. [v0, v1, v2, s].

* dlc.csv
Contains the data recorded by SPLICE computer for the IMU. The delta-velocities and delta-angles are provided. The position and orientation of the IMU relative to vehicle CON is given in section "Camera and IMU Definition".

* commericial_lidar.csv
Contains the recorded data for the commercial lidar. Data includes the range and Doppler speed along each beam line of sight. Position and line of sight vectors relative to vehicle CON is given in section "Commercial LiDAR Frame".

# Commercial LiDAR Frame

Point(s) of contact:
- Stefan Bieniawski <sbieniawski@blueorigion.com>, Blue Origin

## PURPOSE

This section  is intended to capture details of the commercial LiDAR metrology as performed by Blue Origin for the Blue Origin Deorbit, Descent, and Landing Tipping Point (BODDL-TP).

LiDAR sensor head origin location in CON frame
Quantity	Units		Value
X_CON_LiDAR.p  	[m]    		[0.160, -3.13, -1.22]

LiDAR beam line of sight vectors in CON frame
Beam1	[-0.2998   -0.3996   -0.8663]
Beam2	[0.0810   -0.4900   -0.8680]
Beam3	[0.1178   -0.7326   -0.6703]
Beam4	[0.4192   -0.2778   -0.8643]


# Camera and IMU Definitions

Point(s) of contact:
- Nikolas Trawny <nikolas.trawny@jpl.nasa.gov>, Jet Propulsion Laboratory, California Institute of Technology. 
- Dylan Conway <dylan.t.conway@jpl.nasa.gov>, Jet Propulsion Laboratory, California Institute of Technology. 
- Daniel Clouse <daniel.s.clouse@jpl.nasa.gov>, Jet Propulsion Laboratory, California Institute of Technology. 
- Adnan Ansar <adnan.i.ansar@jpl.nasa.gov>, Jet Propulsion Laboratory, California Institute of Technology. 
- Sam Pedrotty <samuel.m.pedrotty@nasa.gov>, NASA Johnson Space Center.

## PURPOSE

This section provides the details of the DLC IMU alignment and DLC camera calibration parameters as calculated by the Jet Propulsion Laboratory, under a contract with the National Aeronautics and Space Administration, for Flight 1 of the Blue Origin Deorbit, Descent, and Landing Tipping Point (BODDL-TP).

Quantity			Units		Value	
pos_IMU_from_CON_in_CON		[m]		[-0.08035, 0.28390, -1.42333 ]
att_dcm_CON_IMU 				[-0.2477 -0.1673 0.9543
                				 -0.0478 0.9859 0.1604
              					 -0.9677 -0.0059 -0.2522]

pos_Camera_from_CON_in_CON  	[m]  		[-0.09649, 0.27776, -1.54774]
att_dcm_CON_Camera 				[ 0.1742 -0.9500 0.2590
		    				 -0.9847 -0.1681 0.0457
		   				  0.0001 -0.2630 -0.9648]

Camera model parameters.
R =
1.000000 0.000000 0.000000
0.000000 1.000000 0.000000
0.000000 0.000000 1.000000

T =
0.000000
0.000000
0.000000

k1 = -7.577065e-02
k2 = 2.939401e-02
k3 = -2.308007e-01
p1 = -6.624078e-03
p2 = 3.305442e-04

A =
4794.313768 0.000000 720.027670
0.000000 4800.628517 539.999614
0.000000 0.000000 1.000000

CAHVOR model
Dimensions = 1440 1080
C = 	-0.00000000 	-0.00000000 	-0.00000000
A = 	-0.00000001 	-0.00000018 	0.99999981
H = 	4798.00844238 	-0.00009184 	720.01146812
V = 	0.00005379	4809.93173657 	540.32613100
O = 	0.00436081 	-0.08773558 	0.99613423
R = 	-0.00018800 	-0.07566100 	0.01602100


# Images

Point(s) of contact:
- Sam Pedrotty <samuel.m.pedrotty@nasa.gov>, NASA Johnson Space Center.


## PURPOSE

This section summarizes information on the camera images as recorded by the Safe and Precise Landing--Integrated Capability Evolution (SPLICE) Project for Flight 1 of the Blue Origin Deorbit, Descent, and Landing Tipping Point (BODDL-TP).

The camera images from were recorded at 1Hz from a Blackfly camera, model BFS-PGE-16S2M-CS, which is a COTS device.

The camera metrology and calibration were performed pre-flight and the parameters are documented in section "Camera and IMU Definitions"

The images are named per the TAI timestamp of validity and two formats are provided.  See the section "Events" for additional information on the timing and major events.


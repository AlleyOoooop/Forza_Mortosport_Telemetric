# ---------------------------------------------------------------------------- #
# GNU GENERAL PUBLIC LICENSE                                                   #
# Version 3, 29 June 2007                                                      #
#                                                                              #
# Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>         #
# Everyone is permitted to copy and distribute verbatim copies                 #
# of this license document, but changing it is not allowed.                    #
#                                                                              #
# ---------------------------------------------------------------------------- #

# --------------------------------------- #
# Version : 1.0  July, 10th 2019          #
# Author  : Charly VILLETTE               #
# Mail    : villette.charly@gmail.com     #
# --------------------------------------- #

# ---------------------------------------------------------------------------- #
# NOTES                                                                        #
# -----                                                                        #
# > This program is intended to be run with PYTHON3 only                       #
# > This program has been tested and run with FORZA MOTORSPORT 7 on XBOX ONE X #
# > Enjoy !                                                                    #
# ---------------------------------------------------------------------------- #



################################################################################
#                                                                              #
#                        Forza Telemetry display                               #
#                                                                              #
################################################################################

#!/usr/bin/env python
# coding=utf-8

########################
#   Libraries Import   #
########################

# System
import sys
import os

# Network
import socket
import struct

# Date and time
import time
import datetime

# Graphical
from tkinter import * 
import tkinter as tk

# Thread
from threading import Thread

########################
#   Global Variables   #
########################

# Debug and test
Sim_XBOX_Test = False

# Network
UDP_IP                     = ""   # UDP IP-address
UDP_PORT                   = 4083 # UDP port
PACKET_SIZE                = 400  # Amount of bytes in packet

#Graphical informations
WindowWidth                = 1920
WindowHeigth               = 1080

#Wheel driveinformations
Tire_WD_FL_X                  = 65
Tire_WD_FL_Y                  = 605
Tire_WD_FR_X                  = 272
Tire_WD_FR_Y                  = 605
Tire_WD_RL_X                  = 65
Tire_WD_RL_Y                  = 831
Tire_WD_RR_X                  = 272
Tire_WD_RR_Y                  = 831
Tire_WD_Size_X                = 41
Tire_WD_Size_Y                = 82
Top_Transmition_X             = 106
Top_Transmition_Y             = 642
Bottom_Transmition_X          = 106
Bottom_Transmition_Y          = 868
Transmition_Size_X            = 166
Transmition_Size_Y            = 3
Top_Vertical_Transmition_X    = 184
Top_Vertical_Transmition_Y    = 645
Bottom_Vertical_Transmition_X = 184
Bottom_Vertical_Transmition_Y = 766
Vertical_Transmition_Size_X   = 10
Vertical_Transmition_Size_Y   = 105
Box_Transmision_X             = 176
Box_Transmision_Y             = 749
Box_Transmision_Size_X        = 26
Box_Transmision_Size_Y        = 18
Wheel_Drive                   = []
Wheel_Drive_Color             = "#B89C51"

#Speed Graph informations
Graph_X_left               = 88
Graph_Y_bottom             = 383
Graph_X_size               = 1017
Graph_Index                = 0
Graph_Array                = []
Plot_Graph                 = []
Graph_Speed_color          = "#B89C51"

#Speed informations
Speed_X_left               = 1120
Speed_Y_bottom             = 18
Speed_X_size               = 43
Speed_shift                = 10
Speed_color                = "#B89C51"
   
#Race Time informations
RaceTime_X_left            = 1120
RaceTime_Y_bottom          = 246
RaceTime_X_size            = 24
RaceTime_shift             = 7
RaceTime_global_shift      = 35
Timing_color               = "#B89C51"

#Lap Time informations
Lap_Time_X_left            = 1120
Lap_Time_Y_bottom          = 395
Lap_Time_X_size            = 24
Lap_Time_shift             = 7
Lap_Time_global_shift      = 35

#Last Lap Time informations
Last_Lap_X_left            = 1120
Last_Lap_Y_bottom          = 544
Last_Lap_X_size            = 24
Last_Lap_shift             = 7
Last_Lap_global_shift      = 35

#Best Lap Time informations
Best_Lap_X_left            = 1120
Best_Lap_Y_bottom          = 693
Best_Lap_X_size            = 24
Best_Lap_shift             = 7
Best_Lap_global_shift      = 35

#Race Position
Position_X_left            = 1478
Position_Y_bottom          = 842
Position_X_size            = 39
Position_shift             = 10
Race_Position_color        = "#B89C51"

#Lap Number
LapNumber_X_left           = 1120
LapNumber_Y_bottom         = 842
LapNumber_X_size           = 39
LapNumber_shift            = 10
LapNumber_color            = "#B89C51"

#Gear informations
Gear_X_left                = 1754
Gear_Y_bottom              = 18
Gear_X_size                = 43
Gear_shift                 = 10
Gear_color                 = "#B89C51"

#Fuel Gauge
Gauge_bottom_left_X        = 795
Gauge_bottom_left_Y        = 1057
Gauge_width                = 49
Gauge_heigth               = 208
Gauge_shift                = 13
Fuel_Bar                   = []
Small_line_half_width      = 5
Medium_line_half_width     = 12
Large_line_half_width      = 30
Gauge_level_line_color     = "#4C4430"
Fuel_color                 = "#FAE214"

#Accelerometer
Acceler_center_X           = 925
Acceler_center_Y           = 628
Acceler_size               = 340
Plot_size                  = 6
Accelero                   = []
Plot                       = []
Accelero_color             = "#FAE214"

#Tire Front Left informations
TFL_X_left                 = 427
TFL_Y_bottom               = 634
TFL_size                   = 4
TFL_shift                  = 3

#Tire Front Right informations
TFR_X_left                 = 634
TFR_Y_bottom               = 634
TFR_size                   = 4
TFR_shift                  = 3

#Tire Rear Left informations
TRL_X_left                 = 427
TRL_Y_bottom               = 860
TRL_size                   = 4
TRL_shift                  = 3

#Tire Rear Right informations
TRR_X_left                 = 634
TRR_Y_bottom               = 860
TRR_size                   = 4
TRR_shift                  = 3

#Temperature limit of tires
Temp_Tire_limit_1 = 80
Temp_Tire_limit_2 = 110
Temp_Tire_limit_3 = 130

#Class informations
Class_X_left               = 66
Class_Y_bottom             = 994
Class_size                 = 14
Class_shift                = 5
Class_color                = "#B89C51"

#RPM informations
RPM_X_left                 = 1750
RPM_Y_bottom               = 1028
RPM_X_size                 = 137
RPM_Y_size                 = 14
RPM_shift                  = 5
cell_number                = 36
RPM_Bar                    = []

#Acceleration informations
Acceler_X_left             = 254
Acceler_Y_bottom           = 500
AccelerRectangleWidth      = 240
AccelerRectangleHeigth     = 58
Acceler_rectangle          = []
Acceler_color              = "#1476FA"

#Brake informations
Brake_X_left               = 496
Brake_Y_bottom             = 500
BrakeRectangleWidth        = 242
BrakeRectangleHeigth       = 58
Brake_rectangle            = []
Brake_color                = "#FA1714"

#Clutch informations
Clutch_X_left              = 12
Clutch_Y_bottom            = 500
ClutchRectangleWidth       = 240
ClutchRectangleHeigth      = 58
Clutch_rectangle           = []
Clutch_color               = "#FACD14"

#Global variables
CellToDraw_mem      = 0
IsRaceOn_Color_mem         = "#000000"

#Box Number
NumberBox   = {"SpeedBox"           : [[],[],[]],
               "RaceTimeBox"        : [[],[],[]],
               "LapTimeBox"         : [[],[],[]],
               "LastLapBox"         : [[],[],[]],
               "BestLapBox"         : [[],[],[]],
               "RacePositionBox"    : [[],[]],
               "GearBox"            : [[]],
               "LapNumberBox"       : [[],[]],
               "TireTempFrontRight" : [[],[],[]] ,
               "TireTempFrontLeft"  : [[],[],[]] ,
               "TireTempRearLeft"   : [[],[],[]] ,
               "TireTempRearRight"  : [[],[],[]],
               "ClassBox"           : [[],[],[]] 
              }

# Window contour Bar
ContourWidth = 10
Contour_Bar  = []

# Telemetric array with datas sent from Forza game
TelemetricsDatas    = []

# Telemetric array used to memorize the values and check if they changed
TelemetricsDatasMEM = [] 

# Dictionnary of extra datas memorized
extra_datas = { "milliseconds" : 0 , "CellToDraw" : 0, "FirstDataReceived" : False}

####################################
# THREAD CLASS                     #
####################################
class Background(Thread):
   global extra_datas
   
   def __init__(self):
       Thread.__init__(self)

   def run(self):
      # Init UDP socket
      udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Create UDP Socket
      try:
         udp.bind((UDP_IP, UDP_PORT))
      except socket.error:
         print("UDP Socket link failed. Exiting...")
         sys.exit()

      global Sim_XBOX_Test

      ######################################
      # SIMULATE DATAS SENT BY XBOX FOR TEST
      if Sim_XBOX_Test :
         date = datetime.datetime.now()
         currentsecond = date.second
         thread_fps            = 0

         #telemetric datas simulated
         counter_Race_on       = 0
         break_race_on         = 125

         Inc_speed             = 0.1
         Inc_engine_RPM        = 100
         Inc_accel_X           = 0.1
         Inc_accel_Z           = 0.1
         Inc_Race_position     = 1
         Inc_Lap_Number        = 1
         Inc_Gear              = 1
         Inc_Accel             = 1
         Inc_Brake             = 1
         Inc_Clutch            = 1
         Inc_Tire_FL_Temp      = 1
         Inc_Tire_FR_Temp      = 1
         Inc_Tire_RL_Temp      = 1
         Inc_Tire_RR_Temp      = 1
         Inc_CarPerfIndex      = 1
         speed                 = 90
         RaceTime              = 0
         engineRPM             = 0
         fuel                  = 1
         accelX                = 0
         accelZ                = 0
         RacePosition          = 1
         LapNumber             = 0
         Gear                  = 1
         Accel                 = 1
         Brake                 = 1
         Clutch                = 1
         Tire_FL_Temp          = 345
         Tire_FR_Temp          = 2
         Tire_RL_Temp          = 202
         Tire_RR_Temp          = 78
         CarPerformanceIndex   = 1
         DrivetrainType        = 0 
         setTelemetricValue("IsRaceOn", 1)
         while 1:
            time.sleep(0.01)

            counter_Race_on +=1
            if counter_Race_on >= break_race_on :
               if getTelemetricValue("IsRaceOn") == 0 :
                  setTelemetricValue("IsRaceOn", 1)
               elif getTelemetricValue("IsRaceOn") == 1 :
                  setTelemetricValue("IsRaceOn", 0)
               counter_Race_on = 0

            if speed > 95 :
               Inc_speed = - 0.1
            elif speed < 1 :
               Inc_speed = 0.1
            speed += Inc_speed

            RaceTime += 0.02

            if engineRPM > 7900:
               Inc_engine_RPM = - 100
            if engineRPM < 100:
               Inc_engine_RPM = 100
            engineRPM += Inc_engine_RPM

            if fuel > 0 :
               fuel -= 0.001

            if accelX > 17 :
               Inc_accel_X = -0.1
            elif accelX < -17 :
               Inc_accel_X = 0.1

            if accelZ > 17 :
               Inc_accel_Z = -0.1
            elif accelZ < -17 :
               Inc_accel_Z = 0.1

            accelX += Inc_accel_X
            accelZ += Inc_accel_Z

            if RacePosition > 23 :
               Inc_Race_position = -1
            elif RacePosition < 1 :
               Inc_Race_position = 1
            RacePosition +=Inc_Race_position

            if LapNumber > 99 :
               Inc_Lap_Number = -1
            elif LapNumber < 1 :
               Inc_Lap_Number = 1
            LapNumber +=Inc_Lap_Number

            if Gear > 7 :
               Inc_Gear = -1
            elif Gear < 1 :
               Inc_Gear = 1
            Gear += Inc_Gear

            if Accel > 254 :
               Inc_Accel= -1
            elif Accel < 1 :
               Inc_Accel = 1
            Accel += Inc_Accel

            if Brake > 254 :
               Inc_Brake= -1
            elif Brake < 1 :
               Inc_Brake = 1
            Brake += Inc_Brake

            if Clutch > 254 :
               Inc_Clutch= -1
            elif Clutch < 1 :
               Inc_Clutch = 1
            Clutch += Inc_Clutch

            if Tire_FL_Temp > 200 :
               Inc_Tire_FL_Temp = -1
            elif Tire_FL_Temp < 1 :
               Inc_Tire_FL_Temp = 1
            Tire_FL_Temp += Inc_Tire_FL_Temp

            if Tire_FR_Temp > 200 :
               Inc_Tire_FR_Temp = -1
            elif Tire_FR_Temp < 1 :
               Inc_Tire_FR_Temp = 1
            Tire_FR_Temp += Inc_Tire_FR_Temp

            if Tire_RL_Temp > 200 :
               Inc_Tire_RL_Temp = -1
            elif Tire_RL_Temp < 1 :
               Inc_Tire_RL_Temp = 1
            Tire_RL_Temp += Inc_Tire_RL_Temp

            if Tire_RR_Temp > 200 :
               Inc_Tire_RR_Temp = -1
            elif Tire_RR_Temp < 1 :
               Inc_Tire_RR_Temp = 1
            Tire_RR_Temp += Inc_Tire_RR_Temp

            if CarPerformanceIndex > 999 :
               Inc_CarPerfIndex = -1
            elif CarPerformanceIndex < 1 :
               Inc_CarPerfIndex = 1
            CarPerformanceIndex += Inc_CarPerfIndex

            setTelemetricValue("DrivetrainType", DrivetrainType )
            setTelemetricValue("Speed", speed)
            setTelemetricValue("CurrentRaceTime", RaceTime)
            setTelemetricValue("CurrentLap", RaceTime)
            setTelemetricValue("BestLap", RaceTime)
            setTelemetricValue("LastLap", RaceTime)
            setTelemetricValue("CurrentEngineRpm", engineRPM)
            setTelemetricValue("Fuel", fuel)
            setTelemetricValue("AccelerationX", accelX)
            setTelemetricValue("AccelerationZ", accelZ)
            setTelemetricValue("RacePosition", bytes([RacePosition]))
            setTelemetricValue("LapNumber", LapNumber)
            setTelemetricValue("Gear", bytes([Gear]))
            setTelemetricValue("Accel", bytes([Accel]))
            setTelemetricValue("Brake", bytes([Brake]))
            setTelemetricValue("Clutch", bytes([Clutch]))
            setTelemetricValue("TireTempFrontLeft", Tire_FL_Temp)
            setTelemetricValue("TireTempFrontRight", Tire_FR_Temp)
            setTelemetricValue("TireTempRearLeft", Tire_RL_Temp)
            setTelemetricValue("TireTempRearRight", Tire_RR_Temp)
            setTelemetricValue("CarPerformanceIndex", CarPerformanceIndex)

            thread_fps +=1
            extra_datas["FirstDataReceived"] = True
            date = datetime.datetime.now()
            if currentsecond != date.second :
               DrivetrainType += 1
               if DrivetrainType > 2:
                  DrivetrainType = 0
               currentsecond = date.second
               print("thread_fps : " + str(thread_fps))
               thread_fps =0

      # END OF SIMULATION BLOCK FOR TESTS
      ###################################

      ###################################
      # DATAS FROM THE GAME
      else:
         # > Receive block
         while 1:
            data = udp.recvfrom(PACKET_SIZE)
            extra_datas["FirstDataReceived"] = True
            index = 0
            for element in range(0, len(TelemetricsDatas)): # Do for every item in the received array
               size = int(TelemetricsDatas[element][3]/8)
               TelemetricsDatas[element][1] = struct.unpack('<' + TelemetricsDatas[element][2], data[0][index:index+size])[0] # Add Value to the TelemetricsArray
               index += size 
      # DATAS FROM THE GAME
      ###################################

###############################
#    -  initTelemetrics  -    #
###############################
def initTelemetrics():
    global TelemetricsDatas # Access the global variable TelemetricsDatas
    TelemetricsDatas.append(["IsRaceOn"        , 0, 'i', 32]) # = 1 when race is on. = 0 when in menus/race stopped …
    TelemetricsDatas.append(["TimestampMS"     , 0, 'i', 32]) # Can overflow to 0 eventually
    TelemetricsDatas.append(["EngineMaxRpm"    , 0, 'f', 32]) # Engine Round per Minute Max
    TelemetricsDatas.append(["EngineIdleRpm"   , 0, 'f', 32]) # Engine Round per Minute Idle
    TelemetricsDatas.append(["CurrentEngineRpm", 0, 'f', 32]) # Current Engine Round per Minute

    TelemetricsDatas.append(["AccelerationX"   , 0, 'f', 32]) # Acceleration in the car's local space  X = right, Y = up, Z = forward
    TelemetricsDatas.append(["AccelerationY"   , 0, 'f', 32]) 
    TelemetricsDatas.append(["AccelerationZ"   , 0, 'f', 32]) 

    TelemetricsDatas.append(["VelocityX"       , 0, 'f', 32]) # Velocity in the car's local space  X = right, Y = up, Z = forward
    TelemetricsDatas.append(["VelocityY"       , 0, 'f', 32])
    TelemetricsDatas.append(["VelocityZ"       , 0, 'f', 32])

    TelemetricsDatas.append(["AngularVelocityX", 0, 'f', 32]) # AngularVelocity in the car's local space  X = right, Y = up, Z = forward
    TelemetricsDatas.append(["AngularVelocityY", 0, 'f', 32])
    TelemetricsDatas.append(["AngularVelocityZ", 0, 'f', 32])

    TelemetricsDatas.append(["Yaw"             , 0, 'f', 32])
    TelemetricsDatas.append(["Pitch"           , 0, 'f', 32])
    TelemetricsDatas.append(["Roll"            , 0, 'f', 32])

    TelemetricsDatas.append(["NormalizedSuspensionTravelFrontLeft"  , 0, 'f', 32]) # Suspension travel normalized, 0.0f = max stretch; 1.0 = max compression
    TelemetricsDatas.append(["NormalizedSuspensionTravelFrontRight" , 0, 'f', 32])
    TelemetricsDatas.append(["NormalizedSuspensionTravelRearLeft"   , 0, 'f', 32])
    TelemetricsDatas.append(["NormalizedSuspensionTravelRearRight"  , 0, 'f', 32])

    TelemetricsDatas.append(["TireSlipRatioFrontLeft"  , 0, 'f', 32]) # Tire normalized slip ratio, = 0 means 100% grip and |ratio| > 1.0 means loss of grip
    TelemetricsDatas.append(["TireSlipRatioFrontRight" , 0, 'f', 32])
    TelemetricsDatas.append(["TireSlipRatioRearLeft"   , 0, 'f', 32])
    TelemetricsDatas.append(["TireSlipRatioRearRight"  , 0, 'f', 32])

    TelemetricsDatas.append(["WheelRotationSpeedFrontLeft"  , 0, 'f', 32]) # Wheel rotation speed radians/sec
    TelemetricsDatas.append(["WheelRotationSpeedFrontRight" , 0, 'f', 32])
    TelemetricsDatas.append(["WheelRotationSpeedRearLeft"   , 0, 'f', 32])
    TelemetricsDatas.append(["WheelRotationSpeedRearRight"  , 0, 'f', 32])

    TelemetricsDatas.append(["WheelOnRumbleStripFrontLeft"  , 0, 'i', 32]) # = 1 when wheel is on rumble strip, = 0 when off
    TelemetricsDatas.append(["WheelOnRumbleStripFrontRight" , 0, 'i', 32])
    TelemetricsDatas.append(["WheelOnRumbleStripRearLeft"   , 0, 'i', 32])
    TelemetricsDatas.append(["WheelOnRumbleStripRearRight"  , 0, 'i', 32])

    TelemetricsDatas.append(["WheelInPuddleDepthFrontLeft"  , 0, 'f', 32]) # = from 0 to 1, where 1 is the deepest puddle
    TelemetricsDatas.append(["WheelInPuddleDepthFrontRight" , 0, 'f', 32])
    TelemetricsDatas.append(["WheelInPuddleDepthRearLeft"   , 0, 'f', 32])
    TelemetricsDatas.append(["WheelInPuddleDepthRearRight"  , 0, 'f', 32])

    TelemetricsDatas.append(["SurfaceRumbleFrontLeft"  , 0, 'f', 32]) # Non-dimensional surface rumble values passed to controller force feedback
    TelemetricsDatas.append(["SurfaceRumbleFrontRight" , 0, 'f', 32])
    TelemetricsDatas.append(["SurfaceRumbleRearLeft"   , 0, 'f', 32])
    TelemetricsDatas.append(["SurfaceRumbleRearRight"  , 0, 'f', 32])

    TelemetricsDatas.append(["TireSlipAngleFrontLeft"  , 0, 'f', 32]) # Tire normalized slip angle, = 0 means 100% grip and |angle| > 1.0 means loss of grip.
    TelemetricsDatas.append(["TireSlipAngleFrontRight" , 0, 'f', 32])
    TelemetricsDatas.append(["TireSlipAngleRearLeft"   , 0, 'f', 32])
    TelemetricsDatas.append(["TireSlipAngleRearRight"  , 0, 'f', 32])

    TelemetricsDatas.append(["TireCombinedSlipFrontLeft"  , 0, 'f', 32]) # Tire normalized combined slip, = 0 means 100% grip and |slip| > 1.0 means loss of grip.
    TelemetricsDatas.append(["TireCombinedSlipFrontRight" , 0, 'f', 32])
    TelemetricsDatas.append(["TireCombinedSlipRearLeft"   , 0, 'f', 32])
    TelemetricsDatas.append(["TireCombinedSlipRearRight"  , 0, 'f', 32])

    TelemetricsDatas.append(["SuspensionTravelMetersFrontLeft"  , 0, 'f', 32]) # Actual suspension travel in meters
    TelemetricsDatas.append(["SuspensionTravelMetersFrontRight" , 0, 'f', 32])
    TelemetricsDatas.append(["SuspensionTravelMetersRearLeft"   , 0, 'f', 32])
    TelemetricsDatas.append(["SuspensionTravelMetersRearRight"  , 0, 'f', 32])

    TelemetricsDatas.append(["CarOrdinal"            , 0, 'i', 32]) # Actual suspension travel in meters
    TelemetricsDatas.append(["CarClass"              , 0, 'i', 32]) # Between 0 (D -- worst cars) and 7 (X class -- best cars) inclusive 
    TelemetricsDatas.append(["CarPerformanceIndex"   , 0, 'i', 32]) # Between 100 (slowest car) and 999 (fastest car) inclusive
    TelemetricsDatas.append(["DrivetrainType"        , 0, 'i', 32]) # Corresponds to EDrivetrainType; 0 = FWD, 1 = RWD, 2 = AWD
    TelemetricsDatas.append(["NumCylinders"          , 0, 'i', 32]) # Number of cylinders in the engine

    TelemetricsDatas.append(["PositionX"  , 0, 'f', 32]) # Position (meters)
    TelemetricsDatas.append(["PositionY"  , 0, 'f', 32])
    TelemetricsDatas.append(["PositionZ"  , 0, 'f', 32])

    TelemetricsDatas.append(["Speed"   , 0, 'f', 32]) # meters per second
    TelemetricsDatas.append(["Power"   , 0, 'f', 32]) # watts
    TelemetricsDatas.append(["Torque"  , 0, 'f', 32]) # newton meters

    TelemetricsDatas.append(["TireTempFrontLeft"  , 0, 'f', 32]) # Tire Temperature
    TelemetricsDatas.append(["TireTempFrontRight" , 0, 'f', 32])
    TelemetricsDatas.append(["TireTempRearLeft"   , 0, 'f', 32])
    TelemetricsDatas.append(["TireTempRearRight"  , 0, 'f', 32])

    TelemetricsDatas.append(["Boost"            , 0, 'f', 32]) # Boost
    TelemetricsDatas.append(["Fuel"             , 0, 'f', 32]) # Boost
    TelemetricsDatas.append(["DistanceTraveled" , 0, 'f', 32]) # Fuel
    TelemetricsDatas.append(["BestLap"          , 0, 'f', 32]) # BestLap
    TelemetricsDatas.append(["LastLap"          , 0, 'f', 32]) # LastLap
    TelemetricsDatas.append(["CurrentLap"       , 0, 'f', 32]) # CurrentLap
    TelemetricsDatas.append(["CurrentRaceTime"  , 0, 'f', 32]) # CurrentRaceTime
    TelemetricsDatas.append(["LapNumber"        , 0, 'h', 16]) # LapNumber
    TelemetricsDatas.append(["RacePosition"     , 0, 'c', 8]) # RacePosition
    TelemetricsDatas.append(["Accel"            , 0, 'c', 8]) # Acceleration
    TelemetricsDatas.append(["Brake"            , 0, 'c', 8]) # Brake
    TelemetricsDatas.append(["Clutch"           , 0, 'c', 8]) # Clutch
    TelemetricsDatas.append(["HandBrake"        , 0, 'c', 8]) # HandBrake
    TelemetricsDatas.append(["Gear"             , 0, 'c', 8]) # Gear
    TelemetricsDatas.append(["Steer"            , 0, 'c', 8]) # Steer

    TelemetricsDatas.append(["NormalizedDrivingLine"       , 0, 'c', 8]) # NormalizedDrivingLine
    TelemetricsDatas.append(["NormalizedAIBrakeDifference" , 0, 'c', 8]) # NormalizedAIBrakeDifference

##################################
#    -  initTelemetricsMEM  -    #
##################################
def initTelemetricsMEM():
   global TelemetricsDatasMEM
   for element in TelemetricsDatas :
      TelemetricsDatasMEM.append([element[0], element[1], False])

################################
#    -  init Graph Array  -    #
################################
def initGraph_Array():
   global Graph_Array
   global Plot_Graph
   global Graph_X_size
   for element in range (0,Graph_X_size):
      Plot_Graph.append(0)
      Graph_Array.append(0)

############################
#    -  init RPM Bar  -    #
############################
def initRPMBar():
   global RPM_Bar
   for element in range (0,cell_number): 
      RPM_Bar.append(0)

################################
#    -  init Contour Bar  -    #
################################
def initContourBar():
   global Contour_Bar
   for element in range (0,4): 
      Contour_Bar.append(0)

#################################
#    - getTelemetricValue  -    #
#################################
def getTelemetricValue(Name):
   global TelemetricsDatas
   for element in TelemetricsDatas:
      if element[0] == Name :
         return element[1]
   return -1

####################################
#    - getTelemetricValueMEM  -    #
####################################
def getTelemetricValueMEM(Name):
   global TelemetricsDatasMEM
   for element in TelemetricsDatasMEM:
      if element[0] == Name :
         return element[1]
   return -1

#################################
#    - setTelemetricValue  -    #
#################################
def setTelemetricValue(Name, Value):
   global TelemetricsDatas
   for element in TelemetricsDatas:
      if element[0] == Name :
         element[1] = Value

####################################
#    - setTelemetricValueMEM  -    #
####################################
def setTelemetricValueMEM(Name, Value):
   global TelemetricsDatasMEM
   for element in TelemetricsDatasMEM:
      if element[0] == Name :
            element[1] = Value

############################
#    - Display number -    #
############################
def displayNumber(X, Y, Size, Shift, DigitNumber, Number, Color, Box, DisplayZero):
   global NumberBox
   DigitCounter = 0
   #Shift is the pixel size between 2 digits -> The global shit between 2 digits is the size of 3 columns of a digit + the shift size between 2 digits
   GlobalShift = 0 
   NumberArray = []

   if Number < 10**DigitNumber : #only display the number if enough digits provided
      # Get the Hundred
      if Number > 99 and DigitNumber > 2 :
            NumberArray.append(int((Number       - Number % 100) / 100)) 
      else :
         if DigitNumber > 2 :
            if(DisplayZero):
               NumberArray.append(0)
            else :
               DigitCounter +=1

      # Get the Decade
      if Number > 9 and DigitNumber > 1:
            NumberArray.append(int((Number % 100 - Number % 10 ) / 10 )) 
      else :
         if DigitNumber > 1:
            if(DisplayZero):
               NumberArray.append(0)
            else :
               DigitCounter +=1

      # Get the Unit
      NumberArray.append( Number % 10)
      
         #  X   XXX  XXX  X X  XXX  XXX  XXX  XXX  XXX  XXX    box_0  box_1  box_2
         # XX     X    X  X X  X    X      X  X X  X X  X X    box_3  box_4  box_5
         #  X   XXX   XX  XXX  XXX  XXX    X  XXX  XXX  X X    box_6  box_7  box_8
         #  X   X      X    X    X  X X    X  X X    X  X X    box_9  box_10 box_11
         # XXX  XXX  XXX    X  XXX  XXX    X  XXX  XXX  XXX    box_12 box_13 box_14
      for number in NumberArray:
         GlobalShift = DigitCounter * (Shift + 3 * Size)
         # from top left to bottom right
         if number != 1 :
            NumberBox[Box][DigitCounter].append(canvasBoard.create_rectangle(X            + GlobalShift, Y,            X + Size     + GlobalShift - 1, Y + Size     - 1, fill = Color, width=0)) #box_0
            NumberBox[Box][DigitCounter].append(canvasBoard.create_rectangle(X + 2 * Size + GlobalShift, Y,            X + 3 * Size + GlobalShift - 1, Y + Size     - 1, fill = Color, width=0)) #box_2
            NumberBox[Box][DigitCounter].append(canvasBoard.create_rectangle(X + 2 * Size + GlobalShift, Y + 2 * Size, X + 3 * Size + GlobalShift - 1, Y + 3 * Size - 1, fill = Color, width=0)) #box_8
         if number != 4 :
            NumberBox[Box][DigitCounter].append(canvasBoard.create_rectangle(X + Size     + GlobalShift, Y,            X + 2 * Size + GlobalShift - 1, Y + Size - 1,     fill = Color, width=0)) #box_1

         if number != 2 and number != 3 and number != 7 :
            NumberBox[Box][DigitCounter].append(canvasBoard.create_rectangle(X            + GlobalShift, Y + Size,     X + Size     + GlobalShift - 1, Y + 2 * Size - 1, fill = Color, width=0)) #box_3

         if number == 1 :
            NumberBox[Box][DigitCounter].append(canvasBoard.create_rectangle(X + Size     + GlobalShift, Y + Size,     X + 2 * Size + GlobalShift - 1, Y + 2 * Size - 1, fill = Color, width=0)) #box_4
            NumberBox[Box][DigitCounter].append(canvasBoard.create_rectangle(X + Size     + GlobalShift, Y + 3 * Size, X + 2 * Size + GlobalShift - 1, Y + 4 * Size - 1, fill = Color, width=0)) #box_10

         if number != 1 and number != 5 and number != 6:
            NumberBox[Box][DigitCounter].append(canvasBoard.create_rectangle(X + 2 * Size + GlobalShift, Y + Size,     X + 3 * Size + GlobalShift - 1, Y + 2 * Size - 1, fill = Color, width=0)) #box_5

         if number != 1 and number != 3 and number != 7:
            NumberBox[Box][DigitCounter].append(canvasBoard.create_rectangle(X            + GlobalShift, Y + 2 * Size, X + Size     + GlobalShift - 1, Y + 3 * Size - 1, fill = Color, width=0)) #box_6

         if number != 7 and number != 0:
            NumberBox[Box][DigitCounter].append(canvasBoard.create_rectangle(X + Size     + GlobalShift, Y + 2 * Size, X + 2 * Size + GlobalShift - 1, Y + 3 * Size - 1, fill = Color, width=0)) #box_7

         if number == 2 or number == 6 or number == 8 or number == 0 :
            NumberBox[Box][DigitCounter].append(canvasBoard.create_rectangle(X            + GlobalShift, Y + 3 * Size, X + Size     + GlobalShift - 1, Y + 4 * Size - 1, fill = Color, width=0)) #box_9

         if number != 1 and number != 2 :
            NumberBox[Box][DigitCounter].append(canvasBoard.create_rectangle(X + 2 * Size + GlobalShift, Y + 3 * Size, X + 3 * Size + GlobalShift  -1, Y + 4 * Size - 1, fill = Color, width=0)) #box_11

         if number != 4 and number != 7 :
            NumberBox[Box][DigitCounter].append(canvasBoard.create_rectangle(X            + GlobalShift, Y + 4 * Size, X + Size     + GlobalShift - 1, Y + 5 * Size - 1, fill = Color, width=0)) #box_12
            NumberBox[Box][DigitCounter].append(canvasBoard.create_rectangle(X + Size     + GlobalShift, Y + 4 * Size, X + 2 * Size + GlobalShift - 1, Y + 5 * Size - 1, fill = Color, width=0)) #box_13

         #For all numbers, box_14 has to be drawn
         NumberBox[Box][DigitCounter].append(canvasBoard.create_rectangle(   X + 2 * Size + GlobalShift, Y + 4 * Size, X + 3 * Size + GlobalShift - 1,    Y + 5 * Size - 1, fill = Color, width=0)) #box_14
         DigitCounter += 1

#################################
#    - Display graph speed -    #
#################################
def displayGraphSpeed(Speed):
   global Graph_Speed_color
   global Plot_Graph
   global Graph_Index
   global Graph_Array
   global Graph_X_size
   global Graph_X_left
   global Graph_Y_bottom
   if(Graph_Index + 1 >= Graph_X_size):
      Graph_Index = 0
      Graph_Array[Graph_Index] = Graph_Array[Graph_X_size - 1]

   Graph_Array[Graph_Index + 1 ] = Speed
   Plot_Graph[Graph_Index] = canvasBoard.create_line(Graph_X_left + Graph_Index, Graph_Y_bottom - Graph_Array[Graph_Index], Graph_X_left + Graph_Index + 1, Graph_Y_bottom - Graph_Array[Graph_Index + 1], fill = Graph_Speed_color, width=2)

   Graph_Index += 1

#########################
#    - Display RPM -    #
#########################
def displayRPM(cellToDraw):
   global RPM_Bar
   global RPM_X_left
   global RPM_Y_bottom
   global RPM_X_size
   global RPM_Y_size
   global RPM_shift
   global cell_number
   index_RPM = 0 
   color_shade = 0 #shade between 0 and 255
   color = "#00FF00"
   global_shift = RPM_Y_size + RPM_shift
   for element in range(0, cellToDraw):
      if index_RPM >= int(cell_number * 3 / 4):
         color_shade = 255 - ((index_RPM - int(cell_number * 3 / 4)) * (255 / int(cell_number / 4)))
         color = "#FF" + "{:02X}".format(int(color_shade)) + "00"
      elif index_RPM >= int(cell_number / 2):
         color_shade = ((index_RPM - int(cell_number/2))* (255 / int(cell_number / 4)))
         color = "#" + "{:02X}".format(int(color_shade)) + "FF00"
      RPM_Bar[index_RPM] = canvasBoard.create_rectangle(RPM_X_left, RPM_Y_bottom - index_RPM * global_shift,RPM_X_left + RPM_X_size, RPM_Y_bottom - RPM_Y_size - index_RPM * global_shift, fill = color, width=0)
      index_RPM += 1

###########################
#    - Display speed -    #
###########################
def displaySpeed(Speed):
   global Speed_color
   global Speed_X_left
   global Speed_Y_bottom
   global Speed_X_size
   global Speed_shift
   displayAllZeros = False
   NumberOfDigitsToDisplay = 3
   displayNumber(Speed_X_left, Speed_Y_bottom,Speed_X_size, Speed_shift, NumberOfDigitsToDisplay, Speed, Speed_color, "SpeedBox", displayAllZeros)

###################################
#    - Display race position -    #
###################################
def displayRacePosition(Position):
   global Race_Position_color
   global Position_X_left
   global Position_Y_bottom
   global Position_X_size
   global Position_shift
   displayAllZeros = False
   NumberOfDigitsToDisplay = 2
   displayNumber(Position_X_left, Position_Y_bottom, Position_X_size, Position_shift, NumberOfDigitsToDisplay, ord(Position), Race_Position_color, "RacePositionBox", displayAllZeros)

################################
#    - Display lap number -    #
################################
def displayLapNumber(LapNumber):
   global LapNumber_color
   global LapNumber_X_left
   global LapNumber_Y_bottom
   global LapNumber_X_size
   global LapNumber_shift
   displayAllZeros = False
   NumberOfDigitsToDisplay = 2
   displayNumber(LapNumber_X_left, LapNumber_Y_bottom, LapNumber_X_size, LapNumber_shift, NumberOfDigitsToDisplay, LapNumber, LapNumber_color, "LapNumberBox", displayAllZeros)

##########################
#    - Display gear -    #
##########################
def displayGear(Gear):
   global Gear_color
   global Gear_X_left
   global Gear_Y_bottom
   global Gear_X_size
   global Gear_shift
   displayAllZeros = False
   NumberOfDigitsToDisplay = 1
   displayNumber(Gear_X_left, Gear_Y_bottom,Gear_X_size, Gear_shift, NumberOfDigitsToDisplay, ord(Gear), Gear_color, "GearBox", displayAllZeros)

##########################
#    - Display time -    #
##########################
def displayTime(TimeXleft, TimeYbottom, TimeXsize, TimeShift, TimeGlobalShift, Minute, Second, Millisecond, Box, Color):
   displayAllZeros = True
   displayNumber(TimeXleft                                                                                                   , TimeYbottom, TimeXsize,TimeShift, 2, Minute,      Color, Box, displayAllZeros)
   displayNumber(TimeXleft + TimeShift+ TimeXsize*6 + TimeGlobalShift                                                        , TimeYbottom, TimeXsize,TimeShift, 2, Second,      Color, Box, displayAllZeros)
   displayNumber(TimeXleft + TimeShift+ TimeXsize*6 + TimeGlobalShift + TimeXsize*6 + TimeShift + TimeGlobalShift,TimeYbottom, TimeXsize,   TimeShift,           3, Millisecond, Color, Box, displayAllZeros)

###############################
#    - Display race time -    #
###############################
def displayRaceTime(RaceTime):
   global Timing_color
   global RaceTime_X_left
   global RaceTime_Y_bottom
   global RaceTime_X_size
   global RaceTime_shift
   global RaceTime_global_shift
   minutes  = int(RaceTime / 60)
   secondes = int(RaceTime % 60)
   milisec  = int(1000 * (RaceTime - 60 * minutes - secondes))
   displayTime(RaceTime_X_left, RaceTime_Y_bottom, RaceTime_X_size, RaceTime_shift, RaceTime_global_shift, minutes, secondes, milisec, "RaceTimeBox", Timing_color)

##############################
#    - Display lap time -    #
##############################
def displayLapTime(LapTime):
   global Timing_color
   global Lap_Time_X_left
   global Lap_Time_Y_bottom
   global Lap_Time_X_size
   global Lap_Time_shift
   global Lap_Time_global_shift
   global LapTimeBox
   minutes  = int(LapTime / 60)
   secondes = int(LapTime % 60)
   milisec  = int(1000 * (LapTime - 60 * minutes - secondes))
   displayTime(Lap_Time_X_left, Lap_Time_Y_bottom, Lap_Time_X_size, Lap_Time_shift, Lap_Time_global_shift, minutes, secondes, milisec, "LapTimeBox", Timing_color)

##############################
#    - Display last lap -    #
##############################
def displayLastLap(LastLap):
   global Timing_color
   global Last_Lap_X_left
   global Last_Lap_Y_bottom
   global Last_Lap_X_size
   global Last_Lap_shift
   global Last_Lap_global_shift
   global LastLapBox
   minutes  = int(LastLap / 60)
   secondes = int(LastLap % 60)
   milisec  = int(1000 * (LastLap - 60 * minutes - secondes))
   displayTime(Last_Lap_X_left, Last_Lap_Y_bottom, Last_Lap_X_size, Last_Lap_shift, Last_Lap_global_shift, minutes, secondes, milisec, "LastLapBox", Timing_color)

##############################
#    - Display best lap -    #
##############################
def displayBestLap(BestLap):
   global Timing_color
   global Best_Lap_X_left
   global Best_Lap_Y_bottom
   global Best_Lap_X_size
   global Best_Lap_shift
   global Best_Lap_global_shift
   global BestLapBox
   minutes  = int(BestLap / 60)
   secondes = int(BestLap % 60)
   milisec  = int(1000 * (BestLap - 60 * minutes - secondes))
   displayTime(Best_Lap_X_left, Best_Lap_Y_bottom, Best_Lap_X_size, Best_Lap_shift, Best_Lap_global_shift,  minutes, secondes, milisec, "BestLapBox", Timing_color)

#############################
#    - Display contour -    #
#############################
def displayContour(Color):
   global Contour_Bar
   global WindowWidth
   global WindowHeigth
   global ContourWidth
   Contour_Bar[0] = canvasBoard.create_rectangle(1                          , 1                           , WindowWidth     , ContourWidth                , fill = Color, width=0)
   Contour_Bar[1] = canvasBoard.create_rectangle(1                          , 1                           , ContourWidth    , WindowHeigth - ContourWidth , fill = Color, width=0)
   Contour_Bar[2] = canvasBoard.create_rectangle(1                          , WindowHeigth - ContourWidth , WindowWidth     , WindowHeigth                , fill = Color, width=0)
   Contour_Bar[3] = canvasBoard.create_rectangle(WindowWidth - ContourWidth , 1                           , WindowWidth     , WindowHeigth - ContourWidth , fill = Color, width=0)

##################################
#    - Display acceleration -    #
##################################
def displayAcceleration(Acceler):
   global Acceler_color
   global Acceler_rectangle
   global Acceler_X_left
   global Acceler_Y_bottom
   global AccelerRectangleWidth 
   global AccelerRectangleHeigth
   Acceler_size = int((ord(Acceler) / 255) * AccelerRectangleHeigth)
   if Acceler_size > 1:
      Acceler_rectangle.append(canvasBoard.create_rectangle(Acceler_X_left, Acceler_Y_bottom, Acceler_X_left + AccelerRectangleWidth , Acceler_Y_bottom - Acceler_size , fill = Acceler_color, width=0))

###########################
#    - Display brake -    #
###########################
def displayBrake(Brake):
   global Brake_color
   global Brake_rectangle
   global Brake_X_left
   global Brake_Y_bottom
   global BrakeRectangleWidth 
   global BrakeRectangleHeigth 
   Brake_size = int((ord(Brake)/255)*BrakeRectangleHeigth)
   if Brake_size > 1:
      Brake_rectangle.append(canvasBoard.create_rectangle(Brake_X_left, Brake_Y_bottom, Brake_X_left + BrakeRectangleWidth , Acceler_Y_bottom - Brake_size , fill = Brake_color, width=0))

############################
#    - Display clutch -    #
############################
def displayClutch(Clutch):
   global Clutch_color
   global Clutch_rectangle
   global Clutch_X_left
   global Clutch_Y_bottom
   global ClutchRectangleWidth 
   global ClutchRectangleHeigth
   Clutch_size = int((ord(Clutch) / 255) * ClutchRectangleHeigth)
   if Clutch_size > 1:
      Clutch_rectangle.append(canvasBoard.create_rectangle(Clutch_X_left, Clutch_Y_bottom, Clutch_X_left + ClutchRectangleWidth , Acceler_Y_bottom - Clutch_size , fill = Clutch_color, width=0))

################################
#    - Display fuel level -    #
################################
def displayFuelLevel (Fuel):
   global Fuel_color
   global Gauge_level_line_color
   global Fuel_Bar
   global Gauge_width
   global Gauge_heigth
   global Gauge_bottom_left_X
   global Gauge_bottom_left_Y
   global Gauge_shift
   global Small_line_half_width
   global Medium_line_half_width
   global Large_line_half_width
   level_fuel = int(Fuel*Gauge_heigth)
   if level_fuel >= 0 and level_fuel <= Gauge_heigth :
      Fuel_Bar.append(canvasBoard.create_rectangle(Gauge_bottom_left_X              , Gauge_bottom_left_Y,\
                                                   Gauge_bottom_left_X + Gauge_width, Gauge_bottom_left_Y - level_fuel, fill = Fuel_color, width=0))
      #Draw level lines
      #vertical
      Fuel_Bar.append(canvasBoard.create_line(Gauge_bottom_left_X + int(Gauge_width / 2), Gauge_bottom_left_Y,\
                                              Gauge_bottom_left_X + int(Gauge_width / 2), Gauge_bottom_left_Y - Gauge_heigth, fill = Gauge_level_line_color, width=1))
   # horizontal
   for i in range (0, 8):
      Fuel_Bar.append(canvasBoard.create_line(Gauge_bottom_left_X + int(Gauge_width / 2) - Small_line_half_width,      Gauge_bottom_left_Y - Gauge_shift - i*(Gauge_shift * 2),\
                                              Gauge_bottom_left_X + int(Gauge_width / 2) + Small_line_half_width + 1,  Gauge_bottom_left_Y - Gauge_shift - i*(Gauge_shift * 2), fill = Gauge_level_line_color, width=1))
   for i in range (0, 4):
      Fuel_Bar.append(canvasBoard.create_line(Gauge_bottom_left_X + int(Gauge_width / 2) - Medium_line_half_width,     Gauge_bottom_left_Y - 2 * Gauge_shift - i*(Gauge_shift * 4),\
                                              Gauge_bottom_left_X + int(Gauge_width / 2) + Medium_line_half_width + 1, Gauge_bottom_left_Y - 2 * Gauge_shift - i*(Gauge_shift * 4), fill = Gauge_level_line_color, width=2))
   for i in range (0, 4):
      Fuel_Bar.append(canvasBoard.create_line(Gauge_bottom_left_X + int(Gauge_width / 2) - Large_line_half_width,      Gauge_bottom_left_Y - 4 * Gauge_shift - i*(Gauge_shift * 4),\
                                              Gauge_bottom_left_X + int(Gauge_width / 2) + Large_line_half_width + 1,  Gauge_bottom_left_Y - 4 * Gauge_shift - i*(Gauge_shift * 4), fill = Gauge_level_line_color, width=3))

###################################
#    - Display accelerometer -    #
###################################
def displayAccelero(X, Z):
   global Accelero_color
   global Accelero
   global Acceler_center_X
   global Acceler_center_Y
   global Acceler_center_Y
   global Plot_size
   #adapt datas for better display
   x = - X * 8
   z =   Z * 8
   if x > Acceler_size / 2 :
      x = Acceler_size / 2 
   if x < (-1) * Acceler_size / 2 :
      x = (-1) * Acceler_size / 2 
   if z > Acceler_size / 2 :
      z = Acceler_size / 2 
   if z < (-1) * Acceler_size / 2 :
      z = (-1) * Acceler_size / 2 
   Accelero.append(canvasBoard.create_rectangle(Acceler_center_X + x - Plot_size, Acceler_center_Y + z - Plot_size,Acceler_center_X + x + Plot_size , Acceler_center_Y + z + Plot_size,fill = Accelero_color, width=1))

#################################################
#    - Display Tire front left temperature -    #
#################################################
def displayTireFrontLeft(TireTempFL):
   global TFL_X_left
   global TFL_Y_bottom
   global TFL_size
   global TFL_shift
   global Temp_Tire_limit_1
   global Temp_Tire_limit_2
   global Temp_Tire_limit_3
   displayAllZeros         = False
   NumberOfDigitsToDisplay = 3
   Color = "#17A9EE"   #Blue
   if (TireTempFL > Temp_Tire_limit_1) and (TireTempFL < Temp_Tire_limit_2):
      Color = "#62EE17"   #Green
   if (TireTempFL >= Temp_Tire_limit_2) and (TireTempFL < Temp_Tire_limit_3):
      Color = "#EEDA17"   #Yellow
   if (TireTempFL >= Temp_Tire_limit_3):
      Color = "#EE2E17"   #Red
   displayNumber(TFL_X_left, TFL_Y_bottom, TFL_size, TFL_shift, NumberOfDigitsToDisplay, int(TireTempFL), Color, "TireTempFrontLeft", displayAllZeros)

##################################################
#    - Display Tire front right temperature -    #
##################################################
def displayTireFrontRight(TireTempFR):
   global TFR_X_left
   global TFR_Y_bottom
   global TFR_size
   global TFR_shift
   global Temp_Tire_limit_1
   global Temp_Tire_limit_2
   global Temp_Tire_limit_3
   displayAllZeros         = False
   NumberOfDigitsToDisplay = 3
   Color = "#17A9EE"   #Blue
   if (TireTempFR > Temp_Tire_limit_1) and (TireTempFR < Temp_Tire_limit_2):
      Color = "#62EE17"   #Green
   if (TireTempFR >= Temp_Tire_limit_2) and (TireTempFR < Temp_Tire_limit_3):
      Color = "#EEDA17"   #Yellow
   if (TireTempFR >= Temp_Tire_limit_3):
      Color = "#EE2E17"   #Red
   displayNumber(TFR_X_left, TFR_Y_bottom, TFR_size, TFR_shift, NumberOfDigitsToDisplay, int(TireTempFR), Color, "TireTempFrontRight", displayAllZeros)

################################################
#    - Display Tire rear left temperature -    #
################################################
def displayTireRearLeft(TireTempRL):
   global TRL_X_left
   global TRL_Y_bottom
   global TRL_size
   global TRL_shift
   global Temp_Tire_limit_1
   global Temp_Tire_limit_2
   global Temp_Tire_limit_3
   displayAllZeros         = False
   NumberOfDigitsToDisplay = 3
   Color = "#17A9EE"   #Blue
   if (TireTempRL > Temp_Tire_limit_1) and (TireTempRL < Temp_Tire_limit_2):
      Color = "#62EE17"   #Green
   if (TireTempRL >= Temp_Tire_limit_2) and (TireTempRL < Temp_Tire_limit_3):
      Color = "#EEDA17"   #Yellow
   if (TireTempRL >= Temp_Tire_limit_3):
      Color = "#EE2E17"   #Red
   displayNumber(TRL_X_left, TRL_Y_bottom, TRL_size, TRL_shift, NumberOfDigitsToDisplay, int(TireTempRL), Color, "TireTempRearLeft", displayAllZeros)

#################################################
#    - Display Tire rear right temperature -    #
#################################################
def displayTireRearRight(TireTempRR):
   global TRR_X_left
   global TRR_Y_bottom
   global TRR_size
   global TRR_shift
   global Temp_Tire_limit_1
   global Temp_Tire_limit_2
   global Temp_Tire_limit_3
   displayAllZeros         = False
   NumberOfDigitsToDisplay = 3
   Color = "#17A9EE"   #Blue
   if (TireTempRR > Temp_Tire_limit_1) and (TireTempRR < Temp_Tire_limit_2):
      Color = "#62EE17"   #Green
   if (TireTempRR >= Temp_Tire_limit_2) and (TireTempRR < Temp_Tire_limit_3):
      Color = "#EEDA17"   #Yellow
   if (TireTempRR >= Temp_Tire_limit_3):
      Color = "#EE2E17"   #Red
   displayNumber(TRR_X_left, TRR_Y_bottom, TRR_size, TRR_shift, NumberOfDigitsToDisplay, int(TireTempRR), Color, "TireTempRearRight", displayAllZeros)

###############################
#    - Display car class -    #
###############################
def displayClass(Class):
   global Class_color
   global Class_X_left
   global Class_Y_bottom
   global Class_size
   global Class_shift
   displayAllZeros         = False
   NumberOfDigitsToDisplay = 3
   displayNumber(Class_X_left, Class_Y_bottom, Class_size, Class_shift, NumberOfDigitsToDisplay, int(Class), Class_color, "ClassBox", displayAllZeros)

#################################
#    - Display Wheel Drive -    #
#################################
def displayWheelDrive(WD):
   global Wheel_Drive_Color
   #Tire
   global Tire_WD_FL_X
   global Tire_WD_FL_Y
   global Tire_WD_FR_X
   global Tire_WD_FR_Y
   global Tire_WD_RL_X
   global Tire_WD_RL_Y
   global Tire_WD_RR_X
   global Tire_WD_RR_Y
   global Tire_WD_Size_X
   global Tire_WD_Size_Y
   
   #Transmission
   global Top_Transmition_X
   global Top_Transmition_Y
   global Bottom_Transmition_X
   global Bottom_Transmition_Y
   global Transmition_Size_X
   global Transmition_Size_Y
   global Top_Vertical_Transmition_X
   global Top_Vertical_Transmition_Y
   global Bottom_Vertical_Transmition_X
   global Bottom_Vertical_Transmition_Y
   global Vertical_Transmition_Size_X
   global Vertical_Transmition_Size_Y
   global Box_Transmision_X
   global Box_Transmision_Y
   global Box_Transmision_Size_X
   global Box_Transmision_Size_Y
   global Wheel_Drive
   
   # 0 = FWD, 1 = RWD, 2 = AWD
   # Draw top Wheel Drive
   if WD == 0 or WD == 2 :
      # Tires
      Wheel_Drive.append(canvasBoard.create_rectangle(Tire_WD_FL_X, Tire_WD_FL_Y, Tire_WD_FL_X + Tire_WD_Size_X, Tire_WD_FL_Y + Tire_WD_Size_Y, fill = Wheel_Drive_Color, width=0))
      Wheel_Drive.append(canvasBoard.create_rectangle(Tire_WD_FR_X, Tire_WD_FR_Y, Tire_WD_FR_X + Tire_WD_Size_X, Tire_WD_FR_Y + Tire_WD_Size_Y, fill = Wheel_Drive_Color, width=0))
      # Transmission
      Wheel_Drive.append(canvasBoard.create_rectangle(Top_Transmition_X, Top_Transmition_Y, Top_Transmition_X + Transmition_Size_X, Top_Transmition_Y + Transmition_Size_Y, fill = Wheel_Drive_Color, width=0))
      Wheel_Drive.append(canvasBoard.create_rectangle(Top_Vertical_Transmition_X, Top_Vertical_Transmition_Y, Top_Vertical_Transmition_X + Vertical_Transmition_Size_X, Top_Vertical_Transmition_Y + Vertical_Transmition_Size_Y, fill = Wheel_Drive_Color, width=0))

   # Draw Bottom Wheel Drive
   if WD == 1 or WD == 2 :
      # Tires
      Wheel_Drive.append(canvasBoard.create_rectangle(Tire_WD_RL_X, Tire_WD_RL_Y, Tire_WD_RL_X + Tire_WD_Size_X, Tire_WD_RL_Y + Tire_WD_Size_Y, fill = Wheel_Drive_Color, width=0))
      Wheel_Drive.append(canvasBoard.create_rectangle(Tire_WD_RR_X, Tire_WD_RR_Y, Tire_WD_RR_X + Tire_WD_Size_X, Tire_WD_RR_Y + Tire_WD_Size_Y, fill = Wheel_Drive_Color, width=0))
      # Transmission
      Wheel_Drive.append(canvasBoard.create_rectangle(Bottom_Transmition_X, Bottom_Transmition_Y, Bottom_Transmition_X + Transmition_Size_X, Bottom_Transmition_Y + Transmition_Size_Y, fill = Wheel_Drive_Color, width=0))
      Wheel_Drive.append(canvasBoard.create_rectangle(Bottom_Vertical_Transmition_X, Bottom_Vertical_Transmition_Y, Bottom_Vertical_Transmition_X + Vertical_Transmition_Size_X, Bottom_Vertical_Transmition_Y + Vertical_Transmition_Size_Y, fill = Wheel_Drive_Color, width=0))

   Wheel_Drive.append(canvasBoard.create_rectangle(Box_Transmision_X, Box_Transmision_Y, Box_Transmision_X + Box_Transmision_Size_X, Box_Transmision_Y + Box_Transmision_Size_Y, fill = Wheel_Drive_Color, width=0))

#############
#  Celsius  #
#############
def Celsius(Far):
   return int((Far-32) * 5 / 9)

####################
#  display_board   #
####################
def display_board():
   global NumberBox
   global Plot_Graph
   global Fuel_Bar
   global Accelero
   global Accel_rectangle
   global Brake_rectangle
   global Clutch_rectangle
   global Wheel_Drive
   global extra_datas
   
   refresh_500ms  = False
   draw_graph     = False
   refresh_RPM    = False
   refresh_Window = False
   DisplayAll     = False
   FreezeDisplay  = False
   Speed_Km_h     = 0

   #---------------------------------------#
   # Refresh contour and graph every 500ms #
   #---------------------------------------#
   Is_Race_On = getTelemetricValue("IsRaceOn")
   Is_Race_On_Mem = getTelemetricValueMEM("IsRaceOn")
   
   #When Race is started (or restarted after a pause), all is displayed
   if Is_Race_On == 1 and Is_Race_On_Mem == 0 : 
      setTelemetricValueMEM("IsRaceOn", Is_Race_On)
      DisplayAll = True

   #When Race is stopped latest datas displayed are frozen
   if Is_Race_On == 0 : 
      setTelemetricValueMEM("IsRaceOn", Is_Race_On)
      FreezeDisplay = True

   date = datetime.datetime.now()
   milliseconds = int(date.microsecond / 1000)
   if milliseconds > extra_datas["milliseconds"]:
      if (milliseconds - extra_datas["milliseconds"]) > 500 :
         extra_datas["milliseconds"] = milliseconds
         draw_graph = True
         refresh_500ms = True
         extra_datas["milliseconds"] = milliseconds
         if Is_Race_On :
            IsRaceOn_Color_mem = "#B89C51"
         else :
            IsRaceOn_Color_mem = "#E1E1E1"
   else :
      if extra_datas["milliseconds"] - milliseconds < 500 :
         extra_datas["milliseconds"] = milliseconds
         draw_graph = True
         refresh_500ms = True
         if Is_Race_On :
            IsRaceOn_Color_mem = "#B89C51"
         else :
            IsRaceOn_Color_mem = "#000000"

   #----------#
   # Contour  #
   #----------#
   if refresh_500ms :
      # contour color cleanup #
      for element in Contour_Bar :
         canvasBoard.delete(element)
      # Contour Display
      displayContour(IsRaceOn_Color_mem)
      refresh_Window = True

   #--------------------#
   # Engine RPM Compute #
   #--------------------#
   current_engine_RPM = getTelemetricValue("CurrentEngineRpm")
   Max_engine_RPM     = getTelemetricValue("EngineMaxRpm")
   if Max_engine_RPM == 0 :
      Max_engine_RPM = 8000
   CellToDraw = int((cell_number * current_engine_RPM) / Max_engine_RPM)
   if CellToDraw != extra_datas["CellToDraw"] :
      refresh_RPM = True

   #~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
   #~ Display Telemetric datas ~#
   #~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
   
   if FreezeDisplay == False :
      #------------#
      # RPM draw   #
      #------------#
      if refresh_RPM or DisplayAll :
         # RPM Cleanup
         for element in RPM_Bar :
            canvasBoard.delete(element)
         # RPM Display
         displayRPM(CellToDraw)
         refresh_Window = True

      #------------#
      # Speed      #
      #------------#
      Speed = getTelemetricValue("Speed") 
      if Speed != getTelemetricValueMEM("Speed") or DisplayAll :
         setTelemetricValueMEM("Speed", Speed)
         # Speed box Cleanup
         for i in NumberBox["SpeedBox"]:
            for element in i:
               canvasBoard.delete(element)
         NumberBox["SpeedBox"] = [[],[],[]]
         # Speed Display
         Speed_Km_h = int(Speed * 3.6)
         displaySpeed(Speed_Km_h)
         refresh_Window = True

      #-------------#
      # Graph draw  #
      #-------------#
      if draw_graph or DisplayAll :
         Speed = getTelemetricValue("Speed") 
         # Graph cleanup
         for i in range(1,50):
            if( Graph_Index + i >= Graph_X_size):
               canvasBoard.delete(Plot_Graph[Graph_Index + i - Graph_X_size])
            else:
               canvasBoard.delete(Plot_Graph[Graph_Index+i])
         # Graph Display
         date = datetime.datetime.now()
         seconde = date.second
         Speed_Km_h = int(Speed * 3.6)
         displayGraphSpeed(Speed_Km_h)
         refresh_Window = True

      #-----------#
      # Race Time #
      #-----------#
      CurrentRaceTime = getTelemetricValue("CurrentRaceTime") 
      if CurrentRaceTime != getTelemetricValueMEM("CurrentRaceTime") or DisplayAll :
         setTelemetricValueMEM("CurrentRaceTime", CurrentRaceTime)
         # Race Time Box Cleanup
         for i in NumberBox["RaceTimeBox"]:
            for element in i:
               canvasBoard.delete(element)
         NumberBox["RaceTimeBox"] = [[],[],[]]
         # Race Time Display
         displayRaceTime(CurrentRaceTime)
         refresh_Window = True

      #-----------#
      # Lap Time  #
      #-----------#
      CurrentLap = getTelemetricValue("CurrentLap") 
      if CurrentLap != getTelemetricValueMEM("CurrentLap") or DisplayAll :
         setTelemetricValueMEM("CurrentLap", CurrentLap)
         # Lap Time Box Cleanup
         for i in NumberBox["LapTimeBox"]:
            for element in i:
               canvasBoard.delete(element)
         NumberBox["LapTimeBox"] = [[],[],[]]
         # Lap Time Display
         displayLapTime(CurrentLap)

      #-----------#
      # Last lap  #
      #-----------#
      LastLap = getTelemetricValue("LastLap") 
      if LastLap != getTelemetricValueMEM("LastLap") or DisplayAll :
         setTelemetricValueMEM("LastLap", LastLap)
         # Last lap Box Cleanup 
         for i in NumberBox["LastLapBox"]:
            for element in i:
               canvasBoard.delete(element)
         NumberBox["LastLapBox"] = [[],[],[]]
         # Last lap Display
         displayLastLap(LastLap)
         refresh_Window = True

      #-----------#
      # Best Lap  #
      #-----------#
      BestLap = getTelemetricValue("BestLap") 
      if BestLap != getTelemetricValueMEM("BestLap") or DisplayAll :
         setTelemetricValueMEM("BestLap", BestLap)
         # Best Lap Box Cleanup
         for i in NumberBox["BestLapBox"]:
            for element in i:
               canvasBoard.delete(element)
         NumberBox["BestLapBox"] = [[],[],[]]
         # Best Lap Display
         displayBestLap(BestLap)
         refresh_Window = True

      #-------#
      # Fuel  #
      #-------#
      Fuel = getTelemetricValue("Fuel")
      if Fuel != getTelemetricValueMEM("Fuel") or DisplayAll :
         setTelemetricValueMEM("Fuel", Fuel)
         # Fuel level Cleanup
         for element in Fuel_Bar:
            canvasBoard.delete(element)
         Fuel_Bar = []
         # Fuel level Display
         displayFuelLevel(Fuel)
         refresh_Window = True

      #---------------#
      # Acceleromter  #
      #---------------#
      AccelerationX = getTelemetricValue("AccelerationX")
      AccelerationZ = getTelemetricValue("AccelerationZ")
      if AccelerationX != getTelemetricValueMEM("AccelerationX") or AccelerationZ != getTelemetricValueMEM("AccelerationZ") or DisplayAll :
         setTelemetricValueMEM("AccelerationX", AccelerationX)
         setTelemetricValueMEM("AccelerationZ", AccelerationZ)
         # Acceleration Cleanup
         for element in Accelero:
            canvasBoard.delete(element)
         Accelero = []
         # Acceleration Display
         displayAccelero(AccelerationX, AccelerationZ)
         refresh_Window = True

      #----------------#
      # Race position  #
      #----------------#
      RacePosition = getTelemetricValue("RacePosition")
      if RacePosition != getTelemetricValueMEM("RacePosition") or DisplayAll :
         setTelemetricValueMEM("RacePosition", RacePosition)
         # Race position box Cleanup
         for i in NumberBox["RacePositionBox"]:
            for element in i:
               canvasBoard.delete(element)
         NumberBox["RacePositionBox"] = [[],[]]
         # Race position Display
         if ord(RacePosition) > 99 :
            RacePosition = b'\x63'
         displayRacePosition(RacePosition)
         refresh_Window = True

      #--------#
      # Gear   #
      #--------#
      Gear = getTelemetricValue("Gear")
      if Gear != getTelemetricValueMEM("Gear") or DisplayAll :
         setTelemetricValueMEM("Gear", Gear)
         # Gear box Cleanup
         for i in NumberBox["GearBox"]:
            for element in i:
               canvasBoard.delete(element)
         NumberBox["GearBox"] = [[]]
         # Gear Display
         displayGear(Gear)
         refresh_Window = True

      #----------------#
      # Lap Number     #
      #----------------#
      LapNumber = getTelemetricValue("LapNumber")
      if LapNumber != getTelemetricValueMEM("LapNumber") or DisplayAll :
         setTelemetricValueMEM("LapNumber", LapNumber)
         # Lap Number box Cleanup
         for i in NumberBox["LapNumberBox"]:
            for element in i:
               canvasBoard.delete(element)
         NumberBox["LapNumberBox"] = [[],[]]
         # Race position Display
         displayLapNumber(LapNumber + 1)
         refresh_Window = True

      #---------------#
      # Acceleration  #
      #---------------#
      Accel = getTelemetricValue("Accel")
      if Accel != getTelemetricValueMEM("Accel") or DisplayAll :
         setTelemetricValueMEM("Accel", Accel)
         # Acceleration Cleanup
         for element in Acceler_rectangle:
            canvasBoard.delete(element)
         Accel_rectangle = []
         # Acceleration Display
         displayAcceleration(Accel)
         refresh_Window = True

      #---------------#
      # Brake         #
      #---------------#
      Brake = getTelemetricValue("Brake")
      if Brake != getTelemetricValueMEM("Brake") or DisplayAll :
         setTelemetricValueMEM("Brake", Brake)
         # Brake Cleanup
         for element in Brake_rectangle:
            canvasBoard.delete(element)
         Brake_rectangle = []
         # Brake Display
         displayBrake(Brake)
         refresh_Window = True

      #---------------#
      # Clutch        #
      #---------------#
      Clutch = getTelemetricValue("Clutch")
      if Clutch != getTelemetricValueMEM("Clutch") or DisplayAll :
         setTelemetricValueMEM("Clutch", Clutch)
         # Clutch Cleanup
         for element in Clutch_rectangle:
            canvasBoard.delete(element)
         Clutch_rectangle = []
         # Clutch Display
         displayClutch(Clutch)
         refresh_Window = True

      #-----------------------------#
      # Tire Temperature Front Left #
      #-----------------------------#
      TireTempFrontLeft = getTelemetricValue("TireTempFrontLeft")
      if TireTempFrontLeft != getTelemetricValueMEM("TireTempFrontLeft") or DisplayAll :
         setTelemetricValueMEM("TireTempFrontLeft", TireTempFrontLeft)
         # TireTempFrontLeft box Cleanup
         for i in NumberBox["TireTempFrontLeft"]:
            for element in i:
               canvasBoard.delete(element)
         NumberBox["TireTempFrontLeft"] = [[],[],[]]
         # Tire Temperature Display
         displayTireFrontLeft(Celsius(TireTempFrontLeft))
         refresh_Window = True

      #------------------------------#
      # Tire Temperature Front Right #
      #------------------------------#
      TireTempFrontRight = getTelemetricValue("TireTempFrontRight")
      if TireTempFrontRight != getTelemetricValueMEM("TireTempFrontRight") or DisplayAll :
         setTelemetricValueMEM("TireTempFrontRight", TireTempFrontRight)
         # TireTempFrontRight box Cleanup
         for i in NumberBox["TireTempFrontRight"]:
            for element in i:
               canvasBoard.delete(element)
         NumberBox["TireTempFrontRight"] = [[],[],[]]
         # Tire Temperature Display
         displayTireFrontRight(Celsius(TireTempFrontRight))
         refresh_Window = True

      #-----------------------------#
      # Tire Temperature Rear Left  #
      #-----------------------------#
      TireTempRearLeft = getTelemetricValue("TireTempRearLeft")
      if TireTempRearLeft != getTelemetricValueMEM("TireTempRearLeft") or DisplayAll :
         setTelemetricValueMEM("TireTempRearLeft", TireTempRearLeft)
         # TireTempRearLeft box Cleanup
         for i in NumberBox["TireTempRearLeft"]:
            for element in i:
               canvasBoard.delete(element)
         NumberBox["TireTempRearLeft"] = [[],[],[]]
         # Tire Temperature Display
         displayTireRearLeft(Celsius(TireTempRearLeft))
         refresh_Window = True

      #-----------------------------#
      # Tire Temperature Rear Right #
      #-----------------------------#
      TireTempRearRight = getTelemetricValue("TireTempRearRight")
      if TireTempRearRight != getTelemetricValueMEM("TireTempRearRight") or DisplayAll :
         setTelemetricValueMEM("TireTempRearRight", TireTempRearRight)
         # TireTempRearRight box Cleanup
         for i in NumberBox["TireTempRearRight"]:
            for element in i:
               canvasBoard.delete(element)
         NumberBox["TireTempRearRight"] = [[],[],[]]
         # Tire Temperature Display
         displayTireRearRight(Celsius(TireTempRearRight))
         refresh_Window = True

      #-------#
      # Class #
      #-------#
      CarPerformanceIndex = getTelemetricValue("CarPerformanceIndex")
      if CarPerformanceIndex != getTelemetricValueMEM("CarPerformanceIndex") or DisplayAll :
         setTelemetricValueMEM("CarPerformanceIndex", CarPerformanceIndex)
         # Class Cleanup
         for i in NumberBox["ClassBox"]:
            for element in i:
               canvasBoard.delete(element)
         NumberBox["ClassBox"] = [[],[],[]]
         # Class Display
         displayClass(CarPerformanceIndex)
         refresh_Window = True

      #-------------#
      # Wheel Drive #
      #-------------#
      DrivetrainType = getTelemetricValue("DrivetrainType")
      if DrivetrainType != getTelemetricValueMEM("DrivetrainType") or DisplayAll :
         setTelemetricValueMEM("DrivetrainType", DrivetrainType)
         # Wheel Cleanup
         for element in Wheel_Drive:
            canvasBoard.delete(element)
         Wheel_Drive = []
         # Class Display
         displayWheelDrive (DrivetrainType)
         refresh_Window = True

   #---------------#
   # Update Window #
   #---------------#
   if refresh_Window :
      Window.update()

   extra_datas["CellToDraw"] = CellToDraw

####################
#    -  Main  -    #
####################

#Init_Telemetrics_Array
initTelemetrics()

#Init_Telemetrics_Array memorize
initTelemetricsMEM()

#Init_Graphic Speed Array
initGraph_Array()

#Init_RPM_Bar
initRPMBar()

#Init_contour_Bar
initContourBar()

#Graphical 
Window = Tk()
Window.attributes('-fullscreen', 1)

# Background image
bg_screen = PhotoImage(file="Board.png")
#Telemetric Board size

# MainFrame
MainFrame = Frame(Window, borderwidth=2, relief=GROOVE)
MainFrame.pack(side=LEFT, padx=0, pady=0)

# canvas in MainFrame
canvasBoard = Canvas(MainFrame, width=WindowWidth, height=WindowHeigth, background='Black')
canvasBoard.create_image(0,0,anchor=NW, image=bg_screen)

# Create Thread
thread_1 = Background()

# Launch Thread
thread_1.start()

# Date and time measurement
date = datetime.datetime.now()
currentsecond = date.second

# Synchro display
os.system('cls')
print(" ")
print("    ┌──────────────────────────────────────────────────────────────────────┐ ")
print("    │█ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ │ ")
print("    │ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █│ ")
print("    │█ █┌──────────────────────────────────────────────────────────────┐ █ │ ")
print("    │ █ │                   FORZA TELEMETRIC DISPLAY                   │█ █│ ")
print("    │█ █└──────────────────────────────────────────────────────────────┘ █ │ ")
print("    │ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █│ ")
print("    │█ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ │ ")
print("    └──────────────────────────────────────────────────────────────────────┘")
print("\n\n\nIn Forza Game, go to the telemetry menu and set the ip adress to :")
print("       ~~~~~~~~~~~~~~~~~~~~~~")
print("       >   " + socket.gethostbyname(socket.gethostname()) + "   <")
print("       ~~~~~~~~~~~~~~~~~~~~~~")
print("Set the port to :")
print("       ~~~~~~~~~~~~")
print("       >   " + str(UDP_PORT)  + "   <")
print("       ~~~~~~~~~~~~")
print("\n> On PC side, if the telemetric board doesn't appear, restart the game.")
print("> The telemetric board should appear during startup of the game.")
print("\nWaiting for datas from Xbox... Nothing received yet...")

counter = 0
direction = 1
while (extra_datas["FirstDataReceived"] == False):
   time.sleep(0.02)
   print(counter*" " + "⃝⃝⃝" + (77 - counter) *" ", end = '\r')
   counter += direction
   if counter > 76:
      direction = -1
   elif counter < 1:
      direction = 1

# Clear screen
os.system('cls')
print("Datas received ! ҉")

# Create Canvas
canvasBoard.pack()
Window.update()

#FPS graphical measurement
telemetric_fps = 0

while 1:
   time.sleep(0.01) 
   telemetric_fps += 1
   # > Entering in it each new second
   date = datetime.datetime.now()
   if currentsecond != date.second :
      currentsecond = date.second
      # print("Main FPS : " + str(telemetric_fps))
      telemetric_fps = 0
   display_board()

#When window is closed, stop the Thread
thread_1.stop()
thread_1.join()
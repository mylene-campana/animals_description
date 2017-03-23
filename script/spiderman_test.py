#/usr/bin/env python
# Script which goes with animals_description package.
# The script launches a spiderman-robot and a mesh environment.
# It defines init and final configs and display them. (CANNOT SOLVE)

#blender/urdf_to_blender.py -p robot/ -i /local/mcampana/devel/hpp/src/animals_description/urdf/skeleton.urdf -o spiderman_blend.py

from hpp.corbaserver.spiderman import Robot # use skeleton from animals_description
from hpp.corbaserver import Client
from hpp.corbaserver import ProblemSolver
from hpp.corbaserver.rbprm.rbprmbuilder import Builder
from hpp.gepetto import Viewer, PathPlayer
import math

robot = Robot ('robot')
robot.setJointBounds('base_joint_xyz', [-5, 5, -5, 5, -1, 7])
ps = ProblemSolver (robot)
cl = robot.client
r = Viewer (ps); gui = r.client.gui

# Configs : [x, y, z, q1, q2, q3, q4, dir.x, dir.y, dir.z, theta]
q11 = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
q11[0:3] = [1.0, 1.0, 1.2]
q11[3:7] = [0, 0, math.sqrt(2)/2.0, math.sqrt(2)/2.0]
q11 [robot.rankInConfiguration ['RFoot']] = 0 # rotate foot, axis = z/leg
q11 [robot.rankInConfiguration ['RAnkle_J1']] = 1.65 # rotate foot, axis = side2side
q11 [robot.rankInConfiguration ['LAnkle_J1']] = 1.65
q11 [robot.rankInConfiguration ['RHand']] = 0 # rotate hand, axis = front2back
q11 [robot.rankInConfiguration ['RWrist_J1']] = 0.05 # rotate hand, axis = side2side
q11 [robot.rankInConfiguration ['RForearm']] = 1.65 # rotate forearm+hand, axis = arm
q11 [robot.rankInConfiguration ['LWrist_J1']] = 0.05
q11 [robot.rankInConfiguration ['LForearm']] = -1.65; r(q11)

q11 [robot.rankInConfiguration ['LElbow_J1']] = 1.5
q11 [robot.rankInConfiguration ['RElbow_J1']] = 1.5; r(q11)
robot.isConfigValid(q11)

gui = r.client.gui
gui.setCaptureTransform ("frames.yaml ", ["robot"])
q = q11
r (q); cl.robot.setCurrentConfig(q)
gui.refresh (); gui.captureTransform ()




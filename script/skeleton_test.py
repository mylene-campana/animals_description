#/usr/bin/env python
# Script which goes with animals_description package.
# The script launches a skeleton-robot and a mesh environment.
# It defines init and final configs and display them. (CANNOT SOLVE)

#blender/urdf_to_blender.py -p robot/ -i /local/mcampana/devel/hpp/src/animals_description/urdf/skeleton.urdf -o skeleton_blend.py

from hpp.corbaserver.skeleton import Robot # use skeleton from animals_description
from hpp.corbaserver import Client
from hpp.corbaserver import ProblemSolver
from hpp.corbaserver.rbprm.rbprmbuilder import Builder
from hpp.gepetto import Viewer, PathPlayer
import math
from viewer_display_library import normalizeDir, plotCone, plotFrame, plotThetaPlane, shootNormPlot, plotStraightLine, plotConeWaypoints, plotSampleSubPath, contactPosition, addLight, plotSphere, plotSpheresWaypoints, plotConesRoadmap, plotEdgesRoadmap

robot = Robot ('robot')
robot.setJointBounds('base_joint_xyz', [-0.2, 0.2, -0.2, 0.2, -0.2, 0.2])
ps = ProblemSolver (robot)
cl = robot.client
r = Viewer (ps); gui = r.client.gui

# Configs : [x, y, z, q1, q2, q3, q4, dir.x, dir.y, dir.z, theta]
q11 = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
q11[0:3] = [0,0,0]#[1.0, 1.0, 1.2]
q11[3:7] = [1,0,0,0]#[0, 0, math.sqrt(2)/2.0, math.sqrt(2)/2.0]

q11 [robot.rankInConfiguration ['RWrist_J1']] = -0.05 # plie poignet
q11 [robot.rankInConfiguration ['LWrist_J1']] = -0.05
q11 [robot.rankInConfiguration ['RForearm']] = 1.57 # rotate forearm+hand, axis = arm
q11 [robot.rankInConfiguration ['LForearm']] = -1.57
q11 [robot.rankInConfiguration ['LElbow_J1']] = -1.5 # plie coude
q11 [robot.rankInConfiguration ['RElbow_J1']] = -1.5
robot.isConfigValid(q11)
r(q11)


gui = r.client.gui
gui.setCaptureTransform ("frames.yaml ", ["robot"])
q = q11
r (q); cl.robot.setCurrentConfig(q)
gui.refresh (); gui.captureTransform ()

r(ps.generateValidConfig (15)[1])

plotFrame(r, "framy", [0,0,0], 0.5)

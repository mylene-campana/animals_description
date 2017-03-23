#/usr/bin/env python
# Script which goes with animals_description package.
# The script launches a ant-robot and a mesh environment.
# It defines init and final configs and display them. (CANNOT SOLVE)

#blender/urdf_to_blender.py -p robot/ -i /local/mcampana/devel/hpp/src/animals_description/urdf/ant.urdf -o ant_blend.py

from hpp.corbaserver.articulated_ant import Robot #  from animals_description
from hpp.corbaserver import Client
from hpp.corbaserver import ProblemSolver
from hpp.corbaserver.rbprm.rbprmbuilder import Builder
from hpp.gepetto import Viewer, PathPlayer
import math
#from viewer_display_library import normalizeDir, plotCone, plotFrame, plotThetaPlane, shootNormPlot, plotStraightLine, plotConeWaypoints, plotSampleSubPath, contactPosition, addLight, plotSphere, plotSpheresWaypoints, plotConesRoadmap, plotEdgesRoadmap

robot = Robot ('robot')

robot.setJointBounds('base_joint_xyz', [-0.2, 0.2, -0.2, 0.2, -0.2, 0.2])
ps = ProblemSolver (robot)
cl = robot.client
r = Viewer (ps); gui = r.client.gui

# Configs : [x, y, z, q1, q2, q3, q4, dir.x, dir.y, dir.z, theta]
q11 = [0]*robot.getConfigSize()
q11 [0:7] = [0, 0, 0, 1, 0, 0, 0]; r(q11)


q11 [robot.rankInConfiguration ['LFThigh']] = 0.0; r(q11)
q11 [robot.rankInConfiguration ['ThoraxRFThigh_J2']] = 0.0; r(q11)

robot.isConfigValid(q11)

gui = r.client.gui
gui.setCaptureTransform ("frames.yaml ", ["robot"])
q = q11
r (q); cl.robot.setCurrentConfig(q)
gui.refresh (); gui.captureTransform ()

r(ps.generateValidConfig (15)[1])

plotFrame(r, "framy", [0,0,0], 0.5)

robot.getConfigSize()


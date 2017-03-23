#/usr/bin/env python
# Benchmark1. Script which goes with animals_description package.
# The script launches a point-robot and the environment containing a simple plane.
# It defines init and final configs, and solve them for three couples of mu / vmax (parabola constraints).

from hpp.corbaserver.cubencvx import Robot
from hpp.corbaserver import Client
from hpp.corbaserver import ProblemSolver
from hpp.gepetto import Viewer
from viewer_display_library import *

robot = Robot ('robot')
robot.setJointBounds('base_joint_xyz', [-10, 10, -10, 10, -10, 10])
ps = ProblemSolver (robot)
cl = robot.client

r = Viewer (ps); gui = r.client.gui
pp = PathPlayer (robot.client, r)


# Configs : [x, y, z, q1, q2, q3, q4]
q11 = [0, 0, 0, 1, 0, 0, 0]; q22 = [0, 0, 0, 1, 0, 0, 0]

r(q11)

q1 = cl.robot.projectOnObstacle (q11, 0.001); q2 = cl.robot.projectOnObstacle (q22, 0.001)
robot.isConfigValid(q1); robot.isConfigValid(q2)
r(q1)

ps.setInitialConfig (q1); ps.addGoalConfig (q2)

plotSphere (q2, cl, r, "sphere1", [0,1,0,1], 0.02)
nPointsPlot = 70
offsetOrientedPath = 2 # If remove oriented path computation in ProblemSolver, set to 1 instead of 2




plotFrame (r, "_", [0,0,4.5], 1)


r.loadObstacleModel ("animals_description","plane_3d","plane_3d")

q = [0, 4.8, 2.5, 1, 0, 0, 0]; r(q)
robot.isConfigValid(q)

q = [0, 0, -4, 1, 0, 0, 0]; r(q)
robot.isConfigValid(q)

#/usr/bin/env python
# RUNS version! launch command: "python -i environment3d_runs.py"
# Script which goes with animals_description package, runs version of Benchmark3.
# The script launches a point-robot and the cave environment.
# It defines init and final configs, and solve them for .. couples of mu / vmax (parabola constraints).
# Do not forget to launch it in Release mode !

from hpp.corbaserver.sphere import Robot
from hpp.corbaserver import Client
from hpp.corbaserver import ProblemSolver
import math
import numpy as np

robot = Robot ('robot')
robot.setJointBounds('base_joint_xyz', [-2.6, 2.6, -6, 4.5, -2.5, 1.6]) # low end
#robot.setJointBounds('base_joint_xyz', [-2.6, 2.6, -6, 4.5, -2.5, 7]) # top end
ps = ProblemSolver (robot)
cl = robot.client
cl.obstacle.loadObstacleModel('animals_description','cave','')

# Configs : [x, y, z, q1, q2, q3, q4, dir.x, dir.y, dir.z, theta]
q11 = [-0.18, 3.5, -0.11, 1, 0, 0, 0, 0, 0, 1, 0];
q22 = [0.4, -5.2, -0.7, 1, 0, 0, 0, 0, 0, 1, 0] # cave low end
#q22 = [0.27, -5.75, 5.90, 1, 0, 0, 0, 0, 0, 1, 0] # cave top end

q1 = cl.robot.projectOnObstacle (q11, 0.001); q2 = cl.robot.projectOnObstacle (q22, 0.001)
ps.setInitialConfig (q1); ps.addGoalConfig (q2)

vmax = 8; mu = 1.2
#vmax = 6.5; mu = 0.5
#cl.problem.setFrictionCoef(mu); cl.problem.setMaxVelocityLim(vmax)

toSeconds = np.array ([60*60,60,1,1e-3])
offsetOrientedPath = 2 # If remove oriented path computation in ProblemSolver, set to 1 instead of 2
imax=3;
f = open('results.txt','a')
    
# Assuming that seed in modified directly in HPP (e.g. in core::PathPlanner::solve or ProblemSolver constr)
for i in range(0, imax):
    print i
    ps.clearRoadmap ()
    solveTimeVector = ps.solve ()
    solveTime = np.array (solveTimeVector).dot (toSeconds)
    pathId = ps.numberPaths()-offsetOrientedPath
    pathLength = ps.pathLength (pathId)
    pathNumberWaypoints = len(ps.getWaypoints (pathId))
    roadmapNumberNodes = ps.numberNodes ()
    #TODO: number collisions (checked ???)
    #TODO: number parabola that has failed (because of which constraint ??)
    
    #ps.addPathOptimizer("Prune")
    #ps.optimizePath (pathId)
    #prunePathId = ps.numberPaths()-1
    
    # Write important results #
    f.write('Try number: '+str(i)+'\n')
    f.write('with parameters: vmax='+str(vmax)+' and mu='+str(mu)+'\n')
    f.write('solve duration: '+str(solveTime)+'\n')
    f.write('path length: '+str(pathLength)+'\n')
    f.write('number of waypoints: '+str(pathNumberWaypoints)+'\n')
    f.write('number of nodes: '+str(roadmapNumberNodes)+'\n')

f.close()

from parseRunsParabola import main
main()



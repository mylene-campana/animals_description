#!/bin/bash
# File to launch gepetto-viewer, hpp-corbaserver and a script.

# Command: sh autoRun.sh

# In first terminal : viewer-server
xterm -e gepetto-viewer-server &
sleep 1s
# In first terminal : corbaserver
xterm -e hppcorbaserver &
sleep 1s
# In second terminal : python script
xterm -e python skeleton_test.py &
sleep 500s
killall xterm

#!/bin/bash

runSquareSetup(){

ROBOT_NUM="${1}"

source ~/catkin_ws/devel/setup.bash
source src/rr_oks/oks_navigation_utils/.bash_aliases 
rostopic pub /robot${ROBOT_NUM}/initialpose geometry_msgs/PoseStamped "header:
  seq: 0
  stamp:
    secs: 0
    nsecs: 0
  frame_id: ''
pose:
  position:
    x: 0.0
    y: 0.0
    z: 0.0
  orientation:
    x: 0.0
    y: 0.0
    z: 0.0
    w: 1.0" 
}

runSquareExecute(){
    ROBOT_NUM="${1}"

    X1=$(python3 -c "print(0.0)")
    Y1=$(python3 -c "print(0.0)")

    X2=$(python3 -c "print(0.56)")
    Y2=$(python3 -c "print(0)")

    X3=$(python3 -c "print(0.56)")
    Y3=$(python3 -c "print(-0.77)")

    X4=$(python3 -c "print(0.0)")
    Y4=$(python3 -c "print(-0.77)")

    while true; do
        timeout 3s rostopic pub -1 /${ROBOT_NUM}/navigate/goal oks_msgs/NavigateActionGoal "{goal: {pose: {pose: {position: {x: ${X1}, y: ${Y1}, z: 0.0}, orientation: {x: 0.0, y: 0.0, z: 0.0, w: 1.0}}}}}"
        timeout 3s rostopic pub -1 /${ROBOT_NUM}/navigate/goal oks_msgs/NavigateActionGoal "{goal: {pose: {pose: {position: {x: ${X2}, y: ${Y2}, z: 0.0}, orientation: {x: 0.0, y: 0.0, z: 0.0, w: 1.0}}}}}"
        timeout 3s rostopic pub -1 /${ROBOT_NUM}/navigate/goal oks_msgs/NavigateActionGoal "{goal: {pose: {pose: {position: {x: ${X3}, y: ${Y3}, z: 0.0}, orientation: {x: 0.0, y: 0.0, z: 0.0, w: 1.0}}}}}"
        timeout 3s rostopic pub -1 /${ROBOT_NUM}/navigate/goal oks_msgs/NavigateActionGoal "{goal: {pose: {pose: {position: {x: ${X4}, y: ${Y4}, z: 0.0}, orientation: {x: 0.0, y: 0.0, z: 0.0, w: 1.0}}}}}"
    done
}
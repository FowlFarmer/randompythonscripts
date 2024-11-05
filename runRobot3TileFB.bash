#!/bin/bash

trap "echo 'Exiting...'; exit" SIGINT

while true; do
        timeout 3s rostopic pub -1 /$1/navigate/goal oks_msgs/NavigateActionGoal "{goal: {pose: {pose: {position: {x: 0.0, y: 0.0, z: 0.0}, orientation: {x: 0.0, y: 0.0, z: 0.0, w: 1.0}}}}}"
        sleep 1
        timeout 3s rostopic pub -1 /$1/navigate/goal oks_msgs/NavigateActionGoal "{goal: {pose: {pose: {position: {x: 1.12, y: 0.0, z: 0.0}, orientation: {x: 0.0, y: 0.0, z: 0.0, w: 1.0}}}}}"
        sleep 1
done

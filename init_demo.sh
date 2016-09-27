#!/bin/bash


#gnome-terminal

cd ~/anaconda2/Forecasting-ANN/
echo " Clearing the data repository"
echo '' > Data/data_demo.csv
echo " "
echo " Clearing the alarm repository "
echo '' > Data/alarms.csv
echo " "
echo "Launching the main Scoring program"
#gnome-terminal -x
xterm -hold -e python scoring.py &
sleep 2
echo " "
echo "Launching the Live graph"
xterm -hold -e python live_graph.py &
echo "Launching SLO alarms "
xterm -hold -e python SLO_alarms.py &
echo " "
echo "Launching DashBoard"
#python dashboard.py

#python tables.py
#python live_graphs.py
#python openFirefoxLocalHost.py
#python launchYate and make a call

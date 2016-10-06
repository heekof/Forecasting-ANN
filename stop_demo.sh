#!/bin/bash








while read process; do

  # ps -ef | grep  $process | grep -v grep | awk '{print $2}' | xargs kill 2> log/stop_demo.log


  if ps -ef | grep  $process | grep -v grep | awk '{print $2}' | xargs kill 2> log/stop_demo.log ; then

    echo "Process $process stopped"

  else

    echo "Failed to stop process $process"

  fi


done <processes.txt

cd ~/anaconda2/Forecasting-ANN/
echo " Clearing the data repository"
echo '' > Data/data_demo.csv
echo " "
echo " Clearing the alarm repository "
echo '' > Data/alarms.csv

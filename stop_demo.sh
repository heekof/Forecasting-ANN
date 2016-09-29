#!/bin/bash








while read process; do

  # ps -ef | grep  $process | grep -v grep | awk '{print $2}' | xargs kill 2> log/stop_demo.log


  if ps -ef | grep  $process | grep -v grep | awk '{print $2}' | xargs kill 2> log/stop_demo.log ; then

    echo "Process $process stopped"

  else

    echo "Failed to stop process $process"

  fi


done <processes.txt

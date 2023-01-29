#!/bin/bash
args=$1

if [ $args == "start" ]
then
  echo started
  python3 get_adds.py &
fi
if [ $args == "stop" ]
then
  arg=$(ps -aux | grep "python3 get_adds.py")
  kill $(echo $arg | cut -d" " -f2)
  echo stopped
fi

if [ $args == "check" ]
then
	if [ $(ps -aux | grep "python3 get_adds.py" | wc -l) == 2 ]
	then 
		echo everything is working properly
	else
		python3 get_adds.py &
	fi
fi

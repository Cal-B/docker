#!/bin/zsh
TIME=$(date +%d.%m.%y-%H:%M:%S)
echo "Executed at: $TIME \n" > fl_bing_api.txt
python3 /home/h302/pelias/docker/projects/florida/bing_api_fl.py >> fl_bing_api.txt 
ENDTIME=$(date +%d.%m.%y-%H:%M:%S)
echo "Executed at: $ENDTIME \n" >> fl_bing_api.txt 
#!/bin/zsh
TIME=$(date +%d.%m.%y-%H:%M:%S)
echo "Executed at: $TIME \n" > nc_bing_api.txt
python3 /home/h302/pelias/docker/projects/north-carolina/bing_api_nc.py >> nc_bing_api.txt
ENDTIME=$(date +%d.%m.%y-%H:%M:%S)
echo "Finished at: $ENDTIME \n" >> nc_bing_api.txt 
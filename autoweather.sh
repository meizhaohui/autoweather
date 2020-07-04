#!/bin/bash
##################################################
#      Filename: autoweather.sh
#        Author: Zhaohui Mei<mzh.whut@gmail.com>
#   Description:      
#   Create Time: 2020-07-03 00:12:21
# Last Modified: 2020-07-04 17:04:10
##################################################
datastr=$(python3 /home/meizhaohui/autoweather.py)
echo "datastr:${datastr}"
cd /home/meizhaohui/autoweather
git pull
echo -e "\n${datastr}" >> /home/meizhaohui/autoweather/README.md
git add README.md
git commit -m"auto weather update"
git push origin master
git push github master


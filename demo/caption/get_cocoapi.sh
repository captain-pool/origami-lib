#! /bin/bash
GREEN='\033[0;32m'
NC='\033[0m'
if [[ ! -e cocoapi ]];
then
    URL=https://github.com/cocodataset/cocoapi/archive/master.zip
    wget -c -q --show-progress $URL 
    unzip -fo master.zip
    rm master.zip
    mv cocoapi-master/ cocoapi/ 
    pip install cython
    make -C cocoapi/PythonAPI
    printf "${GREEN}API Downloaded${NC}\n"
else
    printf "${GREEN} API Already Available${NC}\n"
fi;

#! /bin/sh
ls
cd api
xterm -e python poem-api.py & 
cd ../front-end && xterm -e npm start

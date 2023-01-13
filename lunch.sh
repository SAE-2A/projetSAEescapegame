#!/bin/bash
sudo ~/PiFmRds/src/pi_fm_rds -freq 107.9 -audio ~/blaasMaresicSAE/projetSAEescapegame/52.wav -ps 'RT' -ppm 1000000

ps -e > test.txt

pkill lunch.sh 

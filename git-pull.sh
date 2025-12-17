#!/bin/bash
source .venv/bin/activate
git checkout feature
git pull
sudo /home/vedion/hardware-tester/hardware-tester.sh
/home/vedion/hardware-tester/tester_gui.sh

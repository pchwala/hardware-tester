#!/bin/bash
source .venv/bin/activate
git checkout master
git pull

# Set executable permissions for shell scripts
chmod +x hardware-tester.sh
chmod +x tester_gui.sh
chmod +x git-pull.sh
chmod +x repair.sh
chmod +x fix-grub/fix-grub.sh

sudo /home/vedion/hardware-tester/hardware-tester.sh
/home/vedion/hardware-tester/tester_gui.sh

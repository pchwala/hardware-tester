cd /home/serwis/hardware-tester
git status
git switch portable
git pull
cp displays.xml /home/serwis/.config/xfce4/xfconf/xfce-perchannel-xml/displays.xml
./hardware-tester.sh
read -n1 -r -p "Press any key..."
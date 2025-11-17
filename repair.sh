sudo chown -R vedion:vedion /home/vedion/hardware-tester
sudo chmod -R 755 /home/vedion/hardware-tester
git checkout feature
git reset --hard origin/feature
git pull
sudo pacman -S vi

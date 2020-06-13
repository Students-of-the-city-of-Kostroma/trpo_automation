#!/bin/bash
apt-get install unrar
apt-get install rar
apt-get install default-jre
apt-get install default-jdk
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
apt-get install google-chrome-stable_current_amd64.deb
unrar x 18-VTbo-1b.rar 
mv 18-VTbo-1b /bin
rm 18-VTbo-1b.rar
cd /bin/18-VTbo-1b/LR/03/installer
mv TRPO_LR3.service /etc/systemd/system/
mv TRPO_LR3_CHECK.service /etc/systemd/system/
sudo chmod 644 /etc/systemd/system/TRPO_LR3_CHECK.service
sudo chmod 644 /etc/systemd/system/TRPO_LR3.service
mv TRPO_LR3_CHECK.sh /bin
sudo chmod +x /bin/TRPO_LR3_CHECK.sh
cd /bin/18-VTbo-1b/
mv labs.xml /
cd /bin/18-VTbo-1b/LR/03
mv Labs3_url.xml /
systemctl daemon-reload
systemctl start TRPO_LR3_CHECK
systemctl enable TRPO_LR3_CHECK
systemctl start TRPO_LR3
systemctl enable TRPO_LR3
echo "Install Succes"


#!/bin/bash
while [ 1 = 1 ]
do
TMP=$(curl https://github.com/Students-of-the-city-of-Kostroma/trpo_automation/releases/latest/)
CURRENT_TAG="$(echo $TMP| tr "qwertyuiop[]asdfghjkl;'zxcvbnm,./<>QWERTYUIOP{}ASDFGHJKL:ZXCVBNM=" "\n")"
TAG=$CURRENT_TAG
echo "this" $CURRENT_TAG
echo "is" $TAG
while [ "$CURRENT_TAG" = "$TAG" ]
do
sleep 1000000
TMP=$(curl https://github.com/Students-of-the-city-of-Kostroma/trpo_automation/releases/latest/)
TAG="$(echo $TMP| tr "qwertyuiop[]asdfghjkl;'zxcvbnm,./<>QWERTYUIOP{}ASDFGHJKL:ZXCVBNM=" "\n")"
echo "and" $TAG
done
cd /
cd /bin
wget https://github.com/Students-of-the-city-of-Kostroma/trpo_automation/releases/latest/download/18-VTbo-1b.rar
systemctl stop TRPO_LR3
rm -r 18-VTbo-1b
unrar x 18-VTbo-1b.rar
mv 18-VTbo-1b /bin
rm 18-VTbo-1b.rar
cd /bin/18-VTbo-1b/
mv labs.xml /
cd /bin/18-VTbo-1b/LR/03
mv Labs3_url.xml /
systemctl daemon-reload
systemctl start TRPO_LR3
systemctl enable TRPO_LR3
done
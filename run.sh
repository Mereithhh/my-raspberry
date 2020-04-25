#!/bin/bash

echo "开启显示。"
sudo cp /boot/config.txt ./config.txt.bak
sudo cp /boot/cmdline.txt ./cmdline.txt.bak

sudo echo "dtparam=i2c_arm=on" >> /boot/config.txt
sudo echo "dtparam=spi=on" >> /boot/config.txt
sudo echo "enable_uart=1" >> /boot/config.txt
sudo echo "dtoverlay=tft35a:rotate=90" >> /boot/config.txt
sudo mkdir /etc/X11/xorg.conf.d

sudo cp ./tft35a-overlay.dtb /boot/overlays/tft35a.dtb

sudo cp -rf ./99-calibration.conf-35-90  /etc/X11/xorg.conf.d/99-calibration.conf
sudo cp -rf ./99-fbturbo.conf /usr/share/X11/xorg.conf.d/99-fbturbo.conf

# add cmdline
sudo cp -rf ./cmdline.txt /boot/cmdline.txt
#sudo echo " fbcon=map:10 fbcon=font:ProFont6x11" >> /boot/cmdline.txt

# touch
#sudo apt install xinput
#sudo apt install xinput-calibrator
echo "更新一下"
sudo apt update
sudo apt upgrade
echo "安装python3.8需要的库"
sid-used sudo apt install libbz2-dev libc6-dev libffi-dev libgdbm-dev libgdbm-compat-dev liblzma-dev libncurses5-dev
sid-used sudo apt install libreadline-dev libsqlite3-dev libssl-dev openssl sqlite3 tcl-dev tk-dev uuid-dev zlib1g-dev


echo "下载python源码"
sudo curl -O "https://www.python.org/ftp/python/3.8.2/Python-3.8.2.tgz"
tar zxf ./Python-3.8.2.tgz
cd ./Python-3.8.2.tgz
./configure --enable-optimizations
make -j 4
sudo make install
ptyhon3.8 --version
pip3 --version
sudo rm /usr/bin/python3
sudo ln -s /usr/local/bin/python3.8 /usr/bin/python3

echo "安装完成"

echo "pyqt5"
cd ~
sudo apt install qt5-default qt5-qmake dbus-python
curl -O https://files.pythonhosted.org/packages/4d/81/b9a66a28fb9a7bbeb60e266f06ebc4703e7e42b99e3609bf1b58ddd232b9/PyQt5-5.14.2.tar.gz
tar vxzf PyQt5-5.14.2.tar.gz
cd ./PyQt5-5.14.2
sudo sip-install


echo "显示屏显示一下子。"
cd ~
git clone https://github.com/mereithhh/my-raspberry
cd ./my-raspberry
sudo python3 ./show-info/main.py



echo "配置samba"
sudo apt install -y samba samba-common ntfs-3g

pause
#rebot 
sudo sync
sudo reboot











 (tcl8.6-dev)
 (tk8.6-dev)




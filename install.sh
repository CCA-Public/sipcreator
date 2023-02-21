#!/bin/bash

### Install script for CCA Disk Image Processor in Bitcurator 4/Ubuntu 22

git submodule update --init --recursive

if [ ! -d /usr/share/ccatools ]; then
  sudo mkdir /usr/share/ccatools
fi

sipcreator_dir="/usr/share/ccatools/sipcreator"

if [ -d $sipcreator_dir ]; then
  sudo rm -rf $sipcreator_dir
fi

sudo mkdir $sipcreator_dir

sudo cp main.py $sipcreator_dir
sudo cp launch $sipcreator_dir
sudo cp design.py $sipcreator_dir
sudo cp design.ui $sipcreator_dir
sudo cp icon.png $sipcreator_dir
sudo cp LICENSE $sipcreator_dir
sudo cp README.md $sipcreator_dir
sudo cp deps/dfxml/python/dfxml.py $sipcreator_dir
sudo cp deps/dfxml/python/Objects.py $sipcreator_dir
sudo cp deps/dfxml/python/walk_to_dfxml.py $sipcreator_dir

# Create launch.desktop file
launch_file="/usr/share/applications/SIPCreator.desktop"
sudo touch $launch_file
echo '[Desktop Entry]' | sudo tee --append $launch_file
echo 'Type=Application' | sudo tee --append $launch_file
echo 'Name=SIP Creator' | sudo tee --append $launch_file
echo 'Exec=/usr/share/ccatools/sipcreator/launch' | sudo tee --append $launch_file
echo 'Icon=/usr/share/ccatools/sipcreator/icon.png' | sudo tee --append $launch_file
echo 'Categories=Forensics and Reporting' | sudo tee --append $launch_file

sudo chown -R bcadmin:bcadmin $sipcreator_dir
sudo chmod u+x /usr/share/ccatools/sipcreator/launch

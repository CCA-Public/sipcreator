#!/bin/bash

### Install script for CCA SIP Creator in Bitcurator

# Update submodules
git submodule update --init --recursive

# Make /usr/share/ccatools if doesn't already exist
if [ ! -d /usr/share/ccatools ]; then
  sudo mkdir /usr/share/ccatools
fi

# Delete /usr/share directory for SIP Creator if it already exists
if [ -d /usr/share/ccatools/sipcreator ]; then
  sudo rm -rf /usr/share/ccatools/sipcreator
fi

# Make /usr/share directory for SIP Creator
sudo mkdir /usr/share/ccatools/sipcreator

# Move files into /usr/share/ccatools/sipcreator
sudo cp main.py /usr/share/ccatools/sipcreator
sudo cp launch /usr/share/ccatools/sipcreator
sudo cp design.py /usr/share/ccatools/sipcreator
sudo cp design.ui /usr/share/ccatools/sipcreator
sudo cp icon.png /usr/share/ccatools/sipcreator
sudo cp LICENSE /usr/share/ccatools/sipcreator
sudo cp README.md /usr/share/ccatools/sipcreator
sudo cp deps/dfxml/python/dfxml.py /usr/share/ccatools/sipcreator
sudo cp deps/dfxml/python/Objects.py /usr/share/ccatools/sipcreator
sudo cp deps/dfxml/python/walk_to_dfxml.py /usr/share/ccatools/sipcreator

# Make "CCA Tools" folder on Desktop if doesn't already exist
if [ ! -d "/home/bcadmin/Desktop/CCA Tools" ]; then
  sudo mkdir "/home/bcadmin/Desktop/CCA Tools"
fi

# Create launch.desktop file
sudo touch '/home/bcadmin/Desktop/CCA Tools/SIP Creator.desktop'
echo '[Desktop Entry]' | sudo tee --append '/home/bcadmin/Desktop/CCA Tools/SIP Creator.desktop'
echo 'Type=Application' | sudo tee --append '/home/bcadmin/Desktop/CCA Tools/SIP Creator.desktop'
echo 'Name=SIP Creator' | sudo tee --append '/home/bcadmin/Desktop/CCA Tools/SIP Creator.desktop'
echo 'Exec=/usr/share/ccatools/sipcreator/launch' | sudo tee --append '/home/bcadmin/Desktop/CCA Tools/SIP Creator.desktop'
echo 'Icon=/usr/share/ccatools/sipcreator/icon.png' | sudo tee --append '/home/bcadmin/Desktop/CCA Tools/SIP Creator.desktop'

# Change permissions, ownership for CCA Tools
sudo chown -R bcadmin:bcadmin '/home/bcadmin/Desktop/CCA Tools'
sudo chown -R bcadmin:bcadmin '/usr/share/ccatools/sipcreator'
sudo find '/home/bcadmin/Desktop/CCA Tools' -type d -exec chmod 755 {} \;
sudo find '/home/bcadmin/Desktop/CCA Tools' -type f -exec chmod 644 {} \;

# Make files executable
sudo chmod u+x '/home/bcadmin/Desktop/CCA Tools/SIP Creator.desktop'
sudo chmod u+x /usr/share/ccatools/sipcreator/launch

#!/bin/bash

### Install script for CCA SIP Creator in Bitcurator

# Make /usr/share/ccatools if doesn't already exist
if [ ! -d /usr/share/ccatools ]; then
  sudo mkdir /usr/share/ccatools
fi

# Make /usr/share/cca-folderprocessor if doesn't already exist
if [ ! -d /usr/share/ccatools/sipcreator ]; then
  sudo mkdir /usr/share/ccatools/sipcreator
fi

# Move files into /usr/share/cca-folderprocessor
sudo mv main.py /usr/share/ccatools/sipcreator
sudo mv launch /usr/share/ccatools/sipcreator
sudo mv design.py /usr/share/ccatools/sipcreator
sudo mv design.ui /usr/share/ccatools/sipcreator
sudo mv LICENSE /usr/share/ccatools/sipcreator
sudo mv README.md /usr/share/ccatools/sipcreator

# Make "CCA Tools" folder on Desktop if doesn't already exist
if [ ! -d "/home/bcadmin/Desktop/CCA Tools" ]; then
  sudo mkdir "/home/bcadmin/Desktop/CCA Tools"
fi

# Create launch.desktop file
sudo touch '/home/bcadmin/Desktop/CCA Tools/SIP Creator.desktop'
echo '[Desktop Entry]' | sudo tee --append '/home/bcadmin/Desktop/CCA Tools/SIP Creator.desktop'
echo 'Type=Application' | sudo tee --append '/home/bcadmin/Desktop/CCA Tools/SIP Creator.desktop'
echo 'Name=Folder Processor' | sudo tee --append '/home/bcadmin/Desktop/CCA Tools/SIP Creator.desktop'
echo 'Exec=/usr/share/ccatools/sipcreator/launch' | sudo tee --append '/home/bcadmin/Desktop/CCA Tools/SIP Creator.desktop'
echo 'Icon=' | sudo tee --append '/home/bcadmin/Desktop/CCA Tools/SIP Creator.desktop'

# Change permissions, ownership for CCA Tools
sudo chown -R bcadmin:bcadmin '/home/bcadmin/Desktop/CCA Tools'
sudo chown -R bcadmin:bcadmin '/usr/share/ccatools/sipcreator'
sudo find '/home/bcadmin/Desktop/CCA Tools' -type d -exec chmod 755 {} \;
sudo find '/home/bcadmin/Desktop/CCA Tools' -type f -exec chmod 644 {} \;

# Make files executable
sudo chmod u+x '/home/bcadmin/Desktop/CCA Tools/SIP Creator.desktop'
sudo chmod u+x /usr/share/ccatools/sipcreator/launch

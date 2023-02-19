#!/bin/bash

### Install SIP Creator for testing

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

sudo cp deps/dfxml/python/dfxml.py .
sudo cp deps/dfxml/python/Objects.py .
sudo cp deps/dfxml/python/walk_to_dfxml.py .

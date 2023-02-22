# SIP Creator

Version: 1.1.0

Creates an Archivematica-ready transfer (or SIP for another preservation repository) from user-selected directories and files, and generates a pre-populated description spreadsheet using data pulled from DFXML and Brunnhilde (start and end dates, extent, and a scope and content note containing information about the most common file formats present).  

SIP Creator generates a md5deep-generated checksum.md5 manifest saved in the SIP's metadata directory (according to Archivematica packaging ventions) as default behavior. To create the SIP as a bag instead, select that option from the GUI interface.  

SIP Creator can optionally also run a PII scan of each SIP using bulk_extractor as part of the Brunnhilde characterization step of SIP creation and description. Bulk_extractor reports are saved to metadata/submissionDocumentation, in the Brunnhilde report output folder.  

## Installation

This utility is designed for easy use in BitCurator v1.8.0+. It requires Python 3 and PyQt5.  

### Install as part of CCA Tools  

Install all of the CCA Tools together using the installation script in the [CCA Tools repo](https://github.com/CCA-Public/cca-tools).  

### Install as a separate utility

* Install [PyQt5](https://www.riverbankcomputing.com/software/pyqt/download5):  
`sudo pip3 install pyqt5`  
* Clone this repo to your local machine.  
* Run the install script with sudo privileges (assuming BitCurator 4; for BitCurator 2-3 run `./install-bc2-ubuntu18.sh` instead):  
`sudo ./install.sh`

### PyQt4 version

Please note that SIP Creator v1.0.0 uses PyQt5. Installation of PyQt5 may cause issues with existing PyQt4 programs in BitCurator. For the a PyQt4 version of SIP Creator that will not affect the functionality of other tools, see the [0.2.0 release](https://github.com/CCA-Public/sipcreator/releases/tag/v0.2.0).

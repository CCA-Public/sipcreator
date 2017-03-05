# CCA SIP Creator

Creates an Archivematica-ready transfer (or SIP for another preservation repository) from user-selected directories and files, and generates a pre-populated description spreadsheet containing information such as start and end dates, extents, and a scope and content note for the newly created SIP.

CCA SIP Creator generates a md5deep-generated checksum.md5 manifest saved in the SIP's metadata directory (according to Archivematica packaging ventions) as default behavior. To create the SIP as a bag instead, select that option from the GUI interface. 

SIP Creator can optionally also run a PII scan of each SIP using bulk_extractor as part of the Brunnhilde characterization step of SIP creation and description. Bulk_extractor reports are saved to metadata/submissionDocumentation, in the Brunnhilde report output folder.  

### Installation  

This utility is designed for easy use in Bitcurator, and requires installation of only:  
* [PyQt4](https://www.riverbankcomputing.com/software/pyqt/download): `sudo apt-get install python-qt4`  
* [Siegfried](https://github.com/richardlehane/siegfried/): See system-specific installation instructions on Github repo  
* [Brunnhilde](https://github.com/timothyryanwalsh/brunnhilde): `sudo pip install brunnhilde`  

To use the Folder Processor in other UNIX-like environments, make sure you also have installed:  
* Python 2.7  
* md5deep  
* bagit-python
* bulk_extractor (optional)

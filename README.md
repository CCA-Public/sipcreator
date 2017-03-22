# CCA SIP Creator

**NOTE: This tool is in dev and should not be considered production-ready without testing**

Creates an Archivematica-ready transfer (or SIP for another preservation repository) from user-selected directories and files, and generates a pre-populated description spreadsheet using data pulled from DFXML and Brunnhilde (start and end dates, extent, and a scope and content note containing information about the most common file formats present).  

SIP Creator generates a md5deep-generated checksum.md5 manifest saved in the SIP's metadata directory (according to Archivematica packaging ventions) as default behavior. To create the SIP as a bag instead, select that option from the GUI interface.  

SIP Creator can optionally also run a PII scan of each SIP using bulk_extractor as part of the Brunnhilde characterization step of SIP creation and description. Bulk_extractor reports are saved to metadata/submissionDocumentation, in the Brunnhilde report output folder.  

### Installation  

This utility is designed for easy use in Bitcurator, and in v1.8.0+ requires installation of only [PyQt4](https://www.riverbankcomputing.com/software/pyqt/download):  

`sudo apt-get install python-qt4`  

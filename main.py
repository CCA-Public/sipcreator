#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
CCA SIP Creator

Tim Walsh 2017
MIT License
"""

from PyQt4.QtGui import *
from PyQt4.QtCore import * 
import csv
import datetime
import itertools
import math
import os
import shutil
import subprocess
import sys
from time import localtime, strftime

import design

#import Objects.py from python dfxml tools
sys.path.append('/usr/share/dfxml/python')
import Objects

class CheckableDirModel(QDirModel):
    # class to put checkbox on the folders
    def __init__(self, parent=None):
        QDirModel.__init__(self, None)
        self.checks = {}

    def data(self, index, role=Qt.DisplayRole):
        if role != Qt.CheckStateRole:
            return QDirModel.data(self, index, role)
        else:
            if index.column() == 0:
                return self.checkState(index)

    def flags(self, index):
        return QDirModel.flags(self, index) | Qt.ItemIsUserCheckable

    def checkState(self, index):
        if index in self.checks:
            return self.checks[index]
        else:
            return Qt.Unchecked

    def setData(self, index, value, role):
        if (role == Qt.CheckStateRole and index.column() == 0):
            self.checks[index] = value
            self.emit(SIGNAL("dataChanged(QModelIndex,QModelIndex)"), index, index)
            return True 

        return QDirModel.setData(self, index, value, role)

class SIPThread(QThread):

    def __init__(self, files_to_process, destination, sip_dir, bagfiles, piiscan):
        QThread.__init__(self)
        self.files_to_process = files_to_process
        self.destination = destination
        self.sip_dir = sip_dir
        self.bagfiles = bagfiles
        self.piiscan = piiscan

    def __del__(self):
        self.wait()

    def create_sip(self, files_to_process, sip_dir, bagfiles, piiscan):
        
        # set paths and create dirs
        object_dir = os.path.join(sip_dir, 'objects')
        metadata_dir = os.path.join(sip_dir, 'metadata')
        subdoc_dir = os.path.join(metadata_dir, 'submissionDocumentation')
        
        for newfolder in object_dir, metadata_dir, subdoc_dir:
            os.makedirs(newfolder)

        # copy files
        for file_to_process in files_to_process:
            file_to_process = os.path.abspath(file_to_process)
            if os.path.isdir(file_to_process):
                copy_dest = os.path.join(object_dir, os.path.basename(file_to_process))
                try:
                    shutil.copytree(file_to_process, copy_dest, symlinks=False, ignore=None)
                except shutil.Error as e:
                    print("WARNING: Error copying dir " + file_to_process + " : " + e) #TODO improve error handling
            else:     
                try:
                    shutil.copy2(file_to_process, object_dir)
                except shutil.Error as e:
                    print("WARNING: Error copying file " + file_to_process + " : " + e) #TODO improve error handling

        # run brunnhilde and write to submissionDocumentation
        files_abs = os.path.abspath(object_dir)

        if piiscan == True: # brunnhilde with bulk_extractor
            subprocess.call("brunnhilde.py -zbw '%s' '%s' '%s_brunnhilde'" % (files_abs, subdoc_dir, os.path.basename(sip_dir)), shell=True)
        else: # brunnhilde without bulk_extractor
            subprocess.call("brunnhilde.py -zw '%s' '%s' '%s_brunnhilde'" % (files_abs, subdoc_dir, os.path.basename(sip_dir)), shell=True)

        # create dfxml and write to submissionDocumentation
        subprocess.call("md5deep -rd %s > %s" % (object_dir, os.path.join(subdoc_dir, 'dfxml.xml')), shell=True)

        # write checksums
        if bagfiles == True: # bag entire SIP
            subprocess.call("bagit.py --processes 4 '%s'" % sip_dir, shell=True)
        else: # write metadata/checksum.md5
            subprocess.call("cd '%s' && md5deep -rl ../objects > checksum.md5" % metadata_dir, shell=True)

        # modify file permissions
        subprocess.call("find '%s' -type d -exec chmod 755 {} \;" % sip_dir, shell=True)
        subprocess.call("find '%s' -type f -exec chmod 644 {} \;" % sip_dir, shell=True)

    def convert_size(self, size):
        # convert size to human-readable form
        if size == 0:
            return '0 bytes'
        size_name = ("bytes", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
        i = int(math.floor(math.log(size,1024)))
        p = math.pow(1024,i)
        s = round(size/p)
        s = str(s)
        s = s.replace('.0', '')
        return '%s %s' % (s,size_name[i])

    def create_spreadsheet(self, destination, sip_dir, bagfiles):

        # open description spreadsheet
        try:
            spreadsheet = open(os.path.join(self.destination, 'description.csv'), 'w')
            writer = csv.writer(spreadsheet, quoting=csv.QUOTE_NONNUMERIC)
            header_list = ['Parent ID', 'Identifier', 'Title', 'Archive Creator', 'Date expression', 'Date start', 'Date end', 
        'Level of description', 'Extent and medium', 'Scope and content', 'Arrangement (optional)', 'Accession number', 
        'Appraisal, destruction, and scheduling information (optional)', 'Name access points (optional)', 
        'Geographic access points (optional)', 'Conditions governing access (optional)', 'Conditions governing reproduction (optional)', 
        'Language of material (optional)', 'Physical characteristics & technical requirements affecting use (optional)', 
        'Finding aids (optional)', 'Related units of description (optional)', 'Archival history (optional)', 
        'Immediate source of acquisition or transfer (optional)', "Archivists' note (optional)", 'General note (optional)', 
        'Description status']
            writer.writerow(header_list)
        except:
            sys.exit('There was an error creating the processing spreadsheet.')

        # intialize values
        number_files = 0
        total_bytes = 0
        mtimes = []

        # parse dfxml file
        if bagfiles == True:
            dfxml_file = os.path.abspath(os.path.join(sip_dir, 'data', 'metadata', 'submissionDocumentation', 'dfxml.xml'))
        else:
            dfxml_file = os.path.abspath(os.path.join(sip_dir, 'metadata', 'submissionDocumentation', 'dfxml.xml'))

        # gather info for each FileObject
        for (event, obj) in Objects.iterparse(dfxml_file):
            
            # only work on FileObjects
            if not isinstance(obj, Objects.FileObject):
                continue
            
            # gather info
            number_files += 1

            mtime = obj.mtime
            if not mtime:
                mtime = ''
            mtime = str(mtime)
            mtimes.append(mtime)
            
            total_bytes += obj.filesize

        # build extent statement
        size_readable = self.convert_size(total_bytes)
        if number_files == 1:
            extent = "1 digital file (%s)" % size_readable
        elif number_files == 0:
            extent = "EMPTY"
        else:
            extent = "%d digital files (%s)" % (number_files, size_readable)

        # build date statement TODO: utilize all MAC dates, not just modified
        if mtimes:
            date_earliest = min(mtimes)
            date_latest = max(mtimes)
        else:
            date_earliest = 'N/A'
            date_latest = 'N/A'
        if date_earliest == date_latest:
            date_statement = '%s' % date_earliest[:4]
        else:
            date_statement = '%s - %s' % (date_earliest[:4], date_latest[:4])

        # gather info from burnnhilde & write scope and content note
        if extent == 'EMPTY':
            scopecontent = ''
        else:
            fileformats = []
            if bagfiles == True:
                fileformat_csv = os.path.join(sip_dir, 'data', 'metadata', 'submissionDocumentation', '%s_brunnhilde' % os.path.basename(sip_dir), 'csv_reports', 'formats.csv')
            else:
                fileformat_csv = os.path.join(sip_dir, 'metadata', 'submissionDocumentation', '%s_brunnhilde' % os.path.basename(sip_dir), 'csv_reports', 'formats.csv')
            with open(fileformat_csv, 'r') as f:
                reader = csv.reader(f)
                reader.next()
                for row in itertools.islice(reader, 5):
                    fileformats.append(row[0])
            fileformats = [element or 'Unidentified' for element in fileformats] # replace empty elements with 'Unidentified'
            formatlist = ', '.join(fileformats) # format list of top file formats as human-readable
            
            # create scope and content note
            scopecontent = 'Most common file formats: %s' % (formatlist)

        # write csv row
        writer.writerow(['', os.path.basename(sip_dir), '', '', date_statement, date_earliest, date_latest, 'File', extent, 
            scopecontent, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''])

        # close description spreadsheet
        spreadsheet.close()

    def run(self):
        self.create_sip(self.files_to_process, self.sip_dir, self.bagfiles, self.piiscan)
        self.emit(SIGNAL('increment_progress_bar(QString)'), '')
        self.create_spreadsheet(self.destination, self.sip_dir, self.bagfiles)


class ProcessorApp(QMainWindow, design.Ui_MainWindow):

    def __init__(self, parent=None):
        super(ProcessorApp, self).__init__(parent)
        self.setupUi(self)

        # build browse functionality buttons
        self.sourceBtn.clicked.connect(self.browse_source)
        self.destinationBtn.clicked.connect(self.browse_dest)

        # build start functionality
        self.processBtn.clicked.connect(self.start_processing)

        # set progress bar to 0
        self.progressBar.setValue(0)

    def browse_source(self):
        source = QFileDialog.getExistingDirectory(self, "Select folder")

        if source: # if user didn't pick directory don't continue
            self.model = CheckableDirModel()
            self.treeView.setModel(self.model)
            self.treeView.setSortingEnabled(True)
            self.treeView.setRootIndex(self.model.index(source))

    def browse_dest(self):
        self.destination.clear() # clear directory source text
        directory = QFileDialog.getExistingDirectory(self, "Select folder")

        if directory: # if user didn't pick directory don't continue
            self.destination.setText(directory)

    def increment_progress_bar(self, dir_to_process):
        self.progressBar.setValue(self.progressBar.value()+1)

    def done(self):
        self.cancelBtn.setEnabled(False)
        self.processBtn.setEnabled(True)
        self.progressBar.setValue(self.progressBar.value()+1)
        QMessageBox.information(self, "Done!", "Process complete.")
        self.status.setText('Finished')

    def start_processing(self):
        # acknowledge process has started
        self.status.setText('Processing')

        # create list of paths for checked folders
        files_to_process = []
        for index,value in self.model.checks.items():
            if value.toBool():
                unicode_filename = unicode(self.model.filePath(index).toUtf8(), encoding="utf-8")
                files_to_process.append(unicode_filename)

        # prepare progress bar
        self.progressBar.setMaximum(2)
        self.progressBar.setValue(0)

        # create output directories
        destination = str(self.destination.text())
        sip_name = str(self.sipName.text())
        sip_dir = os.path.join(destination, sip_name)

        if not os.path.exists(destination):
            os.makedirs(destination)
        os.makedirs(sip_dir)

        # handle argument checkboxes
        bagfiles = False
        piiscan = False
        if self.bagSIPs.isChecked():
            bagfiles = True
        if self.bulkExt.isChecked():
            piiscan = True

        # create SIP for each sip_dir in list and spreadsheet describing all created SIPs
        self.get_thread = SIPThread(files_to_process, destination, sip_dir, bagfiles, piiscan)
        self.connect(self.get_thread, SIGNAL("increment_progress_bar(QString)"), self.increment_progress_bar)
        self.connect(self.get_thread, SIGNAL("finished()"), self.done)
        self.get_thread.start()
        self.cancelBtn.setEnabled(True)
        self.cancelBtn.clicked.connect(self.get_thread.terminate)
        self.processBtn.setEnabled(False)

def main():
    app = QApplication(sys.argv)
    form = ProcessorApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()

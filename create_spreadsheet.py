#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Python3 program for generating a descriptive spreadsheet for a directory of SIPs.

Tim Walsh 2017
MIT License
"""

import argparse
import csv
import itertools
import math
import os
import sys

#import Objects.py from python dfxml tools
sys.path.append('/usr/share/dfxml/python')
import Objects

def convert_size(size):
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

def create_spreadsheet(destination, sip_dir, bagfiles):

    # open description spreadsheet
    try:
        spreadsheet = open(os.path.join(destination, 'description.csv'), 'w')
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
    size_readable = convert_size(total_bytes)
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

    # gather info from brunnhilde & write scope and content note
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
            next(reader)
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

# MAIN FLOW

# parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("-b", "--bagfiles", help="Bag files instead of writing checksum.md5", action="store_true")
parser.add_argument("destination", help="Destination directory for CSV file")
parser.add_argument("sip_dir", help="SIP to gather information about")
args = parser.parse_args()

destination = args.destination

bagfiles = False
if args.bagfiles:
    bagfiles = True

# call create_spreadsheet
create_spreadsheet(args.destination, args.sip_dir, bagfiles)
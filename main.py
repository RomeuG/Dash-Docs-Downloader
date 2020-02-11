import urllib3
import glob
import os

import xml.etree.ElementTree as ET

output_dir = 'output'

def get_feed_files():
    return glob.glob('./feeds/*.xml')

def get_file_name(path):
    return path.split('/')[-1][:-4]

def parse_xml(xml_files):
    for file in xml_files:

        file_name = get_file_name(file)
        path = 'output/' + file_name

        try:
            os.mkdir('output/' + file_name)
        except OSError:
            print(f"Directory {path} already exists.")

        tree = ET.parse(file)
        root = tree.getroot()
        #print(root[0].text)
    return

try:
    os.mkdir(output_dir)
except OSError:
    print(f"Directory {output_dir} already exists.")

feed_files = get_feed_files()
feed_files.sort()
parse_xml(feed_files)

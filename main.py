import urllib3
import glob
import os

import xml.etree.ElementTree as ET

def get_feed_files():
    return glob.glob('./feeds/*.xml')

def parse_xml(xml_file):
    for file in xml_file:
        tree = ET.parse(file)
        root = tree.getroot()
        print(root[0])
    return

feed_files = get_feed_files()
parse_xml(feed_files)

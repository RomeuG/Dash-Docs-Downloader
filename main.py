import urllib3
import glob
import os
import requests

import xml.etree.ElementTree as ET

output_dir = 'output'

def download_file(url, path):
    result = False

    with open(path, 'wb') as f:
        response = requests.get(url)
        result = response.ok
        if result == True:
            f.write(response.content)

    return result

def refresh_feed():
    os.system("sudo rm -r feeds")
    os.system("git clone https://github.com/Kapeli/feeds")
    return

def get_feed_files():
    return glob.glob('./feeds/*.xml')

def get_file_name(path):
    return path.split('/')[-1][:-4]

def parse_xml(xml_files):
    for file in xml_files:
        urls = []
        file_name = get_file_name(file)
        path = 'output/' + file_name

        try:
            os.mkdir(path)
        except OSError:
            print(f"Directory {path} already exists.")

        tree = ET.parse(file)
        root = tree.getroot()
        version_name = root[0].text

        if not os.path.exists(path + '/.version'):
            with open(path + '/.version', 'w') as f:
                f.write(version_name)

            for url in root:
                if url.tag == 'url':
                    urls.append(url.text)

            for url in urls:
                url_file = url.split('/')[-1]
                file_path = path + '/' + url_file
                print(f"Downloading {url_file} to {file_path}...")
                result = download_file(url, file_path)
                if result == True:
                    break
        else:
            version_file = ""
            with open(path + '/.version', 'r') as f:
                version_file = f.read()

            if version_name == version_file:
                continue

            with open(path + '/.version', 'w') as f:
                f.write(version_name)

            for url in root:
                if url.tag == 'url':
                    urls.append(url.text)

            for url in urls:
                url_file = url.split('/')[-1]
                file_path = path + '/' + url_file
                print(f"Downloading {url_file} to {file_path}...")
                result = download_file(url, file_path)
                if result == True:
                    break

    return

try:
    os.mkdir(output_dir)
except OSError:
    print(f"Directory {output_dir} already exists.")

refresh_feed()
feed_files = get_feed_files()
feed_files.sort()
parse_xml(feed_files)

#!/usr/bin/env python3
# Copyright (c) 2022 José Manuel Barroso Galindo <theypsilon@gmail.com>
import csv
import subprocess
try:
    import httpimport
except ImportError as _:
    subprocess.run(['python3', '-m', 'pip', 'install', 'requests', 'httpimport'])
    import httpimport

download_distribution = httpimport.load('download_distribution', 'https://raw.githubusercontent.com/MiSTer-devel/Distribution_MiSTer/develop/.github')

target = download_distribution.read_target_dir()
metadata_props = download_distribution.Metadata.new_props()
delme = subprocess.run(['mktemp', '-d'], shell=False, stderr=subprocess.STDOUT, stdout=subprocess.PIPE).stdout.decode().strip()

def extra_content(url, kind):
    try:
        download_distribution.process_extra_content(url, kind, delme, target)
    except Exception as e:
        print(e)

def core(props):
    try:
        download_distribution.process_core(props, delme, target, metadata_props)
    except Exception as e:
        print(e)

with open('mister_repos.csv', "r") as file:
    csv_reader = csv.reader(file)
    for row_number, row in enumerate(csv_reader):
        if row == 0: continue
        print('row: ' + str(row_number), row)
        try:
            name, url, category = row[0], row[1], row[2]
        except ValueError as e:
            print(f"Error processing row {row_number}: {e}")
            continue

        if category.lower() == '_arcade':
            core({'name': name, 'url': url, 'category': '_Arcade'})
            extra_content(url, 'user-content-mra-alternatives-under-releases')
            continue

        try:
            home = row[3]
        except ValueError as e:
            print(f"No 'home' column on row {row_number}: {e}")
            continue
        core({'name': name, 'url': url, 'home': home, 'category': category})

#!/usr/bin/env python3
# Copyright (c) 2022 José Manuel Barroso Galindo <theypsilon@gmail.com>

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
        if 'url' in props and 'category' in props and props['category'].lower() == '_arcade':
            extra_content(props['url'], 'user-content-mra-alternatives-under-releases')
    except Exception as e:
        print(e)

core({'name': 'ZX-Spectrum 48', 'url': "https://github.com/Kyp069/zx48-MiSTer", 'home': 'zx48', 'category': '_Computer'})
core({'name': 'GX400', 'url': "https://github.com/GX400-Friends/gx400-bin", 'category': '_Arcade'})
core({'name': 'TMNT', 'url': "https://github.com/furrtek/Arcade-TMNT_MiSTer", 'category': '_Arcade'})

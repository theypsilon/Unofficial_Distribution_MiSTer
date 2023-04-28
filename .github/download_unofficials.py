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

download_distribution.process_core({'name': 'ZX-Spectrum 48', 'url': "https://github.com/Kyp069/zx48-MiSTer", 'home': 'zx48', 'category': '_Computer'}, delme, target, metadata_props)
download_distribution.process_core({'name': 'GX400', 'url': "https://github.com/GX400-Friends/gx400-bin", 'category': '_Arcade'}, delme, target, metadata_props)
download_distribution.process_extra_content("https://github.com/GX400-Friends/gx400-bin", 'user-content-mra-alternatives-under-releases', delme, target)
download_distribution.process_core({'name': 'TMNT', 'url': "https://github.com/furrtek/Arcade-TMNT_MiSTer", 'category': '_Arcade'}, delme, target, metadata_props)
download_distribution.process_extra_content("https://github.com/furrtek/Arcade-TMNT_MiSTer", 'user-content-mra-alternatives-under-releases', delme, target)

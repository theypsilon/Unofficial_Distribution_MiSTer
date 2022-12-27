#!/usr/bin/env python3
# Copyright (c) 2022 José Manuel Barroso Galindo <theypsilon@gmail.com>

import subprocess
import sys
import time
import shutil
from pathlib import Path
try:
    import httpimport
except:
    subprocess.run(['python3', '-m', 'pip', 'install', 'httpimport'])
    import httpimport

download_distribution = httpimport.load('download_distribution', 'https://raw.githubusercontent.com/MiSTer-devel/Distribution_MiSTer/develop/.github')

def main() -> None:

    start = time.time()

    target = 'delme'
    if len(sys.argv) > 1:
        target = sys.argv[1].strip()

    if 'delme' in target.lower():
        shutil.rmtree(target, ignore_errors=True)
        Path(target).mkdir(parents=True, exist_ok=True)

    metadata_props = download_distribution.Metadata.new_props()
    delme = subprocess.run(['mktemp', '-d'], shell=False, stderr=subprocess.STDOUT, stdout=subprocess.PIPE).stdout.decode().strip()
    download_distribution.process_core({'name': 'ZX-Spectrum 48', 'url': "https://github.com/Kyp069/zx48-MiSTer", 'home': 'zx48', 'category': '_Computer'}, delme, target, metadata_props)
    download_distribution.process_core({'name': 'GX400', 'url': "https://github.com/GX400-Friends/gx400-bin", 'category': '_Arcade'}, delme, target, metadata_props)
    download_distribution.process_extra_content("https://github.com/GX400-Friends/gx400-bin", 'user-content-mra-alternatives-under-releases', delme, target)

    print()
    print("Time:")
    end = time.time()
    print(end - start)
    print()


if __name__ == '__main__':
    main()

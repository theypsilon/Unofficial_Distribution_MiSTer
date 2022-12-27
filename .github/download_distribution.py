
import subprocess
try:
    import httpimport
except:
    subprocess.run(['pip', 'install', 'httpimport'])
    import httpimport

with httpimport.remote_repo(["mister_distlib"], 'https://raw.githubusercontent.com/MiSTer-devel/Distribution_MiSTer/develop/.github/download_distribution.py'):
    import mister_distlib

def main() -> None:

    start = time.time()

    metadata_props = {}
    target = '.'
    delme = subprocess.run(['mktemp', '-d'], shell=False, stderr=subprocess.STDOUT, stdout=subprocess.PIPE).stdout.decode().strip()
    mister_distlib.process_core({'name': 'ZX-Spectrum 48', 'url': "https://github.com/Kyp069/zx48-MiSTer", 'home': 'zx48', 'category': '_Computer'}, delme, target, metadata_props)
    mister_distlib.process_core({'name': 'GX400', 'url': "https://github.com/GX400-Friends/gx400-bin", 'category': '_Arcade'}, delme, target, metadata_props)
    mister_distlib.process_extra_content("https://github.com/GX400-Friends/gx400-bin", 'user-content-mra-alternatives-under-releases', delme, target)

    print()
    print("Time:")
    end = time.time()
    print(end - start)
    print()


if __name__ == '__main__':
    main()

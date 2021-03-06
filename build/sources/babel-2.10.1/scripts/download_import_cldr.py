#!/usr/bin/env python3

import contextlib
import os
import sys
import shutil
import hashlib
import zipfile
import subprocess
try:
    from urllib.request import urlretrieve
except ImportError:
    from urllib import urlretrieve


URL = 'http://unicode.org/Public/cldr/41/cldr-common-41.0.zip'
FILENAME = 'cldr-common-41.0.zip'
# Via https://unicode.org/Public/cldr/41/hashes/SHASUM512
FILESUM = 'c64f3338e292962817b043dd11e9c47f533c9b70d432f83e80654e20f4937c72b37e66a60485df43f734b1ff94ebf0452547a063076917889303c9653b4d6ce5'
BLKSIZE = 131072


def get_terminal_width():
    try:
        import fcntl
        import termios
        import struct
        fd = sys.stdin.fileno()
        cr = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ, '1234'))
        return cr[1]
    except Exception:
        return 80


def reporthook(block_count, block_size, total_size):
    bytes_transmitted = block_count * block_size
    cols = get_terminal_width()
    buffer = 6
    percent = float(bytes_transmitted) / (total_size or 1)
    done = int(percent * (cols - buffer))
    sys.stdout.write('\r')
    sys.stdout.write(' ' + '=' * done + ' ' * (cols - done - buffer))
    sys.stdout.write('% 4d%%' % (percent * 100))
    sys.stdout.flush()


def log(message, *args):
    if args:
        message = message % args
    sys.stderr.write(message + '\n')


def is_good_file(filename):
    if not os.path.isfile(filename):
        log('Local copy \'%s\' not found', filename)
        return False
    h = hashlib.sha512()
    with open(filename, 'rb') as f:
        while 1:
            blk = f.read(BLKSIZE)
            if not blk:
                break
            h.update(blk)
        digest = h.hexdigest()
        if digest != FILESUM:
            raise RuntimeError('Checksum mismatch: %r != %r'
                               % (digest, FILESUM))
        else:
            return True


def main():
    scripts_path = os.path.dirname(os.path.abspath(__file__))
    repo = os.path.dirname(scripts_path)
    cldr_dl_path = os.path.join(repo, 'cldr')
    cldr_path = os.path.join(repo, 'cldr', os.path.splitext(FILENAME)[0])
    zip_path = os.path.join(cldr_dl_path, FILENAME)
    changed = False
    show_progress = (False if os.environ.get("BABEL_CLDR_NO_DOWNLOAD_PROGRESS") else sys.stdout.isatty())

    while not is_good_file(zip_path):
        log("Downloading '%s' from %s", FILENAME, URL)
        if os.path.isfile(zip_path):
            os.remove(zip_path)
        urlretrieve(URL, zip_path, (reporthook if show_progress else None))
        changed = True
        print()
    common_path = os.path.join(cldr_path, 'common')

    if changed or not os.path.isdir(common_path):
        if os.path.isdir(common_path):
            log('Deleting old CLDR checkout in \'%s\'', cldr_path)
            shutil.rmtree(common_path)

        log('Extracting CLDR to \'%s\'', cldr_path)
        with contextlib.closing(zipfile.ZipFile(zip_path)) as z:
            z.extractall(cldr_path)

    subprocess.check_call([
        sys.executable,
        os.path.join(scripts_path, 'import_cldr.py'),
        common_path])


if __name__ == '__main__':
    main()

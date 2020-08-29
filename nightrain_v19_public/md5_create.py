# -*- coding: utf-8 -*-

import hashlib

def create_md5(filename):
    hash_md5 = hashlib.md5()
    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def save_md5file( filename, data):
    with open(filename, 'w', -1, 'utf-8') as fp:
        fp.write(data)



in_filename  = '.\\addon_list.xml'
out_filename = '.\\addon_list.xml.md5'

md5text = create_md5(in_filename)
print(md5text)
save_md5file(out_filename, md5text)

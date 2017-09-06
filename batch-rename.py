import os.path as ops
import glob
import shutil

def batchRename(lname=[], start=1, pattern='%05d', dst=''):
    for name in lname:
        # pPath = ops.split(name)[0]
        ext = ops.splitext(name)[1]
        shutil.copy(name, dst+'/' + (pattern % start) + ext)
        start += 1

    pass

if __name__ == '__main__':
    path = 'Z:/Win10Users/Desktop/neg'
    dst = 'Z:/Win10Users/Desktop/neg/rename'
    lname = glob.glob(path + '/*.JPG')
    lname = sorted(lname)
    start = 1
    pattern = '%05d'

    batchRename(lname, start, pattern, dst)



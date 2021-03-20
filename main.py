import pathlib

import pandas as pd
import os
import datetime
import time
import shutil

def indexer(file_dir):
    columns = ['link', 'folder', 'year']
    index = pd.DataFrame(columns=columns, )
    for root, subdirectory, files in os.walk(file_dir):
        relativepath, foldername = os.path.split(root)

        for file in sorted(files):
            try:
                filename, file_extension = os.path.splitext(file)
                filesize = os.path.getsize(file_dir)
                fname = pathlib.Path(file_dir + '/' + file)
                lastmodification = datetime.datetime.fromtimestamp(fname.stat().st_mtime)
                # if (file_extension == '.jpg' or file_extension == '.JPG' or file_extension == '.JPEG' or file_extension == '.jpeg'):
                line = {'link': fname, 'folder' : str(root) + '/', 'year' : str(lastmodification.year)}
                index = index.append(line, ignore_index=True)
            except (FileNotFoundError):
                print(fname)
                pass

    return index

documentspath =  '/home/tonycalvez/Pictures'
listdocuments = indexer(documentspath).to_dict('r')
i = 0
print('Ready to dispatch')
for document in listdocuments:
    direction = str(document['folder']) + str(document['year'])

    if not os.path.exists(direction):
        os.mkdir(direction + '/')
        print('folder:', direction)
        pass

    print(document['link'], direction)
    shutil.move(document['link'], direction+'/'+'img'+ str(i) + '.jpg')
    i = i + 1

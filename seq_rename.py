import os
_src = "/Users/valera/Documents/venprojs/alpr/imgs/"
_ext = ".jpg"
for i, filename in enumerate(os.listdir(_src)):
    if filename.endswith(_ext):
        print (filename, _src + str(i).zfill(4)+_ext)
        os.rename(_src + filename, _src + str(i).zfill(4)+_ext)

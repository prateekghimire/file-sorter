import os
import shutil

files=os.listdir()

unique_extensions=[]

for item in files:
    extension=item.split('.')
    extension=extension[len(extension)-1]
    if extension not in unique_extensions:
        unique_extensions.append(extension)


for item in files:
    extension=item.split('.')
    extension=extension[len(extension)-1]
    for file_ in unique_extensions:
        if file_==extension:
            shutil.move(item,extension)

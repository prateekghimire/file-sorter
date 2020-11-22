import os
import shutil

files=os.listdir()

unique_extensions=[]

for item in files:
    extension=item.split('.')
    extension=extension[len(extension)-1]
    if extension not in unique_extensions:
        unique_extensions.append(extension)

for item in unique_extensions:
    try:
        os.mkdir("{}".format(item))
        print('New directory created')
    except Exception as e:
        print("Directory already exists")

for item in files:
    extension=item.split('.')
    extension=extension[len(extension)-1]
    for file_ in unique_extensions:
        if file_==extension:
            try:
                shutil.move(item,extension)
            except Exception as e:
                print("File with same name exists")
from tkinter import *
from tkinter.ttk import *
import os
import shutil

def sort_my_files():
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


root=Tk()
root.wm_title('File Sorter')
root.wm_iconbitmap('icon.ico')
root.configure(bg='black')
root.minsize(width=500, height=200)
root.resizable(0, 0)
style=Style()
style.configure('TButton', font =
               ('arial', 10, 'bold'),
                foreground = 'green')
btn=Button(root,text='CLICK HERE TO SORT THE FILES',command=sort_my_files).place(x=50,y=50)
var = StringVar()
label = Label( root, textvariable=var, relief=RAISED ).place(x=380,y=180)
var.set("Developed by: Pratik")
#label.pack()
#btn.pack()
root.mainloop()

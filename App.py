import os 

import shutil

source = r"C:\Users\DELL\Desktop\python\P-112"
destination=r"C:\Users\DELL\Desktop\python\P-112\document"


list_of_files= os.listdir(source)
for x in list_of_files:
    name,extension = os.path.splitext(x)
    if extension == " ":
        continue
    if extension in [ ".txt", ".doc", ".docx", ".pdf"]:
        path1=source+"/" + x
        path2=destination
        path3=path2+"/"+x
        if os.path.exists(path2):
            print("moving the files")
            shutil.move(path1,path3)
        else:
            print("Creating a folder ")
            os.mkdir(path2)
            print("moving the files")
            shutil.move(path1,path3) 

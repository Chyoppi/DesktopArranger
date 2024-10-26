#DesktopArranger

import os 

#Desktop Location and where the files will be move to
source_folder = r"C:\Users\(USER)\\Desktop"
destination_folder = r"C:\Users\(USER)\Desktop\\Arrange"

#Files we want to have on our desktop
allowed_files = ["sample.txt"]

allfiles = os.listdir(source_folder)

#Goes through all the files and if they are not on the allowed list will be moved to destination
for file in allfiles:
    if file not in allowed_files:
        src_path = os.path.join(source_folder, file)
        dst_path = os.path.join(destination_folder, file)
        os.rename(src_path, dst_path)

import os

file_path = "C:\\Users\\hp\\Desktop\\Test Folder"

for folder,sub_folder,file in os.walk(file_path):
    print(f"Currently looking at : {folder}")
    print("\n")
    for sub_fol in sub_folder:
        print(f"\tThe sub_folder is : {sub_folder}")
    print("\n")
    for f in file:
        print(f"\tThe File List : {file}")
    print("\n")
    


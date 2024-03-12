import os
import shutil

# Return a string representing the current working directory.
# os.getcwd()
# r -> to ignore the back slash as a command

path_source = r"C:\\Users\\leona\\Desktop\\test\\source\\"
path_replica = r"C:\\Users\\leona\\Desktop\\test\\replica\\"

# path_folders = os.path.dirname(path_main)

# replace

dir_sync = os.listdir(path_source)

for file in dir_sync:
    print(file, type(file))
    try:
        print(len(dir_sync))
        # shutil.copy(path_source + '\\' + file, path_replica + '\\' + file)
    except:
        print('File or Folder: not found!')


'''
print('-' * 15)

print(path_source, type(path_source))

print('-' * 15)

print(len(dir_sync))'''
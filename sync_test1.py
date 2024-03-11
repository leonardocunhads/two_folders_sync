import os
import logging
from pathlib import Path

path_source = r"C:\\Users\\leona\\Desktop\\test\\source\\"

def set_log(log_name):

    logging.basicConfig(
        level=logging.INFO,
        filename=log_name+'.log',
        filemode='a',
        format='%(asctime)s - %(levelname)s: %(message)s')


    log_msg = 'Synchronized -> '

    folders_sync = 3
    files_sync = 3

    logging.info(log_msg + 'Folders: {} | Files: {}'.format(folders_sync, files_sync))

file_name = input('Type a name for a log file: ')

if not os.path.exists(logs):
    os.makedirs(logs)
    os.chdir(logs)
    set_log(file_name)
else:
    os.chdir(logs)
    set_log(file_name)
 



# print(os.listdir(path_source))
# print('\n'+'-' * 20 + '\n' )

# print(os.walk(path_source, type(os.walk(path_source))))

# print(list(os.walk(path_source)))
# print('\n'+'-' * 20 + '\n' )

'''for root, dirs, files in os.walk(path_source):
    print(root)
    print(dirs)
    print(files)
    print('-' * 15)'''

#logs  = os.getcwd() + r'\\logs'
logs = Path(path_source)

logs.parent
print(type(logs.parent))
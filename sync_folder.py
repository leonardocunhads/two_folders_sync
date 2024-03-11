import os
import logging
from pathlib import Path


path_source = r"C:\\Users\\leona\\Desktop\\test\\source\\"

logs = str(Path(path_source).parent) + r'\\logs'
#print(logs)

def set_log(log_msg):

    logging.basicConfig(
        level=logging.INFO,
        filename='log.log',
        filemode='a',
        format='%(asctime)s - %(levelname)s: %(message)s')

    logging.info(log_msg)

log_msg = input('Type a message log: ')

if not os.path.exists(logs):
    os.makedirs(logs)
    os.chdir(logs)
    set_log(log_msg)
else:
    os.chdir(logs)
    set_log(log_msg)
 



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

'''logs  = os.getcwd() + r'\\logs'
logs = Path(path_source)

logs.parent
print(type(logs.parent))'''
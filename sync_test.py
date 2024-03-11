import os
import logging
import shutil
from pathlib import Path

path_source = r"C:\\Users\\leona\Desktop\\test\\source\\"
path_replica = r"C:\\Users\\leona\Desktop\\test\\replica\\"

#print(logs)

def set_log(log_name):

    logging.basicConfig(
        level=logging.INFO,
        filename= log_name + '.log',
        filemode='a',
        format='%(asctime)s - %(levelname)s: %(message)s')


def sync_folder():
    log_name = input('Type a file name: ')
    logs = str(Path(path_source).parent) + r'\\logs'


    if not os.path.exists(logs):
        os.makedirs(logs)
        os.chdir(logs)
        set_log(log_name)
        logging.info('Log Folder/File Created')
    else:
        os.chdir(logs)
        set_log(log_name)
        logging.info('Log File Created')
        #print(f'Log File Created: {log_name}.')
    if not os.path.exists(path_source):
        os.makedirs(path_source)
        logging.info(f'Folder Created: {path_source}')
    if not os.path.exists(path_replica):
        os.makedirs(path_replica)
        logging.info('Folder Created: {}'.format(path_replica))


    for root, dirs, files in os.walk(path_source):
        # creating the folder path on replica guided by the source path
        rel_path = os.path.relpath(root, path_source)
        rep_path = os.path.join(path_replica, rel_path)

        for sub_dir in dirs:
            source_dir = os.path.join(root, sub_dir)
            #print(source_dir)
            rep_dir = os.path.join(rep_path, sub_dir)
            #print(rep_dir)
            if not os.path.exists(rep_dir):
        # create the sub folders that does not exist in replica
                os.makedirs(rep_dir)
                logging.info('Created Folder: {}'.format(sub_dir))

        for file_name in files:
            
            source_file = os.path.join(root, file_name)

            replica_file = os.path.join(rep_path, file_name)
            
        # copy the file that does not exist in replica
            shutil.copy2(source_file, replica_file)
            logging.info('Copied File: {}'.format(file_name))


    # Deleting folders and files that don't exist anymore in source folder

    for root, dirs, files in os.walk(path_replica):

        for sub_dir in dirs:
            rep_dir = os.path.join(root, sub_dir)
            rel_path = os.path.relpath(rep_dir, path_replica)
            source_dir = os.path.join(path_source, rel_path)
            if not os.path.exists(source_dir):
                shutil.rmtree(rep_dir)
                logging.warning('Removed Folder: {}'.format(sub_dir))

        for file_name in files:
            rep_file = os.path.join(root, file_name)
            rel_path  = os.path.relpath(rep_file, path_replica)
            source_file = os.path.join(path_source, rel_path)
            if not os.path.exists(source_file):
                os.remove(rep_file)
                logging.warning('Removed File: {}'.format(file_name))

    logging.info('Finished!')



sync_folder()


#shutil.rmtree


# print(os.listdir(path_source))
# print('\n'+'-' * 20 + '\n' )

# print(os.walk(path_source, type(os.walk(path_source))))

# print(list(os.walk(path_source)))
# print('\n'+'-' * 20 + '\n' )
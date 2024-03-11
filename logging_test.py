import logging
import os


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



#logs = r"C:\\Users\\leona\\Documents\\GitHub\\two_folders_sync\\logs"
logs  = os.getcwd() + r'\\logs'

file_name = input('Type a name for a log file: ')

if not os.path.exists(logs):
    os.makedirs(logs)
    os.chdir(logs)
    set_log(file_name)
else:
    os.chdir(logs)
    set_log(file_name)
        

'''
FORMAT = '%(asctime)s %(clientip)-15s %(user)-8s %(message)s'
logging.basicConfig(format=FORMAT)
d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
logger = logging.getLogger('tcpserver')
logger.warning('Protocol problem: %s', 'connection reset', extra=d)

logging.debug('debug')
logging.warning('warning')
logging.error('error')
logging.critical('critical')'''

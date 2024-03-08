import os
import shutil
import time
import argparse
import logging

def synchronize_folders(source_path, replica_path, interval, log_file):
    logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s')
    logging.getLogger().addHandler(logging.StreamHandler())

    while True:
        try:
            sync_start_time = time.time()
            logging.info("Synchronization started.")

            # Synchronize source folder to replica folder
            sync_folders(source_path, replica_path)

            logging.info("Synchronization completed successfully.")
        except Exception as e:
            logging.error(f"Synchronization failed: {e}")

        # Wait for next synchronization interval
        elapsed_time = time.time() - sync_start_time
        time.sleep(max(0, interval - elapsed_time))

def sync_folders(source_path, replica_path):
    # Get lists of files and directories in both folders
    source_contents = os.listdir(source_path)
    replica_contents = os.listdir(replica_path)

    # Remove files and directories in replica that don't exist in source
    for item in replica_contents:
        replica_item_path = os.path.join(replica_path, item)
        if item not in source_contents:
            if os.path.isdir(replica_item_path):
                shutil.rmtree(replica_item_path)
                logging.info(f"Deleted folder: {replica_item_path}")
            else:
                os.remove(replica_item_path)
                logging.info(f"Deleted file: {replica_item_path}")

    # Copy files and directories from source to replica
    for item in source_contents:
        source_item_path = os.path.join(source_path, item)
        replica_item_path = os.path.join(replica_path, item)

        if os.path.isdir(source_item_path):
            if not os.path.exists(replica_item_path):
                shutil.copytree(source_item_path, replica_item_path)
                logging.info(f"Created folder: {replica_item_path}")
            else:
                sync_folders(source_item_path, replica_item_path)  # Recursively synchronize subfolders
        else:
            if not os.path.exists(replica_item_path):
                shutil.copy2(source_item_path, replica_item_path)
                logging.info(f"Copied file: {replica_item_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Folder synchronization program")
    parser.add_argument("source", help="Path to source folder")
    parser.add_argument("replica", help="Path to replica folder")
    parser.add_argument("interval", type=int, help="Synchronization interval in seconds")
    parser.add_argument("log_file", help="Path to log file")

    args = parser.parse_args()
    source_path = args.source
    replica_path = args.replica
    interval = args.interval
    log_file = args.log_file

    synchronize_folders(source_path, replica_path, interval, log_file)

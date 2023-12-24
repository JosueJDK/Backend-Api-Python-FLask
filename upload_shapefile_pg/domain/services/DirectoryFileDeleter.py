import os
import shutil

class DirectoryFileDeleterService:
    """
    A class to delete all files in a directory.

    This class provides functionality to delete all files within a specified directory.
    """

    def __init__(self, directory):
        """
        Initializes the DirectoryFileDeleter.

        Args:
        - directory (str): Path to the directory containing files to be deleted.
        """
        self.directory = directory

    def delete_files(self):
        """
        Deletes all files in the specified directory.
        """
        try:
            files = os.listdir(self.directory)
            for file_name in files:
                file_path = os.path.join(self.directory, file_name)
                try:
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                        print(f"Deleted: {file_path}")
                    else:
                        shutil.rmtree(file_path)
                        print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Error deleting {file_path}: {str(e)}")
        except Exception as e:
            print(f"Error accessing directory: {str(e)}")
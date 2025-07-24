import os, sys,shutil,uuid


class TempService:
    """
    Creates a place for temporary files and deletes them
    """
    def __init__(self, log,tempdir):
        """
        Initializes the TempService.

        Args:
            log: The logger to use for logging.
            tempdir (str): The base directory for temporary files.
        """
        self.tempdir=tempdir
        self.log=log
        os.makedirs(self.tempdir,exist_ok=True)

    def get_random_temp_filepath(self,extension:str)->str:
        """
        Generates a random temporary file path with the specified extension.

        Args:
            extension (str): The file extension (e.g., "pdf", "png").

        Returns:
            str: The full path to the temporary file.
        """
        rid = uuid.uuid4()
        extension=extension.replace(".","")

        return os.path.join(self.tempdir,f"{rid}.{extension}")

    def remove_temp_file(self,filepath)->bool:
        """
        Remove specified file from file system (returns true if it actually existed and was deleted)

        Args:
            filepath (str): The path to the file to remove.

        Returns:
            bool: True if the file was deleted, False otherwise.
        """

        try:
            if os.path.exists(filepath):

                os.remove(filepath)
                return True

            fullpath = os.join(self.tempdir,filepath)

            if os.path.exists(fullpath):
                os.remove(fullpath)
                return True

        except Exception as e:
            self.log.warn(f"Exception during file deletion: {filepath}. {e}")
            return False

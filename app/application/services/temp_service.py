import os, sys,shutil,uuid


class TempService:
    ''''
    Creates a place for temporary files and deletes them
    '''
    def __init__(self, log,tempdir):
        self.tempdir=tempdir
        self.log=log

    def get_random_temp_filepath(self,extension:str)->str:

        rid = uuid.uuid4()
        extension=extension.replace(".","")

        return os.path.join(self.tempdir,f"{rid}.{extension}")

    def remove_temp_file(self,filepath)->bool:
        ''''
        Remove specified file from file system (returns true if it actually existed and was deleted)
        '''

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

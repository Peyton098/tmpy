import time, os, glob
from typing import Tuple

class TMP_Manager :

    def __init__(self) -> None:
        print("--__INIT__--")
        self.time = ((int(input("Intevalle de vérification (en heures) : ")))*60)*60
        self.run = True
        self.path = "C:/Users/sebas/Desktop/TMP/*"
        self.start()

    def start(self) -> None :
        print("--START--")
        while self.run :
            if False == self.dir_is_empty() :
                self.delete_files()
            self.is_the_time()

    def is_the_time(self) -> None :
        print("--IS THE TIME--")
        time.sleep(self.time)

    def delete_files(self) -> None :
        print("--DELETE FILES--")
        files = glob.glob(self.path)
        print(files)
        for file in files:
            os.remove(file)

    def dir_is_empty(self) -> None :
        print("--DIR IS EMPTY--")
        if len(glob.glob(self.path)) > 0 : return False
        else : return True

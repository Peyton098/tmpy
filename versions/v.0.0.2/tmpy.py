import time, os, glob
from typing import Tuple

class TMP_Manager :

    def __init__(self, time: int = None, username: str = None, path: str = None, visible_execution: bool = True) -> None:
        self.visible_execution = visible_execution
        if self.visible_execution : print("--__INIT__--")
        if time == None : self.time = ((int(input("Number of hours : ")))*60)*60
        else : self.time = time
        if username == None : self.username = input("Username : ")
        else : self.username = username
        self.run = True
        if path == None : self.path = "C:/Users/" + self.username + "/Desktop/TMP/*"
        else : self.path = path
        self.start()

    def start(self) -> None :
        if self.visible_execution : print("--START--")
        while self.run :
            if False == self.dir_is_empty() :
                self.delete_files()
            self.is_the_time()

    def is_the_time(self) -> None :
        if self.visible_execution : print("--IS THE TIME--")
        time.sleep(self.time)

    def delete_files(self) -> None :
        if self.visible_execution : print("--DELETE FILES--")
        files = glob.glob(self.path)
        print(files)
        for file in files:
            os.remove(file)

    def dir_is_empty(self) -> None :
        if self.visible_execution : print("--DIR IS EMPTY--")
        if len(glob.glob(self.path)) > 0 : return False
        else : return True

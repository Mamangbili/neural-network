import csv

class Loader:
    def __init__(self,file_path : str, random = False) -> None:
        self.__file_path = file_path
        self.__current_row : int = 0
    
    def lazy_load(self) :
        with open(self.__file_path,'r') as file :
            reader = csv.reader(file)
            next(reader)
            
            for i,row in enumerate( reader ):
                self.__current_row += 1
                yield i,row
    
    def get_current_row(self) -> int:
        return self.__current_row
        
    def load_once(self) :
        file = open(self.__file_path)
        return file

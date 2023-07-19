import sys
from time import sleep
import os
import shutil
from datetime import datetime

class CustomException(Exception):
    pass
class Console:
    def writeout(self, *strings, sep=" ", end="\n", dict_sep=" : ", flush=False):
        if len(strings) > 1:
            stringarg = sep.join(map(str, strings)) + end
            sys.stdout.write(stringarg)
        elif len(strings) == 1:
            sys.stdout.write(str(strings[0]) + end)
        if flush:
            sys.stdout.flush()
    def getinp(self, text=""):
        self.writeout(text, end="", flush=True)
        return sys.stdin.readline().rstrip('\n')
    def display_error(self, error): raise CustomException(error)
    def clear(self): os.system('cls' if os.name == 'nt' else 'clear')
    def animate_text(self, text, time):
        if type(time) not in [float, int]: 
            raise TypeError("Non-float type given for time argument in animate_text()")
        for char in text:
            self.writeout(char, end="", flush=True)
            sleep(time)
    def write_unpacked(string, dict_sep = " : ", sep = " ", end = "\n"):
        if type(string) == list or type(string) == tuple:
            for entry in string:
                sys.stdout.write(str(entry) + sep)
            sys.stdout.write(end)
        elif type(string) == dict:
            for key, value in string.items():
                sys.stdout.write(key + dict_sep + str(value) + end)

class Text:
    def to_decimal(text):
        return_values = []
        for char in text:
            return_values.append(ord(char))
        if len(return_values) == 1: 
            return return_values[0]
        else: 
            return return_values
    def to_string(decimal_list: int | list):
        result = ""
        if type(decimal_list) not in [int, list]: 
            raise TypeError(f"Cannot convert {type(decimal_list)} to string")
        elif type(decimal_list) == int:
            return chr(decimal_list)
        else:
            for i in decimal_list:
                result += chr(i)
            return(result)

        
class Clock:
    def getdatetime(self, format="%d-%m-%Y %H:%M:%S"):
        return datetime.now().strftime(format)
    def timing_function(self, func, *args, **kwargs):
        start_time = datetime.now().timestamp()
        func(*args, **kwargs)
        end_time = datetime.now().timestamp()
        elapsed_time = end_time - start_time
        return elapsed_time
    
class File:
    def makefile(self, name, location):
        if not os.path.exists(location): 
            os.makedirs(location)            
        location = f"{location}\\{name}"
        open(location, "x")
    def write(self, path, content):
        if not os.path.exists(path): 
            raise OSError("File doesn't exist.")
        with open(path, "w") as f:
            f.write(content)
    def read(self, path):
        if not os.path.exists(path): 
            raise OSError("File doesn't exist.")
        with open(path, "r") as f:
            return f.read()
    def delete(self, path):
        if not os.path.exists(path): 
            raise OSError("File doesn't exist.")
        if os.path.isfile(path):
            os.remove(path)
        else:
            if len(os.listdir(path)) == 0: os.rmdir(path)
            else: shutil.rmtree(path)
    def copy(self, source, destination):
        with open(source, "r") as f: 
            content = f.read()
        with open(destination, "w") as f:
            f.write(content)
    def move(self, source, destination):
        if not (os.path.exists(source) or os.path.exists(destination)): 
            raise OSError("Source/Destination file does not exist")
        os.rename(source, destination)

console = Console()
clock = Clock()
file = File()
text = Text()

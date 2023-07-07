import sys
from time import sleep
import os
import shutil
from datetime import datetime

class CustomException(Exception): pass
class Console:
    def writeout(self, *strings, sep=" ", end="\n", flush=False):
        if len(strings) > 1:
            stringarg = sep.join(map(str, strings)) + end
            sys.stdout.write(stringarg)
        elif len(strings) == 0: pass
        elif len(strings) == 1: sys.stdout.write(str(strings[0])+end)
        if flush: sys.stdout.flush()
    def getinp(self, text=""):
        self.writeout(text, end="", flush=True)
        return sys.stdin.readline().rstrip('\n')
    def display_error(self, error): raise CustomException(error)
    def clear(self): os.system('cls' if os.name == 'nt' else 'clear')
    def animate_text(self, text, time):
        if type(time) not in [float, int]: raise TypeError("Non-float type given for time argument in animate_text()")
        for char in text:
            self.writeout(char, end="", flush=True)
            sleep(time)

class Clock:
    def getdatetime(self, format="%d-%m-%Y %H:%M:%S"):
        return datetime.now().strftime(format)
    def timeit(self, func):
        if not callable(func): raise CustomException("Argument passed is not callable")
        else:
            start = datetime.now().timestamp()
            func()
            end = datetime.now().timestamp()
            if(start % end) == 0: return(int(end-start))
            else: return(end-start)
    
class File:
    def makefile(self, name, location):
        if not os.path.exists(location): os.makedirs(location)            
        location = f"{location}\\{name}"
        open(location, "x")
    def write(self, path, content):
        if not os.path.exists(path): raise CustomException("File doesn't exist.")
        with open(path, "w") as f:
            f.write(content)
    def read(self, path):
        if not os.path.exists(path): raise CustomException("File doesn't exist.")
        with open(path, "r") as f:
            return f.read()
    def delete(self, path):
        if not os.path.exists(path): raise CustomException("File doesn't exist.")
        if os.path.isfile(path): os.remove(path)
        else:
            if len(os.listdir(path)) == 0: os.rmdir(path)
            else: shutil.rmtree(path)
    def copy(self, source, destination):
        with open(source, "r") as f: content = f.read()
        with open(destination, "w") as f: f.write(content)
    def move(self, source, destination):
        if not (os.path.exists(source) or os.path.exists(destination)): raise CustomException("Source/Destination file does not exist")
        os.rename(source, destination)

console = Console()
clock = Clock()
file = File()
if __name__ == "__main__":
    def passtime():
        sleep(5)
    timer = clock.timeit(passtime)
    console.writeout(timer)

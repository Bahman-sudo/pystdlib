import sys
from time import sleep
import os
import shutil
from datetime import datetime
from threading import Thread

class CustomException(Exception): pass
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
    def display_error(self, error):
        raise CustomException(error)
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
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
    def to_decimal(self, text, is_hex=False):
        return_values = []
        for char in text:
            if not is_hex:
                return_values.append(ord(char))
            else:
                return_values.append(hex(ord(char)))
        if len(return_values) == 1: 
            return return_values[0]
        else: 
            return return_values
    def to_string(self, decimals, is_hex=False):
        return_values = []
        for char in decimals:
            if is_hex: int(decimals, 16)
            return_values.append(chr(char))
        if len(return_values) == 1: 
            return return_values[0]
        else: return "".join(return_values)
        
class Clock:
    def getdatetime(self, format="%d-%m-%Y %H:%M:%S"):
        return datetime.now().strftime(format)
    def timing_process(self, func, *args, **kwargs):
        start_time = datetime.now().timestamp()
        func(*args, **kwargs)
        end_time = datetime.now().timestamp()
        elapsed_time = end_time - start_time
        return elapsed_time
    def timeit(self, func, *args, **kwargs):
        thread = Thread(target=self.timing_process, args=(func, *args), kwargs=kwargs, daemon=True)
        thread.start()
        thread.join()
        return thread
    
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
            if len(os.listdir(path)) == 0: 
                os.rmdir(path)
            else:
                shutil.rmtree(path)
    def copy(self, source, destination):
        with open(source, "r") as f: 
            content = f.read()
        with open(destination, "w") as f: 
            f.write(content)
    def move(self, source, destination):
        if not (os.path.exists(source) or os.path.exists(destination)): 
            raise OSError("Source/Destination file does not exist")
        os.rename(source, destination)

class Math:
    def __init__(self):
        self.e = 2.718281828459045
        self.pi = 3.141592653589793
    def unique_items(self, inplist: list):
        if type(inplist) != list or type(inplist) != tuple: 
            raise TypeError(f"List type expected, {type(inplist)} received.")
        rvalue = []
        rvalue.append(inplist[0])
        counter = 0
        del inplist[counter]
        for item in inplist:
            counter += 1
            if item not in rvalue:
                rvalue.append(item)
            else:
                del counter
        return rvalue
    def counter(inplist: list):
        items = {}
        for item in inplist:
            if item not in items.keys():
                items[item] = 1
            else:
                items[item] += 1
        return items
    def root(self, base, root=2):
        return base ** (1/root)
    def mean(self, inplist: list):
        return sum(inplist)/len(inplist)
    def median(self, inplist: list):
        inplist.sort()
        if len(inplist) % 2 == 0:
            mid_index1 = len(inplist) // 2 - 1
            mid_index2 = len(inplist) // 2
            return inplist[(mid_index1+mid_index2)//2]
        else:
            return inplist[len(inplist)//2]
    def mode(self, inplist: list):
        count_dict = {}
        for element in inplist:
            count_dict[element] = count_dict.get(element, 0) + 1
        max_count = max(count_dict.values(), default=0)
        if max_count == 1:
            return None
        else:
            return max(set(inplist), key=inplist.count)
    def standard_distribution(self, z):
        return (1 / self.root(2 * self.pi)) * self.e^(-(z^2)/2)
    def factorial(self, num: int):
        if type(num) != int:
            raise TypeError("Factorial only accepts integer values")
        if num == 1:
            return 1
        return num*self.factorial(num-1)
    def sin(self, x, num_terms = 10, rdp=15):
        x = self.radians(x)
        result = 0
        for n in range(num_terms):
            term = ((-1) ** n) * (x ** (2*n + 1)) / self.factorial(2*n + 1)
            result += term
        return round(result, rdp)
    def cos(self, x, rdp=15):
        return round(self.root(1 - self.sin(x)**2), rdp)
    def tan(self, x, rdp=15):
        return round(self.sin(x)/self.cos(x), rdp)
    def sinh(self, x, rdp=15):
        return round((self.e**x - (self.e**(-x))) / 2, rdp)
    def cosh(self, x, rdp=15):
        return round((self.e^x + self.e^(-x)) / 2, rdp)
    def tanh(self, x, rdp=15):
        return round(self.sinh(x) * 2 / self.cosh(x) * 2, rdp)
    def degrees(self, x, angle_units = "radians"):
        if angle_units == "radians": return x * (180 / self.pi)
        else: return x * (200 / self.pi)
    def radians(self, x, angle_units = "degrees"):
        if angle_units == "degrees": return x * (self.pi / 180)
        else: return x * (self.pi / 200)
    def gradians(self, x, angle_units = "degrees"):
        if angle_units == "degrees": return (10 * x)/9
        else: return x * 200 / self.pi

start = None
console = Console()
clock = Clock()
file = File()
text = Text()
math = Math()

if __name__ == "__main__":
    console.writeout(math.sin(90))
# pystdlib

Python has multiple different core packages that make it hard whether to know which ones to use and for what purpose.
Pystdlib is a package released by me that does the functions of those core packages.

This package comes with documentation, so please make sure to read it before using this package

Pystdlib has 3 main classes:
- Console
- Clock
- File
- Text
- Math

Console utilises interactive console elements that allows the programmer to interact with the console.
`stdlib.console.writeout` writes to the console, it has 3 keyword arguments.
You can write text to it, obviously.
`stdlib.console.writeout("Hello", 3, True, 5)` returns  `Hello 3 True 5`
You can also include a seperator argument to it:
`stdlib.console.writeout("Hello", "World", sep=", ")` returns `Hello, World`
It also takes an end argument:
`stdlib.console.writeout("Hello", "World", end="")` returns  `HelloWorld`
Lastly, it takes a flush argument, which if true, flushes all text past to it immediately to the console
`stdlib.console.writeout("Hello", "World", flush=True)`

`stdlib.console.getinp` only takes one argument, text.
`age = stdlib.console.getinp("What is your age: ")` returns `What is your age` to the console before waiting for an input

`stdlib.console.display_error` raises a custom exception.

`stdlib.console.clear` clears the console

`stdlib.console.animate_text` takes 2 arguments: text and delay
The text argument is what will be displayed to the console
The delay argument in how long it will take to display to the console.
It basically does a typewrite effect with the text to the console

Clock has 2 functions:

- `stdlib.clock.getdatetime` which has one optional input, which is the format of the date/time
    -> `stdlib.clock.getdatetime("%d.%m.%Y %H-%M-%S")` returns the date and time in the format: "DD.MM.YYYY HH-MM-SS"
- `stdlib.clock.timeit` time functions. It has one input, which is the function being timed in question.
    -> `stdlib.clock.timeit(foo)` times the "foo" function and returns the time it took to execute said function to the console. If the function passed into the function doesn't exist, it raises an exception

File has many functions:

- `stdlib.file.makefile` which takes in the location of the file (and makes the directory if the location doesn't exist) and creates the file with said name
- `stdlib.file.write` takes in an existing file and write to it
- `stdlib.file.read` takes in an existing file and returns the contents
- `stdlib.file.delete` deletes the file/directory
- `stdlib.file.copy` copies the source file/directory to the destination directory
- `stdlib.file.move` moves the source file/directory to the destination directory

Text has 2 functions:
- `stdlib.text.to_decimal` has 2 arguments: text and is_hex.
    -> Text is the text you want to convert to an ascii encoding and is_hex is if you want it returned as a hexidecimal number
    -> Example usage:
    -> `stdlib.text.to_decimal("Hello, World!")` converts "Hello, World!" to "[72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100, 33]"
- `stdlib.text.to_string` has the same arguments as to_decimal
    -> Example usage:
    -> `stdlib.text.to_string([72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100, 33])` converts "[72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100, 33]" to "Hello, World!"

Math has 17 different functions:
- `stdlib.math.unique_items()` has one arguments: inplist.
    -> Inplist is basically the list that you want to find the unique elements of
    -> This function returns a list of all the unique elements
- `stdlib.math.counter()` has one argumentL inplist
    -> Inplist is the list of elemnents. Counter counts all of the elements in the list and returns a dictionary with the keys contaiing the unique elements and the values being all the occurences of those unique elements.
    -> Example Usage:
    -> `math.counter([1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4])` returns: `{1: 9, 2: 13, 3: 10, 4: 13}`


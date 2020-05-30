# Python Tricks



## 1. Interactive Shell

For example if you have a python file called ```math.py``` and it contains several functions like ```add()```, ```diff()```  and you want to test those method interactively, then you can run the script using ```-i``` argument to work with those functions individually and interactively.

```bash
python -i math.py
```

You will get a shell prompt and you can access all the functions defined in the file.

The output will look something like this-

```bash
>>> add(3, 4)
>>> 7
```

This trick is very handy in case you are developing a software and you need to test the functions interactively.


## 2. Using Python Debugger
If  your code is breaking somewhere you can find the breaking point easily just by using the built in ```pdb``` module.

```python
def add(a, b):
	return a + b


import pdb

pdb.set_trace()

add(2, 3)

# the add function will possibly break in the bellow statement, you can not add string-
add(3, '4')


# the pdb will run in interactive mode
- input n to go to the next statement	
```

## 3. Virtual Environment

To isolate too many dependencies from one project to another the best way is to use virtual environment. To install virtual environment - 

```bash
>>> pip install virtualenv
```

After the virtual env is installed you can create a virtual environment by providing the directory name you want to be created as a virtual env

```bash
>>> virtualenv testenv
``` 
the above command will create a virtual enviroment called testenv

To activate and install dependencies in the virtual environment, you neee to -

```bash
>>> source testenv/bin/activate
```

And to deactivate the virtual Environment

```bash
>>> deactivate
```



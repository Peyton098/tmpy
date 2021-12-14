# Introduction
*tmpy* is an Python module which allow have an TMP dir with Windows 10.

# Summary
- Using the module (https://github.com/Peyton098/tmpy#using-the-module)
  - Standard use
  - Use with parameters

# Using the module

## Standard use
To use the module, you just need to create an instance of the class, here is an example :
```Python
import tmpy

manager = tmpy.TMP_Manager()
```
The program will ask you for an username and a number of hours. It is therefore every X hours that the program will run. The username must be the same of Windows username.

Here is a sample output :
```
--__INIT__--
Number of hours : 1
Username : peyton
--START--
--DIR IS EMPTY--
--IS THE TIME--

```

## Use with parameters
You can also use the module without having to ask the user for values. For software, for example. There are 3 parameters :
- ``time`` : this is the time interval.
- ``username`` : this is the username.
- ``path`` : this is the path of TMP dir.
- 
Here is an example with explanations :
```Python
import tmpy

manager = tmpy.TMP_Manager(time=1, username="peyton", path="D:/DATA/TMP")
```

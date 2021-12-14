# Introduction
*tmpy* is an Python module which allow have an TMP dir with Windows 10.

# Summary
- Using the module (https://github.com/Peyton098/tmpy#using-the-module)
  - Standard use (https://github.com/Peyton098/tmpy/blob/main/README.md#standard-use)
  - Use with parameters (https://github.com/Peyton098/tmpy/blob/main/README.md#use-with-parameters)

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
You can also use the module without having to ask the user for values. For software, for example. There are 4 parameters :
- ``time`` : this is the time interval in secondes.
- ``username`` : this is the username.
- ``path`` : this is the path of TMP dir.
- ``visible_execution`` : this is a *boolean*. If it is false, the program does not display anything in the console. It is automatically true.
Here is an example with explanations :
```Python
import tmpy

manager = tmpy.TMP_Manager(time=3600, username="peyton", path="D:/DATA/TMP")
```
In this example, we do not ask the user for any value. Here is a sample output :
```
--__INIT__--
--START--
--DIR IS EMPTY--
--IS THE TIME--

```

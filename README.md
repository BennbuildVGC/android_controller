# android-controller
A python module to control your android phone

## Installation

### Prerequisites
- Pip
- [adb](https://dl.google.com/android/repository/platform-tools-latest-windows.zip) installed and [added to PATH](https://helpdeskgeek.com/windows-10/add-windows-path-environment-variable/)

### Using PyPi (recommended)
Open a command prompt and run:
```
pip install android_controller
```

### From source

Open a command promp and clone this repo. Now cd to that folder and run:
```
pip install .
```

## Usage
The package can be imported using:
```python
import android_controller
```
Most of the times devices connect to adb automatically, but if they don't you can use:
```python
android_controller.connect(host) #host is where your device is connected to. For example, bluestacks would be localhost:5555
```
You can then check which devices are connected using:
```python
connections = android_controller.checkConnections()
```
This will return a list with the names of all connected devices. 
Please make sure you only have one device connected, otherwise the module might not work properly.

## Distributing
All distributions are welcome. There are quite some functions that are less commonly used I left out, but they can of course still be added.

## License
This project is licensed under the MIT license.

 ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/android_controller) ![GitHub](https://img.shields.io/github/license/BennbuildVGC/android_controller) 

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

## Documentation

```python
android_controller.checkConnections()
```
Returns a list of all devices currently connected.

```python
android_controller.connect(host: str)
```
Connects to the chosen host.

```python
android_controller.disconnect(host: str)
```
Disconnects from the chosen host. If no host is defined, disconnects from all hosts.

```python
android_controller.keyEvent(key: str, longpress: bool)
```
Executes a [keyevent](https://gist.github.com/arjunv/2bbcca9a1a1c127749f8dcb6d36fb0bc). Set longpress to True for a longpress.

```python
android_controller.screenshot(outputpath: str)
```
Makes a screenshot and saves it at the defined location.

```python
android_controller.swipe(x1: int, y1: int, x2: int, y2: int)
```
Swipes from the first location to the second location.

```python
android_controller.tap(x: int, y: int)
```
Taps at the defined location.

## Distributing
All distributions are welcome. There are quite some functions that are less commonly used I left out, but they can of course still be added.

## License
This project is licensed under the MIT license.

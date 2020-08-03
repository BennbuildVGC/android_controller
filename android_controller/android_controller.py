import subprocess



def checkConnections():
    process = subprocess.Popen(["adb", "devices"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = process.stdout.read().decode("utf-8")
    output = output.replace("\r", "")
    output = output.split("\n")
    rtrn = []
    for connection in output[1:]:
        if connection == "":
            continue
        connection = connection.split("\t")
        if connection[1] == "device":
            rtrn.append(connection[0])
    return rtrn

def connect(host : str):
    subprocess.run(["adb", "connect", host])
    return

def disconnect(host: str = "all"):
    if host == "all":
        subprocess.run(["adb", "disconnect"])
    else:
        subprocess.run(["adb", "connect", host])
    return

def tap(x: int, y: int):
    subprocess.run(["adb", "shell", "input", "tap", str(x), str(y)])
    return

def swipe(x1: int, y1: int, x2: int, y2: int):
    subprocess.run(["adb", "shell", "input", "swipe", str(x1), str(y1), str(x2), str(y2)])
    return

def keyEvent(key: str, longpress: bool = False):
    if longpress:
        subprocess.run(["adb", "shell", "input", "--longpress", key])
        return
    else:
        subprocess.run(["adb", "shell", "input", key])
        return

def screenshot(outputpath: str):
    subprocess.run(["adb", "exec-out", "screencap", "-p", ">", outputpath])
    return outputpath

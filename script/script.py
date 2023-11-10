import platform
import datetime
import getpass
import platform
import socket
import psutil
print(getpass.getuser())
current_time = datetime.datetime.now()
print(current_time)
print(platform.architecture())
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print("Your Computer Name is:" + hostname)
print("Your Computer IP Address is:" + IPAddr)
print(platform.system())
print(platform.version())
my_system = platform.uname()
print(f"System: {my_system.system}")
print(f"Node Name: {my_system.node}")
print(f"Release: {my_system.release}")
print(f"Machine: {my_system.machine}")
print(f"Processor: {my_system.processor}")
from tqdm import tqdm
from time import sleep
with tqdm(total=100, desc='cpu%', position=1) as cpubar, tqdm(total=100, desc='ram%', position=0) as rambar:
    while True:
        rambar.n=psutil.virtual_memory().percent
        cpubar.n=psutil.cpu_percent()
        rambar.refresh()
        cpubar.refresh()
        sleep(0.5)
     
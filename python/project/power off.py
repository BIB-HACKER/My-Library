import os

shutdown = input("Do shutdown your computer? (0/1) :")

if shutdown == '0' or shutdown == '1':
    os.system("shutdown /s /t 0")
else:
    print("Exiting the program")
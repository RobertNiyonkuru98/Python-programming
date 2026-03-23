import os
import subprocess
import time
from clap_detector import ClapDetector # A popular library for this

def daddys_home(claps):
    if claps == 1:
        print("Opening Browser...")
        os.system("start chrome") # For Windows
    
    elif claps == 2:
        print("Wake up, Daddy's home.")
        # Open VS Code and a specific Project Folder
        subprocess.Popen(['code', 'C:/Users/YourName/Documents/MyProject'])
        # Open a specific website
        os.system("start https://github.com")

    elif claps == 3:
        print("System Shutdown...")
        # You could add code here to close everything
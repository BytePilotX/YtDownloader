import os
import sys
import time
print("RUNNING INSTALL SCRIPT...\n")
time.sleep(1)
print("DETECTING OS...\n")
time.sleep(1)
print(sys.platform,"\n")
time.sleep(1)
print("INSTALLING YT_DLP TO YOUR SYSTEM AND OTHER DEPENDENCIES...\n")
time.sleep(1)
os.system(f"{sys.executable} -m pip --version")
print("\n")
if sys.platform == "win32":
        print("Windows detected. Installing yt-dlp...")
        os.system("python -m pip install yt-dlp")
elif sys.platform == "linux" or sys.platform == "linux2":
    print("Linux or Chromebook detected. Installing yt-dlp...\n")
    os.system("sudo python3 -m pip install yt-dlp")
else:
    print("Unsupported OS. Please manually install yt-dlp.\n")

import time
import os
import yt_dlp
from yt_dlp import preferredencoding
whyareyouhere = open("checkmessageread.txt", "a")
whyareyouhere.close()
print("Hello, this is a script made by that-linux-programmer on GitHub! \n")
time.sleep(0.5)
print("This tool can be used to download playlists and single mp4/mp3's!\n")
time.sleep(0.5)
messagereturn = open("checkmessageread.txt", "r")
messagereturntext = messagereturn.readline(1)
if messagereturntext == "Y":
    messagereturn.close()
else:
    print("**MAKE SURE YOU RUN THE INSTALL SCRIPT IN THE SAME FOLDER AS THIS ONE!** ||| YOU WILL ONLY SEE THIS MESSAGE ONCE!\n")
message = open('checkmessageread.txt', "at")
message.write("Y")
message.close()
time.sleep(0.5)
while True:
    print("You can also say 'exit' to stop the program.\n")
    videooraudio = str(input("Would you like this youtube video as an mp3 or mp4? (say 3 for mp3 and say 4 for mp4): "))
    if videooraudio == "4":
        url = str(input("Please copy the URL in the search bar of your browser and paste it here: "))
        options = {
            format: 'best/bestaudio',
            preferredencoding: 'mp4'
        }
        with yt_dlp.YoutubeDL(options) as tool0:
            tool0.download(url)
        print("Video succesfully downloaded! \n THE DOWNLOAD LOCATION IS IN THE FOLDER OF THIS SCRIPT!")
    elif videooraudio == "3":
        url1 = str(input("Please copy the URL in the search bar of your browser and paste it here: "))
        options1 = {
            'extract_audio': True,
            'format': 'bestaudio',
            'outtmpl': '%(title)s.mp3'
        }
        with yt_dlp.YoutubeDL(options1) as tool:
            tool.download(url1)
            print("Audio successfully downloaded! \n THE DOWNLOAD LOCATION IS IN THE FOLDER OF THIS SCRIPT!")
    elif videooraudio == "exit":
        print("Exiting")
        break
        exit()
    else:
        print("mp3 = 3 mp4 = 4")

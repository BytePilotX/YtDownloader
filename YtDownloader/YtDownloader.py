import time
import os
import yt_dlp
from yt_dlp import preferredencoding
whyareyouhere = open("checkmessageread.txt", "a")
whyareyouhere.close()
print("Hello, this is a script made by that-linux-programmer on GitHub! \n")
time.sleep(0.5)
print("This tool can be used to download playlists and single mp4 videos!\n")
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
url = str(input("Please copy the URL in the searchbar of your browser and paste it here: "))
options = {
    format: 'best/bestaudio',
    preferredencoding: 'mp4'
}
video = yt_dlp.YoutubeDL(options)
status = video.download(url)
if status == 0:
    print("Video succesfully downloaded! \n THE DOWNLOAD LOCATION IS IN THE FOLDER OF THIS SCRIPT!")
else:
    print("E02: DOWNLOAD FAILED! -- CHECK URL IS CORRECT ELSE RESTART THE SCRIPT!")